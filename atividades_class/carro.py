#Crie uma classe chamada "Carro" que represente um carro.
#  A classe deve ter os atributos: marca, modelo e ano.
#  Ela deve ter métodos para acelerar, frear e exibir as informações completas do carro.
class Carro():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def acelerar(self):
        print(f'Estou acelerando o/a {self.modelo}')
    def frear(self):
        print(f'Estou freando o carro {self.modelo}')
    def infos_completas(self):
        print(f'Segue as informações do carro: marca {self.marca}, modelo {self.modelo} e ano {self.ano}')
teste = Carro('Hyundai', 'Creta', '2020')
teste.acelerar()
teste.infos_completas()