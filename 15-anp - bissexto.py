#Faça um programa que determine se um ano inserido pelo usuario e bissexto ou nao.

ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0 ) or (ano % 400 ==0):
    print(f" O ano {ano} é bissexto")

else:
    print(f"O ano {ano} não é bissexto.")
