Distancia_TotalX=input("qual a distancia?:120,150:")
Total_CombustivelY=input("quanto de combustivel?[15,25]:")
Distancia_TotalX1=120
Total_CombustivelY1=15
media1 = 120//15
media2=150//25

if Distancia_TotalX=="120" and Total_CombustivelY=="15":
    print(f"a media é {media1:3f} km/l")
elif Distancia_TotalX=="150" and Total_CombustivelY=="25":
    print(f"a media é {media2:3f} km/l")
else:
    print("não encontrado")