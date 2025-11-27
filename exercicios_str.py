'''
    Strings (str)
11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
'''

# Exercício 11
maiusculas = input('Digite uma string: ')
print(maiusculas.upper())


# Exercício 12
nome_usurio = input('Digite seu nome completo: ')
print(nome_usurio.lower())


#Exercício 13
frase = input('Digite uma frase: ')
print(frase.strip())


# Exercício 14
data = (input('Digite uma data no formato "dd/mm/aaaa": '))
print(f'Dia {data[:2]}')
print(f'Mês {data[3:5]}')
print(f'Ano {data[6:]}')

# Exercício 15
nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
print(f'Seu nome completo é: {nome + " " + sobrenome}')