import numpy as np
import scipy.stats as sts
import matplotlib.pyplot as plt
import helper_function as hf

S0=100
K=100
r=0.02
vol=0.2
T=1.0

n_paths=50000
n_steps=252
gammas=[0.5,1.0,1.5]

for g in gammas:
    np.random.seed(100)
    paths=hf.cev_paths(S0,r,vol,g,T,n_paths,n_steps)
    payoff=np.maximum(paths[:,-1]-K,0)
    disc=np.exp(-r*T)*payoff
    price=disc.mean()
    err=disc.std(ddof=1)/np.sqrt(n_paths)
    tval=sts.t.ppf(0.975,n_paths-1)
    ci_l=price-tval*err
    ci_u=price+tval*err
    iv=hf.implied_vol(price,S0,K,T,r)*100

    print("Gamma="+str(g))
    print("Price="+str(price))
    print("CI=("+str(ci_l)+","+str(ci_u)+")")
    print("Implied Vol="+str(iv))
    print("")

strike=[80,90,100,110,120]
gamma=0.5
ivs=[]
price=0
i=0
while i<len(strike):
    np.random.seed(100)
    k=strike[i]
    pr=hf.cev_call_price(S0,k,r,vol,gamma,T,n_paths,n_steps)
    iv=hf.implied_vol(pr,S0,k,T,r)*100
    ivs.append(iv)
    print("Strike="+str(k)+" Implied Volatility="+str(iv))
    i=i+1

plt.plot(strike,ivs)
plt.xlabel("Strike Price")
plt.ylabel("Implied Volatility")
plt.title("Volatility Smile")
plt.savefig("vol_smile.png")
plt.show()
