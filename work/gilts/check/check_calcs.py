"""Independent check: UK Gilts Exhibit 1. Annual coupons, per 100 face, valuation on a coupon date."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# (maturity yrs, coupon %, known price or None, known YTM % or None) -- Exhibit 1, work/gilts/exhibits.csv
BONDS = [
    (1, 3.25, 102.50, None), (2, 5.25, None, 1.74), (3, 4.50, 107.02, None),
    (5, 2.75, None, 3.00), (7, 5.00, 108.91, None), (10, 3.75, None, 4.04),
    (20, 4.75, 104.93, None), (30, 4.50, None, 4.36), (50, 4.00, 94.96, None),
]

def flows(n, c, m):          # m payments a year; n years
    k = int(round(n * m))
    return [(t / m, c / m + (100 if t == k else 0)) for t in range(1, k + 1)]

def price(n, c, y, m=1):
    return sum(cf / (1 + y / m) ** (t * m) for t, cf in flows(n, c, m))

def ytm(n, c, p, m=1):
    lo, hi = -0.5, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if price(n, c, mid, m) > p: lo = mid
        else: hi = mid
    return mid

def risk(n, c, y, m=1):
    """Macaulay (yrs), modified, convexity (yrs^2, annual-comp), all with m=1 formulas unless m>1."""
    P = price(n, c, y, m)
    mac = sum(t * cf / (1 + y / m) ** (t * m) for t, cf in flows(n, c, m)) / P
    mod = mac / (1 + y / m)
    conv = sum(cf * (t * m) * (t * m + 1) / (1 + y / m) ** (t * m + 2) for t, cf in flows(n, c, m)) / P / m**2
    return P, mac, mod, conv

print("=== Q2 annual coupons ===")
rows = []
for n, c, p, y in BONDS:
    if p is None:
        p = price(n, c, y / 100); filled = "price"
    else:
        y = ytm(n, c, p) * 100; filled = "ytm"
    rows.append((n, c, p, y, filled))
    print(f"{n:>2}y  cpn {c:5.2f}%  price {p:8.4f}  YTM {y:7.4f}%  (solved: {filled})  {'premium' if p>100 else 'discount' if p<100 else 'par'}")

print("\n=== Q2 semi-annual (coupon/2, YTM = annual rate comp. semi-annually) ===")
for n, c, p, y, f in rows:
    if f == "price":
        ps = price(n, c, y / 100, 2); ys = y
    else:
        ps = p; ys = ytm(n, c, p, 2) * 100
    print(f"{n:>2}y  cpn {c:5.2f}%  price {ps:8.4f}  YTM {ys:7.4f}%  (solved: {f})  [annual-basis: price {p:.4f}, YTM {y:.4f}]")

print("\n=== Q4 +1% (100bp) shift, annual ===")
print("n   P0      y0     Mac    Mod    Conv    P(+1%)  chg%    dur-est P  conv-est P")
q4 = []
for n, c, p, y, f in rows:
    P, mac, mod, cv = risk(n, c, y / 100)
    P1 = price(n, c, y / 100 + 0.01)
    dy = 0.01
    d_est = P * (1 - mod * dy)
    dc_est = P * (1 - mod * dy + 0.5 * cv * dy**2)
    q4.append((n, P, y, mac, mod, cv, P1, d_est, dc_est))
    print(f"{n:>2} {P:8.4f} {y:6.3f} {mac:7.4f} {mod:7.4f} {cv:9.4f} {P1:8.4f} {100*(P1/P-1):7.3f} {d_est:8.4f} {dc_est:8.4f}")
print("errors (estimate - actual): dur-only / dur+conv")
for n, P, y, mac, mod, cv, P1, de, dce in q4:
    print(f"{n:>2}  {de-P1:8.4f}  {dce-P1:8.4f}")

print("\n=== Q4 +1% semi-annual basis ===")
for n, c, p, y, f in rows:
    ys = y if f == "price" else ytm(n, c, p, 2) * 100
    P0 = price(n, c, ys / 100, 2); P1 = price(n, c, ys / 100 + 0.01, 2)
    print(f"{n:>2}  P0 {P0:8.4f}  P1 {P1:8.4f}  chg {100*(P1/P0-1):7.3f}%")

# Q3 plot
x = [r[0] for r in rows]; yv = [r[3] for r in rows]
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, yv, "o-", color="#3F3FBF")
for a, b in zip(x, yv): ax.annotate(f"{b:.2f}", (a, b), textcoords="offset points", xytext=(0, 7), ha="center", fontsize=9)
ax.set_xlabel("Maturity (years)"); ax.set_ylabel("Yield to maturity (% per year)")
ax.set_title("UK gilt yield curve from Exhibit 1 (annual coupons)")
ax.grid(alpha=.3); fig.tight_layout(); fig.savefig("yield_curve.png", dpi=150)
print("\nsaved yield_curve.png")
