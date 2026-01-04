import numpy as np
from math import log,sqrt,exp
from scipy.stats import norm
from datetime import datetime

def _d1d2(S,K,T,r,vol):
    d1=(log(S/K)+(r+0.5*vol*vol)*T)/(vol*sqrt(T))
    d2=d1-vol*sqrt(T)
    return d1,d2

def call_price(S,K,T,r,vol):
    d1,d2=_d1d2(S,K,T,r,vol)
    return S*norm.cdf(d1)-K*exp(-r*T)*norm.cdf(d2)

def put_price(S,K,T,r,vol):
    return K*exp(-r*T)-S+call_price(S,K,T,r,vol)

def time_to_expiry(exp):
    dt=datetime.strptime(exp,"%m-%d-%Y")
    return max((dt-datetime.now()).days/365,1e-6)

def implied_vol(price,S,K,T,r):
    from scipy.optimize import brentq
    floor=call_price(S,K,T,r,1e-8)
    target=max(price,floor+1e-8)
    def f(v):
        return call_price(S,K,T,r,v)-target
    try:
        return brentq(f,1e-6,5.0)
    except:
        return np.nan

def cev_paths(S0,r,vol,gamma,T,n_p,n_s):
    dt=T/n_s
    Z=np.random.normal(0,1,(n_p,n_s))
    paths=np.zeros((n_p,n_s+1))
    paths[:,0]=S0
    for i in range(n_s):
        drift=r*paths[:,i]*dt
        diff=(vol*(paths[:,i]**gamma)*sqrt(dt)*Z[:,i])
        paths[:,i+1]=np.maximum(paths[:,i]+drift+diff,1e-8)
    return paths

def cev_call_price(S,K,r,vol,gamma,T,n_p,n_s):
    paths=cev_paths(S,r,vol,gamma,T,n_p,n_s)
    payoff=np.maximum(paths[:,-1]-K,0)
    pf=payoff.mean()
    return exp(-r*T)*pf
