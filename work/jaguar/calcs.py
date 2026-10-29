"""Jaguar Land Rover 2015 refinancing: every calculation for the deck.
Run: python3 work/jaguar/calcs.py

User decisions (gate 0): Q2 leads with the call-aware value; all bond maths in US$,
converted to GBP once at the case's 1.50.
Conventions (CFA FI LM06): prices per 100 face; semi-annual coupons; 30/360 day count;
full (dirty) price = flat (clean) price + accrued interest; discounting in coupon periods.
Inputs marked VERIFY are assumptions until confirmed in work/jaguar/sources*.md.
"""
from datetime import date

from scipy.optimize import brentq

# ---------- inputs ----------
FACE = 410.0            # US$m, Exhibit 1
OLD_CPN = 8.125         # % a year, Exhibit 1
NEW_CPN = 3.5           # % a year, case p.1
NEW_FACE = 500.0        # US$m, case p.1
FX = 1.50               # US$ per GBP, March 2015, Exhibit 1 note
MKT_PRICE = 111.276     # Exhibit 2, last traded 04/02/2015 (indicative)
MKT_DATE = date(2015, 2, 4)
SETTLE = date(2015, 3, 17)          # early settlement date (JLR release, sources_research A)
FINAL_SETTLE = date(2015, 3, 31)    # final settlement date (JLR release)
LAST_CPN = date(2014, 11, 15)
MATURITY = date(2021, 5, 15)
CALL_DATE = date(2016, 5, 15)       # Exhibit 1: first call May 2016
CALL_PRICE = 104.0625               # par + half coupon; reproduces the tender price to the cent (OM prints 104.663%, a typo)
TENDER_TOTAL = 112.352              # US$1,123.52 per US$1,000 incl. early premium (JLR pricing release 16 Mar 2015)
TENDER_LATE = 109.352               # US$1,093.52 per US$1,000 (same release)
EARLY_PREMIUM = 3.0                 # US$30 per US$1,000 (same release)
REF_YIELD = 0.395                   # % 0.25% UST due 15 May 2016, 10:00 NY 16 Mar 2015 (same release)
FIXED_SPREAD = 0.50                 # % (same release)
TENDERED = 326.417                  # US$m, final results 31 Mar 2015 (79.61%)
TENDERED_EARLY = 326.117            # US$m, early results 17 Mar 2015 (79.54%)
TAX = 0.20                          # UK main corporation tax rate from 1 Apr 2015 (Finance Act 2013 s.6)
MATURITY_ALT = date(2021, 11, 15)   # maturity per Tata Motors SEC 6-K (case says 15 May 2021): user to decide
# US Treasury par yields, % (Exhibit 3 rebuilt from home.treasury.gov)
UST_2011 = {"5Y": 1.83, "10Y": 3.15}
UST_2015 = {"5Y": 1.57, "7Y": 1.90, "10Y": 2.10, "1Y": 0.26}


# ---------- helpers ----------
def days360(d1, d2):
    """30/360 (US) day count."""
    a, b = min(d1.day, 30), d2.day
    if a == 30 and b == 31:
        b = 30
    return 360 * (d2.year - d1.year) + 30 * (d2.month - d1.month) + (b - a)


def accrued(settle, cpn=OLD_CPN, last=LAST_CPN):
    t = days360(last, settle)
    return t, t / 180 * cpn / 2


def coupon_dates(first, last):
    out, y, m = [], first.year, first.month
    while True:
        d = date(y, m, 15)
        out.append(d)
        if d >= last:
            return out
        m += 6
        if m > 12:
            m, y = m - 12, y + 1


def full_price(y, settle, end, redemption, cpn=OLD_CPN, last=LAST_CPN):
    """PV at settle of the coupons to `end` plus `redemption`, at annual yield y (s.a. compounding)."""
    nxt = coupon_dates(date(last.year + (last.month + 6 > 12), (last.month + 6 - 1) % 12 + 1, 15), end)
    w = (180 - days360(last, settle)) / 180       # fraction of a period to the next coupon
    pv = 0.0
    for i, d in enumerate(nxt):
        cf = cpn / 2 + (redemption if d == end else 0)
        pv += cf / (1 + y / 2) ** (i + w)
    return pv


def clean_price(y, settle, end, redemption):
    return full_price(y, settle, end, redemption) - accrued(settle)[1]


def solve_y(clean, settle, end, redemption):
    return brentq(lambda y: clean_price(y, settle, end, redemption) - clean, -0.05, 0.5)


