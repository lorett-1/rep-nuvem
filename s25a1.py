estoque=[20,15,10,30,5]
#criar funçoes atualizar,adicionar,exibir
def atualizar(elemento, quantidade):
    posiçao=elemento-1
    if 0<=posiçao<len(estoque):
        estoque[posiçao] -= quantidade
    else:
        print("elemento invalido!")

def exibir(estoque):
    print(f"estoque atual:{estoque}")
    
exibir(estoque)
atualizar(1,3)
print("estoque alterado")
exibir(estoque)
