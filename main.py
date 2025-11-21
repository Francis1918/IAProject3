from logic_solver import LogicPuzzleSolver
from examples import get_unicorn_example
from input_handler import InputHandler


def show_menu():
    """Muestra el menú principal."""
    print("\n" + "=" * 80)
    print("MENÚ PRINCIPAL")
    print("=" * 80)
    print("\n1. Resolver ejemplo del unicornio (predefinido)")
    print("2. Crear y resolver rompecabezas personalizado")
    print("3. Salir")
    print("\nSelecciona una opción: ", end="")


def main():
    print("=" * 80)
    print("SOLUCIONADOR DE ROMPECABEZAS LÓGICOS")
    print("Usando Lógica Proposicional y Tablas de Verdad")
    print("Con visualizaciones avanzadas (Matplotlib, Pandas, NumPy, SymPy)")
    print("=" * 80)

    # Crear el solucionador
    solver = LogicPuzzleSolver()

    while True:
        show_menu()
        opcion = input().strip()

        if opcion == '1':
            # Ejemplo del unicornio
            print("\n" + "=" * 80)
            print("EJEMPLO: EL UNICORNIO MÍTICO")
            print("=" * 80)
            unicorn_puzzle = get_unicorn_example()
            solver.solve_puzzle(unicorn_puzzle)

        elif opcion == '2':
            # Rompecabezas personalizado
            handler = InputHandler()
            custom_puzzle = handler.create_custom_puzzle()

            if custom_puzzle:
                print("\n" + "=" * 80)
                print("RESOLVIENDO TU ROMPECABEZAS PERSONALIZADO")
                print("=" * 80)
                solver.solve_puzzle(custom_puzzle)

        elif opcion == '3':
            print("\n¡Hasta luego! Gracias por usar el solucionador de rompecabezas lógicos.")
            break

        else:
            print("\n⚠ Opción no válida. Por favor, selecciona 1, 2 o 3.")


if __name__ == "__main__":
    main()