#Enunciado:
#Crie um programa que solicite a idade do usuario e classifique-o em uma das seguintes categorias:
while True:
    try:
        idade = int(input("Digite a sua idade: "))
        
        if idade < 0:
            print("Idade não pode ser negativa. Tente novamente.")
            continue

        if idade <= 12:
            print("Criança")
            break

        if idade <= 17:
            print("Adolescente")
            break

        if idade <= 59:
            print("Adulto")
            break  
        
        if idade >=60 :
            print("Idoso")
            break  
    except ValueError:
        print("Por favor digite um número inteiro.")       
