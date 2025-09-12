import random
lista=[]
numero = int(input("quantos elementos??"))
while lista >=1 or lista<100:
    numero = int(input("quantos elementos??"))
    lista.append(numero)
    print(lista)
    continua = int(input("deseja continar?[sim,nao]: ").lower())
    if continua == 'nao':
        break