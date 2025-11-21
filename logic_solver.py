from logic import *
from truth_table import TruthTable
from visualizer import Visualizer
from matplotlib_visualizer import MatplotlibVisualizer
from logic_simplifier import LogicSimplifier


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
        self.matplotlib_viz = MatplotlibVisualizer()
        self.simplifier = LogicSimplifier()

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

        # Mostrar simplificación de la base de conocimiento
        print("\n" + "=" * 80)
        print("ANÁLISIS Y SIMPLIFICACIÓN (usando SymPy)")
        print("=" * 80)
        self.simplifier.display_analysis(self.knowledge_base,
                                         "Base de Conocimiento Completa")

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

        # Mostrar estadísticas de la tabla
        truth_table.display_statistics()

        # Visualizaciones con matplotlib
        print("\n" + "=" * 80)
        print("VISUALIZACIONES AVANZADAS")
        print("=" * 80)
        print("\nGenerando visualizaciones con Matplotlib...")

        # 1. Tabla de verdad colorida
        df = truth_table.get_dataframe()
        if df is not None:
            self.matplotlib_viz.visualize_truth_table(df, "Tabla de Verdad - Visualización")

        # 2. Distribución de resultados
        queries_results = []
        for query_data in self.queries:
            query = query_data['query']
            question = query_data['question']
            result = self.check_entailment(query)
            queries_results.append((question, result))

        self.matplotlib_viz.visualize_results_distribution(
            queries_results, "Resultados de las Consultas"
        )

        # 3. Modelos válidos
        total_models = len(truth_table.table_data)
        valid_models = len(truth_table.get_valid_models())
        self.matplotlib_viz.visualize_valid_models_count(
            total_models, valid_models, "Proporción de Modelos Válidos"
        )

        # 4. Frecuencia de símbolos
        symbol_stats = truth_table.get_symbol_statistics()
        if symbol_stats:
            self.matplotlib_viz.visualize_symbol_frequency(
                symbol_stats, "Frecuencia de Símbolos en Modelos Válidos"
            )

        # Preguntar si desea guardar las visualizaciones
        if self.matplotlib_viz.ask_to_save():
            self.matplotlib_viz.save_all_figures()
            print("\n✓ Visualizaciones guardadas exitosamente.")

        # Limpiar figuras para el próximo uso
        self.matplotlib_viz.clear_figures()

        # Opción para exportar a CSV
        print("\n¿Deseas exportar la tabla de verdad a CSV? (s/n): ", end="")
        if input().strip().lower() == 's':
            truth_table.export_to_csv()

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