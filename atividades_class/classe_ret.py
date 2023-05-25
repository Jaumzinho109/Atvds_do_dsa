class retangulo():
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura
    def perimetro(self):
        return (self.largura * 2 + self.altura * 2)
    def area(self):
        return (self.largura * self.altura)

teste = retangulo(12, 15)
setattr(teste, 'altura', 14)
print(getattr(teste, 'altura'))