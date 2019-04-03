import numpy as np
import matplotlib.pyplot as plt
xs=np.linspace(0,1,1001)
r=2.0
def f(x,r):
    if x<=0.5:
        return r*x
    else:
        return r-r*x

Y=[f(x,r) for x in xs]
Z=[f(f(x,r),r) for x in xs]

plt.plot(xs,Y,'r')
plt.plot(xs,Z,'b')
plt.plot(xs,xs,'g')
plt.xlabel('$x_n$')
plt.ylabel('$x_{n+1}$')
plt.show()
