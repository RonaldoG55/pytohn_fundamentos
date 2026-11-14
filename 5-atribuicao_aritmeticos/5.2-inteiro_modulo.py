# Definindo o valor das variavéis 
total_sensores= int(input("Quantos sensores pretente embalar: "))
CAPACIDADE_CAIXA= 12

# Quantas caixas completas podemos encher?
caixas_fechadas= total_sensores // CAPACIDADE_CAIXA

# Quantos sensores vão sobrar avusos 
sobra_sensores= total_sensores % CAPACIDADE_CAIXA
print(f"Preencher {caixas_fechadas} caixas e guardar {sobra_sensores} peças avusas")