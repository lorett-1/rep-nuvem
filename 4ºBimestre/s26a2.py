def mover_esquerda_2048(tabuleiro_original):
    
    novo_tabuleiro = []

    for linha_original in tabuleiro_original:
        
        linha_comprimida = [num for num in linha_original if num != 0]
        
        i = 0
        while i < len(linha_comprimida) - 1:
            if linha_comprimida[i] == linha_comprimida[i+1]:
                linha_comprimida[i] *= 2  
                linha_comprimida.pop(i+1) 
            else:
                
                i += 1
        
        while len(linha_comprimida) < 4:
            linha_comprimida.append(0)
            
        novo_tabuleiro.append(linha_comprimida)

    return novo_tabuleiro

tabuleiro_exemplo_1 = [
    [2, 2, 4, 4],
    [8, 0, 8, 0],
    [0, 2, 2, 2],
    [4, 0, 0, 4]
]

novo_tabuleiro_1 = mover_esquerda_2048(tabuleiro_exemplo_1)
print("Tabuleiro Original 1:")
for linha in tabuleiro_exemplo_1:
    print(linha)
print("\nTabuleiro Após Jogada para Esquerda 1:")
for linha in novo_tabuleiro_1:
    print(linha)

print("\n" + "-" * 30 + "\n")

tabuleiro_exemplo_2 = [
    [2, 4, 8, 16],
    [0, 0, 0, 0],
    [2, 0, 4, 0],
    [0, 0, 8, 16]
]

novo_tabuleiro_2 = mover_esquerda_2048(tabuleiro_exemplo_2)
print("Tabuleiro Original 2:")
for linha in tabuleiro_exemplo_2:
    print(linha)
print("\nTabuleiro Após Jogada para Esquerda 2:")
for linha in novo_tabuleiro_2:
    print(linha)

