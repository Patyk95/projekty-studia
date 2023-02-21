import pandas as pd
import numpy as np

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
print(pd.DataFrame(final_frame)) 