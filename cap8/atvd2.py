# Exercício 2 - Crie uma classe chamada Pessoa() com os atributos: nome, cidade, telefone e e-mail. Use pelo menos 2
# métodos especiais na sua classe. Crie um objeto da sua classe e faça uma chamada a pelo menos um dos seus métodos
# especiais.

class Pessoa():
    def __init__(self, nome = '', cidade = '', telefone = '', email = ''):
        self.nome = nome
        self.cidade = cidade
        self.telefone = telefone
        self.email = email
    def printnome(self):
        print(self.nome)
    def formas_p_contato(self):
        print(f'Telefone: {self.telefone}; e-mail: {self.email}')

p1 = Pessoa('João', 'Cuiabá', '99354-3457', 'joaoh7041@gmail.com')
p1.printnome()
p1.formas_p_contato()
