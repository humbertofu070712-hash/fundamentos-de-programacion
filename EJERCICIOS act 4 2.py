# EJEMPLO 1: Mostrar el menú
print("\nEjemplo 1 mostrar el menu\n")

def mostrar_menu():
    print("=== MENÚ ===")
    print("1. Hamburguesa")
    print("2. Pizza")
    print("3. Tacos")

mostrar_menu()



# EJEMPLO 2: Reproducir tu canción favorita (sin parámetros)
print("\nEjemplo 2 la fav canción\n")

def reproducir_favorita():
    print("Reproduciendo: 'Blinding Lights' de The Weeknd")

reproducir_favorita()



# EJEMPLO 3: Mostrar reglas del juego
print("\nEjemplo 3 reglas del juego\n")

def mostrar_reglas():
    print("REGLAS DEL JUEGO:")
    print("- No hacer trampa")
    print("- Respetar turnos")
    print("- Divertirse")

mostrar_reglas()



# EJEMPLO 4: Reproducir cualquier canción (con parámetros)
print("\nEjemplo 4\n")

def reproducir_cancion(nombre_cancion):
    print(f"🎵 Reproduciendo: {nombre_cancion}")

reproducir_cancion("Bad Bunny - Titi Me Preguntó")
reproducir_cancion("Karol G - TQG")
reproducir_cancion("Taylor Swift - Anti-Hero")



# EJEMPLO 5: Calcular impuesto
print("\nEjemplo 5\n")

def calcular_impuesto(precio):
    total = precio * 1.16  # impuesto 16%
    return total

print(calcular_impuesto(110))
print(calcular_impuesto(500))
print(calcular_impuesto(1200))





# EJERCICIO 1: Mostrar tu perfil (sin parámetros)
print("\nEjercicio 1\n")

def mostrar_perfil():
    print("Usuario: @taylorswift")
    print("Seguidores: 1.2b")
    print("Bio: Cantante")

mostrar_perfil()
print()  # línea en blanco
mostrar_perfil()



# EJERCICIO 2: Horas de TikTok
print("\nEjercicio 2\n")

def calcular_horas_tiktok(minutos_por_dia):
    minutos_totales = minutos_por_dia * 7
    horas_totales = minutos_totales / 60
    return horas_totales

horas = calcular_horas_tiktok(30)
print(f"Ves {horas} horas de TikTok a la semana ")

horas2 = calcular_horas_tiktok(60)
print(f"Ves {horas2} horas de TikTok a la semana ")



# EJERCICIO 3: Comprar productos
print("\nEjercicio 3\n")

def puedo_comprar(dinero_que_tengo, precio_producto):
    if dinero_que_tengo >= precio_producto:
        return "Sí puedes comprarlo"
    else:
        return "No te alcanza"

resultado1 = puedo_comprar(500, 300)
print(f"Tenis nuevos: {resultado1}")

resultado2 = puedo_comprar(150, 800)
print(f"Celular nuevo: {resultado2}")

resultado3 = puedo_comprar(100, 100)
print(f"Audífonos: {resultado3}")



# EJERCICIO 4: Likes de Instagram
print("\nEjercicio 4\n")

def calcular_likes_totales(likes_foto1, likes_foto2, likes_foto3):
    total = likes_foto1 + likes_foto2 + likes_foto3
    return total

total = calcular_likes_totales(150, 230, 89)
print(f"Tienes {total} likes en total ")

total2 = calcular_likes_totales(800, 420, 300)
print(f"Tienes {total2} likes en total ")



# EJERCICIO 5: Descuento en tienda
print("\nEjercicio 5\n")

def aplicar_descuento(precio_original, porcentaje_descuento):
    descuento = precio_original * porcentaje_descuento / 100
    precio_final = precio_original - descuento
    return precio_final

precio_final = aplicar_descuento(1000, 20)
print(f"Precio final: ${precio_final} ")

precio_final2 = aplicar_descuento(500, 10)
print(f"Precio final: ${precio_final2} ")



# EJERCICIO 6: Promedio de calificaciones
print("\nEjercicio 3\n")

def calcular_promedio(cal1, cal2, cal3):
    suma = cal1 + cal2 + cal3
    promedio = suma / 3
    return promedio

promedio = calcular_promedio(85, 90, 78)
print(f"Tu promedio es: {promedio} ")

promedio2 = calcular_promedio(100, 95, 88)
print(f"Tu promedio es: {promedio2} ")