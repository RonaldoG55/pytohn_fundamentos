# Solicitando dados do veículo

combustivel= float(input("Quantidade de combustível: "))
pneus_calibrados= input("Os pneus estão calibrados? (sim/nao):").lower().strip()
documento_ok= input("A documentação está em dia? (sim/nao):").lower().strip()

# Checagem individual (Retorna True ou False) 
combustivel_suficiente= combustivel >= 10.0
pneus_ok= pneus_calibrados== "sim"
documento_regularizado= documento_ok == "sim"

# Combinação lógica para liberação a viagem 
viagem_liberada= combustivel_suficiente and documento_regularizado and pneus_ok

# Apresentando o status e liberação da viagem
print("\n----STATUS DE SEGURANÇA PARA VIAGEM----")
print(F"1. Combustível Sufuciente (>=10L): {combustivel_suficiente} ")
print(f"2. Pneus Calibrados: {pneus_ok}")
print(f"Documentação Regularizada: {documento_regularizado}")
print(f"\n VIAGEM LIBERADA: {viagem_liberada}")