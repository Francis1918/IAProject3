from Python.logic import *
import itertools

# 1. Definición de Símbolos (Átomos)
Mi = Symbol("Mítico")
I  = Symbol("Inmortal")
Ma = Symbol("Mamífero")
Mo = Symbol("Mortal")
H  = Symbol("Cuernos")
Mg = Symbol("Mágico")

# 2. Construcción de la Base de Conocimiento (KB)
# Traducimos las oraciones del documento a código

knowledge = And(
    # Premisa 1: Si es mítico, es inmortal; si no es mítico, es mamífero y mortal.
    # "Si el unicornio es mítico, entonces es inmortal..."
    Implication(Mi, I),
    # "...pero si no es mítico, entonces es un mamífero mortal."
    Implication(Not(Mi), And(Ma, Mo)),

    # Premisa 2: Si es inmortal o mamífero, tiene cuernos.
    Implication(Or(I, Ma), H),

    # Premisa 3: Si tiene cuernos, es mágico.
    # (Corrigiendo el error "is" del documento por "si")
    Implication(H, Mg)
)

# 3. Función para Generar e Imprimir la Tabla de Verdad
def imprimir_tabla_verdad(kb, simbolos):
    # Encabezado de la tabla
    encabezados = [s.name for s in simbolos] + ["KB (Es válida?)"]
    print(f"{' | '.join(encabezados)}")
    print("-" * (len(encabezados) * 12))

    # Generar todas las combinaciones posibles de verdad (True/False)
    # Si son 6 símbolos, habrá 2^6 = 64 filas
    combinaciones = list(itertools.product([True, False], repeat=len(simbolos)))
    
    modelos_validos = 0

    for valores in combinaciones:
        # Crear un modelo (diccionario) para esta fila: {Mítico: True, Inmortal: False...}
        modelo = dict(zip([s.name for s in simbolos], valores))
        
        # Evaluar si la Base de Conocimiento es verdadera en este modelo
        es_verdad = kb.evaluate(modelo)
        
        # Opcional: Para no imprimir una tabla gigante de 64 filas, 
        # podemos imprimir solo las filas donde la KB es Verdadera (el "Mundo posible")
        # Si quieres ver TODA la tabla, quita el 'if es_verdad:'
        if es_verdad: 
            modelos_validos += 1
            fila = [str(modelo[s.name]) for s in simbolos] + [str(es_verdad)]
            print(f"{' | '.join(f'{val:<5}' for val in fila)}")

    print(f"\nNro de modelos donde la KB se cumple: {modelos_validos}")

# 4. Resolución del Problema (Inferencia)
def resolver_preguntas():
    print("\n--- RESULTADOS DE INFERENCIA ---")
    
    # Pregunta 1: ¿Es mítico?
    es_mitico = model_check(knowledge, Mi)
    print(f"¿Se puede probar que es Mítico? {es_mitico}")

    # Pregunta 2: ¿Es mágico?
    es_magico = model_check(knowledge, Mg)
    print(f"¿Se puede probar que es Mágico? {es_magico}")

    # Pregunta 3: ¿Tiene cuernos?
    tiene_cuernos = model_check(knowledge, H)
    print(f"¿Se puede probar que tiene Cuernos? {tiene_cuernos}")

# --- EJECUCIÓN PRINCIPAL ---
if __name__ == "__main__":
    # Lista de símbolos para la tabla
    lista_simbolos = [Mi, I, Ma, Mo, H, Mg]
    
    print("--- TABLA DE VERDAD (Solo filas válidas/consistentes) ---")
    imprimir_tabla_verdad(knowledge, lista_simbolos)
    
    resolver_preguntas()