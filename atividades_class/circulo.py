#Crie uma classe chamada "Circulo" que represente um círculo.
#  A classe deve ter o atributo raio e métodos para calcular a área e o perímetro do círculo.

class Circulo():
    def __init__(self, raio=2):
        self.raio = raio
        self.valor_pi = 3.14

    def area(self):
        return self.raio ** 2 * self.valor_pi

    def perimetro(self):
        return 2 * self.raio * self.valor_pi

teste = Circulo(5)
print(teste.perimetro())
print(teste.area())
