# matplotlib_visualizer.py - Visualizaciones avanzadas con matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os
from datetime import datetime


class MatplotlibVisualizer:
    """
    Clase para crear visualizaciones avanzadas usando matplotlib.
    """

    def __init__(self):
        self.save_dir = "resultados_de_visualizaciones"
        self.figures = []

    def ask_to_save(self):
        """Pregunta al usuario si desea guardar las visualizaciones."""
        print("\n¿Deseas guardar las visualizaciones? (s/n): ", end="")
        respuesta = input().strip().lower()
        return respuesta == 's'

    def save_all_figures(self):
        """Guarda todas las figuras generadas."""
        if not self.figures:
            print("No hay visualizaciones para guardar.")
            return

        # Crear el directorio si no existe
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)
            print(f"\n✓ Carpeta '{self.save_dir}' creada.")

        # Generar timestamp para nombres únicos
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        saved_files = []
        for i, (fig, name) in enumerate(self.figures):
            filename = f"{name}_{timestamp}.png"
            filepath = os.path.join(self.save_dir, filename)
            fig.savefig(filepath, dpi=300, bbox_inches='tight')
            saved_files.append(filepath)

        print(f"\n✓ {len(saved_files)} visualización(es) guardada(s) en '{self.save_dir}/':")
        for filepath in saved_files:
            print(f"  - {os.path.basename(filepath)}")

    def visualize_truth_table(self, truth_table_df, title="Tabla de Verdad"):
        """
        Crea una visualización de la tabla de verdad usando colores.

        Args:
            truth_table_df: DataFrame de pandas con la tabla de verdad
            title: Título de la visualización
        """
        fig, ax = plt.subplots(figsize=(12, max(6, len(truth_table_df) * 0.3)))
        ax.axis('tight')
        ax.axis('off')

        # Crear colores para las celdas
        colors = []
        for idx, row in truth_table_df.iterrows():
            row_colors = []
            for val in row:
                if val == 1:
                    row_colors.append('#90EE90')  # Verde claro para True
                elif val == 0:
                    row_colors.append('#FFB6C6')  # Rosa claro para False
                else:
                    row_colors.append('#FFFFFF')  # Blanco para otros
            colors.append(row_colors)

        # Crear la tabla
        table = ax.table(cellText=truth_table_df.values,
                        colLabels=truth_table_df.columns,
                        cellColours=colors,
                        cellLoc='center',
                        loc='center',
                        bbox=[0, 0, 1, 1])

        table.auto_set_font_size(False)
        table.set_fontsize(9)
        table.scale(1, 2)

        # Estilizar encabezados
        for i in range(len(truth_table_df.columns)):
            table[(0, i)].set_facecolor('#4472C4')
            table[(0, i)].set_text_props(weight='bold', color='white')

        plt.title(title, fontsize=14, weight='bold', pad=20)

        # Agregar leyenda
        legend_elements = [
            mpatches.Patch(facecolor='#90EE90', label='Verdadero (1)'),
            mpatches.Patch(facecolor='#FFB6C6', label='Falso (0)')
        ]
        ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.15, 1))

        self.figures.append((fig, "tabla_verdad"))
        plt.tight_layout()
        plt.show()

    def visualize_results_distribution(self, queries_results, title="Distribución de Resultados"):
        """
        Crea un gráfico de barras mostrando los resultados de las consultas.

        Args:
            queries_results: Lista de tuplas (pregunta, resultado)
            title: Título del gráfico
        """
        if not queries_results:
            return

        fig, ax = plt.subplots(figsize=(10, 6))

        questions = [q[0] for q in queries_results]
        results = [q[1] for q in queries_results]

        # Colores según el resultado
        colors = []
        for result in results:
            if result == "YES":
                colors.append('#4CAF50')  # Verde
            elif result == "NO":
                colors.append('#F44336')  # Rojo
            else:
                colors.append('#FFC107')  # Amarillo

        y_pos = np.arange(len(questions))

        bars = ax.barh(y_pos, [1] * len(questions), color=colors, alpha=0.7)
        ax.set_yticks(y_pos)
        ax.set_yticklabels(questions, fontsize=9)
        ax.set_xlim(0, 1.5)
        ax.set_xticks([])
        ax.set_xlabel('')
        ax.set_title(title, fontsize=14, weight='bold', pad=20)

        # Agregar etiquetas en las barras
        for i, (bar, result) in enumerate(zip(bars, results)):
            if result == "YES":
                text = "✓ VERDADERO"
            elif result == "NO":
                text = "✗ FALSO"
            else:
                text = "? INDETERMINADO"

            ax.text(0.5, bar.get_y() + bar.get_height()/2, text,
                   ha='center', va='center', fontsize=10, weight='bold',
                   color='white')

        # Leyenda
        legend_elements = [
            mpatches.Patch(facecolor='#4CAF50', label='Verdadero'),
            mpatches.Patch(facecolor='#F44336', label='Falso'),
            mpatches.Patch(facecolor='#FFC107', label='Indeterminado')
        ]
        ax.legend(handles=legend_elements, loc='lower right')

        plt.tight_layout()
        self.figures.append((fig, "distribucion_resultados"))
        plt.show()

    def visualize_valid_models_count(self, total_models, valid_models, title="Modelos Válidos"):
        """
        Crea un gráfico de pastel mostrando la proporción de modelos válidos.

        Args:
            total_models: Total de modelos posibles
            valid_models: Número de modelos válidos
            title: Título del gráfico
        """
        fig, ax = plt.subplots(figsize=(8, 6))

        invalid_models = total_models - valid_models
        sizes = [valid_models, invalid_models]
        labels = [f'Válidos\n({valid_models})', f'Inválidos\n({invalid_models})']
        colors = ['#4CAF50', '#F44336']
        explode = (0.1, 0)

        ax.pie(sizes, explode=explode, labels=labels, colors=colors,
               autopct='%1.1f%%', shadow=True, startangle=90,
               textprops={'fontsize': 12, 'weight': 'bold'})

        ax.set_title(title, fontsize=14, weight='bold', pad=20)

        # Agregar información adicional
        info_text = f"Total de modelos posibles: {total_models}\n"
        info_text += f"Modelos que satisfacen KB: {valid_models}\n"
        info_text += f"Porcentaje de validez: {(valid_models/total_models)*100:.1f}%"

        plt.figtext(0.5, 0.02, info_text, ha='center', fontsize=9,
                   bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

        plt.tight_layout()
        self.figures.append((fig, "modelos_validos"))
        plt.show()

    def visualize_symbol_frequency(self, symbol_values, title="Frecuencia de Símbolos en Modelos Válidos"):
        """
        Visualiza la frecuencia de cada símbolo siendo verdadero en modelos válidos.

        Args:
            symbol_values: Diccionario {símbolo: [True/False counts]}
            title: Título del gráfico
        """
        if not symbol_values:
            return

        fig, ax = plt.subplots(figsize=(10, 6))

        symbols = list(symbol_values.keys())
        true_counts = [symbol_values[s]['true'] for s in symbols]
        false_counts = [symbol_values[s]['false'] for s in symbols]

        x = np.arange(len(symbols))
        width = 0.35

        bars1 = ax.bar(x - width/2, true_counts, width, label='Verdadero',
                      color='#4CAF50', alpha=0.8)
        bars2 = ax.bar(x + width/2, false_counts, width, label='Falso',
                      color='#F44336', alpha=0.8)

        ax.set_xlabel('Símbolos', fontsize=12, weight='bold')
        ax.set_ylabel('Frecuencia en modelos válidos', fontsize=12, weight='bold')
        ax.set_title(title, fontsize=14, weight='bold', pad=20)
        ax.set_xticks(x)
        ax.set_xticklabels(symbols, rotation=45, ha='right')
        ax.legend()
        ax.grid(axis='y', alpha=0.3)

        # Agregar valores en las barras
        def autolabel(bars):
            for bar in bars:
                height = bar.get_height()
                if height > 0:
                    ax.annotate(f'{int(height)}',
                              xy=(bar.get_x() + bar.get_width() / 2, height),
                              xytext=(0, 3),
                              textcoords="offset points",
                              ha='center', va='bottom',
                              fontsize=9)

        autolabel(bars1)
        autolabel(bars2)

        plt.tight_layout()
        self.figures.append((fig, "frecuencia_simbolos"))
        plt.show()

    def clear_figures(self):
        """Limpia la lista de figuras."""
        for fig, _ in self.figures:
            plt.close(fig)
        self.figures = []

