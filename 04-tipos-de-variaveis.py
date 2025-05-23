"""
Imprima na tela o tipo de cada variável abaixo, 
depois mude o tipo de cada uma e verifique o novo tipo
"""

x = 10
y = "Dez"

print("Tipo  original de x: ",type(x))
print("Tipo  original de y: ",type(y))

x = str(x)
y = 10

print("Tipo  modificado de x: ",type(x))
print("Tipo  modificado de y: ",type(y))
