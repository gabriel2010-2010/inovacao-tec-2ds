# Programa para calcular a média de 4 números

# Solicita os 4 números ao usuário via input
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))
numero4 = float(input("Digite o quarto número: "))

# Calcula a média somando os 4 números e dividindo por 4
media = (numero1 + numero2 + numero3 + numero4) / 4

# Exibe o resultado com duas casas decimais usando f-string
print(f"A média dos números é: {media:.2f}")
