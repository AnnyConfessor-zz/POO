class pessoa():
    def __init__(self,nome, rg):
        self.nome = nomePessoa
        self.rg = rg

class funcionario(pessoa, contribuinte):
    def __init__(self, matricula):
        self.matricula = matricula

    @abstractmethod
    def declara(self):
        print('Funcionário declara imposto')

class contribuinte():
    def __init__(self,identificador):
        self.identificador = identificador

    @abstractmethod
    def declara(self):
        print('declara imposto')

class empresa(contribuinte):
    def __init__(self, nome):
        self.nome = nomeEmpresa

    @abstractmethod
    def declara(self):
        print('Empresa declara imposto')