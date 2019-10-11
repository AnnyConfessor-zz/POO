class library:
    def __init__(self, id):
        self.id = identifier

class book(library):
        print('Books')

class periodic(library):
        print('Periodics')

    #
    def quantLibrary(self, loands):
        self.loands = [1000] #total quantity in library
        for i in loands:
            print('Loand done')

class user:
    def __init__(self, adress, cpf, dataNas):
        self.__adress = adress
        self.__cpf = cpf
        self.__dataNas = dataNas

    @abstractmethod
    def quantUser(self):
        if (l>=2):
            print('Loand faild')


class studant(user):
    def __init__(self, curse, numRegister, ingresso):
        self.curse = curse
        self.__numRegister = numRegister
        self.ingresso = ingresso

    def quantUser(self, booksStudant):
         self.booksStudant = [3]
            if (l>4):
                print('Loand faild')
            else:
                loands = '' #nome do livro
                for i in booksStudant:
                    booksStudant = i  
                print('Loand done')
            
class teacher(user):
    def __init__(self,lotacao):
        self.lotacao = lotacao

        def quantUser(self, booksTeacher):
            self.booksTeacher = [1]
            if (l>2):
                print('Loand faild')
            else:
                loands = '' #nome do livro
                for i in booksTeacher:
                    booksTeacher = i  
                print('Loand done')

class special(user):
    def quantUser(self, booksOthers):
        self.booksOthers = [5]
            if (l>6):
                print('Loand faild')
            else:
                loands = '' #nome do livro
                for i in booksOthers:
                    booksOthers = i  
                print('Loand done')