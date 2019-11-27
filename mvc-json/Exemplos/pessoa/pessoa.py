#!-*- conding: utf8 -*
class CPFJaExiste(Exception):
    def __init__(self):
        super().__init__("CPF ja existe")

class CPFNaoExiste(Exception):
    def __init__(self):
        super().__init__("CPF nao existe")

class Pessoa:
    '''
    Classe do modelo. Representacao de uma pessoa
    '''

    #Dicionario com as pessoas (key = CPF)
    __pessoas = {}

    def __init__(self, cpf, nome, email):
        self.__nome = nome
        self.__email = email
        self.__cpf = cpf

    @property
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @staticmethod
    def adicionar(P):
        '''
        Adicionar a Pessoa P no dicionario/banco de dados.

        Parametros
        ----------
        P: Pessoa
          A pessoa a ser inserida
        
        Excecoes
        --------
        CPFJaExiste
          Se P.cpf ja existe
        '''
        if P.cpf in Pessoa.__pessoas:
            raise CPFJaExiste

        Pessoa.__pessoas[P.cpf] = P

    @staticmethod
    def dadosPessoa(cpf):
        '''
        Retorna o objeto P que corresponde ao CPF cpf.

        Parametros
        ----------
        cpf: str
          O CPF da pessoa
        
        Excecoes
        --------
        CPFNaoExiste
          Se o cpf nao esta cadastrado
        
        Retorna
        --------
        Pessoa
          A pessoa associada ao cpf
        '''
        if cpf not in Pessoa.__pessoas:
            raise CPFNaoExiste()
        return Pessoa.__pessoas[cpf]

    @staticmethod
    def cpfCadastrado(cpf):
        '''
        Retorna True se o CPF ja esta cadastrado

        Parametros
        ----------
        cpf: str

        Retorna
        -------
        bool
        '''
        return cpf in Pessoa.__pessoas

    @staticmethod
    def removerPessoa(cpf):
        '''
        Remover uma pessoa

        Parametros
        -----------
        cpf : str
          CPF da pessoa

        Execoes
        -------
        CPFNaoExiste
          Se o CPF nao esta cadastrado
        '''
        if cpf not in Pessoa.__pessoas:
            raise CPFNaoExiste()
        Pessoa.__pessoas.pop(cpf)


    @staticmethod
    def updateEmail(cpf, email):
        '''Atualiza o email da pessoa

        Parametros
        ---------
        cpf : str
        
        Excecoes
        --------
        CPFNaoExiste
        Se o cpf nao esta cadastrado
        
       email: str
       '''

        if cpf not in Pessoa.__pessoas:
            raise CPFNaoExiste()
        P= Pessoa.__pessoas[cpf]
        P.email = email

    @staticmethod
    def listaPessoas():
        '''Retorna a lista de todas as pessoas cadastradas'''
        return list(Pessoa.__pessoas.values())

    def __repr__(self):
        return f'Pessoa({self.cpf, self.nome, self.email})'


