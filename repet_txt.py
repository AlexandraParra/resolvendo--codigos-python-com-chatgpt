# Vamos a solicitar uma string e um número inteiro como entrada. Depois será impressa a string o número de vezes do valor do número.

# Solicita uma string e um número inteiro ao usuário
texto = input("Digite uma string: ")
vezes = int(input("Digite um número inteiro: "))

# Imprime a string o número de vezes especificado
for _ in range(vezes):
    print(texto)