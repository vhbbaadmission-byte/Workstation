"""UK Gilts: every calculation for the deck. Run: python3 work/gilts/calcs.py

Basis (user decision, gate 0): annual coupons as the main answer (as Exhibit 1),
plus one semi-annual comparison. Prices per GBP 100 face, valued on a coupon date.
All inputs come from work/gilts/exhibits.csv.
"""
import csv
from pathlib import Path

from scipy.optimize import brentq

HERE = Path(__file__).parent
SHIFT = 0.01  # Q4: every yield up by 1 percentage point (parallel shift)


# ---------- inputs ----------
def load_exhibit():
    rows = {}
    for r in csv.DictReader(open(HERE / "exhibits.csv")):
        if r["exhibit"] != "1" or not r["value"]:
            continue
        n = int(r["row"].split()[0])
        col = r["column"].strip().lower()
        try:
            rows.setdefault(n, {})[col] = float(r["value"])
        except ValueError:
            pass
    return dict(sorted(rows.items()))


# ---------- pricing ----------
def cash_flows(c, n, freq=1):
    """Coupon c in % of face; n years; returns [(t in years, cash flow)]."""
    k = int(n * freq)
    return [((i / freq), c / freq + (100 if i == k else 0)) for i in range(1, k + 1)]


def price(c, y, n, freq=1):
    """y = annual yield (decimal), compounded freq times a year."""
    return sum(cf / (1 + y / freq) ** (t * freq) for t, cf in cash_flows(c, n, freq))


def ytm(c, p, n, freq=1):
    return brentq(lambda y: price(c, y, n, freq) - p, -0.05, 0.50)


def macaulay(c, y, n, freq=1):
    p = price(c, y, n, freq)
    return sum(t * cf / (1 + y / freq) ** (t * freq) for t, cf in cash_flows(c, n, freq)) / p


def convexity(c, y, n):
    """Annual-pay convexity (CFA): sum t(t+1) PV(CF) / [P (1+y)^2]."""
    p = price(c, y, n)
    return sum(t * (t + 1) * cf / (1 + y) ** t for t, cf in cash_flows(c, n)) / (p * (1 + y) ** 2)


