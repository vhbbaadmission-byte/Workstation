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
SETTLE = date(2015, 3, 17)          # early settlement date (VERIFY: tender notice)
FINAL_SETTLE = date(2015, 3, 31)    # final settlement date (VERIFY)
LAST_CPN = date(2014, 11, 15)
MATURITY = date(2021, 5, 15)
CALL_DATE = date(2016, 5, 15)       # Exhibit 1: first call May 2016
CALL_PRICE = 104.0625               # VERIFY: assumed par + half the coupon (usual 10NC5 schedule)
TENDER_TOTAL = 112.352              # US$1,123.52 per US$1,000 incl. early premium (VERIFY)
TENDER_LATE = 109.352               # US$1,093.52 per US$1,000 (VERIFY)
EARLY_PREMIUM = 3.0                 # US$30 per US$1,000 (VERIFY)
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


if __name__ == "__main__":
    main()
