import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3

#Zad1
def rectangle_method(f,a,b,k):
    q=0
    n = int((a + b) / k)
    dx=(b-a)/n
    for i in range (n):
        if i <=n:
            sr=dx/2
            q=q+f((a+sr)+(i*dx))*dx
        if i>n:
            q = q * dx / 2
            break
    return q
i=rectangle_method(f,0,2,0.0001)
print(i)


#Zad1+wiz
def rectangle_method_vis(f,a,b,k):
    q=0
    l=0.00001
    fig=plt.figure()
    n=int((a+b)/l)
    x=np.linspace(a-.2,b+.2,n)
    y = f(x)
    plt.axvline(a, color='r', ls='--')
    plt.axvline(b, color='r', ls='--')
    plt.plot(x, y, color='b', linewidth=1)
    a1=int(a/k)
    b1=int(b/k)
    for i in range (a1,b1):
        x=i*k+k/2
        y=f(x)
        q+=y*k
        wx = [[x - k / 2],[ x - k / 2],[ x + k / 2],[x + k / 2], [x - k / 2]]
        wy = [0, y, y, 0, 0]
        plt.plot(wx, wy, color='r')
    fig.tight_layout()
    plt.title('Rectangle method')
    plt.grid()
    plt.show()
rectangle_method_vis(f,0,2,0.5)

#Zad 2

def trapezoidal_method(f,a,b,k):
    n=int((a+b)/k)
    dx = (b - a) /n
    s=0.5*f(a)+0.5*f(b)
    for i in range (1,n):
        if i<n:
            s=s+f(a+i*dx)
            i+=1
        else:
            s=(s+f(a)+f(b))/2*dx
            break
    s*=dx
    return s
i=trapezoidal_method(f,0,2,0.01)
print(i)

def trapezoidal_method_vis(f,a,b,k):
    s=0
    fig=plt.figure()
    l=0.00001
    n = int((b - a) / l)
    x=np.linspace(a-.2,b+.2,n)
    y=f(x)
    plt.axvline(a,color='r', ls='--')
    plt.axvline(b,color='r', ls='--')
    plt.plot(x, y)
    plt.grid()
    plt.title("trapezoidal method")
    for i in range (int(a/k),int(b/k)):
        xl=i*k
        xp=xl+k
        yl=f(xl)
        yp=f(xp)
        s+=(yl+yp)/2*k
        wx = [xl, xl, xp, xp, xl]
        wy = [0, yl, yp, 0, 0]
        plt.plot(wx, wy, color='r', linewidth=1)
    fig.tight_layout()
    plt.show()

trapezoidal_method_vis(f,0,2,0.5)


#Zad3 Monte carlo


def monte_carlo(a,b,n):
    k=0.1
    x=np.arange(a,b,k)
    y=f(x)
    s=0
    dx=b-a
    for i in range(1,n):
        if i<=n:
            x1 = np.random.uniform(a, b)
            s=s+f(x1)
            i+=1
        elif i>n:
            break
    return dx*s/n

mon=monte_carlo(0,2,10000)
print(mon)
