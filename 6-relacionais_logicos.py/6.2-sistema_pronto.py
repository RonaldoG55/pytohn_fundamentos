# Criando status dos sensores
grande_fechada= True
emergencia_desativada= True

# Ambas precisam ser True para libarar o sistema 
sistema_pronto= grande_fechada and emergencia_desativada
print(f"Sistema Liberao: {sistema_pronto}")
