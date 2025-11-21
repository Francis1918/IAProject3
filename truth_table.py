# truth_table.py - Generador de tablas de verdad
import itertools
from tabulate import tabulate
import pandas as pd


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
        self.df = None  # DataFrame de pandas

    def generate(self):
        """Genera la tabla de verdad completa."""
        # Crear encabezados
        self.headers = self.symbols.copy()
        self.headers.append("KB")
        for query_data in self.queries:
            query_symbol = query_data.get('symbol', 'Q')
            self.headers.append(query_symbol)

        # Generar todas las combinaciones posibles usando numpy para eficiencia
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

        # Crear DataFrame de pandas
        self.df = pd.DataFrame(self.table_data, columns=self.headers)

        # Convertir a tipo int para mejor visualización
        self.df = self.df.astype(int)

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

    def get_dataframe(self):
        """Retorna el DataFrame de pandas con la tabla de verdad."""
        return self.df

    def get_valid_models_df(self):
        """Retorna un DataFrame con solo los modelos válidos."""
        if self.df is None:
            return None
        kb_column = 'KB'
        return self.df[self.df[kb_column] == 1]

    def export_to_csv(self, filename="tabla_verdad.csv"):
        """Exporta la tabla de verdad a un archivo CSV."""
        if self.df is not None:
            import os
            from datetime import datetime

            # Crear el directorio si no existe
            save_dir = "tablas_de_verdad"
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)
                print(f"\n✓ Carpeta '{save_dir}' creada.")

            # Agregar timestamp al nombre del archivo
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            base_name = filename.replace(".csv", "")
            filename_with_timestamp = f"{base_name}_{timestamp}.csv"
            filepath = os.path.join(save_dir, filename_with_timestamp)

            # Guardar el archivo
            self.df.to_csv(filepath, index=False)
            print(f"\n✓ Tabla exportada a: {filepath}")
        else:
            print("⚠ No hay tabla de verdad generada.")

    def get_symbol_statistics(self):
        """
        Calcula estadísticas sobre los símbolos en modelos válidos.

        Returns:
            Diccionario con frecuencias de cada símbolo
        """
        if self.df is None:
            return {}

        valid_df = self.get_valid_models_df()
        if valid_df.empty:
            return {}

        stats = {}
        for symbol in self.symbols:
            stats[symbol] = {
                'true': int(valid_df[symbol].sum()),
                'false': int(len(valid_df) - valid_df[symbol].sum()),
                'total': len(valid_df)
            }

        return stats

    def display_statistics(self):
        """Muestra estadísticas sobre la tabla de verdad."""
        if self.df is None:
            print("No hay tabla de verdad generada.")
            return

        print("\n" + "=" * 80)
        print("ESTADÍSTICAS DE LA TABLA DE VERDAD")
        print("=" * 80)

        total_models = len(self.df)
        valid_models = len(self.get_valid_models_df())

        print(f"\nTotal de modelos posibles: {total_models}")
        print(f"Modelos que satisfacen KB: {valid_models}")
        print(f"Porcentaje de validez: {(valid_models/total_models)*100:.2f}%")

        # Estadísticas por símbolo
        stats = self.get_symbol_statistics()
        if stats:
            print("\nFrecuencia de símbolos en modelos válidos:")
            for symbol, data in stats.items():
                print(f"  {symbol}:")
                print(f"    Verdadero: {data['true']} ({data['true']/data['total']*100:.1f}%)")
                print(f"    Falso: {data['false']} ({data['false']/data['total']*100:.1f}%)")

        print("=" * 80)
