quantidade = int(input("Digite a quantidade de peças compradas: "))
preco_unitario = float(input("Digite o preço unitário de cada peça (ex: $50.00): "))

desconto_percentual = 0
preco_base = quantidade * preco_unitario

if quantidade <= 5:
    pass
elif quantidade <= 10:
    desconto_percentual = 0.10
else:
    desconto_percentual = 0.20

valor_desconto = preco_base * desconto_percentual

preco_final = preco_base - valor_desconto

print(" " * 30)
print("-" * 40)
print(f"Resumo da Compra:")
print(f"Preço base (total sem desconto): R$ {preco_base:.2f}")
print(f"Desconto aplicado: {desconto_percentual * 100:.0f}% (R$ {valor_desconto:.2f})")
print(f"Preço final a pagar: R$ {preco_final:.2f}")
print("-" * 40)
print(" " * 30)