import os 

# limpando o terminal

os.system ("cls || clear")

 # Ler dois valores inteiros
 
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

# Verificar se são iguais

if A == B:
    C = A + B
else:
    C = A * B

# Mostrar o resultado

print("O valor de C é:", C)

print("\nfim do programa")


#danterks