def main():
    ex = load_exhibit()
    print("=" * 78)
    print("EXHIBIT 1 INPUTS (per GBP 100 face)")
    for n, r in ex.items():
        print(f"  {n:>2}y  coupon {r['coupon']:.2f}%  price {r.get('price', '—')}  ytm {r.get('ytm', '—')}")

    # ---------- Q2: fill in the gaps (annual) ----------
    print("\n" + "=" * 78)
    print("Q2  MISSING VALUES, ANNUAL COUPONS")
    res = {}
    for n, r in ex.items():
        c = r["coupon"]
        if "price" in r:
            p = r["price"]
            y = ytm(c, p, n)
            src = "YTM solved"
        else:
            y = r["ytm"] / 100
            p = price(c, y, n)
            src = "price computed"
        res[n] = dict(c=c, p=p, y=y)
        tag = "premium" if p > 100.005 else "discount" if p < 99.995 else "par"
        print(f"  {n:>2}y  c={c:.2f}%  P={p:7.2f}  YTM={100*y:5.2f}%  ({src}; {tag}: YTM {'<' if y*100 < c else '>'} coupon)")

    # worked example 1: price from YTM (5-year 2.75% at 3.00%)
    print("\n  Worked example A: 5-year 2.75% gilt, YTM 3.00%  ->  price")
    c, y, n = 2.75, 0.03, 5
    tot = 0
    for t, cf in cash_flows(c, n):
        df = 1 / (1 + y) ** t
        tot += cf * df
        print(f"    year {t:.0f}: CF {cf:7.2f} x 1/1.03^{t:.0f} ({df:.4f}) = {cf*df:7.2f}   running {tot:7.2f}")
    print(f"    price = {tot:.2f}")

    # worked example 2: YTM from price (1-year 3.25% at 102.50) - closed form
    print("\n  Worked example B: 1-year 3.25% gilt, price 102.50  ->  YTM")
    print(f"    102.50 = 103.25 / (1 + y)  ->  1 + y = 103.25 / 102.50 = {103.25/102.50:.6f}  ->  y = {100*(103.25/102.50-1):.2f}%")

    # worked example 3: YTM by trial (3-year 4.5% at 107.02)
    print("\n  Worked example C: 3-year 4.5% gilt, price 107.02  ->  YTM by trial and error")
    for g in (0.02, 0.021, res[3]["y"]):
        print(f"    try y = {100*g:.3f}%: price = {price(4.5, g, 3):.4f}")
    print(f"    YTM = {100*res[3]['y']:.2f}%")

    # ---------- semi-annual comparison ----------
    print("\n" + "=" * 78)
    print("Q2  COMPARISON: SEMI-ANNUAL COUPONS (yield quoted annually, compounded twice a year)")
    for n, r in ex.items():
        c = r["coupon"]
        if "price" in r:
            ys = ytm(c, r["price"], n, 2)
            print(f"  {n:>2}y  price {r['price']:.2f} given:  YTM annual-pay {100*res[n]['y']:.2f}%  vs semi-annual {100*ys:.2f}%  (diff {10000*(ys-res[n]['y']):+.0f}bp)")
        else:
            ps = price(c, r["ytm"] / 100, n, 2)
            print(f"  {n:>2}y  YTM {r['ytm']:.2f}% given:  price annual-pay {res[n]['p']:.2f}  vs semi-annual {ps:.2f}  (diff {ps-res[n]['p']:+.2f})")

    # ---------- Q3: yield curve ----------
    print("\n" + "=" * 78)
    print("Q3  YIELD CURVE POINTS (YTM, annual)")
    ys = [(n, 100 * v["y"]) for n, v in res.items()]
    for (n, y), (_, yp) in zip(ys, [(None, None)] + ys[:-1]):
        print(f"  {n:>2}y  {y:5.2f}%" + ("" if yp is None else f"   change vs previous {100*(y-yp):+5.0f}bp"))
    print(f"  slope 1y->10y: {100*(res[10]['y']-res[1]['y'])*100:+.0f}bp ; 10y->20y: {10000*(res[20]['y']-res[10]['y']):+.0f}bp ;"
          f" 20y->50y: {10000*(res[50]['y']-res[20]['y']):+.0f}bp")

    # ---------- Q4: +1% ----------
    print("\n" + "=" * 78)
    print("Q4  ALL YIELDS +1 PERCENTAGE POINT")
    print("  mat  P0      y0     y1     P1      dP      %dP     MacD   ModD   Conv     dur-only  dur+conv")
    for n, v in res.items():
        c, p0, y0 = v["c"], v["p"], v["y"]
        y1 = y0 + SHIFT
        p1 = price(c, y1, n)
        mac = macaulay(c, y0, n)
        mod = mac / (1 + y0)
        cvx = convexity(c, y0, n)
        est1 = -mod * SHIFT
        est2 = est1 + 0.5 * cvx * SHIFT ** 2
        v.update(p1=p1, mac=mac, mod=mod, cvx=cvx)
        print(f"  {n:>2}y {p0:7.2f} {100*y0:5.2f}% {100*y1:5.2f}% {p1:7.2f} {p1-p0:+7.2f} {100*(p1/p0-1):+7.2f}%"
              f"  {mac:5.2f}  {mod:5.2f} {cvx:7.2f}   {100*est1:+7.2f}%  {100*est2:+7.2f}%")

    print("\n  Worked example D: 10-year 3.75% gilt, YTM 4.04% -> 5.04%")
    c, n, y0 = 3.75, 10, res[10]["y"]
    print(f"    P0 = {res[10]['p']:.2f};  P1 = {res[10]['p1']:.2f};  change = {100*(res[10]['p1']/res[10]['p']-1):.2f}%")
    print(f"    Macaulay D = {res[10]['mac']:.2f} years; modified D = {res[10]['mac']:.2f}/(1+{y0:.4f}) = {res[10]['mod']:.2f}")
    print(f"    duration estimate = -{res[10]['mod']:.2f} x 1% = {-res[10]['mod']:.2f}%")
    print(f"    + convexity: 0.5 x {res[10]['cvx']:.2f} x 0.01^2 = +{100*0.5*res[10]['cvx']*1e-4:.2f}%  ->  {-res[10]['mod']+100*0.5*res[10]['cvx']*1e-4:.2f}%")
    extras(res)
    strict_extras(res)


