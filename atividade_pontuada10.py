import os 

os.system("cls || clear")

# entrada de dados

litros = float(input("Digite a quantidade de litros: "))
tipo = input("Digite o tipo de combustível (A-álcool / G-gasolina): ").upper()

# Definir preços

preco_alcool = 3.79
preco_gasolina = 6.59

# Calculos


if tipo == "A":
    if litros <= 25:
        desconto = 0.02
    else:
        desconto = 0.04
    total = litros * preco_alcool * (1 - desconto)

elif tipo == "G":
    if litros <= 25:
        desconto = 0.03
    else:
        desconto = 0.05
    total = litros * preco_gasolina * (1 - desconto)

else:
    total = None
    print("Tipo de combustível inválido.")

# saida de dados
if total is not None:
    print("Valor a pagar: R$", round(total, 2))
    
print ("\n fim de programa")
       
# danterks