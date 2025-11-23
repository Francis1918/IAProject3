# Sistema de Resolución Lógica Proposicional

```
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║   ∀x ∈ U : P(x) ⇒ Q(x)  |  ¬(A ∧ B) ≡ ¬A ∨ ¬B  |  ∃y : R(y) ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

👥 Autores

**Equipo de Desarrollo:**

```
┌─────────────────────────────────────────┐
│  Bravo Francis                          │
│  Freire Ismael                          │
│  Pasquel Johann                         │
│  Torres Jorge                           │
└─────────────────────────────────────────┘
```

**Institución:** Escuela Politécnica Nacional
**Curso:** Inteligencia Artificial y Programación
**Fecha:** Noviembre 2025

**Análisis y Resolución de Rompecabezas Lógicos mediante Tabla de Verdad**

Sistema formal de resolución de problemas lógicos basado en **lógica proposicional** y **tablas de verdad**. Implementa un motor de inferencia completo que permite verificar la validez de conclusiones a partir de un conjunto de premisas mediante el método de **model checking**.

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Educational-green.svg)]()

### Características Principales

```
⊢ Resolución automática mediante tablas de verdad
⊢ Motor de inferencia lógica (model checking)
⊢ Soporte completo para operadores lógicos (¬, ∧, ∨, ⇒, ⇔)
⊢ Interfaz web profesional con visualizaciones matemáticas
⊢ Análisis de consistencia de bases de conocimiento
⊢ Generación de modelos válidos
```

### Caso de Estudio: El Problema del Unicornio

El sistema resuelve el clásico problema lógico:

```
Dado:
  1. Si el unicornio es mítico ⇒ es inmortal
  2. Si ¬mítico ⇒ (mamífero ∧ mortal)
  3. (inmortal ∨ mamífero) ⇒ tiene cuernos
  4. tiene cuernos ⇒ es mágico

Demostrar:
  ¿Es mítico?
  ¿Es mágico?
  ¿Tiene cuernos?
```

## 🏗️ Arquitectura del Sistema

```
┌─────────────────────────────────────────────────────────────┐
│                    CAPA DE PRESENTACIÓN                     │
│  ┌──────────────────┐         ┌──────────────────┐         │
│  │   index.html     │         │  proyecto3.py    │         │
│  │  (Interfaz Web)  │         │ (CLI Interface)  │         │
│  └────────┬─────────┘         └────────┬─────────┘         │
└───────────┼──────────────────────────────┼──────────────────┘
            │                              │
┌───────────┼──────────────────────────────┼──────────────────┐
│           │        CAPA LÓGICA           │                  │
│           └──────────────┬───────────────┘                  │
│                          │                                  │
│              ┌───────────▼───────────┐                      │
│              │      logic.py         │                      │
│              │  ┌─────────────────┐  │                      │
│              │  │ Symbol          │  │                      │
│              │  │ Not, And, Or    │  │                      │
│              │  │ Implication     │  │                      │
│              │  │ Biconditional   │  │                      │
│              │  │ model_check()   │  │                      │
│              │  └─────────────────┘  │                      │
│              └───────────────────────┘                      │
└─────────────────────────────────────────────────────────────┘
```

### Flujo de Ejecución

1. Definición de Símbolos
   ↓
2. Construcción de Base de Conocimiento ($KB$)
   ↓
3. Generación de Tabla de Verdad ($2^n $combinaciones)
   ↓
4. Evaluación de KB en cada modelo
   ↓
5. Model Checking (KB ⊨ Query)
   ↓
6. Presentación de Resultados

## 🚀 Instalación

### Requisitos Previos

```bash
Python 3.7+
Navegador web moderno (Chrome, Firefox, Edge, Safari)
```

### Instalación Rápida

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/proyecto3-logica.git
cd proyecto3-logica

# 2. No se requieren dependencias externas para la versión web
# Para la versión CLI, Python estándar es suficiente
```

### Verificación de Instalación

```bash
# Verificar Python
python --version  # Debe ser 3.7 o superior

# Ejecutar versión CLI
python proyecto3.py
```

---

## 📖 Guía de Uso

### Opción 1: Interfaz Web (Recomendado)

```bash
# Abrir index.html en tu navegador
# Doble clic en el archivo o:
open index.html        # macOS
start index.html       # Windows
xdg-open index.html    # Linux
```

**Funcionalidades:**

1. **Generar Tabla de Verdad**: Muestra todos los modelos válidos
2. **Resolver Acertijo**: Ejecuta el model checking y muestra resultados
3. **Visualizaciones**: Animaciones matemáticas en tiempo real
4. **Estadísticas**: Análisis de consistencia de la KB

### Opción 2: Interfaz CLI

```bash
python proyecto3.py
```

**Salida esperada:**

