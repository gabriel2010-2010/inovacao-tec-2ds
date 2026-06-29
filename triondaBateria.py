# 1. Definição das variáveis (altere os valores para testar outros cenários)
bateria_atual = 14  # Número inteiro de 0 a 100
bola_em_jogo = False  # Valor booleano (True ou False)

# 2. Estrutura condicional ordenada para avaliar o estado da bola Trionda
if bateria_atual < 15 and bola_em_jogo:
    print(
        "ALERTA MÁXIMO: Bateria baixa! Substitua a bola na próxima paralisação."
    )

elif bateria_atual < 15 and not bola_em_jogo:
    print("Aviso: Bateria baixa. Aproveite a bola parada para trocá-la.")

else:
    print("Sistema Trionda operando normalmente. Bateria ok.")
