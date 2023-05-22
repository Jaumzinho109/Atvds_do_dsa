import random
from os import system, name

def limpatela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
def boasvindas(n):
    print('_'*30)
    print(n)
    print('_'*30)
def game():
    limpatela()
    boasvindas('Bem vindo ao jogo da forca!')
    boasvindas('Adivinhe a palavra abaixo: ')

    palavras = ['banana', 'uva', 'abacaxi', 'abacate', 'morango']
    palavra = random.choice(palavras)
    letras_descobertas = ['_' for letra in palavra]
    chances = 6
    letras_erradas = []
    while chances > 0:
        print(''.join(letras_descobertas))
        print('\nChances restantes: ', chances)
        print('Letras erradas: ',''.join(letras_erradas))

        tentativa = input('\nDigite uma letra: ').lower()
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1 
            letras_erradas.append(tentativa)
        if '_' not in letras_descobertas:
            print('\nVocê venceu, parabéns!')
            break
    if '_' in letras_descobertas:
        print('Você perdeu, mais sorte na próxima.')

if __name__ == "__main__":
    game()