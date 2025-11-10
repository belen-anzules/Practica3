import csv

class Analizador:
    def __init__(self, ruta_csv):
        # Guardamos la ruta del archivo CSV
        self.ruta_csv = ruta_csv
        # Leemos el archivo CSV y guardamos los datos en memoria
        self.datos = self.leer_csv()

    def leer_csv(self):
        """Lee el archivo CSV y devuelve una lista de filas."""
        datos = []
        try:
            with open(self.ruta_csv, "r", encoding="utf-8") as archivo:
                # Usamos el delimitador '|'
                lector = csv.DictReader(archivo, delimiter= '|')
                for fila in lector:
                    datos.append(fila)
            return datos
        except FileNotFoundError:
            print(f"Error: El archivo {self.ruta_csv} no fue encontrado.")
            return []

    def provincias_unicas(self):
        """
        Devuelve un conjunto (set) de todas las provincias únicas, normalizadas a minúsculas.
        Esto se usa para la validación de la entrada del usuario.
        """
        # Usamos un 'set' para obtener solo valores únicos de forma eficiente
        return {fila["PROVINCIA"].lower() for fila in self.datos}

    def ventas_totales_por_provincia(self):
        """
        Devuelve un diccionario con el total de ventas por provincia.
        La clave de la provincia se convierte a minúsculas (.lower()).
        """
        totales = {}
        for fila in self.datos:
            provincia = fila["PROVINCIA"].lower() 
            # Aseguramos que la columna exista y que sea un número válido antes de convertir
            try:
                total_venta = float(fila["TOTAL_VENTAS"])
                totales[provincia] = totales.get(provincia, 0.0) + total_venta
            except ValueError:
                # Opcional: Manejar filas con datos no numéricos en TOTAL_VENTAS
                # print(f"Advertencia: Valor no numérico en TOTAL_VENTAS en la fila: {fila}")
                continue
            except KeyError:
                # Opcional: Manejar filas donde falta la columna TOTAL_VENTAS o PROVINCIA
                # print(f"Advertencia: Faltan columnas requeridas en la fila: {fila}")
                continue
        return totales

    def ventas_por_provincia(self, nombre):
        """
        Devuelve el total de ventas de una provincia específica.
        El nombre de entrada se convierte a minúsculas (.lower()).
        """
        totales = self.ventas_totales_por_provincia()
        nombre_normalizado = nombre.lower()

        # Retorna el total o 0.0 si no existe (ya está normalizado)
        return totales.get(nombre_normalizado, 0.0)

# --- FIN DE LA CLASE ANALIZADOR ---