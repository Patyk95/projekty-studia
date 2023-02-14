import numpy as np
import threading
import time
from matplotlib import pyplot as plt




size = 100
max_level = 5
matrix = np.zeros((size, size))
print("Zadanie 3")

def drawSquare(x, y, level):
    x = int(x)
    y = int(y)
    # sprawdzenie poziomu zagłębienia
    if level == max_level: return
    # obliczenie obszaru pracy
    offsetX = int(size / 3 ** level)
    offsetY = int(size / 3 ** level)
    # wstawienie odpowiednich wartości do macierzy
    for i in range(0, offsetX):
        for j in range(0, offsetY):
            if level % 2 == 0:
                matrix[x + i][y + j] = 1
            else:
                matrix[x + i][y + j] = 0
    # lista z wątkami
    threads = list()
    # Pierwszy rząd
    t1 = threading.Thread(target=drawSquare, args=(x, y, level + 1))
    threads.append(t1)
    t1.start()
    t2 = threading.Thread(target=drawSquare, args=(x + offsetX / 3, y, level + 1))
    threads.append(t2)
    t2.start()
    t3 = threading.Thread(target=drawSquare, args=(x + offsetX / 3 * 2, y, level + 1))
    threads.append(t3)
    t3.start()
    # Drugi rząd
    t4 = threading.Thread(target=drawSquare, args=(x, y + offsetY / 3, level + 1))
    threads.append(t4)
    t4.start()
    t5 = threading.Thread(target=drawSquare, args=(x + offsetX / 3 * 2, y + offsetY / 3, level + 1))
    threads.append(t5)
    t5.start()
    # Trzeci rząd
    t6 = threading.Thread(target=drawSquare, args=(x, y + offsetY / 3 * 2, level + 1))
    threads.append(t6)
    t6.start()
    t7 = threading.Thread(target=drawSquare, args=(x + offsetX / 3, y + offsetY / 3 * 2, level + 1))
    threads.append(t7)
    t7.start()
    t8 = threading.Thread(target=drawSquare, args=(x + offsetX / 3 * 2, y + offsetY / 3 * 2, level + 1))
    threads.append(t8)
    t8.start()
    # łączenie działania wszystkich wątków
    for index, thread in enumerate(threads):
        thread.join()


#drawSquare(0, 0, 0)
#Rozmiar 100
time_func = 0
for i in range(10):
    plt.subplot(1,3,2)
    start_time = time.time()
    drawSquare(0, 0, 0)
    run_time = time.time() - start_time
    plt.scatter(i,run_time,marker="*")
    time_func = time_func + run_time
    #print(run_time)
#print(time_func)
w=average_func_exec = time_func / 10
print("Średni czas działania dla  rozmairu 100 to " + str(average_func_exec))
plt.xlabel('LICZBA ITERACJI')
x=[0,1,2,3,4,5,6,7,8,9]
default_x_ticks = range(len(x))
plt.xticks(default_x_ticks, x)
plt.xlim([-1,11])
plt.axhline(y=average_func_exec, color='r')
plt.ylabel("CZAS")
plt.grid(True)

print("Zadanie 4")
#Zad2:
#Rozmiar 50

size = 50
max_level = 5
matrix = np.zeros((size, size))
time_func = 0
for i in range(10):
    plt.subplot(1,3,1)
    start_time = time.time()
    drawSquare(0, 0, 0)
    run_time = time.time() - start_time
    plt.scatter(i,run_time,marker="*")
    time_func = time_func + run_time
    #print(run_time)
#print(time_func)
average_func_exec = time_func / 10
print("Średni czas działania dla  rozmairu 50 to " + str(average_func_exec))
plt.xlabel('LICZBA ITERACJI')
x=[0,1,2,3,4,5,6,7,8,9]
default_x_ticks = range(len(x))
plt.xticks(default_x_ticks, x)
plt.xlim([-1,11])
plt.axhline(y=average_func_exec, color='r')
plt.ylabel("CZAS")

plt.grid(True)


#Rozmiar 150

size = 150
max_level = 5
matrix = np.zeros((size, size))
time_func = 0
for i in range(10):
    plt.subplot(1,3,3)
    start_time = time.time()
    drawSquare(0, 0, 0)
    run_time = time.time() - start_time
    plt.scatter(i,run_time,marker="*")
    time_func = time_func + run_time
    #print(run_time)
#print(time_func)
average_func_exec = time_func / 10
print("Średni czas działania dla  rozmairu 150 to " + str(average_func_exec))
plt.xlabel('LICZBA ITERACJI')
x=[0,1,2,3,4,5,6,7,8,9]
default_x_ticks = range(len(x))
plt.xticks(default_x_ticks, x)
plt.xlim([-1,11])
plt.axhline(y=average_func_exec, color='r')
plt.ylabel("CZAS")
plt.grid(True)
plt.show()

