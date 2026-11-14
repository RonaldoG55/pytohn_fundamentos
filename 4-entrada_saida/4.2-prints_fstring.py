nome = "Ronaldo"
curso = "fundamentos python"
preco = 49.9
codigo_peca = 7

print("Aluno: ", nome," | Curso: ", curso.title())
print(f"Aluno: {nome} | Curso: {curso.title()}")

print(f"Valor original (ponto): R$ {preco:.2f}".replace(".",","))

print(f"Código da peça: #{codigo_peca:05d}")