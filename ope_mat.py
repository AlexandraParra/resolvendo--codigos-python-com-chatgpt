# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

# Solicita os dois números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Solicita a operação desejada
operacao = input("Digite a operação que deseja realizar (+, -, *, /): ")

# Verifica a operação e realiza o cálculo
if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    # Verifica se o divisor é zero
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: Divisão por zero não é permitida."
else:
    resultado = "Operação inválida."

# Imprime o resultado
print(f"O resultado da operação {num1} {operacao} {num2} é: {resultado}")