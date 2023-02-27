
import numpy as np

class pricingTree:
    class euroCall:
        def __init__(self, K, T, S, r, N, sigma):
            dt = T/N
            u = np.exp(sigma*np.sqrt(dt))
            d = np.exp(-sigma*np.sqrt(dt))
            p = (np.exp(r*dt)-d)/(u-d)
            disc = np.exp(-r*dt)
        
            self.K = K
            self.T = T
            self.dt = dt
            self.S = S
            self.r = r
            self.N = N
            self.u = u
            self.d = d
            self.p = p
            self.disc = disc

            # initialize asset prices at maturity
            self.St = [0]*(N+1)
            self.St[0] = S*(d**N)
            for i in range(1,N+1):
                self.St[i] = self.St[i-1]*u/d

            # initialize option values at maturity
            self.C = [0]*(N+1)
            for i in range(0,N+1):
                self.C[i] = max(self.St[i]-K,0)
        
        def computePrice(self):
            for i in range(self.N,-1,-1):
                for j in range(0,i):
                    self.C[j] = self.disc*(self.p*self.C[j+1]+(1-self.p)*self.C[j])
            return self.C[0]

K = 100
T = 1
S = 100
r = 0.05
N = 3
sigma = 0.2

a = pricingTree.euroCall(K,T,S,r,N,sigma)
print(f'$ {round(a.computePrice(),2)}')
