n=int(input("qual o número?"))
while n<1 or n >1000:
    n=int(input("qual o número?"))
for i in range (1,n+1):
    print(f"{i}{i**2}{i**3}")
    print(f"{i}{(i**2)+1}{(i**3)+1}")