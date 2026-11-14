# Solicitando o CPF ao usuário
cpf= input("Digite o seu cpf: ")

# Realizando a remoção do . e - e armarzenando CPF limpo
cpf_limpo= cpf.replace(".","").replace("-","")

# Apresentando resultado do CPF limpo
print(f"CPF Limpo: {cpf_limpo}")