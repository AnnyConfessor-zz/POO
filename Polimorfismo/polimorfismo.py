class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def media(self, listaPessoas):
        soma = 0
        listaPessoas = []
        for i in listaPessoas:
            soma = soma + listaPessoas.Pessoa.idade
            cont += 1
        media = soma/cont
        return media

    def __repr__(self):
        return f'A lista de pessoas é: {self.nome}, {self.idade}'

#como usar polimorfismo nesse codigo?
#como estamos usando uma listaPessoas que alunos e professores tbm sao pessoas
#entao isso é um conceito de polimorfismo
class Aluno(Pessoa):
    def __init__(self, matricula):
        self.matricula = matricula

class Professor(Pessoa):
    def __init__(self, lattes):
        self.lattes = lattes