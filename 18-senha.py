while True:
    senha = input("Digite uma senha: ")
    
    if senha.lower() == "sair":
     print("Encerrado. Até logo!")
     break
    print("Verificando senha...")

    if len(senha) < 8:
       print("Sua senha tem menos de 8 caracteres!")
       continue
    else:
       print("Sua senha tem 8 ou mais caracterres")

       temNum = False

       for caractere in senha:
         if caractere in '0123456789' :
          temNum = True
          print("Número encontrado")
          break
         
       if not temNum:
         print("Sua senha não tem nenhum número")
         continue
       else:
         print("Sua senha tem pelo menos um número")

         print("Senha forte! Aprovada")
         break
