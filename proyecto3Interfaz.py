import tkinter as tk
from tkinter import scrolledtext, font
from logic import *
import itertools

# --- 1. LÓGICA DEL UNICORNIO (Igual que antes) ---
Mi = Symbol("Mítico")
I  = Symbol("Inmortal")
Ma = Symbol("Mamífero")
Mo = Symbol("Mortal")
H  = Symbol("Cuernos")
Mg = Symbol("Mágico")

knowledge = And(
    Implication(Mi, I),
    Implication(Not(Mi), And(Ma, Mo)),
    Implication(Or(I, Ma), H),
    Implication(H, Mg)
)

simbolos = [Mi, I, Ma, Mo, H, Mg]

# --- 2. FUNCIONES DE LÓGICA ADAPTADAS PARA LA GUI ---

def obtener_tabla_verdad():
    """Genera la tabla de verdad y la devuelve como un string grande."""
    resultado = ""
    encabezados = [s.name[:4] + "." for s in simbolos] + ["KB"] # Nombres cortos
    header = " | ".join(f"{h:<6}" for h in encabezados)
    resultado += header + "\n"
    resultado += "-" * len(header) + "\n"

    combinaciones = list(itertools.product([True, False], repeat=len(simbolos)))
    modelos_validos = 0

    for valores in combinaciones:
        modelo = dict(zip([s.name for s in simbolos], valores))
        es_verdad = knowledge.evaluate(modelo)
        
        if es_verdad:
            modelos_validos += 1
            fila = [str(modelo[s.name]) for s in simbolos] + ["TRUE"]
            # Formateo para que se vea alineado
            fila_str = " | ".join(f"{str(val):<6}" for val in fila)
            resultado += fila_str + "\n"
    
    return resultado, modelos_validos

def resolver_inferencia():
    """Devuelve las respuestas a las 3 preguntas."""
    res_mitico = model_check(knowledge, Mi)
    res_magico = model_check(knowledge, Mg)
    res_cuernos = model_check(knowledge, H)
    
    return res_mitico, res_magico, res_cuernos

# --- 3. INTERFAZ GRÁFICA (Ventana) ---

def iniciar_app():
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Proyecto 3: El Misterio del Unicornio")
    ventana.geometry("700x550")
    ventana.configure(bg="#f0f0f0") # Color de fondo suave

    # Fuente personalizada
    estilo_fuente = font.Font(family="Helvetica", size=10)
    titulo_fuente = font.Font(family="Helvetica", size=14, weight="bold")

    # Título
    lbl_titulo = tk.Label(ventana, text="🦁🦄 Buscador de Verdad Lógica 🦄🦁", 
                          font=titulo_fuente, bg="#f0f0f0", fg="#333")
    lbl_titulo.pack(pady=10)

    # Frame para los botones
    frame_botones = tk.Frame(ventana, bg="#f0f0f0")
    frame_botones.pack(pady=5)

    # Función del Botón "Generar Tabla"
    def cmd_mostrar_tabla():
        texto_tabla, num_modelos = obtener_tabla_verdad()
        txt_output.delete(1.0, tk.END) # Limpiar pantalla
        txt_output.insert(tk.END, f"--- TABLA DE VERDAD (Solo filas válidas: {num_modelos}) ---\n\n")
        txt_output.insert(tk.END, texto_tabla)
    
    # Función del Botón "Resolver Preguntas"
    def cmd_resolver():
        mitico, magico, cuernos = resolver_inferencia()
        
        # Crear mensaje de resultado
        msj = "\n--- RESULTADOS DE LA INFERENCIA ---\n\n"
        msj += f"1. ¿Es Mítico?   -> {'SÍ' if mitico else 'NO SE PUEDE PROBAR'}\n"
        msj += f"2. ¿Es Mágico?   -> {'SÍ' if magico else 'NO'}\n"
        msj += f"3. ¿Tiene Cuernos? -> {'SÍ' if cuernos else 'NO'}\n\n"
        msj += "CONCLUSIÓN:\nEl sistema lógico ha demostrado que el animal\n"
        msj += "definitivamente tiene cuernos y es mágico."
        
        txt_output.delete(1.0, tk.END)
        txt_output.insert(tk.END, msj)

    # Botones
    btn_tabla = tk.Button(frame_botones, text="Generar Tabla de Verdad", 
                          command=cmd_mostrar_tabla, bg="#4a90e2", fg="white", 
                          font=estilo_fuente, padx=10, pady=5)
    btn_tabla.pack(side=tk.LEFT, padx=10)

    btn_resolver = tk.Button(frame_botones, text="Resolver Acertijo", 
                             command=cmd_resolver, bg="#27ae60", fg="white", 
                             font=estilo_fuente, padx=10, pady=5)
    btn_resolver.pack(side=tk.LEFT, padx=10)

    # Área de Texto (Pantalla de resultados)
    txt_output = scrolledtext.ScrolledText(ventana, width=80, height=20, 
                                           font=("Consolas", 10)) # Fuente monoespaciada para la tabla
    txt_output.pack(pady=20, padx=20)

    # Pie de página
    lbl_footer = tk.Label(ventana, text="Proyecto de IA - Lógica Proposicional", 
                          bg="#f0f0f0", fg="#777")
    lbl_footer.pack(side=tk.BOTTOM, pady=5)

    # Iniciar el bucle de la ventana
    ventana.mainloop()

if __name__ == "__main__":
    iniciar_app()