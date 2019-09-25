    from abc import ABC, abstractmethod

    class animal(ABC):
        def __init__(self, nasce, morre):
            self.__nasce = nasce
            self.__morre = morre
        
        @abstractmethod
        def nasce(self): #é um método abstrato, pois alguns nascem de modo diferente
            print('Animal nasce')

        def morre(self): #é um método concreto
            print('Animal morreu')

        @abstractmethod
        def emite_som(self):
            pass
        
    class mamifero(animal): #super classe
        def amamenta():
            print('Mamífero amamenta')

    class gato(mamifero):
        print('Gato é um mamífero')

        def emite_som():
            print('Emite som')

    class cachorro(mamifero):
        print('Cachorro é um mamífero')

        def emite_som():
            print('Emite som')    
        
    class onitorrino(mamifero):
        def nasce():
            print('Onitorrino nasce de um ovo')
        
        def emite_som():
            print('Emite som')
            
    class ave(animal):
        def nasce():
            print('Ave nasce de ovo')

    class pinguim(ave):
        print('É um pinguim')

        def emite_som():
            print('Emite som')

    class aguia(ave):
        print('é uma Água')

        def emite_som():
            print('Emite som')
