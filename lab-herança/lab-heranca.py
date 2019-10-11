class dicionary(self, ...):
    #classe mais fácil para poder comparar os livros que o usuário tem e os que tem na library

class library:
    def __init__(self, id):
        self.id = identifier

    def book(self, idBooks):
        print('Books')
        #cada livro precisa ter um id

    def periodics(self, idPeriodics):
        print('Periodics')
        #cada periódico precisa ter um id
    
    def quantLibrary(self, loands):
        self.loands = [1000] #total quantity in library 
        for i in loands:
            print('Loand done')

    def register(self):

    #propety aqui
    #tem que fazer o get para os livros e para a library
    #tem que fazer as cópias dos livros que pertencem à biblioteca


class user:
    def __init__(self, adress, cpf, dataNas):
        self.__adress = adress
        self.__cpf = cpf
        self.__dataNas = dataNas

    @abstractmethod
    def quantUser(self):
        if (loands>=2):
            print('Loand faild')


class studant(user):
    def __init__(self, curse, numRegister, ingresso):
        self.curse = curse
        self.__numRegister = numRegister
        self.ingresso = ingresso

    def quantUser(self, booksStudant):
         self.booksStudant = [3]
            if (loands>4):
                print('Loand faild')
            else:
                loands = '' #nome do livro
                for i in booksStudant:
                    booksStudant = i  
                print('Loand done')

    def livrosEmprestados(self, idBookUser):
        print('Aqui é o id do livro que a pessoa tem para comparar com o livro que tem na biblioteca')
            
class teacher(user):
    def __init__(self,lotacao):
        self.lotacao = lotacao

        def quantUser(self, booksTeacher):
            self.booksTeacher = [1]
            if (loands>2):
                print('Loand faild')
            else:
                loands = '' #nome do livro
                for i in booksTeacher:
                    booksTeacher = i  
                print('Loand done')

class special(user):
    def quantUser(self, booksOthers):
        self.booksOthers = [5]
            if (loands>6):
                print('Loand faild')
            else:
                loands = '' #nome do livro
                for i in booksOthers:
                    booksOthers = i  
                print('Loand done')

