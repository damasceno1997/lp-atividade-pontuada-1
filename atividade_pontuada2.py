import os 

# limpando o terminal

os.system ("cls || clear")

# Ler os dados da pessoa
nome = input("Digite o nome: ")
sexo = input("Digite o sexo (M/F): ").upper()
estado_civil = input("Digite o estado civil: ").upper()

tempo_casada = None

# Verificar condição
if sexo == "F" and estado_civil == "CASADA":
    tempo_casada = int(input("Digite o tempo de casada (anos): "))

# Mostrar os dados
print("\n--- Dados do Usuário ---")
print("Nome:", nome)
print("Sexo:", sexo)
print("Estado civil:", estado_civil)

if tempo_casada is not None:
    print("Tempo de casada:", tempo_casada, "anos")
    
    
print("\nfim do programa")


#danterks