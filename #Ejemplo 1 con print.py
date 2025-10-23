#Ejemplo 1 con print

print("Ejemplo 1\n")

# Introduccion 1
nombre = "Beto"

# Introduccion 2
edad = 18

# Introduccion 3
print("Hola, soy", nombre)

#Introduccion 4
print ("Tengo", edad, "años")


#Ejemplo 2 con print
#2. Nueva linea (\n)
print("\nEjemplo 2\n")

# Sin \n (todo es una linea)
print("Hola Mundo")
# Salida: Hola Mundo

# Con \n (salto de linea)
print("Hola\nMundo")

# Multiples \n
print("Linea 1\nLinea 2\nLinea 3")








#Ejemplo 3 con tabulacion
print ("\n Ejemplo 3\n")

print("Nombre: \tBeto")
print("Edad: \t18")
print("Ciudad: \tMonterrey")

#Ejemplo 4 con tabulacion
print("\nEjemplo 4\n")

#Crear una conversacion de chat
print("Ana:\tHola, ¿como estas?")
print("Luis:\tBien, ¿ tu?")
print("Ana: \t¡Genial\n")
print("===== Chat guardado en =====")
print ("C:\\Users\\BETO\\Documents\\chat.txt")


# Ejemplo 5
print("\nEjemplo 5\n")

# Dos argumentos
print("Hola", "Mundo")
# Salida: Hola Mundo



# Tres argumentos
print("Me","gusta", "dibujar" )

#Mezclando tipos de datos
print ("Tengo", 2, "mascotas en mi casa")

#Con ventajas
nombre = "Dany"
cantidad_hermanos = 2
print("Me dicen", nombre, "y tengo", cantidad_hermanos, "hermanos")


#Ejercicio 6. OPERADORES ARIMETICOS
print("Ejercicio 6. OPERADORES ARIMETICOS")
# SUMA (+): vamos a sumar dos numeros
numero1 = 42
numero2 = 22
suma = numero1 + numero2
print("Operador suma:" , suma)

# RESTA (-): ahora vamos a restar
resta = numero1 - numero2
print("Operador resta", resta)

# MULTIPLICACION (*): multiplicaciones dos numeros
multiplicacion = numero1 * numero2
print("Operador multiplicacion:", multiplicacion)

# DIVISION (/): dividimos y obtenemos resultado con decimales
division = numero1 / numero2
print("Operador division:", division)


print("Ejercicio 7, Operadores de comparacion")

print("¿He aprobado o no la materia?")
# MAYOR O IGUAL (>=): La calificacion minima para pasar es 70
calificacion = 70
resultado5 = calificacion >= 70
print("¿Aprobe?:", resultado5)

# MAYOR (>): La calificacion minima para pasar es 70
resultado6 = calificacion > 70
print("¿Aprobe?:", resultado6)

# Vamos a comparar estos dos numeros 
mi_edad = 17
edad_minima = 18

# IGUAL A (==): Pregunta: ¿Los numeros son iguales?
resultado1 = mi_edad == 15
print ("\n¿Soy mayor de edad? (==):", resultado1)

# DIFERENTE DE (!=) Pregunta: ¿Los numeros son diferentes?
resultado2 = mi_edad != 20
print("¿Tengo 18 años? (!=):", resultado2)

# MENOR QUE (<): Pregunta: ¿El primer numero es menor?
resultado3 = mi_edad < 18 
print("¿Mi edad es menor que 18? (<):", resultado3)

# MENOR O IGUAL (<=): Pregunta: ¿Es menor o igual?
resultado4 = mi_edad <= 10
print("¿Mi edad es menor o igual a 10? (<=):_", resultado4)


#Ejercicio 8. Operadore logicos
print("Ejercicio 8. Operadores logisticos")
#Imagina que queremos entrar a un juego online
tengo_internet = True #Si tengo internet
tengo_cuenta = True #Si teng cuenta

# AND (y): Las DOS condiciones deben ser verdaderas
puedo_jugar = tengo_internet and tengo_cuenta
print("¿Puedo jugar? (ambas true):", puedo_jugar)

#Problemas cuando falta algo
tengo_internet2 = True
tengo_cuenta2 = False
puedo_jugar2 = tengo_internet2 and tengo_cuenta2
print("¿Pued jugar? (una es False)", puedo_jugar2)

# OR (o): Al menos UNA condicion debe ser verdadera
tengo_celular = True
tengo_tablet = False
tengo_dispositivo = tengo_celular or tengo_tablet
print("¿Tengo dispositivo? (al menos una True):", tengo_dispositivo)

# NOT (no): Invierte el valor: True se vuelve False y viceversa
esta_lloviendo = False
puedo_salir = not esta_lloviendo
print("¿Puedo salir? (NOT False = True):", puedo_salir)


print("Ejercicio 9. Operadores de asignación\n")

#ASIGNACIÓN SIMPLE (=): Guardamos un valor en una variable
puntos = 0
print("Puntos iniciales:", puntos)

7 #SUMA Y ASIGNA (+-): Es lo mismo que escribir: puntos puntos + 10
puntos += 10
print("Ganaste 10 puntos (+-):", puntos)

#RESTA Y ASIGNA (--): Es lo mismo que escribir: puntos puntos - 5
puntos -= 5
print("Perdiste 5 puntos (--):", puntos)

# MULTIPLICA Y ASIGNA (*): Es lo mismo que escribir: puntos puntos 2
puntos *= 2
print("Puntos x21 (*=):", puntos)

# DIVIDE Y ASIGNA (/-): Es lo mismo que escribir: puntos puntos / 2
puntos /= 2
print("Dividir puntos (/=):", puntos)



print("Ejercicio 10. Operadores de identidad\n")

# Programa que compara objetos
print("=== SON LA MISMA COSA? ===")
# Creamos dos listas que se ven iguales
listal = ["manzana", "pera"]
lista2 = ["manzana", "pera"]
lista3= listal # lista3 es la MISMA que listal

# IS (es): Pregunta Son el mismo objeto en la memoria?
print("¿listal es lista2? (is):", listal is lista2) # False (diferentes objetos)
print("listal es listas? (is):", listal is lista3) # True (mismo objeto)

# IS NOT (no es): Pregunta ¿NO son el mismo objeto?
print("lista1 NO es lista2? (is not):", listal is not lista2) # True