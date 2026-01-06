# WiDS-2025 Black-Scholes

## Concepts Learnt:-
### Basics of Options (European):-
   - What options are and why they are used in financial markets
   - Types of Options:-
      - Call options
      - Put options
   - Key terms related to options:-
      - Strike price
      - Premium
      - Expiry
      - Volatility
      - Risk-free interest rate
   - Moneyness of options:-
       - In the money (ITM)
       - At the money (ATM)
       - Out of the money (OTM)
### Black-Scholes Model (Theory):-
   - Assumptions in Black Scholes Model
   - Lognormal distribution of (stock price/strike price)
   - Effect of time and volatility in option pricing
   - Derivation and formulas for paramters like d1,d2,options greeks,etc
  
## Work Done (Coding):-
### Exploring the CEV model:-
   - Black Scholes assumes constant volatility but in real life volatility is not constant.
   - CEV model allows the volatility to depend on current stock price.
### Solved the Assignment:-
   - Implemented the CEV stock price using the Euler–Maruyama method and did simulations and statistical analysis with the         following setup:
      - Number of simulated paths:- 50000 (n_paths)
      - Times steps per path:- 252 (n_steps)
      - Gamma for which calculation and simulation were done:- [0.5,1,1.5]
      - Random seed was kept fixed at 42 for reproductibility
      - Implemented all required functions in function.py file
      - Estimated stock price using paramters given in assignemnt
      - Calculated the standard error in pricing for each gamma
      - Reported the 95% confidence interval for the price calculated
   - At gamma=0.5 varied the strike price keeping other parameters same to obtain the smile or skew shaped plot
## Results and Observations:-
   - Gamma=1 very closely represents Black scholes model (constant volatility)
   - For gamma=0.5 obtained a smile or skew plot which was caused at lower strike prices because they cause higher implied         volatility
   - CEV model represents real life option market better than Black Scholes model 


