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
