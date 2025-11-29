'''
    Booleanos (bool)
16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
'''

# Exercício 16

expressao1 = input('Digite a primeira expressão booleana: True ou False? ')
expressao2 = input('Digite a segunda expressão booleana: True ou False? ')
if expressao1 != expressao2:
    print(f'O resultado da operação AND entre as expressões é: False')
else:
    print(f'O resultado da operação AND entre as expressões é: True')


# Exercício 17
valor1 = input('Digite o primeiro valor booleano: True ou False?')
valor2 = input('Digite o segundo valor booleano: True ou False?')
resultado_or = valor1 or valor2
print(f'O resultado da operação OR foi: {resultado_or}')


# Exercício 18
booleano = input('Digite um valor booleano: ')
if booleano == 'True':
    booleano = True
else:
    booleano = False
resultado_invertido = not booleano
print(f'O valor invertido é: {resultado_invertido}')


# Exercício 19
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
resultado_num = num1 == num2
print(f'Os valores digitados são iguais? {resultado_num}')


# Exercício 20
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
resultado_num = numero1 != numero2
print(f'Os valores digitados são diferentes? {resultado_num}')