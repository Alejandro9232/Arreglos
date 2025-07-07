#Las listas que se van a crear para hacer las multiplicaciones
a = []
b = []
#Se pide al usuario cuantas multiplicaciones se van a hacer

c = int(input("Ingrese cuantas multiplicaciones se van a realizar: "))

#valor para iniciar la multiplocacion
producto = 0

#Revisa que los numeros que se ingresan a las listas sea mayor a cero
if c <= 0:
    print("Ingresa un numero positivo")
else: 
    print("Ingresa numeros para la lista a")
    #Se indica cuantos numeros se van a pedir y los numeros para la lista a y a.append los guarda en la lista
    for i in range(0, c):
        d = float(input("Numeros de la lista a: "))
        a.append(d)
    print("Ingresa numeros para la lista b") 
    #Ahora los numeros para la lista b   
    for i in range(0, c):
        e = float(input("Numeros de la lista b: "))
        b.append(e)
        
    #Se imprimen los resultados multiplicacion por multiplicacion y la suma de su producto punto
    print("Los resultados son: ")
    for i in range(0, c):
        resultado = a[i] * b[i]
        print(str(a[i]) + " * " + str(b[i]) + " = " + str(resultado))
        producto += resultado

    print("El producto punto es: " + str(producto))
