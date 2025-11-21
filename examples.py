# examples.py - Ejemplos de rompecabezas
from logic import *


def get_unicorn_example():
    """
    Ejemplo del unicornio mitico.

    Premisas:
    1. Si el unicornio es mitico, entonces es inmortal
    2. Si el unicornio no es mitico, entonces es un mamifero mortal
    3. Si el unicornio es inmortal o mamifero, entonces tiene cuernos
    4. El unicornio es magico si tiene cuernos

    Preguntas:
    - Es mitico el unicornio?
    - Es magico el unicornio?
    - Tiene cuernos el unicornio?
    """

    # Definir simbolos
    mitico = Symbol("mitico")
    inmortal = Symbol("inmortal")
    mamifero = Symbol("mamifero")
    mortal = Symbol("mortal")
    cuernos = Symbol("cuernos")
    magico = Symbol("magico")

    # Definir premisas
    premises = [
        {
            'sentence': Implication(mitico, inmortal),
            'description': "Si el unicornio es mitico, entonces es inmortal"
        },
        {
            'sentence': Implication(Not(mitico), And(mamifero, mortal)),
            'description': "Si el unicornio no es mitico, entonces es un mamifero mortal"
        },
        {
            'sentence': Implication(Or(inmortal, mamifero), cuernos),
            'description': "Si el unicornio es inmortal o mamifero, entonces tiene cuernos"
        },
        {
            'sentence': Implication(cuernos, magico),
            'description': "El unicornio es magico si tiene cuernos"
        }
    ]

    # Definir consultas
    queries = [
        {
            'query': mitico,
            'question': "Es mitico el unicornio?",
            'symbol': 'Mitico?'
        },
        {
            'query': magico,
            'question': "Es magico el unicornio?",
            'symbol': 'Magico?'
        },
        {
            'query': cuernos,
            'question': "Tiene cuernos el unicornio?",
            'symbol': 'Cuernos?'
        }
    ]

    return {
        'description': """Dado lo siguiente, se puede probar que el unicornio es mitico? Magico? Tiene cuernos?

Si el unicornio es mitico, entonces es inmortal, pero si no es mitico, 
entonces es un mamifero mortal. Si el unicornio es o inmortal o mamifero, 
entonces tiene cuernos. El unicornio es magico si tiene cuernos.""",
        'symbols': {
            'mitico': 'El unicornio es mitico',
            'inmortal': 'El unicornio es inmortal',
            'mamifero': 'El unicornio es mamifero',
            'mortal': 'El unicornio es mortal',
            'cuernos': 'El unicornio tiene cuernos',
            'magico': 'El unicornio es magico'
        },
        'premises': premises,
        'queries': queries
    }


def get_custom_example():
    """
    Plantilla para crear ejemplos personalizados.
    """
    # Aqui puedes agregar mas ejemplos siguiendo la misma estructura
    pass