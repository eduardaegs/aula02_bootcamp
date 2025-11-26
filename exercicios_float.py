'''
    Números de Ponto Flutuante (float)
6. Escreva um programa que receba dois números flutuantes e realize sua adição.
7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

'''


# Exercício 6
num_1 = float(input('Digite um número flutuante: '))
num_2 = float(input('Digite outro número flutuante: '))
print(f'A soma dos dois números digitados é: {num_1 + num_2}')


# Exercício 7
numero_1 = float(input('Digite o primeiro número flutuante: '))
numero_2 = float(input('Digite outro número flutuante: '))
print(f'A média dos números é: {(numero_1 + numero_2)/2}')


# Exercício 8
base = float(input('Digite a base: '))
expoente = float(input('Digite o expoente: '))
print(f'O resultado da potenciação do número {base} elevado a {expoente} é: {base ** expoente}')


# Exercício 9
celsius = float(input('Digite a temperatura que deseja converter para Farenheit: '))
farenheit = (celsius * 1.8) + 32
print(f'A temperatura em Farenheit é: {farenheit:.1f} °F')


# Exercício 10
raio = float(input('Digite o raio do círculo: '))
area = 3.14159 * (raio **2)
print(f'A área do círculo é de: {area:.2f}')