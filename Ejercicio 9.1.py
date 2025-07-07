#Se crea una lista donde se guardaran los numeros
numeros = [ ]
#Se agrega la cantidad de numeros que se van a sumar
c = int(input("Cuantos numeros vas a ingresar: "))
#Revisa que se agregue un numero mayor a cero
print("Ingresa los " + str(c) + " numeros")
for i in range( 0 , c):
	if c <= 0:
		print("Ingresa un numero positivo")
	else: 
	#Se pide que se ingresen los numeros, se hace la suma y se saca el promedio
		n = float(input("Los numeros son:   "))
		numeros.append(n)
		suma = sum(numeros)
		promedio = suma / c
		
#Se imprimen los numeros ingresados, la suma y el promedio		
print("Los numeros ingresados fueron " + str(numeros))
print("La suma de los numeros es " + str(suma))
print("El promedio es " + str(promedio))