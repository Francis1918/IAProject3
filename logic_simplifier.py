# logic_simplifier.py - Simplificación de expresiones lógicas con SymPy
from sympy import symbols, simplify_logic, Or as SymOr, And as SymAnd, Not as SymNot, Implies
from sympy.logic.boolalg import to_cnf, to_dnf
from logic import *


class LogicSimplifier:
    """
    Clase para simplificar expresiones lógicas usando SymPy.
    """

    def __init__(self):
        self.sympy_symbols = {}

    def convert_to_sympy(self, sentence):
        """
        Convierte una sentencia de nuestra lógica a SymPy.

        Args:
            sentence: Objeto Sentence de nuestro sistema

        Returns:
            Expresión de SymPy
        """
        if isinstance(sentence, Symbol):
            if sentence.name not in self.sympy_symbols:
                self.sympy_symbols[sentence.name] = symbols(sentence.name)
            return self.sympy_symbols[sentence.name]

        elif isinstance(sentence, Not):
            return SymNot(self.convert_to_sympy(sentence.operand))

        elif isinstance(sentence, And):
            return SymAnd(*[self.convert_to_sympy(c) for c in sentence.conjuncts])

        elif isinstance(sentence, Or):
            return SymOr(*[self.convert_to_sympy(d) for d in sentence.disjuncts])

        elif isinstance(sentence, Implication):
            return Implies(
                self.convert_to_sympy(sentence.antecedent),
                self.convert_to_sympy(sentence.consequent)
            )

        elif isinstance(sentence, Biconditional):
            # A <=> B es equivalente a (A => B) ∧ (B => A)
            left = self.convert_to_sympy(sentence.left)
            right = self.convert_to_sympy(sentence.right)
            return SymAnd(Implies(left, right), Implies(right, left))

        else:
            raise ValueError(f"Tipo de sentencia no soportado: {type(sentence)}")

    def simplify(self, sentence):
        """
        Simplifica una expresión lógica.

        Args:
            sentence: Sentencia lógica a simplificar

        Returns:
            Expresión simplificada (como string)
        """
        sympy_expr = self.convert_to_sympy(sentence)
        simplified = simplify_logic(sympy_expr)
        return str(simplified)

    def to_cnf(self, sentence):
        """
        Convierte una sentencia a Forma Normal Conjuntiva (CNF).

        Args:
            sentence: Sentencia lógica

        Returns:
            String con la expresión en CNF
        """
        sympy_expr = self.convert_to_sympy(sentence)
        cnf_form = to_cnf(sympy_expr)
        return str(cnf_form)

    def to_dnf(self, sentence):
        """
        Convierte una sentencia a Forma Normal Disyuntiva (DNF).

        Args:
            sentence: Sentencia lógica

        Returns:
            String con la expresión en DNF
        """
        sympy_expr = self.convert_to_sympy(sentence)
        dnf_form = to_dnf(sympy_expr)
        return str(dnf_form)

    def get_analysis(self, sentence):
        """
        Obtiene un análisis completo de una expresión lógica.

        Args:
            sentence: Sentencia lógica

        Returns:
            Diccionario con diferentes formas de la expresión
        """
        original = sentence.formula()
        simplified = self.simplify(sentence)
        cnf = self.to_cnf(sentence)
        dnf = self.to_dnf(sentence)

        return {
            'original': original,
            'simplified': simplified,
            'cnf': cnf,
            'dnf': dnf
        }

    def display_analysis(self, sentence, title="Análisis de Expresión Lógica"):
        """
        Muestra un análisis completo de una expresión lógica.

        Args:
            sentence: Sentencia lógica a analizar
            title: Título del análisis
        """
        print("\n" + "=" * 80)
        print(title)
        print("=" * 80)

        analysis = self.get_analysis(sentence)

        print(f"\n{'Original:':<20} {analysis['original']}")
        print(f"{'Simplificada:':<20} {analysis['simplified']}")
        print(f"{'Forma CNF:':<20} {analysis['cnf']}")
        print(f"{'Forma DNF:':<20} {analysis['dnf']}")
        print("=" * 80)

    def simplify_knowledge_base(self, premises):
        """
        Simplifica toda la base de conocimiento.

        Args:
            premises: Lista de premisas

        Returns:
            Lista de premisas simplificadas
        """
        simplified_premises = []

        for premise in premises:
            sentence = premise['sentence']
            analysis = self.get_analysis(sentence)

            simplified_premises.append({
                'original': premise,
                'simplified': analysis['simplified'],
                'cnf': analysis['cnf'],
                'dnf': analysis['dnf']
            })

        return simplified_premises

