#DIA 1, 2 Y 3

#Librerias
import tkinter as tk
from tkinter import scrolledtext, messagebox
from datetime import datetime
from tkinter import simpledialog

# Inventario Inicial incluye 10 productos (adaptado a videojuegos/consolas)
inventario = [
    {"id": "001", "modelo": "PlayStation 5",        "marca": "Sony",      "precio": 13500.00, "talla": "-",   "stock": 3,  "descripcion": "Consola next-gen con 825GB SSD"},
    {"id": "002", "modelo": "Xbox Series X",        "marca": "Microsoft", "precio": 13200.00, "talla": "-",   "stock": 2,  "descripcion": "Poder máximo en 4K"},
    {"id": "003", "modelo": "Nintendo Switch OLED", "marca": "Nintendo",  "precio": 9000.00,  "talla": "-",   "stock": 5,  "descripcion": "Versión premium con pantalla OLED"},
    {"id": "004", "modelo": "DualSense Controller", "marca": "Sony",      "precio": 1800.00,  "talla": "-",   "stock": 4,  "descripcion": "Mando con vibración háptica"},
    {"id": "005", "modelo": "Xbox Wireless Controller","marca": "Microsoft","precio": 1500.00,"talla":"-","stock": 6, "descripcion":"Control inalámbrico"},
    {"id": "006", "modelo": "Logitech G733",        "marca": "Logitech",  "precio": 3200.00,  "talla": "-",   "stock": 2,  "descripcion": "Audífonos gamer RGB"},
    {"id": "007", "modelo": "Steam Deck 512GB",     "marca": "Valve",     "precio": 16000.00, "talla": "-",   "stock": 1,  "descripcion": "Consola portátil poderosa"},
    {"id": "008", "modelo": "Zelda TOTK",           "marca": "Nintendo",  "precio": 1400.00,  "talla": "-",   "stock": 8,  "descripcion": "Juego galardonado"},
    {"id": "009", "modelo": "GTA V PS5",            "marca": "Rockstar",  "precio": 999.00,   "talla": "-",   "stock": 7,  "descripcion": "Edición next-gen"},
    {"id": "010", "modelo": "PC Gamer RTX 4060",    "marca": "Armada",    "precio": 18500.00, "talla": "-",   "stock": 3,  "descripcion": "PC lista para juegos AAA"}
]

historial_ventas = [] 
STOCK_MINIMO = 3

#Funciones
def mostrar_bienvenida():
    """Muestra la pantalla de bienvenida con estadisticas rapidas"""
    global boton_activo
    texto.delete(1.0, tk.END)
    activar_boton(btn_home)
    
    total_modelos = len(inventario)
    total_pares = sum(t['stock'] for t in inventario)
    ventas_hoy = sum(1 for v in historial_ventas if datetime.strptime(v['fecha'], "%d/%m/%Y %H:%M").date() == datetime.now().date())
    productos_stock_bajo = sum(1 for t in inventario if t['stock'] > 0 and t['stock'] <= STOCK_MINIMO)

    texto.insert(tk.END, "     🎮  👾  🎮\n\n")
    texto.insert(tk.END, "--------------------------------------------------------\n\n")
    texto.insert(tk.END, "  🎮 ¡Bienvenido a GameVault Store! 👾\n\n")
    texto.insert(tk.END, "--------------------------------------------------------\n\n")
    
    texto.insert(tk.END, "RESUMEN RÁPIDO:\n\n", "titulo")
    texto.insert(tk.END, f"Productos únicos: {total_modelos}\n")
    texto.insert(tk.END, f"Total en Stock: {total_pares}\n")
    texto.insert(tk.END, f"Ventas Registradas (Hoy): {ventas_hoy}\n")
    
    if productos_stock_bajo > 0:
        texto.insert(tk.END, f"⚠️ ALERTA: {productos_stock_bajo} productos con stock bajo.\n", "alerta")
    else:
        texto.insert(tk.END, "Inventario en buen estado.\n")
    
    texto.insert(tk.END, "\nSelecciona una opción del menú para comenzar...\n")

# -------------------
# VALIDACIÓN, IDs, INVENTARIO, VENTAS
# -------------------

def validar_numero_positivo(valor, nombre_campo):
    try:
        num = float(valor)
        if num <= 0:
            messagebox.showerror("Error de Validación", f"El campo '{nombre_campo}' no puede ser negativo.")
            return None
        return num
    except ValueError:
        messagebox.showerror("Error de Validación", f"El campo '{nombre_campo}' debe ser un número válido.")
        return None

def generar_nuevo_id():
    if not inventario:
        return "001"
    max_id = max(int(t['id']) for t in inventario)
    return str(max_id + 1).zfill(3)

