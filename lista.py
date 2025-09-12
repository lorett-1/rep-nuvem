lista=[1,2,3,4,5]
while True:
    numero = int(input("qual o numero??"))
    lista.append(numero)
    print(lista)
    continua = int(input("deseja continar?[sim,nao]: ").strip().lower())
    if continua == 'nao':
        break
    


