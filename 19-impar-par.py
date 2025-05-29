#Crie um programa que solicite ao usuario que insira numeros inteiros. 
#O programa deve continuar solicitando numeros ate que o usuario digite 'fim'. 
#Para cada numero inserido, o programa deve informar se e par ou impar. 
#Se o usuario inserir algo que nao seja um numero inteiro, o programa deve informar o erro e continuar. 
#No final, o programa deve exibir a quantidade de numeros pares e impares inseridos.

qtdePar = 0
qtdeImpar = 0

while True:
     entrada = input("Digite um número inteiro para continuar ou 'fim' para encerrar: ")

     if entrada.lower() == 'fim':
        print("Encerrando o programa")
        break

     try:
      num = int(entrada)

      if num  % 2 == 0:
       print(f"O número {num} é PAR") 
       qtdePar += 1
      else:  
        print(f"O número {num} é ÍMPAR") 
        qtdeImpar += 1  

     except:
      print("ERROR: Esse não é um número inteiro")  
print(f"A quantidade de números pares é: {qtdePar}")    
print(f"A quantidade de números ímpares é: {qtdeImpar}")    