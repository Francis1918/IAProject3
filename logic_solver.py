# logic_solver.py - Motor principal del solucionador
from logic import *
import itertools
from truth_table import TruthTable
from visualizer import Visualizer


class LogicPuzzleSolver:
    """
    Clase principal para resolver rompecabezas logicos usando
    logica proposicional y tablas de verdad.
    """

    def __init__(self):
        self.knowledge_base = None
        self.symbols_dict = {}
        self.premises = []
        self.queries = []

    def solve_puzzle(self, puzzle_data):
        """
        Resuelve un rompecabezas logico completo.

        Args:
            puzzle_data: Diccionario con la estructura del rompecabezas
        """
        print(f"\nDESCRIPCION DEL PROBLEMA:")
        print(f"{puzzle_data['description']}\n")

        # Mostrar simbolos
        print("SIMBOLOS PROPOSICIONALES:")
        self.symbols_dict = puzzle_data['symbols']
        for symbol, meaning in self.symbols_dict.items():
            print(f"   {symbol}: {meaning}")

        # Construir la base de conocimiento
        print("\nPREMISAS (Base de Conocimiento):")
        self.premises = puzzle_data['premises']
        knowledge_sentences = []

        for i, premise in enumerate(self.premises, 1):
            sentence = premise['sentence']
            description = premise['description']
            knowledge_sentences.append(sentence)
            print(f"   {i}. {description}")
            print(f"      Formula: {sentence.formula()}")

        # Combinar todas las premisas en una base de conocimiento
        self.knowledge_base = And(*knowledge_sentences)

        # Mostrar preguntas
        print("\nPREGUNTAS A RESOLVER:")
        self.queries = puzzle_data['queries']
        for i, query in enumerate(self.queries, 1):
            print(f"   {i}. {query['question']}")

        # Generar y mostrar tabla de verdad
        print("\n" + "=" * 80)
        print("TABLA DE VERDAD")
        print("=" * 80)

        truth_table = TruthTable(self.knowledge_base, self.queries)
        truth_table.generate()
        truth_table.display()

        # Resolver cada pregunta
        print("\n" + "=" * 80)
        print("RESPUESTAS")
        print("=" * 80)

        for i, query_data in enumerate(self.queries, 1):
            query = query_data['query']
            question = query_data['question']

            print(f"\n{i}. {question}")
            print(f"   Formula: {query.formula()}")

            # Verificar si la base de conocimiento implica la consulta
            result = self.check_entailment(query)

            if result == "YES":
                print(f"   RESPUESTA: SI")
                print(f"   La base de conocimiento implica que {query.formula()} es VERDADERO")
            elif result == "NO":
                print(f"   RESPUESTA: NO")
                print(f"   La base de conocimiento implica que {query.formula()} es FALSO")
            else:
                print(f"   RESPUESTA: NO SE PUEDE DETERMINAR")
                print(f"   La base de conocimiento no proporciona informacion suficiente")

        # Visualizacion opcional
        print("\n" + "=" * 80)
        visualizer = Visualizer()
        visualizer.create_summary(puzzle_data, self.queries, self)

    def check_entailment(self, query):
        """
        Verifica si la base de conocimiento implica la consulta.

        Returns:
            "YES" si KB implica query
            "NO" si KB implica NOT query
            "UNKNOWN" si no se puede determinar
        """
        # Obtener todos los simbolos
        symbols = list(self.knowledge_base.symbols().union(query.symbols()))

        # Verificar si KB implica query
        if model_check(self.knowledge_base, query):
            return "YES"

        # Verificar si KB implica NOT query
        if model_check(self.knowledge_base, Not(query)):
            return "NO"

        return "UNKNOWN"