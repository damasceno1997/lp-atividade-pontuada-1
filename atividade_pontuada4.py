import os 

# limpando o terminal 

os.system ("cls || clear")

# Ler quantidade de frutas
morango = float(input("Digite a quantidade de morangos (kg): "))
maca = float(input("Digite a quantidade de maçãs (kg): "))

# Preço do morango
if morango <= 5:
    preco_morango = morango * 2.50
else:
    preco_morango = morango * 2.20

# Preço da maçã
if maca <= 5:
    preco_maca = maca * 1.80
else:
    preco_maca = maca * 1.50

# Total da compra
total = preco_morango + preco_maca
peso_total = morango + maca

# Verificar desconto
if peso_total >= 10 or total > 15:
    total = total * 0.90  # 10% de desconto

# Mostrar resultado
print("Valor a pagar: R$", round(total, 2))


print("\nfim do programa")


#danterks