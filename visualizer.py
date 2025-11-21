# visualizer.py - Visualizacion de resultados
import matplotlib.pyplot as plt
import numpy as np


class Visualizer:
    """
    Clase para crear visualizaciones de los resultados.
    """

    def create_summary(self, puzzle_data, queries, solver):
        """Crea un resumen visual de los resultados."""
        print("\nRESUMEN DE RESULTADOS:")
        print("-" * 80)

        for query_data in queries:
            query = query_data['query']
            question = query_data['question']
            result = solver.check_entailment(query)

            if result == "YES":
                status = "[VERDADERO]"
            elif result == "NO":
                status = "[FALSO]"
            else:
                status = "[INDETERMINADO]"

            print(f"{question:<50} {status}")

        print("-" * 80)