```
--- TABLA DE VERDAD (Solo filas válidas/consistentes) ---
Mítico | Inmortal | Mamífero | Mortal | Cuernos | Mágico | KB (Es válida?)
------------------------------------------------------------------------
True   | True     | False    | False  | True    | True   | True
False  | False    | True     | True   | True    | True   | True

Nro de modelos donde la KB se cumple: 2

--- RESULTADOS DE INFERENCIA ---
¿Se puede probar que es Mítico? False
¿Se puede probar que es Mágico? True
¿Se puede probar que tiene Cuernos? True
```

## 🔬 Documentación Técnica

### `logic.py` - Motor de Lógica Proposicional

#### Clases Principales

##### 1. `Sentence` (Clase Base Abstracta)

```python
class Sentence():
    def evaluate(self, model: dict) -> bool
    def formula(self) -> str
    def symbols(self) -> set
```

**Métodos:**

- `evaluate(model)`: Evalúa la sentencia en un modelo dado
- `formula()`: Retorna representación en string
- `symbols()`: Retorna conjunto de símbolos

##### 2. `Symbol` - Símbolos Proposicionales

```python
Mi = Symbol("Mítico")
I = Symbol("Inmortal")
```

**Propósito:** Representa variables booleanas atómicas.

##### 3. `Not` - Negación Lógica (¬)

```python
Not(Mi)  # ¬Mítico
```

**Tabla de Verdad:**

```
P  | ¬P
---|----
1  | 0
0  | 1
```

##### 4. `And` - Conjunción Lógica (∧)

```python
And(Ma, Mo)  # Mamífero ∧ Mortal
```

**Tabla de Verdad:**

```
P  Q | P∧Q
-----|----
1  1 | 1
1  0 | 0
0  1 | 0
0  0 | 0
```

##### 5. `Or` - Disyunción Lógica (∨)

```python
Or(I, Ma)  # Inmortal ∨ Mamífero
```

**Tabla de Verdad:**

```
P  Q | P∨Q
-----|----
1  1 | 1
1  0 | 1
0  1 | 1
0  0 | 0
```

##### 6. `Implication` - Implicación Lógica (⇒)

```python
Implication(Mi, I)  # Mítico ⇒ Inmortal
```

**Tabla de Verdad:**

```
P  Q | P⇒Q
-----|----
1  1 | 1
1  0 | 0
0  1 | 1
0  0 | 1
```

**Equivalencia:** `P ⇒ Q ≡ ¬P ∨ Q`

##### 7. `Biconditional` - Bicondicional Lógico (⇔)

```python
Biconditional(P, Q)  # P ⇔ Q
```

**Tabla de Verdad:**

```
P  Q | P⇔Q
-----|----
1  1 | 1
1  0 | 0
0  1 | 0
0  0 | 1
```

#### Función Principal: `model_check()`

```python
def model_check(knowledge: Sentence, query: Sentence) -> bool
```

**Algoritmo:**

```
function MODEL-CHECK(KB, α):
    symbols ← SYMBOLS(KB) ∪ SYMBOLS(α)
    return CHECK-ALL(KB, α, symbols, {})

function CHECK-ALL(KB, α, symbols, model):
    if symbols is empty:
        if KB is true in model:
            return α is true in model
        return true
    else:
        P ← FIRST(symbols)
        rest ← REST(symbols)
        return (CHECK-ALL(KB, α, rest, model ∪ {P=true}) and
                CHECK-ALL(KB, α, rest, model ∪ {P=false}))
```

**Complejidad:** O(2^n) donde n = número de símbolos

**Retorna:**

- `True`: KB ⊨ query (la KB implica la query)
- `False`: KB ⊭ query (la KB no implica la query)

---

### `proyecto3.py` - Implementación del Problema

#### Estructura del Código

```python
# 1. DEFINICIÓN DE SÍMBOLOS
Mi = Symbol("Mítico")
I  = Symbol("Inmortal")
Ma = Symbol("Mamífero")
Mo = Symbol("Mortal")
H  = Symbol("Cuernos")
Mg = Symbol("Mágico")

# 2. BASE DE CONOCIMIENTO
knowledge = And(
    Implication(Mi, I),                    # Axioma 1
    Implication(Not(Mi), And(Ma, Mo)),     # Axioma 2
    Implication(Or(I, Ma), H),             # Axioma 3
    Implication(H, Mg)                     # Axioma 4
)

# 3. GENERACIÓN DE TABLA DE VERDAD
def imprimir_tabla_verdad(kb, simbolos):
    combinaciones = list(itertools.product([True, False], 
                                          repeat=len(simbolos)))
    for valores in combinaciones:
        modelo = dict(zip([s.name for s in simbolos], valores))
        es_verdad = kb.evaluate(modelo)
        if es_verdad:
            # Imprimir fila válida

# 4. RESOLUCIÓN
def resolver_preguntas():
    es_mitico = model_check(knowledge, Mi)
    es_magico = model_check(knowledge, Mg)
    tiene_cuernos = model_check(knowledge, H)
```

#### Análisis de Complejidad

