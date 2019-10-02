class desenhavel:
    @abstractmethod
    def desenha(self):
        pass

class falante:
    @abstractmethod
    def emite_som(self):
        pass

class figura(desenhavel):
    pass

class animal(desenhavel,falante):
    def nasce(self):
        print('Animal nasceu')

class circulo(figura):
    def raio(self):
        raio = 1.5
        return raio

class galinha(animal):
    pass

if __name__ == "__main__":
    a = desenhavel()
    b = falante()
    c = figura()
    d = animal()
    e = circulo()
    f = galinha()