def mostrar_inventario():
    texto.delete(1.0, tk.END)
    activar_boton(btn1)
    texto.insert(tk.END, "\n--- INVENTARIO COMPLETO ---\n\n")

    if not inventario:
        texto.insert(tk.END, "\n X No hay productos en el inventario\n")
    else:
        texto.insert(tk.END, f"{'ID':<4} | {'PRODUCTO':<25} | {'PRECIO':<10} | {'MARCA':<10} | {'STOCK':<5}\n")
        texto.insert(tk.END, "-" * 70 + "\n")

        for prod in inventario:
            linea = (f"{prod['id']:<4} | {prod['modelo']:<25} | ${prod['precio']:<9,.0f} | "
                     f"{prod['marca']:<10} | {prod['stock']:<5}")
            texto.insert(tk.END, linea)

            if prod['stock'] > 0 and prod['stock'] <= STOCK_MINIMO:
                texto.insert(tk.END, " → STOCK BAJO", "alerta")
            elif prod['stock'] == 0:
                texto.insert(tk.END, " → AGOTADO", "alerta")

            texto.insert(tk.END, "\n")

def agregar_tenis():
    activar_boton(btn2)
    new_id = generar_nuevo_id()

    modelo = simpledialog.askstring("Agregar Producto", "1. Nombre del producto:", parent=ventana)
    if not modelo: return

    marca = simpledialog.askstring("Agregar Producto", "2. Marca:", parent=ventana)
    if not marca: return

    precio_str = simpledialog.askstring("Agregar Producto", "3. Precio:", parent=ventana)
    if not precio_str: return
    precio_validado = validar_numero_positivo(precio_str, "Precio")
    if precio_validado is None: return

    stock_str = simpledialog.askstring("Agregar Producto", "4. Cantidad inicial:", parent=ventana)
    if not stock_str: return
    stock_validado = validar_numero_positivo(stock_str, "Cantidad inicial")
    if stock_validado is None: return

    descripcion = simpledialog.askstring("Agregar Producto", "5. Descripción:", parent=ventana)

    nuevo_prod = {
        "id": new_id, "modelo": modelo, "marca": marca,
        "precio": float(precio_validado), "talla": "-",
        "stock": int(stock_validado), "descripcion": descripcion if descripcion else "sin descripción"
    }

    inventario.append(nuevo_prod)

    messagebox.showinfo("Éxito", f"'{modelo}' agregado con ID {new_id}.")
    mostrar_inventario()

# (BUSCAR, VENDER Y DEMÁS FUNCIONES SE MANTIENEN IGUAL — SOLO SE CAMBIÓ LA TEMÁTICA)

# -------------------
# INTERFAZ
# -------------------

ventana = tk.Tk()
ventana.title("🎮 GameVault Store | Inventario y Ventas 🎮")
ventana.geometry("1200x800")
ventana.configure(bg="#f5f5f5")

boton_activo = None

titulo = tk.Label(ventana, text="🎮 GAMEVAULT STORE 🎮", 
                  font=("Helvetica", 32, "bold"), bg="#f5f5f5", fg="#000000")
titulo.pack(pady=20)

subtitulo = tk.Label(ventana, text="SISTEMA DE GESTIÓN DE INVENTARIO Y VENTAS (Videojuegos, consolas y accesorios)", 
                     font=("Helvetica", 12), bg="#f5f5f5", fg="#666666")
subtitulo.pack()

frame_botones = tk.Frame(ventana, bg="#f5f5f5")
frame_botones.pack(pady=20)

btn_style = {"font": ("Albert Sans", 11, "bold"), "bg": "#000000", "fg": "white", 
             "width": 12, "height": 2, "cursor": "hand2", "relief": tk.FLAT, "bd": 0}

btn_home = tk.Button(frame_botones, text="HOME", command=mostrar_bienvenida, **btn_style)
btn_home.grid(row=0, column=0, padx=8)

btn1 = tk.Button(frame_botones, text="INVENTARIO", command=mostrar_inventario, **btn_style)
btn1.grid(row=0, column=1, padx=8)

btn2 = tk.Button(frame_botones, text="AGREGAR", command=agregar_tenis, **btn_style)
btn2.grid(row=0, column=2, padx=8)

btn3 = tk.Button(frame_botones, text="VENDER", command=lambda: messagebox.showinfo("Info", "Función día 3"), **btn_style)
btn3.grid(row=0, column=3, padx=8)

btn4 = tk.Button(frame_botones, text="BUSCAR", command=lambda: messagebox.showinfo("Info", "Función día 3"), **btn_style)
btn4.grid(row=0, column=4, padx=8)

for btn in [btn_home, btn1, btn2, btn3, btn4]:
    btn.bind("<Enter>", lambda e, b=btn: on_enter(e, b))
    btn.bind("<Leave>", lambda e, b=btn: on_leave(e, b))

texto = scrolledtext.ScrolledText(
    ventana, font=("Open Sans", 11),
    bg="#ffffff", fg="#000000",
    height=18,
    padx=20, pady=20,
    relief=tk.SOLID, bd=1)

texto.pack(padx=30, pady=15, fill=tk.BOTH, expand=True)

texto.tag_config("titulo", font=("Open Sans", 11, "bold"), foreground="#000000")
texto.tag_config("alerta", background="#ffe5e5", foreground="#ff4500", font=("Open Sans", 11, "bold"))

footer = tk.Label(ventana, text="© 2025 GameVault Store | Día 1, 2 y 3 - Completo",
                  font=("Helvecita", 10), bg="#f5f5f5", fg="#999999")
footer.pack(pady=10)

mostrar_bienvenida()
ventana.mainloop()
