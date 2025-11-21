# 🧩 Solucionador de Rompecabezas Lógicos

## 📋 Descripción

Este proyecto es un **solucionador automático de rompecabezas lógicos** que utiliza lógica proposicional y tablas de verdad para resolver problemas de razonamiento deductivo. El sistema permite tanto usar ejemplos predefinidos como crear rompecabezas personalizados de forma interactiva.

### Características principales:
- ✅ Resolución de problemas lógicos mediante tablas de verdad
- ✅ Sistema interactivo para crear rompecabezas personalizados
- ✅ Visualizaciones avanzadas con **Matplotlib** (tablas coloreadas, gráficos)
- ✅ Simplificación de expresiones lógicas con **SymPy** (CNF, DNF)
- ✅ Análisis estadístico de modelos válidos con **Pandas**
- ✅ Exportación de resultados a CSV
- ✅ Guardado de visualizaciones en PNG

---

## 📁 Estructura del Proyecto

```
IAPj3/
│
├── logic.py                      # Clases base de lógica proposicional
├── logic_solver.py               # Motor principal de resolución
├── truth_table.py                # Generador de tablas de verdad
├── visualizer.py                 # Visualizador básico de resultados
├── matplotlib_visualizer.py      # Visualizaciones avanzadas
├── logic_simplifier.py           # Simplificación con SymPy
├── input_handler.py              # Sistema de entrada interactiva
├── examples.py                   # Ejemplos predefinidos
├── main.py                       # Punto de entrada principal
├── requirements.txt              # Dependencias del proyecto
│
├── resultados_de_visualizaciones/   # Gráficos guardados (PNG)
└── tablas_de_verdad/                # Tablas exportadas (CSV)
```

---

## 📄 Descripción de Archivos

### Archivos Principales

#### `logic.py`
Contiene las **clases base** para representar sentencias lógicas:
- `Sentence`: Clase base abstracta
- `Symbol`: Símbolos proposicionales (variables booleanas)
- `Not`: Negación lógica (¬)
- `And`: Conjunción lógica (∧)
- `Or`: Disyunción lógica (∨)
- `Implication`: Implicación lógica (=>)
- `Biconditional`: Bicondicional lógico (<=>)
- `model_check()`: Algoritmo para verificar si una base de conocimiento implica una consulta

#### `logic_solver.py`
Motor principal del solucionador:
- Carga y procesa rompecabezas lógicos
- Construye la base de conocimiento a partir de premisas
- Verifica implicaciones lógicas (entailment)
- Coordina la generación de tablas de verdad
- Integra visualizaciones y simplificaciones
- Gestiona la exportación de resultados

#### `truth_table.py`
Generador de tablas de verdad:
- Genera todas las combinaciones posibles de valores
- Evalúa la base de conocimiento en cada modelo
- Crea DataFrames de Pandas para análisis
- Exporta tablas a CSV con timestamp
- Calcula estadísticas sobre modelos válidos
- Identifica modelos que satisfacen la base de conocimiento

#### `matplotlib_visualizer.py`
Visualizaciones avanzadas con Matplotlib:
- **Tabla de verdad colorizada**: Verde (verdadero), Rosa (falso)
- **Gráfico de resultados**: Barras horizontales con resultados de consultas
- **Gráfico de pastel**: Proporción de modelos válidos vs inválidos
- **Gráfico de frecuencia**: Frecuencia de símbolos en modelos válidos
- Sistema de guardado en carpeta `resultados_de_visualizaciones/`

#### `logic_simplifier.py`
Simplificación y análisis con SymPy:
- Convierte expresiones propias a formato SymPy
- Simplifica expresiones lógicas complejas
- Convierte a **CNF** (Forma Normal Conjuntiva)
- Convierte a **DNF** (Forma Normal Disyuntiva)
- Muestra análisis completo de expresiones

#### `input_handler.py`
Sistema interactivo de entrada personalizada:
- **Paso 1**: Descripción del problema
- **Paso 2**: Definición de símbolos proposicionales
- **Paso 3**: Creación de premisas (reglas lógicas)
  - Implicaciones (Si A entonces B)
  - Conjunciones (A y B)
  - Disyunciones (A o B)
  - Negaciones (No A)
  - Bicondicionales (A si y solo si B)
