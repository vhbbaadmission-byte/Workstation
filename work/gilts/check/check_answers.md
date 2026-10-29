# UK Gilts independent check (Exhibit 1 + case text only)

Run `python3 check_calcs.py` to reproduce every number. Chart: `yield_curve.png`.

## Assumptions
- Annual coupons (case text says semi-annual in reality; Exhibit 1 treated as annual main answer). Price per £100 face, valuation on a coupon date (no accrued interest), so prices are clean = dirty. Coupons are fractions in the exhibit (3¼% = 3.25).
- Price = sum C/(1+y)^t + 100/(1+y)^n. YTM solved by bisection (no closed form). Semi-annual version: coupon/2 per half-year, YTM = annual rate compounded semi-annually (bond-equivalent yield).
- Q4: parallel shift of +1.00 percentage point (100bp) in every YTM; full repricing, compared with duration estimates.

## Q1 Coupon vs YTM
Coupon rate = fixed annual cash coupon / face; set at issue, never changes. YTM = the single discount rate that equates PV of all remaining cash flows to the market price (IRR if held to maturity, coupons reinvested at YTM); it moves with the market. Relationship is inverse: coupon > YTM gives price above par (premium), coupon = YTM gives par, coupon < YTM gives discount. Pull to par: premium/discount shrinks to 0 at maturity. Price is a convex, decreasing function of YTM. Check in table: 2y (5.25 > 1.74) premium 106.84; 5y (2.75 < 3.00) discount 98.86; 30y (4.50 > 4.36) 102.32; 50y (4.00 < 4.24) 94.96.

## Q2 Missing values (annual coupons)
| Maturity | Coupon % | Price | YTM % | Solved |
|---|---|---|---|---|
| 1 | 3.25 | 102.50 | 0.73 (0.7317) | YTM |
| 2 | 5.25 | 106.84 (106.8409) | 1.74 | Price |
| 3 | 4.50 | 107.02 | 2.06 (2.0628) | YTM |
| 5 | 2.75 | 98.86 (98.8551) | 3.00 | Price |
| 7 | 5.00 | 108.91 | 3.54 (3.5406) | YTM |
| 10 | 3.75 | 97.65 (97.6525) | 4.04 | Price |
| 20 | 4.75 | 104.93 | 4.38 (4.3751) | YTM |
| 30 | 4.50 | 102.32 (102.3185) | 4.36 | Price |
| 50 | 4.00 | 94.96 | 4.24 (4.2445) | YTM |

Worked example, 1-year: 102.50 = 103.25/(1+y), y = 103.25/102.50 - 1 = 0.7317%. 2-year: 5.25/1.0174 + 105.25/1.0174^2 = 5.1601 + 101.6808 = 106.8409.

Semi-annual version (same inputs):
| Maturity | Price (given/solved) | YTM % (semi-annual comp.) | Annual-basis comparison |
|---|---|---|---|
| 1 | 102.50 | 0.7362 | 0.7317 |
| 2 | 106.8699 | 1.74 | price 106.8409 |
| 3 | 107.02 | 2.0743 | 2.0628 |
| 5 | 98.8472 | 3.00 | price 98.8551 |
| 7 | 108.91 | 3.5512 | 3.5406 |
| 10 | 97.6336 | 4.04 | price 97.6525 |
| 20 | 104.93 | 4.3775 | 4.3751 |
| 30 | 102.3306 | 4.36 | price 102.3185 |
| 50 | 94.96 | 4.2437 | 4.2445 |
Differences are small (price <= 0.03; YTM <= 1.2bp). Premium bonds get slightly higher price under semi-annual (coupons come earlier), discount bonds slightly lower.

## Q3 Yield curve
Points (maturity, YTM%): (1, 0.73) (2, 1.74) (3, 2.06) (5, 3.00) (7, 3.54) (10, 4.04) (20, 4.38) (30, 4.36) (50, 4.24). Upward sloping steeply to ~10y, flattening, peak around 20y (4.38), then slightly humped/inverted at long end (30y 4.36, 50y 4.24). Caveat: these are YTMs of coupon bonds with different coupons (coupon effect), not spot rates; 50y gilt is illiquid (case). A proper curve would bootstrap spot rates. Plot: `yield_curve.png`.

## Q4 +1% in all yields (annual coupons)
| Mat | P0 | Mac D | Mod D | Convexity | P at y+1% | Chg % | Duration-only P | Dur+conv P |
|---|---|---|---|---|---|---|---|---|
| 1 | 102.50 | 1.0000 | 0.9927 | 1.97 | 101.49 | -0.98 | 101.48 | 101.49 |
| 2 | 106.84 | 1.9517 | 1.9183 | 5.61 | 104.82 | -1.89 | 104.79 | 104.82 |
| 3 | 107.02 | 2.8772 | 2.8191 | 10.89 | 104.06 | -2.77 | 104.00 | 104.06 |
| 5 | 98.86 | 4.7377 | 4.5997 | 26.31 | 94.44 | -4.47 | 94.31 | 94.44 |
| 7 | 108.91 | 6.1202 | 5.9109 | 43.54 | 102.70 | -5.70 | 102.47 | 102.71 |
| 10 | 97.65 | 8.4999 | 8.1698 | 81.56 | 90.06 | -7.78 | 89.67 | 90.07 |
| 20 | 104.93 | 13.5076 | 12.9414 | 223.70 | 92.45 | -11.89 | 91.35 | 92.52 |
| 30 | 102.32 | 17.1717 | 16.4543 | 389.11 | 87.31 | -14.67 | 85.48 | 87.47 |
| 50 | 94.96 | 21.7032 | 20.8195 | 701.03 | 78.11 | -17.74 | 75.19 | 78.52 |

Formulas: ModD = MacD/(1+y); dP/P ~ -ModD*dy + 0.5*Conv*dy^2 with dy = 0.01; Conv = [sum CF*t*(t+1)/(1+y)^(t+2)]/P (years^2). Estimate error (estimate - actual): duration-only understates the price (too low) by 0.01 (1y) to 2.92 (50y); with convexity error is +0.0001 to +0.41. Longer maturity and lower coupon mean higher duration and convexity; all prices fall, longer bonds fall most (-0.98% for 1y vs -17.74% for 50y). Duration-only is always too pessimistic for a rise (and too optimistic for a fall) because convexity is positive.

Semi-annual-basis actual changes for +1%: 1y -0.981%, 2y -1.888%, 3y -2.770%, 5y -4.513%, 7y -5.734%, 10y -7.856%, 20y -11.971%, 30y -14.749%, 50y -17.793% (similar to annual).

## Flags
- Exhibit 1's 1-year bond: YTM 0.73% is low vs 2y 1.74%; looks like the curve is built on mixed-coupon bonds.
- 50y bond YTM below 30y/20y: humped long end; illiquidity noted in case.
