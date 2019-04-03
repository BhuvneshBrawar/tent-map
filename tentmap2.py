import numpy as np
import matplotlib.pyplot as plt
xs=np.linspace(0,1,1001)
r=1.8
for x in xs:
    def f(x,r):
        if x<=0.5:
            return r*x
        else:
            return r-r*x
    

    plt.plot(x,f(x,r),'r.')
    plt.plot(x,f(f(x,r),r),'b.')
    #plt.plot(x,f(f(f(x,r),r),r),'k.')
    plt.plot(x,x,'g.')
plt.xlabel('$x_n$')
plt.ylabel('$x_{n+1}$')
plt.show()