- **Paso 4**: Definición de preguntas a resolver

#### `visualizer.py`
Visualizador básico de consola:
- Muestra resumen textual de resultados
- Presenta conclusiones de forma clara

#### `examples.py`
Ejemplos predefinidos:
- **Ejemplo del Unicornio**: Problema clásico de lógica proposicional
- Plantilla para agregar más ejemplos

#### `main.py`
Punto de entrada del programa:
- Menú interactivo principal
- Opción 1: Resolver ejemplo predefinido
- Opción 2: Crear rompecabezas personalizado
- Opción 3: Salir

---

## 🚀 Instalación

### Requisitos Previos
- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Paso 1: Clonar o descargar el proyecto
```
https://github.com/Francis1918/IAProject3.git
```

### Paso 2: Crear un entorno virtual (opcional pero recomendado)
```bash
python -m venv .venv
.venv\Scripts\activate
```

### Paso 3: Instalar las dependencias
```bash
pip install -r requirements.txt
```

Las dependencias que se instalarán son:
- **matplotlib** >= 3.7.0 - Visualizaciones gráficas
- **pandas** >= 2.0.0 - Manejo de datos tabulares
- **numpy** >= 1.24.0 - Computación numérica
- **sympy** >= 1.12 - Matemática simbólica
- **tabulate** >= 0.9.0 - Formateo de tablas en consola

---

## 📖 Guía de Uso

### Ejecución del Programa

```bash
python main.py
```

### Opción 1: Resolver Ejemplo Predefinido

Al seleccionar la opción 1, el programa resolverá el **Problema del Unicornio**:

**Premisas:**
1. Si el unicornio es mítico, entonces es inmortal
2. Si el unicornio no es mítico, entonces es un mamífero mortal
3. Si el unicornio es inmortal o mamífero, entonces tiene cuernos
4. El unicornio es mágico si tiene cuernos

**Preguntas:**
- ¿Es mítico el unicornio?
- ¿Es mágico el unicornio?
- ¿Tiene cuernos el unicornio?

El programa mostrará:
1. Descripción del problema
2. Símbolos definidos
3. Premisas en lenguaje natural
4. Análisis y simplificación con SymPy
5. Tabla de verdad completa
6. Resultados de las consultas
7. Estadísticas de modelos válidos
8. Visualizaciones gráficas interactivas

### Opción 2: Crear Rompecabezas Personalizado

Esta opción te guía paso a paso:

#### **Paso 1: Descripción**
```
Descripción: Determinar las características de un dragón
```

#### **Paso 2: Definir Símbolos**
```
¿Deseas agregar un símbolo? (s/n): s
Nombre del símbolo: vuela
Descripción de 'vuela': El dragón puede volar

¿Deseas agregar un símbolo? (s/n): s
Nombre del símbolo: escupe_fuego
Descripción de 'escupe_fuego': El dragón escupe fuego

¿Deseas agregar un símbolo? (s/n): n
```

#### **Paso 3: Crear Premisas**
```
¿Deseas agregar una premisa? (s/n): s
Selecciona el tipo de premisa:
  1. Implicación (Si... entonces...)
  2. Conjunción (Y)
  3. Disyunción (O)
  4. Negación (No)
  5. Bicondicional (Si y solo si)

Elige una opción (1-5): 1

Antecedente (el 'Si'):
Nombre del símbolo: vuela
¿Negar 'vuela'? (s/n): n

Consecuente (el 'entonces'):
Nombre del símbolo: escupe_fuego
¿Negar 'escupe_fuego'? (s/n): n

Descripción en lenguaje natural: Si el dragón vuela, entonces escupe fuego
```

#### **Paso 4: Definir Preguntas**
```
¿Deseas agregar una pregunta? (s/n): s
¿Sobre qué símbolo es la pregunta?: vuela
Formula la pregunta sobre 'vuela': ¿Puede volar el dragón?
```

### Opciones Posteriores a la Resolución

