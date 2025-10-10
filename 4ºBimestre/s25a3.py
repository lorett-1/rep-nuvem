cinema=[[0 for _ in range(8)]for _ in range(5)]

matriz=[
[1,2,3,4,5,6,7,8],
[9,10,11,12,13,14,15,16],
[17,18,19,20,21,22,23,24],
[25,26,27,28,29,30,31,32],
[33,34,35,36,37,38,39,40]
]
def reserva_assento(cinema,linha,coluna):
    posiçao_linha=-1
    posiçao_coluna=-1
    if 0<=posiçao_linha<5 and 0<=posiçao_coluna<8:
        if cinema[posiçao_linha][posiçao_coluna]==0:
            cinema[posiçao_linha][posiçao_linha]=1
            print(f"a cadeira [{linha}][{coluna}]foi reservada")
        else:
            print(f"a cadeira[{linha}][{coluna}]ja esta reservada")

        
            


