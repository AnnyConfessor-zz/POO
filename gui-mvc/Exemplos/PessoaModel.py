# Classe do Modelo

class CPFRepetido (Exception):
    '''
    Exceção lançada ao tentar cadastrar duas pessoas com o 
    mesmo CPF
    '''
    def __init__(self):
        super().__init__("CPF Repetido")
        
class Pessoa:
    '''Classe do modelo'''

    #Banco de dados,por enquanto simplesmente um dicionário indexado
    #com os CPFs
    _bd = {}

    def __init__(self, cpf, nome, email=""):
        self._cpf = cpf
        self._nome = nome
        self._email = email

    def __repr__(self):
        return 'Pessoa({0},{1},{2})'.format(self.cpf, self.nome, self.email)

    @property
    def cpf(self):
        return self._cpf
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @staticmethod
    def adicionar(P):
        '''
        Adiciona a pessoa P no banco de dados.
        ----------
        raise:
          CPFRepetido se o CPF já está no banco de dados
        '''
        
        if P.cpf in Pessoa._bd:
            raise CPFRepetido()
        Pessoa._bd[P.cpf] = P

    @staticmethod
    def listar():
        '''Retornar todas as pessoas cadastradas no banco de dados'''
        return Pessoa._bd.values()

#Alguns dados de teste
Pessoa._bd['00000'] = Pessoa('00000','Pessoa 0','Email 0')
Pessoa._bd['11111'] = Pessoa('11111','Pessoa 1','Email 1')
Pessoa._bd['22222'] = Pessoa('22222','Pessoa 2','Email 2')
Pessoa._bd['33333'] = Pessoa('33333','Pessoa 3','Email 3')

    
