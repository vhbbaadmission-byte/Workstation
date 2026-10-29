"""Independent cross-check of the Jaguar (JLR) bond case. Run: python3 check_calcs.py
All inputs from case text / exhibits.csv; assumptions flagged ASSUMPTION."""
import csv, os
from datetime import date
from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))
def hdr(s): print("\n" + "=" * 8, s, "=" * 8)

# ---------- helpers ----------
def d360(a, b):
    """30/360 US day count (days)."""
    d1, d2 = min(a.day, 30), b.day
    if d2 == 31 and d1 == 30: d2 = 30
    return (b.year - a.year) * 360 + (b.month - a.month) * 30 + (d2 - d1)

def semi_dates(first, last):
    """semi-annual dates from 'first' to 'last' inclusive (same day-of-month pair)"""
    out, y, m = [], first.year, first.month
    while True:
        d = date(y, m, first.day)
        if d > last: break
        out.append(d); m += 6
        if m > 12: m -= 12; y += 1
    return out

def price(settle, cfs, y):
    """dirty price per 100: cfs=[(date,amt)], semiannual comp, periods = 30/360 days/180"""
    return sum(a / (1 + y / 2) ** (d360(settle, d) / 180) for d, a in cfs if d > settle)

def solve_y(settle, cfs, dirty):
    return brentq(lambda y: price(settle, cfs, y) - dirty, -0.5, 1.0)

# ---------- inputs ----------
rows = list(csv.DictReader(open(os.path.join(HERE, "../exhibits.csv"))))
def ex(e, row, col):
    for r in rows:
        if r["exhibit"] == str(e) and r["row"] == row and r["column"] == col:
            return float(r["value"]) if r["value"] != "" else 0.0
FX = ex(1, "Note: average GBP/US$ rate March 2015", "GBP/US$")          # 1.50 US$ per GBP (Ex.1 note)
mkt_px = {"USG50027AB03 (4-Feb-15)": ex(2, "8.125%; USG50027AB03", "Last Traded Price"),
          "US47009XAB55 (7-Aug-14)": ex(2, "8.125%; US47009XAB55", "Last Traded Price")}
T5_2015, T5_2011 = ex(3, "5-year point", "3/16/2015"), ex(3, "5-year point", "5/16/2011")
tsy15 = {k: ex(3, k, "3/16/2015") for k in ["1YR", "2YR", "3YR", "7YR", "10YR"]}
tsy11 = {k: ex(3, k, "5/16/2011") for k in ["1YR", "2YR", "3YR", "7YR", "10YR"]}
tsy15["5YR"] = T5_2015; tsy11["5YR"] = T5_2011

# ASSUMPTIONS
SETTLE = date(2015, 3, 31)           # tender expires 30-Mar-15 (case); settle next day
CPN = 8.125; FACE_USD = 410.0
OLD_MAT = date(2021, 5, 15); CALL_DT = date(2016, 5, 15)
CALL_PX = 100 + CPN / 2              # ASSUMPTION: typical HY first call price = par + half coupon = 104.0625
NEW_CPN = 3.5; NEW_FACE = 500.0; NEW_MAT = date(2020, 3, 15)
FEE = 0.0125                         # ASSUMPTION (sensitivity): 1.25% underwriting/legal on new issue

hdr("INPUTS")
print("FX US$ per GBP", FX, "| market indicative px", mkt_px)
print("UST 16-Mar-15", tsy15); print("UST 16-May-11", tsy11)
print("Settlement", SETTLE, "| call price assumed", CALL_PX)

