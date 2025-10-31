# Ejercicio 1
#  SALIDA - Bienvenida
print("=" * 45)
print("BIENVENIDO A GAME STORE")
print ("=" * 45)
print()

#  ENTRADA - Datos del cliente
nombre = input ("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
#  PROCESAMIENTO - Precios fijos de los juegos
precio_fifa = 899.00
precio_cod = 1299.00
precio_hello_kitty = 599.00

#  SALIDA - Catalogo de productos
print("------- CATALOGO DE PRODUCTOS -------")
print("1. FIFA 2025 - $" + str(precio_fifa))
print("2. Call of Duty - $" + str(precio_cod))
print("3. Hello Kitty Island Adventure - $" + str(precio_hello_kitty))
print()

#Entrada - Cantidad de cada juego
cantidad_fifa = float(input("¿Cuantos FIFA 2025 quieres?"))
cantidad_cod = float(input("¿Cuantos Call of Duty quieres"))
cantidad_hello_kitty = float(input("Cuantos Hello Kitty Island Adventure quieres?"))

# PROCESAMIENTO - Calculos por juego
total_fifa = precio_fifa * precio_fifa
total_cod = precio_cod * cantidad_cod
total_hello_kitty = precio_hello_kitty * cantidad_hello_kitty

# PROCESAMIENTO - Calculos totales
Subtotal = total_fifa + total_cod + total_hello_kitty
iva = Subtotal * 0.10
total = Subtotal + iva

#PROCESAMIENTO - Cantidad total de juegos
Cantidad_total = cantidad_fifa + cantidad_cod + cantidad_hello_kitty

# PROCESAMIENTO - Crear ticket
print("TICKET DE COMPRA")
print("=" * 18)
print("Cliente: " + nombre)
print("Edad: " + str(edad) + " años")
print("Fifa =", cantidad_fifa, "COD =", cantidad_cod, "Hello Kitty =", cantidad_hello_kitty, "PRECIO FINAL=", total)

print("=" * 18)

print("DETALLE DE COMPRA")
print("FIFA 2025:")
print(" Cantidad: " + str(cantidad_fifa))
print(" Precio unitario: $" + str(precio_fifa))
print(" Total: $" + str(total_fifa))
print("Call of Duty:")
print(" Cantidad: " + str(cantidad_cod))
print(" Precio unitario: $" + str(precio_cod))
print(" Total: $" + str(total_cod))
print("Hello Kitty Island Adventure:")
print(" Cantidad: " + str(cantidad_hello_kitty))
print(" Precio unitario: $" + str(precio_hello_kitty))
print(" Total: $" + str(total_hello_kitty))
print("=" * 45)
print("Cantidad total de juegos: " + str(Cantidad_total))
print("Subtotal: $" + str(Subtotal))
print("IVA (16%): $" + str(iva))
print("=" * 45)
print("TOTAL A PAGAR $" + str(total))
print()
# SALIDA - Mensaje de despedida
print("¡Gracias por tu compra", + nombre + "|")