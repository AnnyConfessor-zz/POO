class Pessoa:
    def __init__(self, nome, cpf, dia, mes, ano):
        self.nome = nomes
        self.cpf = cpf
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def idade(self, idade):
        self.idade = idade
        return idade
    
    def aniv_mes(self, n):
        self.n = n
        if (n >= 1 and n <=12):
            if (n ==1 ):
                print('Janeiro')
            elif (n == 2):
                print('Fevereiro')
                elif (n == 3):
                    print('Março')
                    elif (n == 4):
                        print('Abril')
                        elif (n == 5):
                            print('Maio')
                            elif (n == 6):
                                print('Junho')
                                elif (n == 7):
                                    print('Julho'):
                                    elif (n == 8):
                                        print('Agosto')
                                        elif (n == 9):
                                            print('Setembro')
                                            elif (n == 10):
                                                print('Outubro')
                                                elif (n == 11):
                                                    print('Novembro')
                                                    elif (n == 12):
                                                        print ('Dezembro')

    def maisnovo(self, Pessoa):
        #como fazer uma nova pessoa P dentro de um método?
        #Isso tem que ser feito em uma nova classe

    def se_apresentar(self):
        return f"Olá, meu nome é {Pessoa.nome} e tenho {Pessoa.idade.idade} anos de idade"
    
    #é assim que se faz esse método? É assim que chama um aatributo dentro de outro atributo?
    def cumprimenatar(self, Pessoa):
        self.Pessoa.nome = nomePessoa
        return f"Olá {Pessoa.nome}, meu nome é {cumprimenatar.nomePessoa}"