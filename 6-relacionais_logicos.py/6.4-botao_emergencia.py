# Situação do botão não pressionada
emergencia_pressionada= False

# Liberação do funcionamento da máquina 
maquina_liberada= not emergencia_pressionada

print(f"Emergência pressionada? {emergencia_pressionada}")
print(f"A máquina pode rodar? {maquina_liberada}")