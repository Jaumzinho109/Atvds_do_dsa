# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:
	# Método Construtor
    def __init__(self, palavra):
        self.palavra = palavra
        self.letras_erradas = []
        self.letras_escolhidas = []

	# Método para adivinhar a letra
    def guess(self, letra):
        if letra in self.palavra and letra not in self.letras_escolhidas:
            self.letras_escolhidas.append(letra)
        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
        else:
            return False
    return True
	
	# Método para verificar se o jogo terminou
    def hangman_over(self):
        return self.hangman_won() or (len(self.letras_erradas) == 6)
	# Método para verificar se o jogador venceu
    def hangman_won(self):
        if '_' not in self.hide_palavra():
            return True
        return False
	# Método para não mostrar a letra no board
    def hide_palavra(self):
        rtn =''
        for letra in self.palavra:

            if letra not in self.letras_escolhidas:
                rtn += '_'
            else:
                rtn += letra
        return rtn

	# Método para checar o status do game e imprimir o board na tela
    def print_game_status(self): 
        print(board[len(self.letras_erradas)])
        print('\n Palavra:' + self.hide_palavra())
        print('\n Letras erradas: ',)
        for letra in self.letras_erradas:
            print(letra,)
        print()
        print('Letras corretas: ',)
        for letra in self.letras_escolhidas:
            print(letra,)
        print()
def rand_palavras(): 
    palavras = ['banana', 'uva', 'abacaxi', 'abacate', 'morango']
    palavra = random.choice(palavras)
    return palavra
def limpatela():
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')
def boasvindas(n):
        print('_'*30)
        print(n)
        print('_'*30)
def main():
    limpatela()
    game = Hangman(rand_palavras())
    while not game.hangman_over():
        game.print_game_status()
        user_input = input('Digite uma letra:')
        game.guess(user_input)
    game.print_game_status()
    if game.hangman_won():
        print('\n Parabéns você venceu')
    else:
        print('Você perdeu.')
if __name__ == "__main__":
    main()