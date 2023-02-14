import matplotlib.pyplot as plt
import matplotlib.patches as patches
#Zad1)
class Punkt:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def nalezy_do(self,a,b):
        if a*self.x+b==self.y:
            return True
        else:
            return False

class Prosta:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def miejsce_zerowe(self):
        if self.a==0:
            print("taki punkt nie istnieje")
        else:
            return -self.b/self.a

p=Punkt(3,6)
pr=Prosta(2,0)
p.nalezy_do(pr.a,pr.b)
print(p.nalezy_do(pr.a,pr.b))
print(pr.miejsce_zerowe())


#Zad2)


class Prostokat:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def pole(self):
        print ((p2.x - p1.x) * (p2.y - p1.y))

    def obwod(self):
        print( 2 * (p2.x - p1.x) + 2 * (p2.y - p1.y))

    def rysuj(self):
        w=(p2.x - p1.x)
        h=(p2.y - p1.y)
        plt.axes().add_patch(patches.Rectangle((p1.x,p1.y),w,h,linewidth=2.5,color='blue',fill=None))
        plt.scatter(p1.x,p1.y,marker="o")
        plt.scatter(p2.x,p2.y,marker='o')

        plt.grid()
        plt.xlim([0,6])
        plt.ylim([0,4])

        plt.show()


p1 = Punkt(1, 1)
p2 = Punkt(2, 3)
prost=Prostokat(p1,p2)
prost.pole()
prost.obwod()
prost.rysuj()