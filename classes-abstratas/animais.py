    from abc import ABC, abstractmethod

    class animal(ABC):
        def __init__(self, nasce, morre):
            self.__nasce = nasce
            self.__morre = morre
        
        @abstractmethod
        def nasce(self): #é um método abstrato, pois alguns nascem de modo diferente
            print('Animal nasceu')

        def morre(self): #é um método concreto
            print('Animal morreu')

        @abstractmethod
        def emite_som(self):
            pass
        
    class mamifero(animal): #super classe
        def amamenta(self):
            print('Mamífero amamenta')

    class gato(mamifero):

        def emite_som(self):
            print('Miau')

    class cachorro(mamifero):
        def emite_som(self):
            print('Auau')    
        
    class onitorrino(mamifero):
        def nasce(self):
            print('Onitorrino nasce de um ovo')
        
        def emite_som(self):
            print('Som de onitorrino')
            
    class ave(animal):
        def nasce(self):
            print('Ave nasce de ovo')

        def voa(self):
            print('A ave voa')

    class pinguim(ave):

        def emite_som(self):
            print('Som de pinguim')
        
        def voa(self):
            print('Pinguim não voa')

    class aguia(ave):

        def emite_som(self):
            print('Som de ave')