#### **Guardar Visualizaciones**
```
¿Deseas guardar las visualizaciones? (s/n): s
```
Se guardarán en `resultados_de_visualizaciones/` con timestamp:
- `tabla_verdad_YYYYMMDD_HHMMSS.png`
- `distribucion_resultados_YYYYMMDD_HHMMSS.png`
- `modelos_validos_YYYYMMDD_HHMMSS.png`
- `frecuencia_simbolos_YYYYMMDD_HHMMSS.png`

#### **Exportar Tabla de Verdad**
```
¿Deseas exportar la tabla de verdad a CSV? (s/n): s
```
Se guardará en `tablas_de_verdad/tabla_verdad_YYYYMMDD_HHMMSS.csv`

---

## 📊 Interpretación de Resultados

### Tabla de Verdad
- **0** = Falso
- **1** = Verdadero
- **KB** = Base de Conocimiento (todas las premisas combinadas)
- Las columnas adicionales muestran las consultas

### Resultados de Consultas
- **[VERDADERO]** - La KB implica necesariamente la consulta
- **[FALSO]** - La KB implica necesariamente la negación de la consulta
- **[INDETERMINADO]** - La KB no puede determinar el valor de la consulta

### Estadísticas
- **Total de modelos posibles**: 2^n donde n es el número de símbolos
- **Modelos que satisfacen KB**: Cuántos modelos hacen verdadera la base de conocimiento
- **Porcentaje de validez**: Proporción de modelos válidos

### Análisis SymPy
- **Original**: Expresión tal como fue definida
- **Simplificada**: Versión simplificada de la expresión
- **CNF**: Forma Normal Conjuntiva (conjunción de disyunciones)
- **DNF**: Forma Normal Disyuntiva (disyunción de conjunciones)

---

## 🎯 Ejemplos de Uso

### Ejemplo 1: Problema de Detectives
```
Símbolos:
- culpable: El sospechoso es culpable
- coartada: El sospechoso tiene coartada
- evidencia: Hay evidencia contra el sospechoso

Premisas:
1. Si hay evidencia y no tiene coartada, entonces es culpable
2. Hay evidencia
3. No tiene coartada

Pregunta: ¿Es culpable?
Resultado: VERDADERO
```

### Ejemplo 2: Elegibilidad para Beca
```
Símbolos:
- buen_promedio: Tiene buen promedio
- bajos_recursos: Es de bajos recursos
- beca: Recibe beca

Premisas:
1. Si tiene buen promedio y es de bajos recursos, entonces recibe beca
2. Tiene buen promedio
3. Es de bajos recursos

Pregunta: ¿Recibe beca?
Resultado: VERDADERO
```

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| Python | 3.7+ | Lenguaje de programación |
| Matplotlib | 3.7.0+ | Visualizaciones gráficas |
| Pandas | 2.0.0+ | Análisis de datos |
| NumPy | 1.24.0+ | Computación numérica |
| SymPy | 1.12+ | Matemática simbólica |
| Tabulate | 0.9.0+ | Formato de tablas |

---

## 📝 Notas Importantes

1. **Límite de Símbolos**: El programa puede manejar cualquier número de símbolos, pero ten en cuenta que el número de modelos crece exponencialmente (2^n). Para más de 10 símbolos, la generación puede ser lenta.

2. **Visualizaciones**: Las visualizaciones de Matplotlib se muestran en ventanas interactivas. Cierra cada ventana para continuar con la siguiente.

3. **Archivos de Salida**: Todos los archivos generados incluyen timestamp para evitar sobrescribir resultados anteriores.

4. **Encoding**: Si experimentas problemas con caracteres especiales en la consola de Windows, considera usar una terminal con soporte UTF-8.

---

## 🤝 Contribuciones

Para agregar nuevos ejemplos predefinidos, edita `examples.py` siguiendo la estructura del ejemplo del unicornio.

---

## 📧 Autores: Bravo Francis, Freire Ismael, Pasquel Johann, Torres Jorge

Proyecto desarrollado para el curso de Inteligencia Artificial y Programación.

**Fecha**: Noviembre 2025

---

## 📄 Licencia

Este proyecto es de uso educativo.