print("Zadanie 5")
#Zad 3)

max_level = 3
size = 50
matrix = np.zeros((size, size))
time_func = 0
for i in range(10):
    plt.subplot(1,3,1)
    start_time = time.time()
    drawSquare(0, 0, 0)
    run_time = time.time() - start_time
    plt.scatter(i,run_time,marker="*")
    time_func = time_func + run_time
    #print(run_time)
#print(time_func)
average_func_exec = time_func / 10
#print(average_func_exec)
print("Średni czas działania dla poziomu zagn 3 i rozmairu 50 to " + str(average_func_exec))


max_level = 4
size = 50
matrix = np.zeros((size, size))
time_func = 0
for i in range(10):
    plt.subplot(1,3,1)
    start_time = time.time()
    drawSquare(0, 0, 0)
    run_time = time.time() - start_time
    plt.scatter(i,run_time,marker="*")
    time_func = time_func + run_time
    #print(run_time)
#print(time_func)
average_func_exec = time_func / 10
#print(average_func_exec)
print("Średni czas działania dla poziomu zagn 4 i rozmairu 50 to " + str(average_func_exec))

max_level = 5
size = 50
matrix = np.zeros((size, size))
time_func = 0
for i in range(10):
    plt.subplot(1,3,1)
    start_time = time.time()
    drawSquare(0, 0, 0)
    run_time = time.time() - start_time
    plt.scatter(i,run_time,marker="*")
    time_func = time_func + run_time
    #print(run_time)
#print(time_func)
average_func_exec = time_func / 10
#print(average_func_exec)
print("Średni czas działania dla poziomu zagn 5 i rozmairu 50 to " + str(average_func_exec))

max_level = 3
size = 100
matrix = np.zeros((size, size))
time_func = 0
for i in range(10):
    plt.subplot(1,3,1)
    start_time = time.time()
    drawSquare(0, 0, 0)
    run_time = time.time() - start_time
    plt.scatter(i,run_time,marker="*")
    time_func = time_func + run_time
    #print(run_time)
#print(time_func)
average_func_exec = time_func / 10
print("Średni czas działania dla poziomu zagn 3 i rozmairu 100 to " + str(average_func_exec))

max_level = 4
size = 100
matrix = np.zeros((size, size))
time_func = 0
for i in range(10):
    plt.subplot(1,3,1)
    start_time = time.time()
    drawSquare(0, 0, 0)
    run_time = time.time() - start_time
    plt.scatter(i,run_time,marker="*")
    time_func = time_func + run_time
    #print(run_time)
#print(time_func)
average_func_exec = time_func / 10
print("Średni czas działania dla poziomu zagn 4 i rozmairu 100 to " + str(average_func_exec))

max_level = 5
size = 100
matrix = np.zeros((size, size))
time_func = 0
for i in range(10):
    plt.subplot(1,3,1)
    start_time = time.time()
    drawSquare(0, 0, 0)
    run_time = time.time() - start_time
    plt.scatter(i,run_time,marker="*")
    time_func = time_func + run_time
    #print(run_time)
#print(time_func)
average_func_exec = time_func / 10
print("Średni czas działania dla poziomu zagn 5 i rozmairu 100 to " + str(average_func_exec))

max_level = 3
size = 150
matrix = np.zeros((size, size))
time_func = 0
for i in range(10):
    plt.subplot(1,3,1)
    start_time = time.time()
    drawSquare(0, 0, 0)
    run_time = time.time() - start_time
    plt.scatter(i,run_time,marker="*")
    time_func = time_func + run_time
    #print(run_time)
#print(time_func)
average_func_exec = time_func / 10
print("Średni czas działania dla poziomu zagn 3 i rozmairu 150 to " + str(average_func_exec))

max_level = 4
size = 150
matrix = np.zeros((size, size))
time_func = 0
for i in range(10):
    plt.subplot(1,3,1)
    start_time = time.time()
    drawSquare(0, 0, 0)
    run_time = time.time() - start_time
    plt.scatter(i,run_time,marker="*")
    time_func = time_func + run_time
    #print(run_time)
#print(time_func)
average_func_exec = time_func / 10
print("Średni czas działania dla poziomu zagn 4 i rozmairu 150 to " + str(average_func_exec))

max_level = 5
size = 150
matrix = np.zeros((size, size))
time_func = 0
for i in range(10):
    plt.subplot(1,3,1)
    start_time = time.time()
    drawSquare(0, 0, 0)
    run_time = time.time() - start_time
    plt.scatter(i,run_time,marker="*")
    time_func = time_func + run_time
    #print(run_time)
#print(time_func)
average_func_exec = time_func / 10
print("Średni czas działania dla poziomu zagn 5 i rozmairu 150 to " + str(average_func_exec))




plt.rcParams['figure.figsize'] = (12, 12)
plt.imshow(matrix)
#plt.show()