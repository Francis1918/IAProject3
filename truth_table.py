# truth_table.py - Generador de tablas de verdad
import itertools
from tabulate import tabulate


class TruthTable:
    """
    Clase para generar y mostrar tablas de verdad.
    """

    def __init__(self, knowledge_base, queries):
        self.knowledge_base = knowledge_base
        self.queries = queries
        self.symbols = sorted(list(knowledge_base.symbols()))
        self.table_data = []
        self.headers = []

    def generate(self):
        """Genera la tabla de verdad completa."""
        # Crear encabezados
        self.headers = self.symbols.copy()
        self.headers.append("KB")
        for query_data in self.queries:
            query_symbol = query_data.get('symbol', 'Q')
            self.headers.append(query_symbol)

        # Generar todas las combinaciones posibles
        n_symbols = len(self.symbols)

        for values in itertools.product([False, True], repeat=n_symbols):
            # Crear modelo
            model = dict(zip(self.symbols, values))

            # Evaluar base de conocimiento
            kb_value = self.knowledge_base.evaluate(model)

            # Crear fila
            row = [self._bool_to_int(v) for v in values]
            row.append(self._bool_to_int(kb_value))

            # Evaluar cada consulta
            for query_data in self.queries:
                query = query_data['query']
                query_value = query.evaluate(model)
                row.append(self._bool_to_int(query_value))

            self.table_data.append(row)

    def display(self):
        """Muestra la tabla de verdad formateada."""
        if not self.table_data:
            print("No hay datos en la tabla de verdad")
            return

        # Usar tabulate para una mejor visualizacion
        print(tabulate(self.table_data, headers=self.headers,
                       tablefmt="grid", stralign="center"))

        # Mostrar leyenda
        print("\nLeyenda:")
        print("   0 = Falso, 1 = Verdadero")
        print("   KB = Base de Conocimiento (todas las premisas)")
        for i, query_data in enumerate(self.queries):
            symbol = query_data.get('symbol', f'Q{i + 1}')
            question = query_data['question']
            print(f"   {symbol} = {question}")

    def _bool_to_int(self, value):
        """Convierte booleano a 0 o 1."""
        return 1 if value else 0

    def get_valid_models(self):
        """Retorna solo los modelos donde KB es verdadero."""
        valid_models = []
        for row in self.table_data:
            if row[len(self.symbols)] == 1:  # KB es verdadero
                valid_models.append(row)
        return valid_models