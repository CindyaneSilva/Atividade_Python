#Enunciado:
#Desenvolva um programa que calcule o Indice de Massa Corporal (IMC) de uma pessoa.
#O programa deve solicitar o peso (em kg) e a altura (em metros), calcular o IMC e informar a classificacao de acordo com a tabela padrao.

peso = float(input("Qual é o seu peso? "))
altura = float(input("Qual é a sua altura? "))

imc = peso / (altura ** 2)

print (f"Seu IMC é:  {imc:.2f}")