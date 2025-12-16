try:
    numero_01 = input('Digite um número: ')
    resultado = numero_01 / 0
    print(resultado)
except TypeError as e:
    print(e) # o código do erro pode entrar num log de erros para ser mapeado posteriormente
else:
    print('Código executado sem erros')
finally:
    print('Execução finalizada')  



numero = int(input('insira um número: '))
if isinstance(numero, int):
    print('A variável é um número inteiro')
else:
    print('A variável não é um número inteiro')

idade = 27

if idade < 18:
    print('Não pode dirigir')
else:
    print('Pode dirigir')


