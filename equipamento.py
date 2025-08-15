departamento=input("qual seu departamento? [DS,Marketing,RH ou P&D?]:")
if departamento == "DS":
    print("equipamento mais adequado é laptops com alto desempenho")
elif departamento == "Marketing":
    print("é recomendavel tablets para facilitar a apresentação e mobilidade")
elif departamento=="RH":
    print("é recomendavel computadores desktop devido à sua estabilidade e custo-benefício")
elif departamento=="P&D":
    print("é necessario equipamentos com especificações de última geração.")
else:
    print("departamento não encontrado")