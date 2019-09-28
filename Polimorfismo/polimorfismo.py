class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Pessoas(Pessoa):
    def __init__(self, listaPessoas, Pessoa.nome, Pessoa.idade):
        self.listaPessoas = []

    def media(self):
        soma = 0
        for i in listaPessoas:
            soma = soma + listaPessoas.Pessoa.idade
            cont += 1
        media = soma/cont
        print(media)

    def __repr__(self):
        return f'A lista de pessoas é: {self.nome}, {self.idade}'

#como usar polimorfismo nesse codigo?
class Aluno(Pessoa):
    def __init__(self, matricula):
        self.matricula = matricula

class Professor(Pessoa):
    def __init__(self, lattes):
        self.lattes = lattes