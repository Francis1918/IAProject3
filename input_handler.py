# input_handler.py - Manejo de entrada de datos personalizada
from logic import *


class InputHandler:
    """
    Clase para manejar la entrada de datos personalizada del usuario.
    Implementa un modo interactivo paso a paso.
    """

    def __init__(self):
        self.symbols = {}
        self.premises = []
        self.queries = []

    def create_custom_puzzle(self):
        """
        Guía al usuario paso a paso para crear un rompecabezas personalizado.
        """
        print("\n" + "=" * 80)
        print("CREADOR DE ROMPECABEZAS LÓGICOS PERSONALIZADO")
        print("=" * 80)
        print("\nVamos a crear tu rompecabezas paso a paso.\n")

        # Obtener descripción
        description = self._get_description()

        # Definir símbolos
        self._define_symbols()

        # Crear premisas
        self._create_premises()

        # Crear preguntas
        self._create_queries()

        # Construir el diccionario del rompecabezas
        puzzle_data = {
            'description': description,
            'symbols': {name: desc for name, desc in self.symbols.items()},
            'premises': self.premises,
            'queries': self.queries
        }

        return puzzle_data

    def _get_description(self):
        """Obtiene la descripción del problema."""
        print("PASO 1: DESCRIPCIÓN DEL PROBLEMA")
        print("-" * 40)
        print("Escribe una breve descripción del problema lógico que deseas resolver.")
        print("Ejemplo: 'Determinar las características de un animal mítico'\n")
        description = input("Descripción: ").strip()

        if not description:
            description = "Rompecabezas lógico personalizado"

        return description

    def _define_symbols(self):
        """Define los símbolos proposicionales."""
        print("\n" + "=" * 80)
        print("PASO 2: DEFINIR SÍMBOLOS PROPOSICIONALES")
        print("-" * 40)
        print("Los símbolos representan proposiciones que pueden ser verdaderas o falsas.")
        print("Ejemplo: 'vuela' = 'El animal puede volar'\n")

        while True:
            print(f"\nSímbolos definidos hasta ahora: {len(self.symbols)}")
            if self.symbols:
                for name, desc in self.symbols.items():
                    print(f"  - {name}: {desc}")

            print("\n¿Deseas agregar un símbolo? (s/n): ", end="")
            respuesta = input().strip().lower()

            if respuesta != 's':
                if len(self.symbols) < 2:
                    print("⚠ Necesitas al menos 2 símbolos para crear un rompecabezas.")
                    continue
                break

            nombre = input("Nombre del símbolo (una palabra, sin espacios): ").strip().lower()

            if not nombre or not nombre.isalnum():
                print("⚠ El nombre debe ser alfanumérico y sin espacios.")
                continue

            if nombre in self.symbols:
                print("⚠ Este símbolo ya existe.")
                continue

            descripcion = input(f"Descripción de '{nombre}': ").strip()

            if not descripcion:
                descripcion = f"Proposición {nombre}"

            self.symbols[nombre] = descripcion

    def _create_premises(self):
        """Crea las premisas del rompecabezas."""
        print("\n" + "=" * 80)
        print("PASO 3: CREAR PREMISAS (REGLAS LÓGICAS)")
        print("-" * 40)
        print("Las premisas son las reglas que conocemos sobre el problema.")
        print("\nTipos de premisas disponibles:")
        print("  1. Implicación: Si A entonces B  (A => B)")
        print("  2. Conjunción: A y B  (A ∧ B)")
        print("  3. Disyunción: A o B  (A ∨ B)")
        print("  4. Negación: No A  (¬A)")
        print("  5. Bicondicional: A si y solo si B  (A <=> B)")

        while True:
            print(f"\nPremisas creadas: {len(self.premises)}")
            if self.premises:
                for i, p in enumerate(self.premises, 1):
                    print(f"  {i}. {p['description']}")

            print("\n¿Deseas agregar una premisa? (s/n): ", end="")
            respuesta = input().strip().lower()

            if respuesta != 's':
                if len(self.premises) < 1:
                    print("⚠ Necesitas al menos 1 premisa.")
                    continue
                break

            premise = self._create_single_premise()
            if premise:
                self.premises.append(premise)

    def _create_single_premise(self):
        """Crea una sola premisa de forma interactiva."""
        print("\n--- Nueva Premisa ---")
        print("Símbolos disponibles:", ", ".join(self.symbols.keys()))
        print("\nSelecciona el tipo de premisa:")
        print("  1. Implicación (Si... entonces...)")
        print("  2. Conjunción (Y)")
        print("  3. Disyunción (O)")
        print("  4. Negación (No)")
        print("  5. Bicondicional (Si y solo si)")

        tipo = input("\nElige una opción (1-5): ").strip()

        try:
            if tipo == '1':
                return self._create_implication()
            elif tipo == '2':
                return self._create_conjunction()
            elif tipo == '3':
                return self._create_disjunction()
            elif tipo == '4':
                return self._create_negation()
            elif tipo == '5':
                return self._create_biconditional()
            else:
                print("⚠ Opción no válida.")
                return None
        except Exception as e:
            print(f"⚠ Error al crear la premisa: {e}")
            return None

    def _get_symbol_or_expression(self, prompt=""):
        """Obtiene un símbolo o permite negarlo."""
        print(prompt)
        nombre = input("Nombre del símbolo: ").strip().lower()

        if nombre not in self.symbols:
            print(f"⚠ El símbolo '{nombre}' no existe.")
            return None

        negar = input(f"¿Negar '{nombre}'? (s/n): ").strip().lower()

        symbol = Symbol(nombre)
        return Not(symbol) if negar == 's' else symbol

    def _create_implication(self):
        """Crea una implicación."""
        print("\nImplicación: Si A entonces B")
        antecedente = self._get_symbol_or_expression("Antecedente (el 'Si'):")
        if not antecedente:
            return None

        consecuente = self._get_symbol_or_expression("Consecuente (el 'entonces'):")
        if not consecuente:
            return None

        descripcion = input("Descripción en lenguaje natural: ").strip()
        if not descripcion:
            descripcion = f"Si {antecedente} entonces {consecuente}"

        return {
            'sentence': Implication(antecedente, consecuente),
            'description': descripcion
        }

    def _create_conjunction(self):
        """Crea una conjunción."""
        print("\nConjunción: A y B")
        conjuncts = []

        while True:
            expr = self._get_symbol_or_expression(f"Elemento {len(conjuncts) + 1}:")
            if expr:
                conjuncts.append(expr)

            if len(conjuncts) >= 2:
                continuar = input("¿Agregar otro elemento? (s/n): ").strip().lower()
                if continuar != 's':
                    break

        descripcion = input("Descripción en lenguaje natural: ").strip()
        if not descripcion:
            descripcion = " y ".join([str(c) for c in conjuncts])

        return {
            'sentence': And(*conjuncts),
            'description': descripcion
        }

    def _create_disjunction(self):
        """Crea una disyunción."""
        print("\nDisyunción: A o B")
        disjuncts = []

        while True:
            expr = self._get_symbol_or_expression(f"Elemento {len(disjuncts) + 1}:")
            if expr:
                disjuncts.append(expr)

            if len(disjuncts) >= 2:
                continuar = input("¿Agregar otro elemento? (s/n): ").strip().lower()
                if continuar != 's':
                    break

        descripcion = input("Descripción en lenguaje natural: ").strip()
        if not descripcion:
            descripcion = " o ".join([str(d) for d in disjuncts])

        return {
            'sentence': Or(*disjuncts),
            'description': descripcion
        }

    def _create_negation(self):
        """Crea una negación."""
        print("\nNegación: No A")
        nombre = input("Símbolo a negar: ").strip().lower()

        if nombre not in self.symbols:
            print(f"⚠ El símbolo '{nombre}' no existe.")
            return None

        descripcion = input("Descripción en lenguaje natural: ").strip()
        if not descripcion:
            descripcion = f"No {nombre}"

        return {
            'sentence': Not(Symbol(nombre)),
            'description': descripcion
        }

    def _create_biconditional(self):
        """Crea un bicondicional."""
        print("\nBicondicional: A si y solo si B")
        izquierda = self._get_symbol_or_expression("Lado izquierdo:")
        if not izquierda:
            return None

        derecha = self._get_symbol_or_expression("Lado derecho:")
        if not derecha:
            return None

        descripcion = input("Descripción en lenguaje natural: ").strip()
        if not descripcion:
            descripcion = f"{izquierda} si y solo si {derecha}"

        return {
            'sentence': Biconditional(izquierda, derecha),
            'description': descripcion
        }

    def _create_queries(self):
        """Crea las preguntas a resolver."""
        print("\n" + "=" * 80)
        print("PASO 4: DEFINIR PREGUNTAS")
        print("-" * 40)
        print("¿Qué quieres averiguar con este rompecabezas?")

        while True:
            print(f"\nPreguntas creadas: {len(self.queries)}")
            if self.queries:
                for i, q in enumerate(self.queries, 1):
                    print(f"  {i}. {q['question']}")

            print("\n¿Deseas agregar una pregunta? (s/n): ", end="")
            respuesta = input().strip().lower()

            if respuesta != 's':
                if len(self.queries) < 1:
                    print("⚠ Necesitas al menos 1 pregunta.")
                    continue
                break

            print("\nSímbolos disponibles:", ", ".join(self.symbols.keys()))
            nombre = input("¿Sobre qué símbolo es la pregunta?: ").strip().lower()

            if nombre not in self.symbols:
                print(f"⚠ El símbolo '{nombre}' no existe.")
                continue

            pregunta = input(f"Formula la pregunta sobre '{nombre}': ").strip()
            if not pregunta:
                pregunta = f"¿Es verdadero {nombre}?"

            self.queries.append({
                'query': Symbol(nombre),
                'question': pregunta,
                'symbol': nombre.capitalize() + '?'
            })

        print("\n✓ Rompecabezas personalizado creado exitosamente!")
        return True