# ---------- Q1 ----------
hdr("Q1: why did the coupon fall by more than half?")
c_old, c_new = 8.125, 3.5
print(f"Coupon fall {c_old-c_new:.3f} pts; new/old = {c_new/c_old:.1%}")
# decomposition: coupon ~ Treasury(same tenor) + spread. 2011 note = 10y; 2015 note = 5y.
sp11 = c_old - tsy11["10YR"]; sp15 = c_new - tsy15["5YR"]
print(f"2011: 10y UST {tsy11['10YR']:.2f}, spread {sp11*100:.0f}bp | 2015: 5y UST {tsy15['5YR']:.2f}, spread {sp15*100:.0f}bp")
lvl = tsy11["5YR"] - tsy15["5YR"]; ten = tsy11["10YR"] - tsy11["5YR"]
print(f"UST effect: level shift at 5y {lvl*100:.0f}bp + tenor (10y->5y on 2011 curve) {ten*100:.0f}bp = {(lvl+ten)*100:.0f}bp")
print(f"Spread compression {(sp11-sp15)*100:.0f}bp ; total {(lvl+ten+sp11-sp15)*100:.0f}bp vs coupon fall {(c_old-c_new)*100:.0f}bp")
print(f"Share of fall: UST level {lvl/(c_old-c_new):.1%}, tenor {ten/(c_old-c_new):.1%}, credit spread {(sp11-sp15)/(c_old-c_new):.1%}")
print("10y-10y comparison: UST 10y change", round((tsy15['10YR']-tsy11['10YR'])*100), "bp")
# credit metrics from Ex 4/5/6
def g(e, r, c): return ex(e, r, c)
yrs = ["FY2012", "FY2013", "FY2014", "FY2015-9 months"]
print("\nCredit metrics (GBP m)")
for y in yrs:
    rev = g(4,"Revenue",y); ebitda = rev+g(4,"Material and other cost of sales",y)+g(4,"Employee cost",y)+g(4,"Other expenses",y)+g(4,"Development costs capitalized",y)+g(4,"Other income",y)
    da = -g(4,"Depreciation &amortization",y); ebit = ebitda - da
    debt = g(6,"Short-term borrowings and current portion of long-term debt",y)+g(6,"Long-term debt",y)
    cash = g(6,"Cash &cash equivalents",y)+(g(6,"Short-term deposits",y) or 0)
    eq = g(6,"Equity attributable to shareholders",y)
    fcf = g(5,"Net cash generated from operations",y)+g(5,"Investment in property, plant and equipment",y)+g(5,"Cash paid for intangible assets",y)
    ann = 4/3 if "9 months" in y else 1
    print(f"{y:16s} rev {rev:7.0f} EBITDA {ebitda:6.0f} ({ebitda/rev:5.1%}) EBIT {ebit:6.0f} PAT {g(4,'Profit after tax',y):5.0f} debt {debt:5.0f} cash+dep {cash:5.0f} net debt {debt-cash:6.0f} "
          f"debt/EBITDA(ann) {debt/(ebitda*ann):.2f}x debt/equity {debt/eq:.2f} FCF(CFO-capex-intang) {fcf:6.0f}")
ebitda15 = 16040-9768-1427-2941+850+150
print("Ex1 total senior notes GBP m:", 500+400+263+321+450+321, "; weighted avg coupon of notes:",
      round((500*8.25+400*5+263*8.125+321*5.625+450*4.125+321*4.25)/(500+400+263+321+450+321),3), "%")
print("Share of 8.25%+8.125% notes in senior notes:", round((500+263)/(2255),3))

# ---------- Q2 ----------
hdr("Q2: price at which holders would surrender the US$410m 8.125% 2021 notes")
cpn_dates = [d for d in semi_dates(date(2015,5,15), OLD_MAT)]      # May/Nov 15 from May-15
cpn_dates = [d for d in [date(2015,5,15)] + semi_dates(date(2015,11,15), OLD_MAT)]
cpn_dates = sorted(set(semi_dates(date(2015,5,15), OLD_MAT)))
c = CPN / 2
last_cpn = date(2014, 11, 15)
acc_days = d360(last_cpn, SETTLE); accrued = c * acc_days / 180
print(f"Last coupon {last_cpn}; accrued days (30/360) {acc_days}; accrued interest = {accrued:.4f} per 100 (= US$ {accrued*FACE_USD/100:.3f}m on 410)")
cf_mat = [(d, c) for d in cpn_dates] + [(OLD_MAT, 100.0)]
cf_call = [(d, c) for d in cpn_dates if d <= CALL_DT] + [(CALL_DT, CALL_PX)]
yrs_mat = d360(SETTLE, OLD_MAT) / 360; yrs_call = d360(SETTLE, CALL_DT) / 360
print(f"Years to maturity {yrs_mat:.3f}; years to first call {yrs_call:.3f}")

