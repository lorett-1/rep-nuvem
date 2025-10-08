matriz=[
[1,2,3],
[4,5,6],
[7,8,9]
]
numero=matriz[2][1]
print(f"numero={numero}")

def exibir(matriz):
    print("  1 2 3")
    for linha in range(3):
        print(linha + 1, end=' ')
        for coluna in range(3):
            print(matriz[linha][coluna], end=' ')
        print()

exibir(matriz)

matriz2=[['x'for _ in range(3)] for _ in range(3)]
exibir(matriz2)

import random
numero=random.randint(0,100)
matriz3=[[numero for _ in range(3)] for _ in range(3)]
exibir(matriz3)