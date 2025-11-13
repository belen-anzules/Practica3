from src.procesador import Analizador

def main():
    archivo = "datos/sri_ventas_2024.csv"
    analizador = Analizador(archivo)

    print(" CONSULTA DE VENTAS POR PROVINCIA")

    resumen = analizador.ventas_totales_por_provincia()

    provincias_ordenadas = sorted(resumen.keys())
    print("\nProvincias disponibles:")
    for prov in provincias_ordenadas:
        print(f" - {prov.capitalize()}")

    provincias_validas = {prov.upper() for prov in resumen.keys()}
    provincia = ""
    provincia_formateada = ""

    # Bucle hasta que el usuario ingrese una provincia válida
    while provincia not in provincias_validas:
        entrada = input("\nIngrese el nombre de una provincia: ")
        provincia = entrada.strip().upper()

        if provincia not in provincias_validas:
            print("⚠️ Provincia no válida. Intente nuevamente.")
        else:
            # Buscar el nombre correcto (con la capitalización original)
            for key in resumen.keys():
                if key.upper() == provincia:
                    provincia_formateada = key
                    break

    # Mostrar ventas de la provincia seleccionada
    ventas = analizador.ventas_por_provincia(provincia_formateada)
    print(f"\n💰 Ventas totales en {provincia_formateada.capitalize()}: ${ventas:,.2f}")

    opcion = input("\n¿Desea ver las estadísticas adicionales? (si/no): ").strip().lower()

    if opcion in ("si", "sí", "s"):
        print("Exportaciones totales por mes:")
        exportaciones = analizador.exportaciones_totales_por_mes()
        for mes, valor in exportaciones.items():
            print(f"\t{mes}: ${valor:,.2f}")

        print("Provincia con mayor volumen de importaciones:")
        resultado = analizador.provincia_mayor_importacion()
        if resultado:
            provincia_max, total = resultado
            print(f"\t{provincia_max.capitalize()}: ${total:,.2f}")
        else:
            print("No se encontraron datos de importaciones.")

        print("Porcentaje promedio de ventas con tarifa 0% por provincia:")
        porcentajes = analizador.porcentaje_tarifa_0_por_provincia()
        for prov, porc in sorted(porcentajes.items()):
            print(f"\t{prov.capitalize()}: {porc:.2f}%")
    else:
        print("Gracias por usar el analizador.")

if __name__ == "__main__":
    main()
