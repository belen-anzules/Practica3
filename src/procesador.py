import csv

class Analizador:
    def __init__(self, ruta_csv):
        """Inicializa la clase y carga los datos del archivo CSV."""
        self.ruta_csv = ruta_csv
        self.datos = self.leer_csv()

    def leer_csv(self):
        """Lee el archivo CSV y devuelve una lista de filas."""
        datos = []
        try:
            with open(self.ruta_csv, "r", encoding="utf-8") as archivo:
                lector = csv.DictReader(archivo, delimiter='|')
                for fila in lector:
                    datos.append(fila)
            return datos
        except FileNotFoundError:
            print(f"Error: El archivo {self.ruta_csv} no fue encontrado.")
            return []

    def provincias_unicas(self):
        """Devuelve un conjunto con todas las provincias únicas en minúsculas."""
        return {fila["PROVINCIA"].lower() for fila in self.datos}

    def ventas_totales_por_provincia(self):
        """Devuelve un diccionario con el total de ventas por provincia."""
        totales = {}
        for fila in self.datos:
            try:
                provincia = fila["PROVINCIA"].lower()
                total_venta = float(fila["TOTAL_VENTAS"])
                totales[provincia] = totales.get(provincia, 0.0) + total_venta
            except (ValueError, KeyError):
                continue
        return totales

    def ventas_por_provincia(self, nombre):
        """Devuelve el total de ventas de una provincia específica."""
        totales = self.ventas_totales_por_provincia()
        nombre_normalizado = nombre.lower()
        return totales.get(nombre_normalizado, 0.0)

    def exportaciones_totales_por_mes(self):
        """Suma las exportaciones agrupadas por mes."""
        resultados = {}
        for fila in self.datos:
            try:
                mes = fila["MES"]
                valor = float(fila["EXPORTACIONES"]) if fila["EXPORTACIONES"] else 0
                resultados[mes] = resultados.get(mes, 0) + valor
            except (ValueError, KeyError):
                continue
        return resultados

    def provincia_mayor_importacion(self):
        """Devuelve la provincia con el mayor volumen total de importaciones."""
        importaciones = {}
        for fila in self.datos:
            try:
                provincia = fila["PROVINCIA"]
                valor = float(fila["IMPORTACIONES"]) if fila["IMPORTACIONES"] else 0
                importaciones[provincia] = importaciones.get(provincia, 0) + valor
            except (ValueError, KeyError):
                continue

        if not importaciones:
            return None

        provincia_max = max(importaciones, key=importaciones.get)
        return provincia_max, importaciones[provincia_max]

    def porcentaje_tarifa_0_por_provincia(self):
        """Calcula el porcentaje promedio de ventas con tarifa 0% respecto al total por provincia."""
        resultados = {}
        conteo = {}

        for fila in self.datos:
            try:
                provincia = fila["PROVINCIA"]
                tarifa_0 = float(fila["VENTAS_NETAS_TARIFA_0"]) if fila["VENTAS_NETAS_TARIFA_0"] else 0
                total = float(fila["TOTAL_VENTAS"]) if fila["TOTAL_VENTAS"] else 0

                if total > 0:
                    porcentaje = (tarifa_0 / total) * 100
                    resultados[provincia] = resultados.get(provincia, 0) + porcentaje
                    conteo[provincia] = conteo.get(provincia, 0) + 1
            except (ValueError, KeyError):
                continue

        for provincia in resultados:
            resultados[provincia] /= conteo[provincia]

        return resultados


# --- FIN DE LA CLASE ANALIZADOR ---
