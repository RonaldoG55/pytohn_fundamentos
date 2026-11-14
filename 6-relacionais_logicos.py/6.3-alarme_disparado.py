# Definindo os valores das variavéis 
temperatura_critica= False

pressao_critica= True

# Realizando a checagem dos sensores
alarme_disparado=temperatura_critica or pressao_critica

# Apresentando disparo do alarme 
print(f"Alerme Ativado: {alarme_disparado}")