def main():
    line = "=" * 78
    # ---------------- Q1 ----------------
    print(line, "\nQ1  WHY THE COUPON HALVED: TREASURY LEVEL vs TENOR vs CREDIT SPREAD")
    s11 = OLD_CPN - UST_2011["10Y"]
    s15 = NEW_CPN - UST_2015["5Y"]
    print(f"  2011: 10-year note at {OLD_CPN:.3f}% vs 10Y UST {UST_2011['10Y']:.2f}%  -> spread {100*s11:.0f}bp")
    print(f"  2015:  5-year note at {NEW_CPN:.3f}% vs  5Y UST {UST_2015['5Y']:.2f}%  -> spread {100*s15:.0f}bp")
    drop = OLD_CPN - NEW_CPN
    lvl = UST_2011["10Y"] - UST_2015["10Y"]
    ten = UST_2015["10Y"] - UST_2015["5Y"]
    spr = s11 - s15
    print(f"  total fall {100*drop:.0f}bp = Treasury level (10Y {UST_2011['10Y']:.2f}->{UST_2015['10Y']:.2f}) {100*lvl:.0f}bp"
          f" + shorter tenor (10Y->5Y in 2015) {100*ten:.0f}bp + credit spread {100*spr:.0f}bp")
    print(f"  shares: level {lvl/drop:.0%}, tenor {ten/drop:.0%}, credit {spr/drop:.0%}")
    print(f"  like for like at 5 years: UST {UST_2011['5Y']:.2f}% -> {UST_2015['5Y']:.2f}% = {100*(UST_2011['5Y']-UST_2015['5Y']):.0f}bp only")

    # old bond's own market yield (Exhibit 2 price)
    ytm_mkt = solve_y(MKT_PRICE, MKT_DATE, MATURITY, 100)
    ytc_mkt = solve_y(MKT_PRICE, MKT_DATE, CALL_DATE, CALL_PRICE)
    print(f"  old 8.125% 2021 at {MKT_PRICE} ({MKT_DATE}): YTM {100*ytm_mkt:.2f}%, yield to first call {100*ytc_mkt:.2f}%"
          f" -> yield-to-worst {100*min(ytm_mkt, ytc_mkt):.2f}%")

    # ---------------- Q2 ----------------
    print(line, "\nQ2  WHAT PRICE WOULD HOLDERS ACCEPT?  (per 100 face, settle", SETTLE, ")")
    t, ai = accrued(SETTLE)
    t2, ai2 = accrued(FINAL_SETTLE)
    print(f"  accrued interest (30/360): {t} days/180 x {OLD_CPN/2:.4f} = {ai:.4f}  -> US${10*ai:.2f} per US$1,000")
    print(f"  at final settlement {FINAL_SETTLE}: {t2} days -> {ai2:.4f} -> US${10*ai2:.2f} per US$1,000")
    w = (180 - t) / 180
    print(f"  fraction of a period to next coupon (15 May 2015): (180-{t})/180 = {w:.4f}")

    # A: naive, to maturity at the new 3.5% rate
    pA = clean_price(NEW_CPN / 100, SETTLE, MATURITY, 100)
    print(f"\n  A  to maturity (May 2021) at JLR's new rate 3.50%: full {pA+ai:.2f}, clean {pA:.2f} -> premium {pA-100:.2f}%")
    # B: to first call at 3.5%
    pB = clean_price(NEW_CPN / 100, SETTLE, CALL_DATE, CALL_PRICE)
    print(f"  B  to first call (May 2016 at {CALL_PRICE}) at 3.50%: clean {pB:.2f} -> premium {pB-100:.2f}%")
    # C: market
    print(f"  C  market (Exhibit 2): clean {MKT_PRICE:.2f}")
    # D: tender formula - implied discount yield to the call date
    yD = solve_y(TENDER_TOTAL, SETTLE, CALL_DATE, CALL_PRICE)
    yD_ex = solve_y(TENDER_TOTAL - EARLY_PREMIUM, SETTLE, CALL_DATE, CALL_PRICE)
    print(f"  D  actual tender: total {TENDER_TOTAL:.2f} (incl. early premium {EARLY_PREMIUM:.2f}), late {TENDER_LATE:.2f}")
    print(f"     yield to call implied by {TENDER_TOTAL:.3f}: {100*yD:.2f}%;  by {TENDER_TOTAL-EARLY_PREMIUM:.3f} (ex premium): {100*yD_ex:.2f}%")
    print("     step table for D (discounting to call at the implied yield):")
    tot = 0
    for i, (d, cf) in enumerate([(date(2015, 5, 15), 4.0625), (date(2015, 11, 15), 4.0625), (CALL_DATE, 4.0625 + CALL_PRICE)]):
        df = 1 / (1 + yD_ex / 2) ** (i + w)
        tot += cf * df
        print(f"       {d}: CF {cf:8.4f} x DF {df:.6f} = {cf*df:8.4f}")
    print(f"       full {tot:.4f} - accrued {ai:.4f} = clean {tot-ai:.4f}")

    print("\n  sensitivity: clean value to call vs discount yield")
    for y in (0.005, 0.0075, 0.01, 0.015, 0.02, 0.025, 0.03, 0.035):
        print(f"     {100*y:4.2f}%  to call {clean_price(y, SETTLE, CALL_DATE, CALL_PRICE):7.2f}   to maturity {clean_price(y, SETTLE, MATURITY, 100):7.2f}")

    # ---------------- Q3 ----------------
    print(line, "\nQ3  INCREMENTAL CASH FLOWS (US$m, whole US$410m bought at the early tender price)")
    pay_clean = FACE * TENDER_TOTAL / 100
    pay_ai = FACE * ai / 100
    prem = pay_clean - FACE
    print(f"  cash paid now: clean {pay_clean:.1f} (premium {prem:.1f}, of which early-tender {FACE*EARLY_PREMIUM/100:.1f}) + accrued {pay_ai:.1f}"
          f" = {pay_clean+pay_ai:.1f}")
    print(f"  accounting view: annual coupon on US$410m {FACE*OLD_CPN/100:.1f} -> {FACE*NEW_CPN/100:.1f}"
          f" (saving {FACE*(OLD_CPN-NEW_CPN)/100:.1f} a year); premium {prem:.1f} = {prem/(FACE*(OLD_CPN-NEW_CPN)/100):.1f} years of savings")
    print(f"  GBP at {FX}: premium £{prem/FX:.1f}m; annual saving £{FACE*(OLD_CPN-NEW_CPN)/100/FX:.1f}m; face £{FACE/FX:.1f}m")

    # build per-period table: funding the full dirty repurchase cost with new 3.5% debt to keep t0 = 0
    B = pay_clean + pay_ai
    print(f"\n  new 3.5% debt needed to fund the purchase: {B:.1f} (coupon {B*NEW_CPN/200:.2f} every 15 Mar/15 Sep, principal Mar 2020)")
    rows = []
    for d in coupon_dates(date(2015, 5, 15), MATURITY):
        rows.append((d, FACE * OLD_CPN / 200 + (FACE if d == MATURITY else 0), 0.0))
    d = date(2015, 9, 15)
    while d <= date(2020, 3, 15):
        rows.append((d, 0.0, B * NEW_CPN / 200 + (B if d == date(2020, 3, 15) else 0)))
        d = date(d.year + (d.month == 9), 3 if d.month == 9 else 9, 15)
    rows.sort()

    def npv(rate, old_end):
        tot = 0
        for d, old, new in rows:
            if old and d > old_end:
                continue
            o = old + (FACE * CALL_PRICE / 100 if (old_end == CALL_DATE and d == CALL_DATE) else 0)
            tt = days360(SETTLE, d) / 180
            tot += (o - new) / (1 + rate / 2) ** tt
        return tot

    print("  date        old avoided   new paid   incremental (+ = JLR better off)")
    for d, old, new in rows:
        print(f"  {d}   {old:9.2f}  {new:9.2f}   {old-new:+9.2f}")
    print("  NPV of incremental flows (US$m):")
    for r in (0.035, NEW_CPN / 100):
        pass
    for label, end in (("old held to 2021", MATURITY), ("old called May 2016", CALL_DATE)):
        for r in (0.035, yD_ex):
            print(f"     {label:20s} @ {100*r:4.2f}%: {npv(r, end):+8.1f}")

    # simple, slide-friendly version: value of the old debt to JLR vs cash paid (clean)
    print("\n  slide version (per 100 face): NPV = value of old debt avoided - price paid (clean)")
    for label, v in (("A to maturity @3.50%", pA), ("B to call @3.50%", pB), ("market", MKT_PRICE),
                     ("tender ex early premium", TENDER_TOTAL - EARLY_PREMIUM)):
        print(f"     {label:24s} {v:7.2f} - {TENDER_TOTAL:.2f} = {v-TENDER_TOTAL:+6.2f}  -> x4.10 = US${4.10*(v-TENDER_TOTAL):+6.1f}m")

    # ---------------- Q4 ----------------
    print(line, "\nQ4  WHO GAINS?  (US$m on US$410m face unless stated)")
    gain_bh = FACE * (TENDER_TOTAL - MKT_PRICE) / 100
    print(f"  bondholders vs market price: ({TENDER_TOTAL:.2f}-{MKT_PRICE:.2f}) x 4.10 = {gain_bh:+.1f}")
    print(f"  bondholders vs being called May 2016 (value to call @3.50% {pB:.2f}): x4.10 = {FACE*(TENDER_TOTAL-pB)/100:+.1f}")
    print(f"  extra US$90m raised beyond the US$410m face = new borrowing, not refinancing: {NEW_FACE-FACE:.0f}")
    ebit_proxy = 2218 + 13 - 36   # FY15 9m PBT + net finance expense - finance income (Exhibit 4), GBP m
    print(f"  interest cover proxy FY15 9m: (PBT {2218} + finance exp {13} - finance inc {36}) = £{ebit_proxy}m (for ratio slides)")


