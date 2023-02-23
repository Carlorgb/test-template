print("Hello")

lista_marcas=[ "audi" , "bmw", "honda", "toyota" ]

for indice , marcas  in enumerate(lista_marcas): 
   print(indice + 1 , marcas)

for elemento in lista_marcas: 
    print (elemento)

print (" fin de juego")




for numero in range (50,101 ,5):
   print (numero)




















digitos = [1, 2, 3, 4, 5, 6, 7 , 8 , 9 , 0]
print (min(digitos))
print (max(digitos))
print (sum(digitos))

#def suma (a,b):
 #  return a + b 

#resultado = suma(10,5)
#print (resultado) #



digitos=list (range (0,1000001 )) 
print (min (digitos))
print (max (digitos))
print (sum(digitos))




#hacer una lista de los multiplos del 3 hasta al 30#

lista_numeros = ("multiplos de 3" )
print ( "multiplos de" [3])

for numero in range(1, 31):
    print(f"{numero} * 3 = {numero * 3}")

for numero in range(1, 31):
    print(f"{numero} * 5 = {numero * 5}")

    n = 0
if n > 0 :
    print("mayor")
else:
    print("menor")