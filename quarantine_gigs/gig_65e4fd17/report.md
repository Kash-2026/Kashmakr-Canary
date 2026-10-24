# Engagement Questions

## Question 1: What is the annualized return of the investment portfolio?
To calculate the annualized return, we use the `annualized_return` function from the financial engine. This function takes the initial investment value, final investment value, and the number of periods as inputs.

## Question 2: What is the Sharpe ratio of the investment portfolio?
The Sharpe ratio is calculated using the `calculate_sharpe_ratio` function. This function requires the portfolio's return, the risk-free rate, and the portfolio's standard deviation as inputs.

## Question 3: What is the Net Present Value (NPV) of the investment?
The NPV is determined using the `calculate_npv` function. This function takes the discount rate and a series of cash flows as inputs.

## Question 4: What is the Internal Rate of Return (IRR) of the investment?
The IRR is calculated using the `calculate_irr` function. This function requires a series of cash flows as input.

## Question 5: What is the Yield to Maturity (YTM) of a bond in the portfolio?
The YTM is determined using the `calculate_ytm` function. This function takes the bond's face value, current price, coupon rate, and time to maturity as inputs.

## Question 6: What is the Macaulay Duration of a bond in the portfolio?
The Macaulay Duration is calculated using the `macaulay_duration` function. This function requires the bond's cash flows and yield to maturity as inputs.

## Question 7: What is the Modified Duration of a bond in the portfolio?
The Modified Duration is determined using the `modified_duration` function. This function takes the bond's Macaulay Duration and yield to maturity as inputs.

## Question 8: What is the bond's convexity?
Bond convexity is calculated using the `bond_convexity` function. This function requires the bond's cash flows and yield to maturity as inputs.

## Question 9: What is the portfolio's Value at Risk (VaR)?
The VaR is determined using the `value_at_risk` function. This function takes the portfolio's returns and a confidence level as inputs.

## Question 10: What is the portfolio's expected shortfall?
The expected shortfall is calculated using the `expected_shortfall` function. This function requires the portfolio's returns and a confidence level as inputs.