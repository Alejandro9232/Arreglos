#Listas donde se van a guardar los numeros
numeros = []
numeros_ordenados = []
#Los numeros que se van a ingresar
a = int(input("Ingresa cuantos numeros vas a añadir a la lista: "))
#Verifica si es mayor de 0
if a <= 0:
	print("El numero tiene que ser positivo")
else:
#Se ingresan los numeros a la lista numeros
    for i in range(a):
        b = int(input("Los numeros son: "))     
        numeros.append(b)
    print("Los numeros ingresados fueron "+str(numeros))
# Revisa si los son diferentes a cero y los envia a la otra lista numeros ordenados
    for i in numeros:
        if i != 0:
            numeros_ordenados.append(i)
#Cuenta cuantos ceros hay en la lista
cantidad_ceros = numeros.count(0)
#Aca los agrega al final de la lista
for i in range(cantidad_ceros):
    numeros_ordenados.append(0)
print("Hay " + str(cantidad_ceros) +" ceros")
print("Lista con ceros al final: " + str(numeros_ordenados))