class library:
    def __init__(self, id):
        self.id = identifier

    def book(self):
        print('Books')

    def periodic(self):
        print('Periodics')

    def quantLibrary(self, loands):
        self.loands = [1000] #total quantity in library
        for i in loands:
            print('Loand done')

    @bstractmethod #isso é só para a superclasse e as subclasses
    def loand(self, identifier):
        #may I put an identifier here?
        lend = []
        for i in lend:
            maximum = identifier
            print('Load done')

class user:
    @abstractmethod
    def __init__(self, adress, cpf, dataNas):
        self.__adress = adress
        self.__cpf = cpf
        self.__dataNas = dataNas

class studant(user):
    def __init__(self, curse, numRegister, ingresso):
        self.curse = curse
        self.__numRegister = numRegister
        self.ingresso = ingresso

    def loand(self, maxStudant):
        #Need fix this
        self.maxStudant = maximum
        if lend > 3:
            print('A studant can take until 4 books or periodics')
            
class teacher(user):
    def __init__(self,lotacao):
        self.lotacao = lotacao

    def loand(self, maxTeacher):
        #Need fix this
        self.max = maximum
        if lend > 2:
            print('A teacher can take until 2 books or periodics')

class special(user):
    #Need fix this
    def loand(self, maxSpecial):
        self.max = maximum