# market-implied yields from the case's indicative prices (assume clean)
for k, p in mkt_px.items():
    ytm = solve_y(SETTLE, cf_mat, p + accrued); ytc = solve_y(SETTLE, cf_call, p + accrued)
    print(f"Indicative clean {p} ({k}): implied YTM {ytm:.4%}, YTC@{CALL_PX} {ytc:.4%}")

# interpolated UST for maturity/call horizon
def interp(t, curve):
    pts = {1:curve["1YR"],2:curve["2YR"],3:curve["3YR"],5:curve["5YR"],7:curve["7YR"],10:curve["10YR"]}
    ks = sorted(pts)
    for a, b in zip(ks, ks[1:]):
        if a <= t <= b: return pts[a] + (pts[b]-pts[a])*(t-a)/(b-a)
    return pts[ks[0]] if t < ks[0] else pts[ks[-1]]
u_mat, u_call = interp(yrs_mat, tsy15), interp(yrs_call, tsy15)
print(f"Interpolated UST: {yrs_mat:.2f}y {u_mat:.3f}% ; {yrs_call:.2f}y {u_call:.3f}%")

# JLR's own market spread, from new issues priced at par in Mar-15 (3.5% 2020 ~5.0y; 3.875% 2023 ~8.0y; both priced at par per Ex.2 i=100)
s20 = 3.5 - tsy15["5YR"]; u8 = tsy15["7YR"] + (tsy15["10YR"]-tsy15["7YR"])/3; s23 = 3.875 - u8
print(f"JLR spread 2020 notes: {s20*100:.0f}bp; 2023 notes (8y UST {u8:.3f}): {s23*100:.0f}bp")
SPREAD = s20   # ASSUMPTION base: fixed spread = 193bp (JLR's own 5y new-issue spread)
print(f"Base-case spread = {SPREAD*100:.0f}bp")

def scen(label, y, cfs, T):
    dirty = price(SETTLE, cfs, y); clean = dirty - accrued
    return label, y, clean, dirty
res = []
y_m = (u_mat + SPREAD) / 100; res.append(scen("A. straight to 2021 maturity, UST(6.1y)+193bp", y_m, cf_mat, 0))
y_c = (u_call + SPREAD) / 100; res.append(scen("B. to first call (May-16 @104.0625), UST(1.1y)+193bp", y_c, cf_call, 0))
y_c2 = (tsy15["1YR"] + SPREAD) / 100
print(f"(1y UST 0.26% rather than interpolated {u_call:.3f}% gives yield {y_c2:.4%})")
print(f"{'scenario':58s} {'yield':>8s} {'clean':>9s} {'dirty':>9s}")
for l, y, cl, di in res: print(f"{l:58s} {y:8.4%} {cl:9.3f} {di:9.3f}")
price_A, price_B = res[0][2], res[1][2]
# rational price = holder's value: lower of the two (issuer can redeem at call price => value capped by call-based price)
P_CLEAN = min(price_A, price_B); P_DIRTY = P_CLEAN + accrued
print(f"\nHEADLINE (call-capped): clean {P_CLEAN:.3f}  dirty {P_DIRTY:.3f} per 100 face; premium over par {P_CLEAN-100:.2f}% (clean), {P_DIRTY-100:.2f}% (dirty)")
print(f"Case market indicative 111.276 clean => premium 11.28%; our headline vs market: {P_CLEAN-111.276:+.3f}")
print(f"Straight-bond price A premium: {price_A-100:.2f}% ; (value of issuer call option ~ {price_A-price_B:.2f} pts)")
# sensitivity to spread
print("\nSensitivity: spread bp -> clean price (B: to call | A: to maturity)")
for sp in [100, 150, 193, 250, 300, 400, 500]:
    pa = price(SETTLE, cf_mat, (u_mat+sp/100)/100) - accrued
    pb = price(SETTLE, cf_call, (u_call+sp/100)/100) - accrued
    print(f"  {sp:4d}bp  to-call {pb:8.3f} | to-maturity {pa:8.3f}")
