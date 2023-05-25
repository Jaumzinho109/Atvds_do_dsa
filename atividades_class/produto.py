#Crie uma classe chamada "Produto" que represente um produto em uma loja.
#  A classe deve ter os atributos: nome, preço e quantidade em estoque.
#  Ela deve ter métodos para atualizar a quantidade em estoque, calcular o valor total em estoque e exibir as informações do produto.
class Produto():
    def __init__(self, nome, preco, quantidade_em_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_em_estoque = quantidade_em_estoque

    def atualizacao_estoque(self, novo_estoque):
        self.quantidade_em_estoque = novo_estoque

    def valor_total_estoque(self):
        total = int(self.preco) * int(self.quantidade_em_estoque)
        print(f'Nós possuímos {total} reais em estoque do produto {self.nome}')

    def infos_produto(self):
        print(f'Produto: {self.nome}, preço: {self.preco} e quantidade em estoque: {self.quantidade_em_estoque}')


det = Produto('Detergente', '5', '3000')
det.valor_total_estoque()

# Corrigindo a atualização do estoque
novo_estoque = int(input('Qual é a nova quantidade do estoque agora? '))
det.atualizacao_estoque(novo_estoque)

det.valor_total_estoque()


