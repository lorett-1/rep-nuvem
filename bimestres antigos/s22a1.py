funcionario=int(input("qual o número??"))
while funcionario<1 or funcionario>10:
    funcionario==int(input("qual o número??"))
horas=int(input("qual a quantidade de horas??"))
recebido_hora=int(input("quanto recebe??"))
salário=recebido_hora*horas
print(f"seu salário é ${salário}.00")