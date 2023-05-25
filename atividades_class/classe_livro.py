#Crie uma classe chamada "Livro" que represente um livro.
#  A classe deve ter os atributos: título, autor e ano de publicação.
#  Ela deve ter um método para exibir as informações completas do livro.
class Livro():
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
    def infos_completas(self):
        print(f'O nome do livro é {self.titulo}, o seu autor se chama {self.autor} e foi publicado em {self.ano_publicacao}')
sapiens = Livro('Sapiens, uma breve história da humanidade', 'Yuval Noah Harari', '2016')
sapiens.infos_completas()