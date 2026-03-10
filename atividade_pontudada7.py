import os 

# limpando o terminal

os.system ("cls || clear")

# entrada de dados

nome = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade adquirida: "))
preco_unitario = float(input("Digite o preço unitário: "))

# Calculo 
total = quantidade * preco_unitario

# Calcular o desconto
if quantidade <= 5:
    desconto = total * 0.02
elif quantidade <= 10:
    desconto = total * 0.03
else:
    desconto = total * 0.05

# Calcular total a pagar

total_pagar = total - desconto

# saida de dados 

print("\n--- Dados da compra ---")
print("Produto:", nome)
print("Total da compra: R$", round(total, 2))
print("Desconto: R$", round(desconto, 2))
print("Total a pagar: R$", round(total_pagar, 2))

print("\nfim do programa")


#danterks