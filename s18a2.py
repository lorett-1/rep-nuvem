import random
tota_percorrido=0
intervalo_n=int(input("qual o intervalo?[1, 1000]:"))
while intervalo_n < 1 or intervalo_n > 1000:
    intervalo_n=int(input("qual o intervalo?[1, 1000]:"))
for i in range(1,intervalo_n+1):
    tempo_t= random.randint(1,100)
    velocidade_v=random.randint(0,120)
print(f"intervalo {i}, tempo {tempo_t}, velocidade {velocidade_v}, distancia {tempo_t*velocidade_v}")
distancia=tempo_t*velocidade_v
total_percorrido=+ distancia
print(f"o total percorrido em km é = {total_percorrido:3f}")
