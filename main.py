# main.py - Archivo principal
from logic_solver import LogicPuzzleSolver
from examples import get_unicorn_example, get_custom_example

def main():
    print("=" * 80)
    print("SOLUCIONADOR DE ROMPECABEZAS LOGICOS")
    print("Usando Logica Proposicional y Tablas de Verdad")
    print("=" * 80)
    print()

    # Crear el solucionador
    solver = LogicPuzzleSolver()

    # Ejemplo del unicornio
    print("\n" + "=" * 80)
    print("EJEMPLO 1: EL UNICORNIO")
    print("=" * 80)

    unicorn_puzzle = get_unicorn_example()
    solver.solve_puzzle(unicorn_puzzle)

    # Puedes agregar mas ejemplos aqui
    print("\n" + "=" * 80)
    print("Deseas resolver otro rompecabezas? (s/n)")
    respuesta = input().lower()

    if respuesta == 's':
        print("\nFuncionalidad para agregar rompecabezas personalizados...")

if __name__ == "__main__":
    main()