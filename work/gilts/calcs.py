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


if __name__ == "__main__":
    main()