def extras():
    line = "=" * 78
    print(line, "\nEXTRA (grader, gate 1)")
    # tender formula from the documents
    y = (REF_YIELD + FIXED_SPREAD) / 100
    p = clean_price(y, SETTLE, CALL_DATE, CALL_PRICE)
    print(f"  tender formula: discount to 15 May 2016 call at {REF_YIELD:.3f}% + {FIXED_SPREAD:.2f}% = {100*y:.3f}% -> clean {p:.4f} -> US${10*p:.2f} per US$1,000 (published 1,123.52)")
    print(f"  late price = total - early premium = {10*(p-EARLY_PREMIUM):.2f}")
    paid_e = TENDERED_EARLY * TENDER_TOTAL / 100
    paid_l = (TENDERED - TENDERED_EARLY) * TENDER_LATE / 100
    ai_e, ai_l = TENDERED_EARLY * accrued(SETTLE)[1] / 100, (TENDERED - TENDERED_EARLY) * accrued(FINAL_SETTLE)[1] / 100
    print(f"  actual cash: early {TENDERED_EARLY} x 112.352% = {paid_e:.2f} + late {TENDERED-TENDERED_EARLY:.3f} x 109.352% = {paid_l:.2f}; accrued {ai_e+ai_l:.2f}; total {paid_e+paid_l+ai_e+ai_l:.2f}")
    print(f"  left outstanding {FACE-TENDERED:.3f}; called May 2016 at {CALL_PRICE}: {(FACE-TENDERED)*CALL_PRICE/100:.2f}")
    # maturity conflict
    for m in (MATURITY, MATURITY_ALT):
        print(f"  maturity {m}: hold-to-maturity value @3.50% {clean_price(0.035, SETTLE, m, 100):.2f}; YTM at market 111.276: {100*solve_y(MKT_PRICE, MKT_DATE, m, 100):.2f}%")
    # Exhibit 2: other old bond (GBP 8.25% 2020, first call Mar 2016)
    # FX implied in Exhibit 1
    print(f"  Exhibit 1 implied FX: 410/263 = {410/263:.3f}, 500/321 = {500/321:.3f}, 700/450 = {700/450:.3f}  (case uses 1.50 for March 2015)")
    # new debt size
    need = FACE * (TENDER_TOTAL + accrued(SETTLE)[1]) / 100
    print(f"  cash needed to buy all US$410m: {need:.1f}; new issue {NEW_FACE:.0f}; surplus before fees {NEW_FACE-need:.1f}")
    print(f"  interest: old {FACE*OLD_CPN/100:.2f} vs new on 410 {FACE*NEW_CPN/100:.2f} vs new on {need:.1f} {need*NEW_CPN/100:.2f} -> saving like-for-like funding {FACE*OLD_CPN/100-need*NEW_CPN/100:.2f} a year")
    # after-tax NPV, per 100 face, two baselines, discount at after-tax cost of new debt
    rt = NEW_CPN / 100 * (1 - TAX)
    w = (180 - accrued(SETTLE)[0]) / 180
    prem = TENDER_TOTAL - 100
    def pv_old_after_tax(end, redemption):
        dates = coupon_dates(date(2015, 5, 15), end)
        pv = 0
        for i, d in enumerate(dates):
            cf = OLD_CPN / 2 * (1 - TAX) + (redemption if d == end else 0)
            if d == end and redemption > 100:
                cf -= (redemption - 100) * TAX      # call premium is deductible
            pv += cf / (1 + rt / 2) ** (i + w)
        return pv - accrued(SETTLE)[1] * (1 - TAX)  # accrued part of first coupon is paid either way
    cost_now = TENDER_TOTAL - prem * TAX                # premium deductible now
    for label, end, red in (("hold to May 2021", MATURITY, 100), ("call May 2016", CALL_DATE, CALL_PRICE)):
        v = pv_old_after_tax(end, red)
        print(f"  after-tax @ {100*rt:.2f}%: value of old debt avoided ({label}) {v:.2f} - after-tax cost {cost_now:.2f} = {v-cost_now:+.2f} per 100 -> US${4.1*(v-cost_now):+.1f}m")
    # FCF and cash interest cover from Exhibits 4-5 (GBP m)
    cfo = {"FY12": 2500, "FY13": 2429, "FY14": 3422, "FY15 9m": 2572}
    ppe = {"FY12": 596, "FY13": 891, "FY14": 1201, "FY15 9m": 1147}
    intang = {"FY12": 814, "FY13": 958, "FY14": 1155, "FY15 9m": 885}
    fin = {"FY12": 128, "FY13": 179, "FY14": 269, "FY15 9m": 97}
    div = {"FY12": 0, "FY13": 150, "FY14": 150, "FY15 9m": 150}
    pbt = {"FY12": 1479, "FY13": 1674, "FY14": 2501, "FY15 9m": 2218}
    da = {"FY12": 465, "FY13": 622, "FY14": 875, "FY15 9m": 743}
    finexp = {"FY12": 85, "FY13": 18, "FY14": 185, "FY15 9m": 13}
    fininc = {"FY12": 16, "FY13": 34, "FY14": 38, "FY15 9m": 36}
    fx = {"FY12": 14, "FY13": -109, "FY14": 236, "FY15 9m": 58}
    rev = {"FY12": 13512, "FY13": 15784, "FY14": 19386, "FY15 9m": 16040}
    for k in cfo:
        fcf = cfo[k] - ppe[k] - intang[k]
        ebitda = pbt[k] + da[k] + finexp[k] - fininc[k] - fx[k]
        print(f"  {k}: FCF {cfo[k]}-{ppe[k]}-{intang[k]} = {fcf}; after finance paid & dividends {fcf-fin[k]-div[k]};"
              f" EBITDA {pbt[k]}+{da[k]}+{finexp[k]}-{fininc[k]}-({fx[k]}) = {ebitda} ({100*ebitda/rev[k]:.1f}%); EBITDA/cash finance {ebitda/fin[k]:.1f}x")

    # balance-sheet and P&L ratios (Exhibits 4 and 6, GBP m)
    bs = {"FY12": (2430, 0, 490, 1484, 2924), "FY13": (2072, 775, 328, 1839, 3539),
          "FY14": (2260, 1199, 167, 1843, 5864), "FY15 9m": (2884, 1143, 193, 2230, 6797)}
    for k, (c, d, st, lt, eq) in bs.items():
        print(f"  {k}: net cash {c}+{d}-{st}-{lt} = {c+d-st-lt}; debt/equity ({st}+{lt})/{eq} = {(st+lt)/eq:.2f};"
              f" tax rate {[19,460,622,482][list(bs).index(k)]}/{pbt[k]} = {100*[19,460,622,482][list(bs).index(k)]/pbt[k]:.1f}%;"
              f" capitalised dev {[751,860,1030,850][list(bs).index(k)]} = {100*[751,860,1030,850][list(bs).index(k)]/pbt[k]:.0f}% of PBT")
    print(f"  growth FY12->FY14: revenue {100*(rev['FY14']/rev['FY12']-1):.1f}%, PBT {100*(pbt['FY14']/pbt['FY12']-1):.1f}%")
    print(f"  Exhibit 1 excess coupon vs 2015 coupons (GBP m/yr): 263 x (8.125-3.5)% = {263*0.04625:.1f}; 500 x (8.25-3.875)% = {500*0.04375:.1f}; total {263*0.04625+500*0.04375:.1f}")
    print(f"  issuer call value implied: straight {clean_price(0.035, SETTLE, MATURITY, 100):.2f} - market {MKT_PRICE:.2f} = {clean_price(0.035, SETTLE, MATURITY, 100)-MKT_PRICE:.2f}; - tender {TENDER_TOTAL:.2f} = {clean_price(0.035, SETTLE, MATURITY, 100)-TENDER_TOTAL:.2f}")


if __name__ == "__main__":
    main()
    extras()