# spread implied by market px 111.276
ytm_mkt = solve_y(SETTLE, cf_mat, 111.276 + accrued); ytc_mkt = solve_y(SETTLE, cf_call, 111.276 + accrued)
print(f"\nMarket 111.276 implies spread to UST: YTM {ytm_mkt*100-u_mat:.2f}% over {u_mat:.2f}%; YTC {ytc_mkt*100-u_call:.2f}% over {u_call:.2f}%")
# if call price were par instead
for cp in [100.0, 104.0625]:
    cfx = [(d, c) for d in cpn_dates if d <= CALL_DT] + [(CALL_DT, cp)]
    print(f"  call price {cp}: to-call clean at base spread {price(SETTLE,cfx,y_c)-accrued:.3f}")
# USD / GBP size
tot_usd = P_DIRTY/100*FACE_USD
print(f"\nTender cost for all US$410m: clean {P_CLEAN/100*FACE_USD:.2f} + accrued {accrued/100*FACE_USD:.2f} = US$ {tot_usd:.2f}m  (= GBP {tot_usd/FX:.2f}m at {FX})")
print(f"Premium over face (clean) US$ {(P_CLEAN-100)/100*FACE_USD:.2f}m = GBP {(P_CLEAN-100)/100*FACE_USD/FX:.2f}m")

# ---------- Q3 ----------
hdr("Q3: incremental cash flows (US$ m); old 410 @8.125% vs new 500 @3.5%")
# discount rate: JLR's current cost of debt for the bond horizon = new 5y yield 3.5% (priced at par)
R = 0.035
new_dates = semi_dates(date(2015, 9, 15), NEW_MAT)
def pvf(d, r=R): return 1 / (1 + r / 2) ** (d360(SETTLE, d) / 180)
def build(base):
    """base='mat' old notes would otherwise run to May-21; 'call' JLR would redeem 15-May-16 at call price"""
    ev = {}
    def add(d, k, v): ev.setdefault(d, {}).setdefault(k, 0.0); ev[d][k] += v
    add(SETTLE, "new_proceeds", NEW_FACE*(1-FEE)); add(SETTLE, "tender", -(P_DIRTY/100*FACE_USD))
    for d in new_dates:
        add(d, "new_coupon", -NEW_FACE*NEW_CPN/200)
    add(NEW_MAT, "new_principal", -NEW_FACE)
    cpn = FACE_USD*CPN/200
    if base == "mat":
        for d in cpn_dates: add(d, "old_coupon_saved", cpn)
        add(OLD_MAT, "old_principal_saved", FACE_USD)
    else:
        for d in cpn_dates:
            if d <= CALL_DT: add(d, "old_coupon_saved", cpn)
        add(CALL_DT, "old_principal_saved", FACE_USD*CALL_PX/100)
    return ev
cols = ["new_proceeds", "tender", "new_coupon", "new_principal", "old_coupon_saved", "old_principal_saved"]
for base in ["mat", "call"]:
    ev = build(base)
    print(f"\n--- Baseline: old notes {'run to 15-May-2021 maturity' if base=='mat' else 'called 15-May-2016 at '+str(CALL_PX)} ---")
    print(f"{'date':12s}" + "".join(f"{c[:13]:>14s}" for c in cols) + f"{'net':>10s}{'DF@3.5%':>9s}{'PV':>9s}")
    tot = 0.0; tot_nf = 0.0
    for d in sorted(ev):
        v = [ev[d].get(k, 0.0) for k in cols]; net = sum(v); pv = net * pvf(d); tot += pv
        print(f"{str(d):12s}" + "".join(f"{x:14.2f}" for x in v) + f"{net:10.2f}{pvf(d):9.4f}{pv:9.2f}")
    undisc = sum(sum(ev[d].values()) for d in ev)
    print(f"Sum undiscounted (US$m) {undisc:.2f} ; NPV @ {R:.2%} = US$ {tot:.2f}m (GBP {tot/FX:.2f}m)")
    if base == "mat":
        npv_mat = tot
        for r in [0.02, 0.035, 0.05, 0.06, 0.08125]:
            ev2 = ev
            print(f"   NPV at {r:.3%}: {sum(sum(ev2[d].values())*pvf(d, r) for d in ev2):8.2f}")
    else: npv_call = tot
