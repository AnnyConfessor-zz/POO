from abc import ABC, abstractmethod

class animal(ABC):
    def __init__(self, nasce, morre):
        self.__nasce = nasce
        self.__morre = morre
    
    @abstractmethod
    def nasce(self):
        print('Animal nasce')

    def morre(self):
        print('Animal morreu')

    
class mamifero(animal):

    def amamenta():
        print('Mamífero amamenta')

class gato(mamifero):
    

class cachorro(mamifero):
    
    
class onitorrinco(mamifero):
    def nasce():
        print('Nasce de modo diferente que na super classe')
     
class ave():

    def nasce():
        print('Nasce de modo diferente que nas super classe')


class pinguim(ave):
   def voar():
       print('É um método diferente que não tem nos outros')


class aguia(ave):
