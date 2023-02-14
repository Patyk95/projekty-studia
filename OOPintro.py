import abc
from abc import ABC, abstractmethod

#ZAD1)


class Ssak:
    rodzaj= "Ssak"

    def __init__(self,info="Brak ciekawostki"):
        self.info=info
        print("Stworzyłeś: " + self.rodzaj)

    def ciekawostka(self):
        print(self.info)


class Pies(Ssak):

    rodzaj = "Pies"

    def __init__(self,info="Ma cztery łapy"):
        super().__init__(info)



class Kot(Ssak):

    rodzaj="Kot"
    def __init__(self,info="Pije mleko"):
        super().__init__(info)




s=Ssak()
s.ciekawostka()
p=Pies()
p.ciekawostka()
k=Kot()
k.ciekawostka()

