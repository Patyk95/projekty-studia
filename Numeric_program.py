from math import fabs
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
#Zad1
def f(x):
    return (x-2)**3- x**2 +2*x


def bisection_method(f,a,b,eps,max_iter):

    if f(a)*f(b)>0:
        return None, print('Funkcja nie spełnia wymagań')
    for i in range(0,max_iter):
        if fabs (b-a)>eps and i <= max_iter:
            c=(a+b)/2
            if f(c)==0:
                return c
                break
            if f(c)*f(a)<0:
                b=c
            if f(c)*f(b)<0:
                a=c
        else:
            if fabs (c)<eps:
                return c
            if i> max_iter:
                return None
    return (c)


l=bisection_method(f,1.5,3,10**-4,100)
print(l)

#Zad 1+wizualizacja
def f(x):
    return (x-2)**3- x**2 +2*x

def bisection_method_vis(f,a,b,eps,max_iter):
    plt.axvline(a)
    plt.axvline(b)
    xcz = np.arange(a, b, 0.0000001)
    plt.plot(xcz, f(xcz), 'r')
    plt.xlabel("X")
    plt.ylabel('Y')
    if f(a)*f(b)>0:
        return None, print('Funkcja nie spełnia wymagań')
    for i in range(0,max_iter):
        if fabs (b-a)>eps and i <= max_iter:
            c=(a+b)/2
            plt.axvline(c)
            if f(c)==0:
                plt.axvline(c)
                return c
                break
            if f(c)*f(a)<0:
                b=c
            if f(c)*f(b)<0:
                a=c
        else:
            if fabs (c)<eps:
                return c
            if i> max_iter:
                return None
    plt.title(c)
    plt.show()
    return c

bisection_method_vis(f,1.5,3,10**-4,100)

#Zad2
def f2(x):
    return ((x-2)**2)-1

def golden_section(f2,a,b,eps,max_iter):
    k=(sqrt(5)-1)/2
    xl=b-k*(b-a)
    xr=a+k*(b-a)
    c=(a+b)/2
    f=f2
    for i in range (max_iter):
        if (b-a)>eps:
            if f(xl)<f(xr):
                b=xr
                xr=xl
                xl=b-k*(b-a)
            else:
                a=xl
                xl=xr
                xr=a+k*(b-a)
            if (b - a) < eps:
                c = (a + b) / 2
                break
        if i>max_iter:
            return None
    return c

i=golden_section(f2,0,5,10**-4,100)
print(i)

#Zad2+wizualizacja


def golden_section_vis(f2,a,b,eps,max_iter):
    plt.axvline(a)
    plt.axvline(b)
    f=f2
    k=(sqrt(5)-1)/2
    xl=b-k*(b-a)
    plt.axvline(xl)
    xr=a+k*(b-a)
    plt.axvline(xr)
    x = np.arange(a, b, 0.0000001)
    plt.plot(x, f2(x), 'y')
    c=(a+b)/2
    for i in range (max_iter):
        if (b-a)>eps:
            if f(xl)<f(xr):
                b=xr
                xr=xl
                xl=b-k*(b-a)
                plt.axvline(xl)
            else:
                a=xl
                xl=xr
                xr=a+k*(b-a)
                plt.axvline(xr)
            if (b - a) < eps:
                c = (a + b) / 2
                plt.axvline(c)
                plt.title(c)
                plt.show()
                break
        if i>max_iter:
            return None
    return c


i=golden_section_vis(f2,0,5,10**-4,100)

#Zad3

def pochodna(f2,x,h=10**-7):
    poch=f2(x+h)- f2(x)
    return poch/(h)

def newton(f2,x0,eps,iter_max):
    x=x0
    fx=f2(x)
    for i in range (iter_max):
        if fabs (fx)<eps:
            break
        fpx=pochodna(f2,x)
        x=x-fx/fpx
        fx=f2(x)
        if fabs(fx) >eps and i==iter_max:
            return None
    return x

z=newton(f2,4,10**-4,100)
print(z)


