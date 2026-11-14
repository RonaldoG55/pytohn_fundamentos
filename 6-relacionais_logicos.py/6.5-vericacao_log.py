# Cerregado os logs do sistema
log_sistema= "ERRO: Falha de comunicação no sensor 04"

# Verificar se a palavra "ERRO" está presente no log
tem_erro= "ERRO" in log_sistema
print(f"Falha detectada no log? {tem_erro}")

sem_critico= "CRÍTICO" not in log_sistema
print(f"Sem nível crtíco? {sem_critico}")