def extras(res):
    line = "=" * 78
    print("\n" + line)
    print("EXTRA (grader, gate 1)")
    # current yield vs coupon vs YTM
    print("  Coupon rate vs current yield vs YTM")
    for n, v in res.items():
        print(f"    {n:>2}y  coupon {v['c']:.2f}%  current yield {100*v['c']/v['p']:.2f}%  YTM {100*v['y']:.2f}%")
    # annuity form
    print("  Annuity form: P = C x [1-(1+y)^-N]/y + 100/(1+y)^N")
    for n, v in res.items():
        c, y = v["c"], v["y"]
        ann = (1 - (1 + y) ** -n) / y
        pvp = 100 / (1 + y) ** n
        print(f"    {n:>2}y  {c:.2f} x {ann:.4f} + 100/{(1+y)**n:.4f} = {c*ann:.2f} + {pvp:.2f} = {c*ann+pvp:.2f}")
    # interpolation for yield search
    print("  Linear interpolation then reprice check (price-given bonds)")
    for n in (3, 7, 20, 50):
        c, p = res[n]["c"], res[n]["p"]
        lo = int(res[n]["y"] * 100) / 100       # bracket by whole percent
        hi = lo + 0.01
        plo, phi = price(c, lo, n), price(c, hi, n)
        yi = lo + (plo - p) / (plo - phi) * (hi - lo)
        print(f"    {n:>2}y  y={100*lo:.2f}% -> {plo:.2f};  y={100*hi:.2f}% -> {phi:.2f};  interpolate: {100*lo:.2f}% + ({plo:.2f}-{p:.2f})/({plo:.2f}-{phi:.2f}) x 1% = {100*yi:.3f}%"
              f"  | exact {100*res[n]['y']:.3f}%  | reprice at exact = {price(c, res[n]['y'], n):.2f}")
    # approximate convexity and duration from +/- 1bp... use CFA approximation with dy = 1%
    print("  CFA approximations with dy = 1%: ApproxModDur = (P- - P+)/(2 x P0 x dy); ApproxCon = (P- + P+ - 2P0)/(P0 x dy^2)")
    for n in (1, 10, 50):
        c, p0, y = res[n]["c"], res[n]["p"], res[n]["y"]
        pm, pp = price(c, y - 0.01, n), price(c, y + 0.01, n)
        print(f"    {n:>2}y  P- {pm:.2f}  P+ {pp:.2f}  P0 {p0:.2f}  ApproxModDur {(pm-pp)/(2*p0*0.01):.2f}  ApproxCon {(pm+pp-2*p0)/(p0*1e-4):.2f}")
    # -1% scenario and asymmetry
    print("  -1% vs +1% (asymmetry from convexity)")
    for n, v in res.items():
        c, p0, y = v["c"], v["p"], v["y"]
        dn, up = price(c, y - 0.01, n), price(c, y + 0.01, n)
        print(f"    {n:>2}y  -1%: {dn:7.2f} ({100*(dn/p0-1):+6.2f}%)   +1%: {up:7.2f} ({100*(up/p0-1):+6.2f}%)")
    # money on a GBP 1m face holding and PVBP
    print("  Money change on GBP 1,000,000 face, and PVBP (price value of a basis point) per GBP 1m face")
    for n, v in res.items():
        c, p0, y = v["c"], v["p"], v["y"]
        dm = (price(c, y + 0.01, n) - p0) * 10000
        pvbp = (price(c, y - 0.0001, n) - price(c, y + 0.0001, n)) / 2 * 10000
        print(f"    {n:>2}y  value {p0*10000:,.0f}  change at +1% {dm:+,.0f}  PVBP {pvbp:,.0f}")
    # bootstrapped spot and implied forward rates from 1,2,3-year bonds
    z1 = res[1]["y"]
    c2, p2 = res[2]["c"], res[2]["p"]
    z2 = ((100 + c2) / (p2 - c2 / (1 + z1))) ** 0.5 - 1
    c3, p3 = res[3]["c"], res[3]["p"]
    z3 = ((100 + c3) / (p3 - c3 / (1 + z1) - c3 / (1 + z2) ** 2)) ** (1 / 3) - 1
    f11 = (1 + z2) ** 2 / (1 + z1) - 1
    f21 = (1 + z3) ** 3 / (1 + z2) ** 2 - 1
    print("  Bootstrapped spot rates and implied 1-year forwards")
    print(f"    z1 = {100*z1:.2f}%")
    print(f"    z2: {p2:.2f} = {c2}/(1+{z1:.4f}) + {100+c2}/(1+z2)^2  ->  z2 = {100*z2:.2f}%")
    print(f"    z3: {p3:.2f} = {c3}/(1+z1) + {c3}/(1+z2)^2 + {100+c3}/(1+z3)^3  ->  z3 = {100*z3:.2f}%")
    print(f"    1y forward in 1 year (1y1y) = (1+z2)^2/(1+z1) - 1 = {100*f11:.2f}%;  2y1y = {100*f21:.2f}%")

    # reinvestment risk: 20-year 4.75% bought at 104.93 (YTM 4.38%), held to maturity
    print("  Reinvestment risk: 20-year 4.75% gilt bought at 104.93, held 20 years")
    c, p0, n = 4.75, res[20]["p"], 20
    for r in (res[20]["y"], 0.02, 0.0):
        fv = sum(c * (1 + r) ** (n - t) for t in range(1, n + 1)) + 100
        print(f"    coupons reinvested at {100*r:.2f}%: end value {fv:.2f}; realised return ({fv:.2f}/{p0:.2f})^(1/20) - 1 = {100*((fv/p0)**(1/n)-1):.2f}%")
    # coupon effect: same maturity, different coupon (hypothetical 10y 0% and 8% at 4.04%)
    print("  Coupon effect on rate risk (hypothetical 10-year bonds at 4.04%)")
    for c in (0.0, 3.75, 8.0):
        y = res[10]["y"]
        p0, p1 = price(c, y, 10), price(c, y + 0.01, 10)
        print(f"    coupon {c:.2f}%  P0 {p0:.2f}  +1% {p1:.2f}  change {100*(p1/p0-1):+.2f}%  ModD {macaulay(c, y, 10)/(1+y):.2f}")


