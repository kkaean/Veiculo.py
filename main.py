from Veiculo import Veiculo
from CarroPasseio import CarroPasseio
from CarroCorrida import CarroCorrida
from Caminhao import Caminhao

print("--- Teste Sistema de Veículos ---")

#Teste Veiculo
print("\n--- Teste Veículo (Moto) ---")
moto = Veiculo("CBR 1000RR", "Honda", 2023, "preto", 2, 1, ["gasolina"])
print(moto)
moto.liga()
moto.acelera(50)
print(f"Velocidade da moto: {moto.velocidade}")
print(moto)

# Teste CarrosPasse
print("\n--- Teste CarroPasseio (Renegade) ---")
reneg = CarroPasseio ("Renegade", "Jeep", 2016, "prata", 4, 4, ["etanol", "gasolina"], 4, True, True)
print(reneg)
reneg.liga()
reneg.acelera (30)
reneg.abre_porta(0)
print(f"Velocidade do Renegade: (reneg.velocidade)")
print(reneg)
reneg.desliga()
print(reneg)

#Teste CarroCorrida
print("\n--- Teste CarroCorrida (Ferrari) ---")
ferrari = CarroCorrida ("SF90", "Ferrari", 2019, "vermelho", True, True, True, 340)
print(ferrari)
ferrari.liga()
ferrari.veloc_max(300)
print(f"Velocidade da Ferrari: {ferrari.velocidade})")
ferrari.acelera (50)
print (f"Velocidade após acelerar: (ferrari, velocidade)")
ferrari.veloc_max(400)
print(f"Velocidade após tentar exceder: (ferrari.velocidade)")
ferrari.desliga()
print (ferrari)

#Teste Caminhão
print("\n--- Teste Caminhão (Volvo FH) ---")
caminhao = Caminhao("FH", "Volvo", 2020, 40)
print(caminhao)
caminhao.liga()
caminhao.acelera (20)
caminhao.carregar(25)
caminhao.carregar (20)
print(f"Velocidade do caminhão: (caminhao.velocidade)")
print(caminhao)