```
Símbolos: 6 (Mi, I, Ma, Mo, H, Mg)
Combinaciones totales: 2^6 = 64
Modelos válidos: 2

Tiempo de ejecución: O(2^n × m)
  donde n = número de símbolos
        m = complejidad de evaluar KB
```

## 🦄 El Problema del Unicornio

### Formalización Matemática

**Símbolos:**

```
Mi : Mítico
I  : Inmortal
Ma : Mamífero
Mo : Mortal
H  : Cuernos
Mg : Mágico
```

**Base de Conocimiento (KB):**

```
KB = (Mi ⇒ I) ∧ 
     (¬Mi ⇒ (Ma ∧ Mo)) ∧ 
     ((I ∨ Ma) ⇒ H) ∧ 
     (H ⇒ Mg)
```

### Tabla de Verdad Completa

```
Mi | I  | Ma | Mo | H  | Mg | KB
---|----|----|----|----|----|----|
1  | 1  | 0  | 0  | 1  | 1  | 1  ✓
0  | 0  | 1  | 1  | 1  | 1  | 1  ✓
```

**Modelos válidos:** 2 de 64 (3.125%)

### Análisis de Resultados

#### Query 1: ¿Es Mítico? (Mi)

```
Modelo 1: Mi = 1  ✓
Modelo 2: Mi = 0  ✓

Conclusión: KB ⊭ Mi (INDETERMINADO)
```

**Explicación:** Existen modelos válidos donde Mi es verdadero y falso.

#### Query 2: ¿Es Mágico? (Mg)

```
Modelo 1: Mg = 1  ✓
Modelo 2: Mg = 1  ✓

Conclusión: KB ⊨ Mg (VERDADERO)
```

**Demostración:**

```
1. (I ∨ Ma) ⇒ H        [Axioma 3]
2. En ambos modelos: I ∨ Ma = 1
3. Por modus ponens: H = 1
4. H ⇒ Mg              [Axioma 4]
5. Por modus ponens: Mg = 1
∴ KB ⊨ Mg
```

#### Query 3: ¿Tiene Cuernos? (H)

```
Modelo 1: H = 1  ✓
Modelo 2: H = 1  ✓

Conclusión: KB ⊨ H (VERDADERO)
```

**Demostración:**

```
Caso 1 (Mi = 1):
  Mi ⇒ I           [Axioma 1]
  I = 1
  I ∨ Ma = 1
  (I ∨ Ma) ⇒ H     [Axioma 3]
  H = 1

Caso 2 (Mi = 0):
  ¬Mi ⇒ (Ma ∧ Mo)  [Axioma 2]
  Ma = 1
  I ∨ Ma = 1
  (I ∨ Ma) ⇒ H     [Axioma 3]
  H = 1

∴ KB ⊨ H
```

### Conclusión Formal

```
⊢ KB ⊨ Mg  (El unicornio es mágico)
⊢ KB ⊨ H   (El unicornio tiene cuernos)
⊢ KB ⊭ Mi  (No se puede determinar si es mítico)
```

## 🎓 Conceptos Teóricos

### Lógica Proposicional

**Definición:** Sistema formal que estudia proposiciones y sus relaciones mediante conectivos lógicos.

**Sintaxis:**

```
φ ::= p | ¬φ | (φ ∧ φ) | (φ ∨ φ) | (φ ⇒ φ) | (φ ⇔ φ)
```

**Semántica:**

- Modelo: Asignación de valores de verdad a símbolos
- Satisfacibilidad: ∃ modelo donde φ es verdadera
- Validez: ∀ modelo, φ es verdadera
- Consecuencia lógica: KB ⊨ α

### Model Checking

**Definición:** Método para verificar si KB ⊨ α mediante enumeración exhaustiva de modelos.

**Teorema:**

```
KB ⊨ α ⟺ ∀ modelo M, si M ⊨ KB entonces M ⊨ α
```

**Propiedades:**

- Correcto (sound)
- Completo (complete)
- Decidible

### Tabla de Verdad

**Definición:** Representación tabular de todas las posibles asignaciones de verdad.

**Tamaño:** 2^n filas para n símbolos

**Uso:** Verificación de tautologías, contradicciones y contingencias.

### 1. Optimizaciones

```python
# Poda de búsqueda
def model_check_optimized(kb, query):
    # Early termination
    # Caching de evaluaciones
    # Heurísticas de ordenamiento
```

### 2. Nuevos Operadores

```python
class Xor(Sentence):  # Disyunción exclusiva
class Nand(Sentence): # NAND
class Nor(Sentence):  # NOR
```

### 3. Resolución por Refutación

```python
def resolution(kb, query):
    # Convertir a CNF
    # Aplicar regla de resolución
    # Buscar cláusula vacía
```

### 4. Lógica de Primer Orden

```python
class Predicate(Sentence):
class Quantifier(Sentence):
    # ∀x P(x)
    # ∃x Q(x)
```
