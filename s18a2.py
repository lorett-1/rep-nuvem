import random

intervalo_n=int(input("qual o intervalo?[1, 1000]:"))
while intervalo_n < 1 or intervalo_n > 1000:
    intervalo_n=int(input("qual o intervalo?[1, 1000]:"))
for i in range(1,intervalo_n+1):
    tempo_t= random.randint(1,100)
    velocidade_v=random.randint(0,120)
    
intervalo_n=[1,1000]
tempo_t=[1,100]
velocidade_v=[0,120]
total_percorrido= tempo_t * velocidade_v
print