def strict_extras(res):
    print("\n" + "=" * 78)
    print("STRICT REVIEW ADDITIONS (gate 1)")
    # reinvestment FV formula
    c, p0, n = 4.75, res[20]["p"], 20
    for r in (res[20]["y"], 0.02):
        f = ((1 + r) ** n - 1) / r
        fv = c * f + 100
        print(f"  FV of coupons at {100*r:.2f}%: 4.75 x [(1+r)^20 - 1]/r = 4.75 x {f:.2f} = {c*f:.2f}; + 100 = {fv:.2f};"
              f" realised return = ({fv:.2f}/{p0:.2f})^(1/20) - 1 = {100*((fv/p0)**(1/n)-1):.2f}%")
    # semi-annual worked example: 2-year at 1.74%
    print("  Semi-annual worked example: 2-year 5.25% at 1.74% a year = 0.87% per half-year")
    tot = 0
    for k in range(1, 5):
        cf = 2.625 + (100 if k == 4 else 0)
        df = 1 / 1.0087 ** k
        tot += cf * df
        print(f"    half-year {k}: {cf:7.3f} x 1/1.0087^{k} ({df:.6f}) = {cf*df:7.3f}")
    print(f"    price = {tot:.2f} (annual-pay 106.84)")
    # Macaulay duration step tables for all nine
    for n, v in res.items():
        c, y, p0 = v["c"], v["y"], v["p"]
        rows = [(t, cf, cf / (1 + y) ** t) for t, cf in cash_flows(c, n)]
        mac = sum(t * pv for t, cf, pv in rows) / p0
        print(f"  Duration {n}y (c {c}%, y {100*y:.2f}%, P {p0:.2f}): MacD = sum(t x PV)/P = {sum(t*pv for t,cf,pv in rows):.2f}/{p0:.2f} = {mac:.2f};"
              f" ModD = {mac:.2f}/(1+{y:.4f}) = {mac/(1+y):.2f}")
        if n in (5, 50):
            show = rows if n == 5 else rows[:3] + rows[-2:]
            for t, cf, pv in show:
                print(f"      t={t:>4.0f}  CF {cf:7.2f}  PV {pv:7.2f}  weight {pv/p0:.4f}  t x weight {t*pv/p0:.4f}")
    # analytic convexity step: 10y and 50y
    for n in (10, 50):
        c, y, p0 = res[n]["c"], res[n]["y"], res[n]["p"]
        sm = sum(t * (t + 1) * cf / (1 + y) ** t for t, cf in cash_flows(c, n))
        print(f"  Convexity {n}y: sum[t(t+1) x PV(CF)] / [P x (1+y)^2] = {sm:.1f} / ({p0:.2f} x {(1+y)**2:.4f}) = {sm/(p0*(1+y)**2):.2f}")
    # -1% worked (50y) and money on GBP 100m face
    c, y, p0 = 4, res[50]["y"], res[50]["p"]
    ann = (1 - (1 + y - 0.01) ** -50) / (y - 0.01)
    print(f"  -1% worked, 50y: y = {100*(y-0.01):.2f}%: 4 x {ann:.4f} + 100/{(1+y-0.01)**50:.4f} = {4*ann:.2f} + {100/(1+y-0.01)**50:.2f} = {price(4, y-0.01, 50):.2f} ({100*(price(4,y-0.01,50)/p0-1):+.2f}%)")
    print("  Money on GBP 100m face: value, change at +1%, PVBP (GBP m)")
    for n, v in res.items():
        c, p0, y = v["c"], v["p"], v["y"]
        print(f"    {n:>2}y  value £{p0:.1f}m  +1%: £{price(c, y+0.01, n)-p0:+.1f}m  PVBP £{(price(c,y-0.0001,n)-price(c,y+0.0001,n))/2:.3f}m")
    c, y = 4, res[50]["y"]
    print(f"  PVBP worked, 50y: [P(y-0.01%) - P(y+0.01%)]/2 = [{price(c,y-0.0001,50):.4f} - {price(c,y+0.0001,50):.4f}]/2 = {(price(c,y-0.0001,50)-price(c,y+0.0001,50))/2:.4f} per £100 -> £{(price(c,y-0.0001,50)-price(c,y+0.0001,50))/2:.4f}m per £100m")
    # real-bond test: 4% Treasury Gilt 2060 (DMO 9 May 2014: clean 114.76, yield 3.364984%, ModD 22.24)
    y0, y1, p_then, p_now, md = 3.364984, 5.737, 114.76, 75.28, 22.24
    print(f"  Real bond, 4% 2060: yield {y0:.2f}% -> {y1:.2f}% (+{100*(y1-y0):.0f}bp); duration-only estimate -{md} x {(y1-y0)/100:.4f} = {-md*(y1-y0):.1f}%;"
          f" actual {p_then} -> {p_now} = {100*(p_now/p_then-1):.1f}%  [latest price/yield secondary source, verify]")


if __name__ == "__main__":
    main()
