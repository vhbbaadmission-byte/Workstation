# UK Gilts: gate 0 brief

## The case in plain words
May 2014. Petr Cech, a gilts trader at MU Securities, has nine UK government bonds maturing in 1 to 50 years. For each, the case gives the coupon and **either** the price **or** the yield to maturity, never both. He must fill in the missing number, see what yield curve the nine bonds trace, and work out how much each would lose if all yields rose by 1 percentage point. There's no company and no decision. It's a bond-maths and interest-rate-risk case, so the depth comes from explaining the concepts well and from linking them to what later happened in the gilt market.

## Exhibits (1), numbers in `work/gilts/exhibits.csv`
| # | What it is |
|---|---|
| 1 | 9 gilts: coupon (2¾%–5¼%), maturity (1–50 years), and either price (5 bonds: 102.50, 107.02, 108.91, 104.93, 94.96) or YTM (4 bonds: 1.74%, 3.00%, 4.04%, 4.36%). Prices are per £100 face. Source: IMD research |

The case PDF has only one exhibit. Pages 1–2 are text (from the UK Debt Management Office: what gilts are, semi-annual coupons, prices per £100 nominal). The spreadsheet `UK Gilts.xlsx` holds the same Exhibit 1 inputs with no conflicts. Its other tabs are someone's worked solution, which we won't use. Two helpers extracted the exhibit independently and every value agreed.

## Questions (4; the file lists them twice)
1. What is the difference between the coupon rate and the YTM, and how does it affect price?
2. Fill in the missing values in Exhibit 1.
3. Plot the yield curve.
4. What happens to the prices if all yields rise by 1%?

## CFA concepts we'll use (Level 1)
- Time value of money, bond pricing as PV of cash flows (QM LM02, FI LM06)
- Coupon vs YTM; premium, par and discount; solving for YTM (FI LM06, LM07); annual vs semi-annual yields (FI LM07)
- The yield curve: shape, spot vs par vs YTM curves, the coupon effect (FI LM09)
- Interest-rate risk: **Macaulay and modified duration, convexity**, the price-change approximation (FI LM10–LM12)
- Background: the gilt market and DMO (FI LM05), the risk-free rate and sovereign credit (FI LM15), Bank of England policy (Econ LM04)

## Our one-line answers (first pass, annual coupons as in Exhibit 1)
1. The coupon is fixed when the bond is issued. The YTM is the return the market demands today. When YTM < coupon the bond trades above par (premium); YTM > coupon gives a discount; when they are equal the price is par. Example: the 1-year 3¼% at 102.50 yields only **0.73%**.
2. **Missing values:**

   | Maturity (years) | 1 | 2 | 3 | 5 | 7 | 10 | 20 | 30 | 50 |
   |---|---|---|---|---|---|---|---|---|---|
   | Price | 102.50 | **106.84** | 107.02 | **98.86** | 108.91 | **97.65** | 104.93 | **102.32** | 94.96 |
   | YTM (%) | **0.73** | 1.74 | **2.06** | 3.00 | **3.54** | 4.04 | **4.38** | 4.36 | **4.24** |

   Bold = computed.
3. **The curve slopes up steeply to 10 years** (0.73% → 4.04%), peaks around 20 years (4.38%), then **dips slightly at 30–50 years** (4.36%, 4.24%). That is a humped curve with an inverted long end, typical of the UK, where pension funds buy long gilts heavily.
4. **Every price falls, and longer bonds fall much more:** 1-year −0.98%, 10-year −7.78%, 50-year −17.74%. Modified duration explains the ranking (0.99 → 20.82). Convexity explains why the long bonds fall *less* than duration alone predicts (50-year: duration says −20.8%, actual −17.7%).

These match the teaching note to within rounding. Its 50-year price is 94.97 against the case's 94.96, so its +1% price is 78.12 against our 78.11. **Solid.**

## Traps found
- **Annual vs semi-annual.** Exhibit 1's answers assume annual coupons, but real gilts pay semi-annually, as page 2 of the case itself says. We'll state the annual simplification on every calculation slide.
- Prices are **per £100 face** (the teaching note's Table 1 uses £1,000 face; don't mix them).
- **YTM curve ≠ spot curve.** Bonds with different coupons at the same maturity can have different YTMs, so the curve we plot is a YTM (approximately par) curve. Say so.
- **The +1% is a parallel shift** (all yields +1pp, e.g. 3.00% → 4.00%), not a 1% relative change.
- **Duration is a linear estimate.** The 50-year bond shows the error clearly, which is a good place to teach convexity.
- The 1-year yield (0.73%) sits close to Bank Rate (0.50% in 2014). Short yields are anchored by policy, long yields by inflation expectations and pension demand.

## Research plan (gate 1)
- Overview: what gilts are, gilt market size and holders (DMO, ONS), the Bank of England and QE (2009–2014), the UK's credit rating, the 2014 context (Bank Rate 0.5%).
- **Identify the real gilts behind Exhibit 1** if the coupons and maturities match DMO's list for May 2014 (e.g. 4% 2060, 4½% 2042, 4¾% 2030 look likely). That gives each bond a name and a fate for the epilogue.
- Epilogue: what rates did next (the 2016 lows, 2022 inflation and rate rises, the **2022 mini-budget and pension (LDI) crisis**, when long gilts lost very heavily and duration became front-page news); today's Bank Rate and gilt curve; the prices of our nine bonds (or their successors) now.
- Tools: web search and fetch both work. The Claude Slides artifact can be created.

## Questions for you (answered 2026-10-29)
- **Basis:** annual coupons as the main answer, plus one semi-annual comparison slide.
- **Names:** name a gilt only when the match with the DMO list is certain; otherwise keep the generic label.

### As asked
1. **Annual vs semi-annual.** Our recommendation is to keep **annual** as the main answer (it matches Exhibit 1 and the teaching note) and add **one comparison slide** with the semi-annual version, showing how small the difference is. The alternative is to do everything semi-annually as real gilts pay, at the cost of departing from the exhibit. Which do you want?
2. **Real gilt names.** If I can match Exhibit 1 to real gilts with confidence, may I name them on the slides (e.g. "4% Treasury Gilt 2060") and follow them in the epilogue? If a match is uncertain, I'll keep the generic "50-year 4%" label.
