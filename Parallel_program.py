import joblib
import time
import matplotlib.pyplot as plt
from joblib import Parallel, delayed
from math import sqrt, pow

# Zad1)

def f(i):
    return i**2+2*i+4

number_of_cpu = joblib.cpu_count()
delayed_func = [delayed(f)(i) for i in range(1000)]
parallel_pool = Parallel(n_jobs=number_of_cpu)

start_time = time.time()
for i in range(1000):
      f(i)

print("time elapsed for sequential way by [f]: {:.2f}s".format(time.time() - start_time))
start_time = time.time()
parallel_pool(delayed(f)(i) for i in range(1000))
print("time elapsed for 6 CPU's by [f]: {:.2f}s".format(time.time() - start_time))
start_time = time.time()
Parallel(n_jobs=number_of_cpu, prefer="threads")(delayed(f)(i) for i in range(1000))
print("time elapsed for 6 CPU's and by using threads by [f] : {:.2f}s".format(time.time() - start_time))

# #Zad2)
#a) adding two elements

def f1(i):
    return (i+778)
start_time = time.time()
for i in range(1000):
    f1(i)
print("time elapsed for sequential way by [f2]: {:.2f}s".format(time.time() - start_time))
start_time = time.time()
parallel_pool(delayed(f1)(i) for i in range(1000))
print("time elapsed for 6 CPU's by [f1]: {:.2f}s".format(time.time() - start_time))
start_time = time.time()
Parallel(n_jobs=number_of_cpu, prefer="threads")(delayed(f1)(i) for i in range(1000))
print("time elapsed for 6 CPU's and by using threads by [f1]: {:.2f}s".format(time.time() - start_time))

#b)substract two elements

def f2(i):
    return (i-98888)

start_time = time.time()
for i in range(1000):
    f2(i)
print("time elapsed for sequential way by [f2]: {:.2f}s".format(time.time() - start_time))
start_time = time.time()
parallel_pool(delayed(f2)(i) for i in range(1000))
print("time elapsed for 6 CPU's by [f2]: {:.2f}s".format(time.time() - start_time))
start_time = time.time()
Parallel(n_jobs=number_of_cpu, prefer="threads")(delayed(f2)(i) for i in range(1000))
print("time elapsed for 6 CPU's and by using threads by [f2]: {:.2f}s".format(time.time() - start_time))

#c) multiplicate two elements

def f3(i):
    return (i*584)

start_time = time.time()
for i in range(1000):
    f3(i)
print("time elapsed for sequential way by [f3]: {:.2f}s".format(time.time() - start_time))
start_time = time.time()
parallel_pool(delayed(f3)(i) for i in range(1000))
print("time elapsed for 6 CPU's by [f3]: {:.2f}s".format(time.time() - start_time))
start_time = time.time()
Parallel(n_jobs=number_of_cpu, prefer="threads")(delayed(f3)(i) for i in range(1000))
print("time elapsed for 6 CPU's and by using threads by [f3]: {:.2f}s".format(time.time() - start_time))

#d) splitting two elements

def f4(i):
    return (i/854)

start_time = time.time()
for i in range(1000):
    f4(i)
print("time elapsed for sequential way by [f4]: {:.2f}s".format(time.time() - start_time))
start_time = time.time()
parallel_pool(delayed(f4)(i) for i in range(1000))
print("time elapsed for 6 CPU's by [f4]: {:.2f}s".format(time.time() - start_time))
start_time = time.time()
Parallel(n_jobs=number_of_cpu, prefer="threads")(delayed(f4)(i) for i in range(1000))
print("time elapsed for 6 CPU's and by using threads by [f4]: {:.2f}s".format(time.time() - start_time))

#e) square of two elements

def f5(i):
    return sqrt(i)

start_time = time.time()
for i in range(1000):
    f5(i)
print("time elapsed for sequential way by [f5]: {:.2f}s".format(time.time() - start_time))
start_time = time.time()
parallel_pool(delayed(f5)(i) for i in range(1000))
print("time elapsed for 6 CPU's by [f5]: {:.2f}s".format(time.time() - start_time))
start_time = time.time()
Parallel(n_jobs=number_of_cpu, prefer="threads")(delayed(f5)(i) for i in range(1000))
print("time elapsed for 6 CPU's and by using threads by [f5]: {:.2f}s".format(time.time() - start_time))

#f)#e) potentiation of two elements
def f6(i):
    return pow(i,2)

start_time = time.time()
for i in range(1000):
    f6(i)
x=print("time elapsed for sequential way by [f6]: {:.2f}s".format(time.time() - start_time))
start_time = time.time()
parallel_pool(delayed(f6)(i) for i in range(1000))
y=print("time elapsed for 6 CPU's by [f6]: {:.2f}s".format(time.time() - start_time))
start_time = time.time()
Parallel(n_jobs=number_of_cpu, prefer="threads")(delayed(f6)(i) for i in range(1000))
z=print("time elapsed for 6 CPU's and by using threads by [f6]: {:.2f}s".format(time.time() - start_time))

#Zad3)

l=[100,250,500,1000,5000]

def f(i):
    return i**2+2*i+4

def show(arg):
    for k in l:
        number_of_cpu = joblib.cpu_count()
        delayed_func = [delayed(f)(i) for i in range(k)]
        parallel_pool = Parallel(n_jobs=number_of_cpu)
        start_time = time.time()
        print("time elapsed for sequential : {:.2f}s".format(time.time() - start_time))
        x=("{:.2f}".format(time.time() - start_time))
        start_time = time.time()
        parallel_pool(delayed(f)(i) for i in range(k))
        print("time elapsed for 6 CPU's]: {:.2f}s".format(time.time() - start_time))
        y=("{:.2f}".format(time.time() - start_time))
        start_time = time.time()
        Parallel(n_jobs=number_of_cpu, prefer="threads")(delayed(f)(i) for i in range(k))
        print("time elapsed for 6 CPU's and by using threads : {:.2f}s".format(time.time() - start_time))
        z=("{:.2f}".format(time.time() - start_time))
        plt.plot()
        plt.title('Wykres zależnej czasu od iteracji')
        plt.scatter(k,x,c='r',)
        plt.scatter(k, y, c='g')
        plt.scatter(k, z, c='b')
        plt.grid(True)
        plt.xlabel('Ilosć iteracji')
        plt.ylabel('czas wykonania')
    plt.scatter(k, x, c='r', label='iteration for seq')
    plt.scatter(k, y, c='g', label='iteration for cpu\'s')
    plt.scatter(k, z, c='b', label='iteration for threads')
    plt.legend(loc='center right', bbox_to_anchor=(1.15, 1.05))
    plt.legend(loc='upper left')
    plt.show()

show(l)




'''Najbardziej korzystnym podziałem zadań jest sposoób sekwencyjny, ponieważ wykonuje on operacje w czasie dość szybkim. Na drugim miejscu jako 
najbardziej wydajny spoósb wykonywania zadań znajduje sie sposób z dzielonyi wątkami, a na miejscu trzecim spośób z udziałem procesorów
dal mojej jednostki obliczeniowej jest to 6 proc.'''



