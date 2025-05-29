#Desenvolva uma calculadora em Python que realize as quatro operacoes basicas entre dois numeros. 
#A calculadora deve ser capaz de lidar com diversos tipos de erros de entrada e operacao. 

#- A calculadora deve solicitar ao usuario que insira dois numeros e uma operacao.
#- As operacoes validas sao: + (adicao), - (subtracao), * (multiplicacao) e / (divisao).
#- O programa deve continuar solicitando entradas ate que uma operacao valida seja concluida.

while True:
    try:
        #Solicita ao user dois números e converte para float
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        # Solicita a operação desejada
        operacao = input("Escolha a operação (+, -, *, /): ")

        # Verifica e executa a operação
        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            if num2 == 0:
                raise ZeroDivisionError("Não é possível dividir por zero.")
            resultado = num1 / num2
        else:
            print("Operação inválida. Tente novamente com +, -, * ou /.")
            continue  # Volta ao início do loop

        # Exibir o resultado da operção
        print(f"Resultado: {resultado}")
        break  # Sai do loop após sucesso

        # Caso o user coloque entradas inválidas
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar números válidos.")
    except ZeroDivisionError as erro:
        print(erro)




