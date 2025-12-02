'''
Exercício 21: Conversor de Temperatura
Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a 
entrada seja numérica, tratando qualquer ValueError. Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

Exercício 22: Verificador de Palíndromo
Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). Utilize try-except para garantir 
que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.

Exercício 23: Calculadora Simples
Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. Use try-except para lidar com divisões por zero e entradas não numéricas. 
Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.

Exercício 24: Classificador de Números
Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número como 
"positivo", "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".

Exercício 25: Conversão de Tipo com Validação
Crie um script que solicite ao usuário uma lista de números separados por vírgula. O programa deve converter a string de entrada em uma lista de números inteiros. Utilize try-except 
para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. 
Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.
'''

#Exercício 21
try:
    celsius = float(input('Digite a temperatura em Celsius: '))
    fahrenheit = (celsius * 9/5) + 32
except ValueError as e:
    print(f'Erro: {e}. Por favor, insira um núumero válido.')
else:
    print(f'Temperatura em Fahrenheit: {fahrenheit}')



#Exercício 22
palavra = input('Digite a palavra a ser verificada: ')

if isinstance(palavra, str):
    check_palavra = palavra[::-1].lower() == palavra.lower()
    if check_palavra:
        print(f'A palavra {palavra} é um palíndromo')
    else:
        print(f'A palavra {palavra} não é um palíndromo')
else:
    print('Error: O texto digitado precisa ser uma string') # Não faz sentido, pois input sempre retorna string


# Exercício 23
try:
    operacao = input('Digite o símbolo da operaçao desejada (+, -, *, /): ')
    if operacao in ['+', '-', '*', '/']:
        if operacao == '+':
            num1 = float(input('Digite o primeiro número: '))
            num2 = float(input('Digite o segundo número: '))
            resultado_1 = num1 + num2
            print(f'O resultado da soma e: {resultado_1}')

        elif operacao == '-':
            num3 = float(input('Digite o primeiro número: '))
            num4 = float(input('Digite o segundo número: '))
            resultado_2 = num3 - num4
            print(f'O resultado da subtração e: {resultado_2}')

        elif operacao == '*':
            num5 = float(input('Digite o primeiro número: '))
            num6 = float(input('Digite o segundo número: '))
            resultado_3 = num5 * num6
            print(f'O resultado da multiplicação é: {resultado_3}')

        elif operacao == '/':
            try:
                resultado_4 = int(input('Digite o dividendo: ')) / int(input('Digite o divisor: '))
                print(f'O resultado da divisão é: {resultado_4}')
            except ZeroDivisionError as e:
                print(f'Erro: {e}. Divisão por zero não é permitida.')
    else:
        print('Operação inválida. Por favor, escolha entre +, -, * ou /.')
except TypeError as e:
    print(f'Erro: {e}. Por favor, insira valores válidos.')


# Exercício 24
try:
    number = int(input('Digite um número: '))
    if number % 2 == 0:
        impar_par = 'Par'
    else:
        impar_par = 'Ímpar'

    if number > 0:
        classificacao = 'Positivo'
        print(f'Número é {classificacao} e {impar_par}')

    elif number == 0:
        classificacao = 'Zero/Nulo'
        print(f'Número é {classificacao} e {impar_par}')
    else:
        classificacao = 'Negativo'
        print(f'Número é {classificacao} e {impar_par}')
except ValueError as e:
    print('Erro: {e}. Insira um número inteiro e válido')


# Exercício 25
numeros = input('Digite uma lista de números separados por vírgula: ')
numeros_str = numeros.split(",")
numeros_int = []
try:
    for num in numeros_str:
        numeros_int.append(int(num.strip()))
    print("Lista de inteiros:", numeros_int)
except ValueError:
    print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")