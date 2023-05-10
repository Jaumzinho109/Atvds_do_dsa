def calculadora(op):
    if op == 1:
        qntd = int(input('Quantos números você deseja somar? '))
        soma = 0
        while qntd > 0:
            num = float(input('Digite o valor a ser somado: '))
            soma += num
            qntd -= 1 
        print(f'A soma vale {soma}')
    elif op == 4:
        qntd = int(input('Quantos números você deseja multiplicar? '))
        mult = 1
        while qntd > 0:
            num = float(input('Digite o valor a ser multiplicado: '))
            mult *= num
            qntd -= 1 
        print(f'O resultado da multiplicação é igual a {mult}')
    elif op == 3:
        num1 = float(input('Informe vai ser o numerador: '))
        num2 = float(input('Agora, o denominador'))
        div = num1 / num2
        print(f'O resultado da divisão é igual a {div}')
    elif op == 2:
        num1 = float(input('Qual é o primeiro valor? '))
        num2 = float(input('Fala o segundo: '))
        print(f'{num1} - {num2} é igual a {num1 - num2}')
    

print('_' * 30)
print()
print('1 - SOMA')
print('2 - SUBTRAÇÃO')
print('3 - DIVISÃO')
print('4 - MULTIPLICAÇÃO')
print('_' * 30)
opcao = int(input('Sua opção: '))
calculadora(opcao)