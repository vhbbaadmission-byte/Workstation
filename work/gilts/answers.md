# UK Gilts: answers (gate 1)

All numbers come from `work/gilts/calcs.py` (run it to see every step). Inputs: `work/gilts/exhibits.csv`.

## Basis and assumptions
- **Annual coupons** for the main answers, as Exhibit 1 implies (user decision, gate 0). Real gilts pay semi-annually; one comparison slide shows the difference is tiny (≤ 0.03 in price, ≤ 1bp in yield).
- Prices per **£100 face**. Each bond is valued on a coupon date, so there is no accrued interest and price = PV of the remaining cash flows.
- YTM = the single discount rate that makes the PV equal the price (an IRR). Solved by trial and error (bisection); the 1-year bond has a closed form.
- **+1% = a parallel shift of +1 percentage point** in every YTM.

## Q1. Coupon rate vs YTM, and the effect on price — *solid*
- The **coupon rate** is fixed at issue: it sets the cash the bond pays (e.g. £4.75 a year per £100 for the 20-year bond).
- The **YTM** is the return the market demands **today** for the bond's risk and maturity. It is the discount rate in the price formula.
- Price = Σ C/(1+y)^t + 100/(1+y)^N, so a higher y gives a lower price (inverse relationship).
  - YTM < coupon → price > 100 (**premium**): 6 of our 9 bonds (e.g. 1-year: 3.25% coupon, 0.73% YTM, price 102.50).
  - YTM > coupon → price < 100 (**discount**): 5-year (2.75% vs 3.00%, 98.86), 10-year (3.75% vs 4.04%, 97.65), 50-year (4.00% vs 4.24%, 94.96).
  - YTM = coupon → par (none here exactly).
- Why they differ: rates have moved since issue. High-coupon gilts were issued when rates were higher (before 2008). Premium/discount pulls to par as maturity approaches.

## Q2. Missing values — *solid*
| Maturity (years) | 1 | 2 | 3 | 5 | 7 | 10 | 20 | 30 | 50 |
|---|---|---|---|---|---|---|---|---|---|
| Coupon (%) | 3.25 | 5.25 | 4.50 | 2.75 | 5.00 | 3.75 | 4.75 | 4.50 | 4.00 |
| Price (£ per £100) | 102.50 | **106.84** | 107.02 | **98.86** | 108.91 | **97.65** | 104.93 | **102.32** | 94.96 |
| YTM (%) | **0.73** | 1.74 | **2.06** | 3.00 | **3.54** | 4.04 | **4.38** | 4.36 | **4.24** |

Bold = computed. Worked examples in calcs.py: A (5-year price from YTM, year-by-year discounting), B (1-year YTM, closed form), C (3-year YTM by trial and error).

Semi-annual comparison: prices 106.87 / 98.85 / 97.63 / 102.33; YTMs 0.74 / 2.07 / 3.55 / 4.38 / 4.24 (%).

## Q3. The yield curve — *solid on the numbers, debatable on the explanation*
- Points: 0.73, 1.74, 2.06, 3.00, 3.54, 4.04, 4.38, 4.36, 4.24 (%).
- **Steep rise to 10 years** (+331bp from 1 to 10 years), **flattening to 20 years** (+34bp), then a **slight fall to 50 years** (−13bp): an upward-sloping curve with a humped, gently inverted long end.
- Reading (CFA term-structure theories):
  - Short end anchored by Bank Rate at 0.5% (2014); markets expected rate rises → upward slope (expectations theory, plus a term premium for liquidity preference).
  - Long end pulled down by heavy demand from UK pension funds and insurers that must match long liabilities (preferred habitat / market segmentation). The 50-year gilt is also less liquid.
- Caveat: this is a curve of **coupon-bond YTMs**, not spot rates; bonds with different coupons at the same maturity would show slightly different YTMs (coupon effect).

## Q4. All yields +1% — *solid*
| Maturity | 1 | 2 | 3 | 5 | 7 | 10 | 20 | 30 | 50 |
|---|---|---|---|---|---|---|---|---|---|
| Price before | 102.50 | 106.84 | 107.02 | 98.86 | 108.91 | 97.65 | 104.93 | 102.32 | 94.96 |
| Price after | 101.49 | 104.82 | 104.06 | 94.44 | 102.70 | 90.06 | 92.45 | 87.31 | 78.11 |
| Change (%) | −0.98 | −1.89 | −2.77 | −4.47 | −5.70 | −7.78 | −11.89 | −14.67 | −17.74 |
| Modified duration | 0.99 | 1.92 | 2.82 | 4.60 | 5.91 | 8.17 | 12.94 | 16.45 | 20.82 |
| Convexity | 1.97 | 5.61 | 10.89 | 26.31 | 43.54 | 81.56 | 223.70 | 389.11 | 701.03 |
| Duration-only estimate (%) | −0.99 | −1.92 | −2.82 | −4.60 | −5.91 | −8.17 | −12.94 | −16.45 | −20.82 |
| Duration + convexity (%) | −0.98 | −1.89 | −2.76 | −4.47 | −5.69 | −7.76 | −11.82 | −14.51 | −17.31 |

- Every price falls (inverse relationship). The fall grows with maturity: longer bonds have more distant cash flows, so a higher discount rate hits them harder. **Duration** measures this: %ΔP ≈ −ModD × Δy.
- Duration alone overstates the fall for long bonds (50-year: −20.82% estimated vs −17.74% actual). The price-yield curve is convex; adding ½ × Convexity × (Δy)² closes most of the gap (−17.31%).
- Implication: in 2014, holding a 50-year gilt meant ~18 times the rate risk of a 1-year gilt for ~3.5 points more yield. Lesson for the epilogue: 2022.

## Independent check (sonnet helper, from the case only)
`work/gilts/check/`. **Every number agrees** with ours to the displayed precision: all prices, YTMs, Macaulay/modified duration, convexity and +1% prices, annual and semi-annual. No differences to explain.

## Teaching note comparison
- Matches its Exhibit 1 (annual) and Exhibit 2 (semi-annual) to within rounding.
- Its 50-year price shows **94.97** where the case gives **94.96**; hence its +1% price 78.12 vs our 78.11. We use the case's 94.96.
- Its Table 2 shows 30-year original yield "4.36%" and 20-year "4.38%"; the same as ours.
