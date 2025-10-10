cinema=[[0 for _ in range(8)] for _ in range(5)]

def reserva_assento(cinema,linha,coluna):
    posiçao_linha = linha - 1
    posiçao_coluna= coluna - 1
    if 0 <= posiçao_linha < 5 and  0 <= posiçao_coluna < 8:
        if cinema[posiçao_linha][posiçao_coluna] == 0:
            cinema[posiçao_linha][posiçao_linha] = 1
            print(f"a cadeira [{linha}][{coluna}]foi reservada")
        else:
            print(f"a cadeira[{linha}][{coluna}]ja esta reservada")
    else:
        print(f"a cadeira[{linha}][{coluna}]não e válida")
        
def cancelar_assento(cinema,linha,coluna):
    posiçao_linha = linha - 1
    posiçao_coluna = coluna - 1
    if 0 <= posiçao_linha < 5 and  0 <= posiçao_coluna < 8:
        if cinema[posiçao_linha][posiçao_coluna] == 1:
            cinema[posiçao_linha][posiçao_linha] = 0
            print(f"\na cadeira [{linha}][{coluna}]foi cancelada")
        else:
            print(f"a cadeira[{linha}][{coluna}]continua livre")
    else:
        print(f"a cadeira[{linha}][{coluna}]não e válida")

def exibir(cinema,linha,coluna):
    for i in range(linha):
        for j in range(coluna):
            print(cinema[i][j], end=' ')
        print()

def execucao(cinema,dim_linha,dim_coluna, linha, coluna):
    print("cinema sem reservas")
    exibir(cinema, dim_linha, dim_coluna)
    reserva_assento(cinema, linha, coluna)
    print("cinema depois da reserva")
    exibir(cinema, dim_linha, dim_coluna)

if __name__=='__main__':
    execucao(cinema, 5,8, 1,3)


