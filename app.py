from src.procesador import Analizador

def main():
    archivo = "datos/sri_ventas_2024.csv"
    analizador = Analizador(archivo)

    print("Ventas totales por provincia:")
    resumen = analizador.ventas_totales_por_provincia()
    
    # Obtener y ordenar las provincias alfabéticamente
    provincias_ordenadas = sorted(resumen.keys())
    
    for prov in provincias_ordenadas:
        total = resumen[prov]
        print(f"\t{prov}: ${total:.2f}")

    print("\nCompras para una provincia")
    
    # 1. Obtener la lista de provincias válidas (en mayúsculas para un chequeo consistente)
    provincias_validas = {prov.upper() for prov in resumen.keys()} 
    
    provincia = ""
    provincia_formateada = "" # Para almacenar la provincia con el formato correcto

    # 2. Bucle de validación para pedir la provincia hasta que sea válida
    while provincia not in provincias_validas:
        # Se pide la provincia y se convierte a mayúsculas para la validación
        entrada = input("\tIngrese el nombre de una provincia: ")
        provincia = entrada.strip().upper() 
        
        if provincia in provincias_validas:
            # Encontramos el nombre original de la provincia (con la capitalización correcta)
            for key in resumen.keys():
                if key.upper() == provincia:
                    provincia_formateada = key
                    break
        else:
            # Si no es válida, no sale nada, solo se vuelve a pedir
            pass 
            
    # Una vez que la provincia es válida y está en el formato correcto
    ventas = analizador.ventas_por_provincia(provincia_formateada)
    print(f"\tVentas de {provincia_formateada}: ${ventas:,.2f}")

if __name__ == "__main__":
    main()