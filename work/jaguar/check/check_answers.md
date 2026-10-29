# Independent cross-check: Jaguar Land Rover bond case

Script: `check_calcs.py` (run `python3 check_calcs.py`; prints every number below). Worked from the case text, `exhibits.csv` only. Not opened: teaching note, review/, answers.md, calcs.py, sources.md.

## Assumptions (mine)
| Item | Choice | Why |
|---|---|---|
| Settlement | 31 Mar 2015 (tender expires 30 Mar, case p.1); new notes also treated as funded that day | simplest; 15-day gap to the 3.5% notes' actual issue is immaterial (<US$0.8m accrued) |
| Day count / compounding | 30/360, semi-annual, coupons 15 May / 15 Nov | US corporate convention; case says semi-annual |
| Accrued | 15 Nov 14 to 31 Mar 15 = 136 days, 4.0625 x 136/180 = **3.069 per 100** (US$12.58m on 410) | paid on top of clean price |
| Call | First call 15 May 2016 (Ex.1). Call price **104.0625 (par + half coupon)** is NOT in the case: external-convention assumption. Sensitivity with call at par given | the case gives only the date |
| Reference rate | UST curve 16 Mar 2015 (Ex.3; 5y = 1.57% printed; other tenors from Treasury CSV in exhibits.csv), linear interpolation | case names the May-2016 UST as reference |
| Credit spread | **193bp** = JLR's own new 3.5% 2020 notes (priced at par, Ex.2 "100 i") minus 5y UST 1.57%. Cross-check: 3.875% 2023 notes imply 191bp over interpolated 8y UST | same issuer, same week, market-given |
| FX | US$1.50 per GBP (Ex.1 note, March 2015 average); used only to convert to GBP | case instructs it; natural hedge so no FX risk |
| Fee on new issue | 1.25% of 500 = US$6.25m (assumption; case silent). Shown as a sensitivity | |
| Discount rate Q3 | 3.5% (JLR's marginal borrowing cost = yield on the new par notes); sensitivities 2%-8.125% | |
| Tax | Ignored in main table; note UK rate 20%; Ex.4 effective 21.7% FY15-9m, 24.9% FY14 | |

## Q1. Why could JLR borrow at under half the coupon?
Coupon 8.125% (2011) vs 3.5% (2015): fall of 462.5bp, new coupon = 43% of old.

Decomposition (coupon ≈ UST at same tenor + credit spread):
| | 2011 note | 2015 note | Change |
|---|---|---|---|
| Tenor | 10y | 5y | |
| UST yield | 3.15% (10y, 16-May-11) | 1.57% (5y, 16-Mar-15) | -158bp |
| Spread | 8.125-3.15 = 497bp | 3.5-1.57 = 193bp | **-304bp** |

The -158bp Treasury change splits into: pure level shift at the same 5y point 1.83% -> 1.57% = **-26bp (about 6% of the fall)**, and tenor/curve effect (2011 curve 10y 3.15 vs 5y 1.83) = **-132bp (about 29%)**. Credit spread compression is **-304bp, about 66%**. (Even a like-for-like 10y UST fell 105bp: 3.15 -> 2.10; the rest of that is not credit.)

So the "half the coupon" is mostly better credit and a shorter, cheaper tenor, not lower rates. Factors:
1. **Rating upgrades**: Moody's Ba3 -> Ba2 (Sept 2013); S&P BB; both outlooks "positive" late 2014 (case p.2).
2. **Operating improvement** (Ex.4, my EBITDA = revenue less operating costs plus capitalised development and other income; ties to PBT): revenue 13,512 -> 19,386 (FY12-FY14); EBITDA margin 14.8% -> 17.0% -> 18.1% (FY15 9m); PAT 1,460 -> 1,879.
3. **Leverage/liquidity** (Ex.5, 6): gross debt/EBITDA 0.99x (FY12) -> 0.61x (FY14), 0.63x (FY15 9m annualised); debt/equity 0.68 -> 0.36; net cash position (cash + deposits exceed debt; net debt -456 -> -1,604 £m); positive pre-dividend free cash (CFO less capex and intangibles: 1,090; 580; 1,066; 540 £m).
4. **Track record / debt maturity**: smoothly spread repayments, undrawn £1,485m revolver (Ex.1, case p.2), established bond investor base (six note issues outstanding, Ex.1).
5. **Lower tenor and call structure**: a 5y bullet with spread curve upward-sloping is cheaper than a 10y issue.
6. **Market-wide**: UST fell modestly at 5y (-26bp) and long end (-105bp at 10y); general low-yield environment and demand for yield (context, not in the case beyond Ex.3).
7. **2011 issue priced as a post-crisis re-entry** to high-yield with Ba3, the first-time-issuer premium; and Tata group parent.

Conclusion: spread compression (about 304bp) dominates; this is a credit-quality story, which is why existing bondholders already hold a bond priced far above par.

## Q2. Price at which holders would surrender US$410m 8.125% 2021 notes
Method (CFA L1 bond valuation): price = PV of remaining cash flows at the required yield; callable bond cannot be worth more than the PV of being called at the first call date (issuer would call once its yield is far below the coupon).

Cash flows per 100 face (semi-annual 4.0625): next coupon 15 May 2015, ... call 15 May 2016 at 104.0625 (plus that day's 4.0625), or maturity 15 May 2021 at 100.

| Basis | Yield | Clean | Dirty (+3.069) | Premium over par (clean) |
|---|---|---|---|---|
| A. To maturity (straight), UST 6.12y 1.756% + 193bp | 3.686% | 124.11 | 127.18 | 24.11% |
| **B. To first call at 104.0625, UST 1.12y 0.310% + 193bp** | **2.240%** | **110.44** | **113.51** | **10.44%** |
| Case market evidence (Ex.2 indicative, 4-Feb-15) | | 111.276 | 114.35 | 11.28% |
| (Ex.2, 7-Aug-14 line) | | 111.583 | | 11.58% |

**Headline: clean 110.44 per 100 (dirty 113.51); premium 10.4% (about 10-11%). Total for US$410m = US$452.8m clean + US$12.6m accrued = US$465.4m (£310.3m at 1.50).** Premium over face US$42.8m (£28.5m).

Reasoning: holders will not accept less than they could get from the market; in an efficient market that price is the call-capped value (B), which also matches the 111.28 quote (indicative price implies yield-to-maturity 5.90%, spread about 414bp, i.e. much wider than JLR's current 193bp: the market clearly prices the bond to the call, not to maturity). A 25-30% premium (basis A) would overpay by ignoring the call option: the option is worth about 13.7 points. Sensitivity (clean, to-call basis): spread 100bp 111.56; 193bp 110.44; 300bp 109.16; 500bp 106.83. If call price were par: 106.48 (call price assumption matters about 4 pts). Confidence: price level *debatable* (call price, spread); the 10-11% region *solid* because the market quote agrees.

## Q3. Incremental cash flows and savings
Old: US$410m, 8.125%, coupons 16.66m per half-year. New: US$500m, 3.5%, 8.75m per half-year, bullet 15 Mar 2020. Incremental cash flow = new-financing flows less old flows avoided (positive = JLR better off). Table (US$m; baseline = old notes would run to maturity), PV at 3.5% semi-annual:

| Date | Net | PV |
|---|---|---|
| 31 Mar 2015: +500 less 6.25 fee = 493.75; tender -465.38 | +28.37 | 28.37 |
| Each 15 May / 15 Nov to 2019: old coupon avoided +16.66 | | |
| Each 15 Mar / 15 Sep to 2019: new coupon -8.75 | | |
| 15 Mar 2020: new coupon and principal -508.75 | -508.75 | -428.34 |
| 15 May 2020, 15 Nov 2020: old coupons avoided | +16.66 each | |
| 15 May 2021: old coupon and principal avoided | +426.66 | +344.97 |
Full dated table with every period is printed by the script. Undiscounted sum +67.4; **NPV at 3.5% = +US$53.8m (£35.9m)** (no fee: +60.1m). NPV by rate: 2% 59.0; 5% 49.6; 8.125% 42.9.

Interpretation, two baselines:
- **Versus holding the old notes to 2021 at 8.125% (accounting/"headline" view):** annual interest falls from US$33.3m to US$17.5m (like-for-like on 410: 33.3 -> 14.4, saving US$19.0m = £12.6m a year, US$15.2m after 20% tax). Premium paid up front (US$42.8m clean) is repaid in about 2.3 years. On this view the strategy "saves" but it compares against an unrealistic status quo: it uses 3.5% to discount an 8.125% bond, so the saving is just the market value of the credit improvement that the premium already hands to holders (old notes worth 128.34 at 3.5% vs 113.51 paid = 14.83 points x 4.1 = US$60.8m, less fee 6.25 = 53.8: matches).
- **Versus the realistic alternative, calling the notes on 15 May 2016 at 104.0625:** NPV at 3.5% = **-US$13.1m** (no-fee -6.9m); at 5% +12.3m. At a consistent yield for each leg the tender at its fair price is roughly NPV = -fee. The tender at 113.51 dirty costs 1.5 points more than the call-based PV at 3.5% (112.0) but buys 14 months of earlier saving; net, near zero or slightly negative.
- Maturity/size mismatch: new notes are 500 vs 410 (+US$90m = £60m extra debt, held as cash/other uses) and mature one year earlier (Mar 2020 vs May 2021).

Conclusion: there are interest cost savings in cash terms (about US$16-19m a year), but little or no value creation: the premium paid transfers the benefit of the credit upgrade to the bondholders. *Debatable* (baseline). 

## Q4. Other benefits and who gains?
Other benefits to JLR:
- Lower interest expense raises EBIT cover and net income (about £10.5m a year on this tranche; senior-note coupon bill £132.9m -> £123.2m, Ex.1).
- Removes the high-coupon 2011 notes and any covenants they carry (covenants not in the case; assumption), re-sets maturity wall: 2021 obligation replaced by 2020; extra US$90m cash (£60m) boosts liquidity ahead of FY16 capex of £3.6-3.8bn (case p.2).
- Signals market access and credit strength; builds a deeper investor base; gets a more liquid benchmark issue (US$500m).
- Reduces the weighted average coupon (Ex.1: 5.89% on £2,255m of notes).
- Risks: net debt up US$90m; interest tax shield on premium paid (deductible? uncertain); refinancing 2020 at an uncertain future rate.

Value creation (efficient market view, Modigliani-Miller + CFA bond pricing):
- **Firm**: roughly zero NPV. Market value of old debt rises as credit improves, so buying it back at the (fair) market price just converts a 8.125% liability priced at 110-114 into a 3.5% liability at 100: no new value, apart from fees and (a) call-option exercise timing, (b) tax shield, (c) covenant relief. The case's own point: no free lunch in an efficient market.
- **Existing bondholders**: receive a premium of about 10% (US$42.8m) plus accrued: gain versus par but zero NPV versus their fair value at current yields; they lose the 8.125% income stream (reinvestment risk) and their upside is capped anyway by the 2016 call. Holders gain relative to the 2011 purchase price (par) because credit improved; those who roll over keep what they had.
- **Equity-holders**: gain only if the price paid is below fair value (wealth transferred from bondholders) or from the earlier-than-call timing; otherwise neutral. Lower fixed charges reduce financial risk (debt/EBITDA 0.6x already low). Interest saving (£12.6m a year) is offset by the up-front premium of about £28.5m, so equity value gain ≈ -fee at fair pricing. A small gain of the 2016 call timing if the bond is priced above the call-based value: ours says 110.4 vs market 111.3.

## Headline numbers
- Q1: spread 497bp -> 193bp (-304bp, 66% of the 462.5bp fall); Treasury level shift only -26bp (6%); tenor effect -132bp (29%).
- Q2: clean 110.44, dirty 113.51 per 100 face; premium 10.4%; US$465.4m total (£310.3m). Straight-to-maturity alternative 124.11 (24.1%).
- Q3: NPV at 3.5% +US$53.8m vs hold-to-maturity, -US$13.1m vs called in May 2016; annual interest saving about US$19.0m on 410 like-for-like.
- Q4: firm value roughly unchanged; bondholders gain ~10% premium; equity roughly neutral.