# decomposition under 'mat': value of old debt vs price paid
def pv_old(r, cfs): return price(SETTLE, cfs, r)
print("\nDecomposition: PV of old notes (dirty) at 3.5% to maturity:", round(pv_old(0.035, cf_mat),3), "-> NPV of retiring at tender price per 100:", round(pv_old(0.035, cf_mat) - P_DIRTY, 3))
print("PV of old notes (dirty) at 3.5% to call:", round(pv_old(0.035, cf_call),3), " vs tender dirty", round(P_DIRTY,3))
# new debt PV at 3.5% = par => zero NPV by construction; fees
print(f"Issue fee at {FEE:.2%} on 500 = US$ {NEW_FACE*FEE:.2f}m")
# coupon (interest) savings on a like-for-like 410 basis
save_pa = FACE_USD*CPN/100 - FACE_USD*NEW_CPN/100
print(f"\nAnnual interest: old 410x8.125% = {FACE_USD*CPN/100:.2f}; new 500x3.5% = {NEW_FACE*NEW_CPN/100:.2f}; new 410x3.5% = {FACE_USD*NEW_CPN/100:.2f}")
print(f"Like-for-like annual saving on 410: US$ {save_pa:.2f}m (GBP {save_pa/FX:.2f}m); net of extra 90 borrowed: {FACE_USD*CPN/100-NEW_FACE*NEW_CPN/100:.2f}")
prem_cash = (P_DIRTY-100)/100*FACE_USD
print(f"Up-front premium + accrued over par: US$ {prem_cash:.2f}m ; simple payback on 410 interest saving: {(P_CLEAN-100)/100*FACE_USD/save_pa:.2f} years (clean premium only)")
evc = build("call")
print("NPV, call baseline, by discount rate:", {f"{r:.2%}": round(sum(sum(evc[d].values())*pvf(d, r) for d in evc),2) for r in [y_c, 0.03, 0.035, 0.05]})
FEE_save = FEE; 
print(f"(add back fee {NEW_FACE*FEE:.2f} for the no-fee case)")
# after-tax illustration: UK corp tax 20% (2015 UK main rate; Ex.4 effective FY14 = 622/2501)
print("Effective tax FY2014 (Ex.4):", round(622/2501, 4), " FY15 9m:", round(482/2218, 4))
print("Annual after-tax interest saving at 20%:", round(save_pa*0.8, 2), "US$ m")

# ---------- Q4 metrics ----------
hdr("Q4: effect on credit ratios (pro forma, GBP m, FY2015 9m balance sheet)")
add_debt_usd = NEW_FACE - FACE_USD; print("Net new debt US$", add_debt_usd, "= GBP", round(add_debt_usd/FX,1))
ebitda_ann = ebitda15*4/3
debt15 = 193 + 2230; 
int_old = 410*CPN/100/FX; int_new = 500*NEW_CPN/100/FX
print(f"Interest on this tranche: old GBP {int_old:.1f}m -> new GBP {int_new:.1f}m (diff {int_old-int_new:.1f}m)")
tot_cash_int = 500*8.25/100+400*5/100+263*8.125/100+321*5.625/100+450*4.125/100+321*4.25/100
print("Annual coupon on all senior notes (Ex.1) GBP m:", round(tot_cash_int,1))
print("After replacing 8.125% (GBP263m) by 3.5% on GBP333m (500/1.5):", round(tot_cash_int - 263*0.08125 + 500/FX*0.035, 1))
print("Ex.1 notes after deal: GBP", 2255-263+round(500/FX,1))
print("EBITDA FY15 9m annualised:", round(ebitda_ann), "; EBITDA/interest on notes ~", round(ebitda_ann/tot_cash_int,1), "x")
print("Equity value effect if tender below fair value: transfer =", "n/a (see answers)")
print("\nDONE")
