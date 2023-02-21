import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeClassifier
import random

kwadrat= np.array([[1,0,0,1],[3,3,0,0],[2,0,0,2],[9,0,9,0],[4,0,4,0],[7,7,0,0],[4.5,0,4.5,0],[3,3,0,0],[0,15,0,15],[0,0,8,8],[0,5,0,5],[1.5,0,1.5,0]])
etykieta_kwadrat =np.array([0,0,0,0,0,0,0,0,0,0,0,0])
#etykieta_kwadrat.reshape(12,1)

#print(kwadrat.shape)
#print(etykieta_kwadrat.shape)


wartosc= np.column_stack((kwadrat,etykieta_kwadrat))




prostokat= np.array([[3,0,0,1],[7,4,0,0],[2.8,0,0,2],[1,5,0,0],[4.65,0,4.2,0],[1,17,0,0],[2.5,0,8.5,0],[0,3,5,0],[1,0,7.55,0],[0,0,4,6],[0,6,0,8],[1.5,0,3.5,0]])
etykieta_prostokat =np.array([1,1,1,1,1,1,1,1,1,1,1,1])

trapez= np.array([[3,2,1,1],[7,4,1.5,1.5],[2.8,0.4,0.4,2],[1,5,2,2],[4.6,0.2,4.2,0.2],[1,17,8,8],[2.5,3,8.5,3],[1,3,5,1],[2.5,1.55,7.55,2.5],[2,2,4,6],[1,1,6,8],[1.5,1,3.5,1]])
etykieta_trapez =np.array([2,2,2,2,2,2,2,2,2,2,2,2])

trojkat= np.array([[3,2,0,1],[1.5,0,1.5,1.5],[3,0,2,4],[0,2,2,2],[0.2,0.2,0,0.2],[0,7,6,8],[2.5,0,2.5,2.5],[4,3,5,0],[6,0,6,6],[2,2,0,2],[1,1,0,1],[1.5,0,1.5,1.5]])
etykieta_trojkat =np.array([3,3,3,3,3,3,3,3,3,3,3,3])


wartosc1 =np.column_stack((prostokat,etykieta_prostokat))
# print(pd.DataFrame(final_frame1))
wartosc2 =np.column_stack((trapez,etykieta_trapez))
wartosc3 =np.column_stack((trojkat,etykieta_trojkat))


w=np.concatenate((wartosc,wartosc1,wartosc2,wartosc3),axis=0)
frame =pd.DataFrame(w)
final_frame={
    "BOK 1": frame[0], 
    "BOK 2": frame[1], 
    "BOK 3": frame[2], 
    "BOK 4": frame[3], 
    "ETYKIETA": frame[4] 
}
#print(pd.DataFrame(final_frame)) 


x=w[:,:4]
y=w[:,4:]

Xtrain, Xtest,Ytrain,Ytest =train_test_split(x,y.ravel(),train_size=0.15)
clasiication= LogisticRegression()
clasiication.fit(Xtrain,Ytrain)
Ypred=clasiication.predict(Xtest)
#print(Xtest)
#print(Ytest)
#print(accuracy_score(Ytest,Ypred))
#print(Ypred)


clasiication1= LinearRegression()
clasiication1.fit(Xtrain,Ytrain)
Ypred1=clasiication1.predict(Xtest)
#print(mean_absolute_error(Ytest,Ypred1))


clas1= KNeighborsClassifier(n_neighbors=3)
clas1.fit(Xtrain,Ytrain)
Ypred2=clas1.predict(Xtest)
#print(accuracy_score(Ytest,Ypred2))
#print(Ypred2)

clas2= DecisionTreeClassifier()
clas2.fit(Xtrain,Ytrain)
Ypred3=clas2.predict(Xtest)
#print(accuracy_score(Ytest,Ypred3))
#print(Ypred3)

# Zwiększamy liczbę testów

var = np.random.randint(0,100)
print(var)
n =np.random.randint(0,3)
print(n)

