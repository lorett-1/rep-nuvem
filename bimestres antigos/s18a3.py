c=int(input("quantos metros?[1 a 10**8]"))
while c < 1 or c > 10**8:
    c=int(input("quantos metros?[1 a 100000000]"))
tamanho_pista=int(input("qual o tamanho da pista?[1 a 100]"))
while tamanho_pista < 1 or tamanho_pista > 100:
    tamanho_pista=int(input("qual o tamanho da pista?[1, 100]:"))
ponto_termino=c % tamanho_pista
if ponto_termino >=1 or ponto_termino <10000:
    print(f"o fim do treinamento sera {ponto_termino}metros")
