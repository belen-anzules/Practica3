# 🧮 Práctica 3 - Análisis de Ventas por Provincia

## 📄 Descripción General

Este proyecto tiene como objetivo analizar la información de **ventas, importaciones y exportaciones** por provincia del Ecuador, utilizando datos del **Servicio de Rentas Internas (SRI)**.  
El programa permite realizar cálculos automáticos y obtener reportes resumidos de las ventas por provincia o por mes, asegurando la validación de datos y la correcta agregación de la información.

La práctica refuerza el uso de **Python**, **estructuras de datos**, **pruebas unitarias** y **análisis de cobertura**.


## 🧩 Estructura del Proyecto

├── app.py # Script principal del proyecto
├── src/
│ └── procesador.py # Clase Analizador con la lógica de negocio
├── datos/
│ ├── sri_ventas_2024.csv # Archivo CSV con los datos base
│ ├── resultados_test.json # Resultados de las pruebas unitarias
│ └── coverage.json # Resultados del análisis de cobertura
└── test_procesador.py # Archivo con las pruebas unitarias

---

## ⚙️ Funcionalidades Principales

- 📂 Lectura y validación de archivos CSV con delimitador `|`.
- 📊 Cálculo de **ventas totales por provincia**.
- 🌎 Cálculo de **exportaciones totales por mes**.
- 🚢 Identificación de la **provincia con mayor volumen de importaciones**.
- 🔍 Consulta de **ventas por provincia específica**.
- 🧾 Generación automática de archivos JSON con los resultados de pruebas y cobertura.

---

## 🧪 Pruebas Unitarias

Las pruebas fueron desarrolladas con el módulo estándar `unittest`, verificando:

1. Que las ventas totales se devuelvan como un diccionario.
2. Que existan datos para las 24 provincias.
3. Que todas las provincias tengan ventas mayores a 5K.
4. Que las consultas a provincias válidas devuelvan valores positivos.
5. Que las consultas a provincias inexistentes devuelvan 0.0.

**Resultados automáticos guardados en:**

datos/resultados_test.json

**Salida esperada al ejecutar las pruebas:**
.....

Ran 5 tests in 0.500s

OK
✅ Los resultados han sido guardados en: datos/resultados_test.json

---

## 📊 Cobertura de Código

El análisis de cobertura se realizó con el paquete `coverage`.

**Comandos utilizados:**
```bash
coverage run -m unittest discover
coverage json -o datos/coverage.json
coverage report
 
Resultado
 Name                      Stmts   Miss  Cover
---------------------------------------------
src/procesador.py            92     39    58%
test_procesador.py           25      0   100%
---------------------------------------------
TOTAL                       117     39    58%
Covertura del 58%

Archivo generado automáticamente en:
datos/coverage.json

** Requisitos

Python 3.10 o superior

Instalar dependencias necesarias:
pip install coverage
** 🧠 Autoría

Nombre: Belén Anzules
Práctica N.º 3: Análisis de datos con Python y pruebas unitarias
Lenguaje: Python 3.14
Repositorio: github.com/belen-anzules/Practica3
