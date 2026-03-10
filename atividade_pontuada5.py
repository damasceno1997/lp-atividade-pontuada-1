import os

# limpando o terminal

os.system ("cls || clear")      

# Ler a operação
operacao = input("Digite a operação (+, -, * ou /): ")

# Ler os valores inteiros
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

# Verificar a operação escolhida
if operacao == "+":
    resultado = A + B
elif operacao == "-":
    resultado = A - B
elif operacao == "*":
    resultado = A * B
elif operacao == "/":
    if B != 0:
        resultado = A / B
    else:
        resultado = "Erro: divisão por zero"
else:
    resultado = "Operação inválida"

# Mostrar o resultado
print("Resultado:", resultado) 


print ("\n fim do programa")

#danterks