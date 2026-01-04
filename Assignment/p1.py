import numpy as np
import matplotlib.pyplot as plt
import helper_function as hf

np.random.seed(100)

S0=100
r=0.02
vol=0.2
T=1.0
n_paths=50000
n_steps=252

gammas=[0.5,1.0,1.5]
time=np.linspace(0,T,n_steps+1)
fig,axes=plt.subplots(3,1,figsize=(12,12),sharex=True)
i=0
while i<len(gammas):
    g=gammas[i]
    paths=hf.cev_paths(S0,r,vol,g,T,n_paths,n_steps)
    j=0
    while j<10:
        axes[i].plot(time,paths[j])
        j=j+1

    axes[i].set_title("gamma="+str(g))
    axes[i].set_ylabel("Stock Price")
    i=i+1

axes[2].set_xlabel("Time (years)")
plt.tight_layout()
plt.savefig("cev_paths.png")
plt.show()
