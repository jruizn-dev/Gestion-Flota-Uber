import tkinter as tk
from tkinter import messagebox

# --- 1. EL CEREBRO ---
def revisar_mantenimiento(km):
    try:
        valor_km = int(km)
        if valor_km >= 5000:
            return "TALLER" # Quitamos el emoji de aquí para evitar errores
        else:
            return "OK"
    except ValueError:
        return "ERROR"

def guardar_auto():
    modelo = entrada_modelo.get()
    chofer = entrada_chofer.get()
    km = entrada_km.get()

    if modelo == "" or chofer == "" or km == "":
        messagebox.showwarning("Atencion", "Por favor llena todos los campos")
        return

    estado = revisar_mantenimiento(km)
    
    if estado == "ERROR":
        messagebox.showerror("Error", "En Kilometraje solo pon numeros")
        return

    linea = f"Modelo: {modelo} | Chofer: {chofer} | KM: {km} | Estado: {estado}\n"

    # --- 2. LA CORRECCIÓN CLAVE AQUÍ ---
    # Agregamos encoding='utf-8' para que soporte cualquier caracter
    with open("flota_jonathan.txt", "a", encoding='utf-8') as archivo:
        archivo.write(linea)

    messagebox.showinfo("Exito", f"Auto registrado.\nEstado: {estado}")
    
    entrada_modelo.delete(0, tk.END)
    entrada_chofer.delete(0, tk.END)
    entrada_km.delete(0, tk.END)

# --- 3. LA VENTANA ---
app = tk.Tk()
app.title("FLOTILLA JONATHAN - Control Uber")
app.geometry("400x450")

tk.Label(app, text="SISTEMA DE GESTION", font=("Arial", 16, "bold")).pack(pady=20)

tk.Label(app, text="Modelo del Auto:").pack()
entrada_modelo = tk.Entry(app, font=("Arial", 12))
entrada_modelo.pack(pady=5)

tk.Label(app, text="Nombre del Chofer:").pack()
entrada_chofer = tk.Entry(app, font=("Arial", 12))
entrada_chofer.pack(pady=5)

tk.Label(app, text="Kilometraje Actual:").pack()
entrada_km = tk.Entry(app, font=("Arial", 12))
entrada_km.pack(pady=5)

boton_guardar = tk.Button(app, text="GUARDAR DATOS", 
                          command=guardar_auto, 
                          bg="green", fg="white", 
                          font=("Arial", 12, "bold"))
boton_guardar.pack(pady=30)

app.mainloop()
