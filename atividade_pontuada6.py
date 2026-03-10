import os 

# limpando o terminal

os .system ("cls || clear")

nota1 = float(input(" digite a primeira nota:"))
nota2 = float(input(" digite a segunda nota:"))
media = (nota1 + nota2) / 2

if media >= 6: 
    print (" aluno aprovado")
elif media >= 4 and media < 6:
    print (" aluno em recuperação")
else:
    print (" aluno reprovado")  


print("Fim do programa")

#danterks
