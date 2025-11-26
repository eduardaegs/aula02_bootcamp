# Exercícios

'''
    Inteiros (int)
1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
'''
# Exercício 1
numero_1 = int(input('Digite o primeiro número inteiro: '))
numero_2 = int(input('Digite outro número inteiro: '))
print('A soma dos dois números inteiros é: ', numero_1 + numero_2)


# Exercício 2
primeiro_numero = int(input('Digite um número: '))
segundo_numero = 5
print(f'O resto inteiro da divisão de {primeiro_numero} por {segundo_numero} é: {primeiro_numero % segundo_numero}')


# Exercício 3
num_1 = int(input('Digite o primeiro número da multiplicação: '))
num_2 = int(input('Digite o segundo número da multiplicação: '))
print(f'O resultado da multiplicaçao é: {num_1 * num_2}')


# Exercício 4
dividendo = int(input('Digite o dividendo: '))
divisor = int(input('Digite o divisor: '))
print('O resultado é: ', dividendo // divisor)

# Exercicio 5
numero = int(input('Digite um número para calcular o quadrado: '))
print(f'O quadrado do número {numero} é: {numero ** 2}')