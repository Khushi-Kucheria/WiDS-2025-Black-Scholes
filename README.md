# WiDS-2025 Black-Scholes

## Concepts Learned

### Fundamentals of European Options
- Gained an understanding of derivative instruments and their applications in financial markets
- Studied the two main categories of options:
  - Call options
  - Put options
- Learned essential terminology associated with options:
  - Strike price
  - Premium
  - Expiration date
  - Volatility
  - Risk-free interest rate
- Analyzed option moneyness classifications:
  - In the Money (ITM)
  - At the Money (ATM)
  - Out of the Money (OTM)

### Black–Scholes Model (Theory)
- Examined the core assumptions underlying the Black–Scholes framework
- Understood the lognormal behavior of the stock price relative to the strike price
- Studied how time to maturity and volatility influence option valuation
- Derived and interpreted pricing parameters such as `d1`, `d2`, and the option Greeks

## Work Done (Coding)

### Study of the CEV Model
- Identified the limitation of the Black–Scholes model in assuming constant volatility
- Explored the Constant Elasticity of Variance (CEV) model, which allows volatility to vary with the stock price level

### Assignment Implementation
- Simulated stock price paths using the CEV model with the Euler–Maruyama discretization method
- Conducted Monte Carlo simulations and statistical analysis using the following configuration:
  - Total simulated paths: **50,000** (`n_paths`)
  - Number of time steps per path: **252** (`n_steps`)
  - Gamma values considered: **[0.5, 1, 1.5]**
  - Fixed random seed (**42**) to ensure reproducibility
- Developed all required functions within the `function.py` module
- Estimated stock prices based on the parameters specified in the assignment
- Computed pricing standard errors for each gamma value
- Constructed **95% confidence intervals** for the estimated option prices
- For **gamma = 0.5**, varied the strike price while keeping other parameters fixed to generate a volatility smile or skew plot

## Results and Observations
- **Gamma = 1** was found to closely replicate the Black–Scholes setting with constant volatility
- For **gamma = 0.5**, the resulting smile or skew pattern was more pronounced at lower strike prices due to elevated implied volatility
- Overall, the CEV model was observed to capture market behavior more realistically than the Black–Scholes model
