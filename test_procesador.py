import unittest
import json
from src.procesador import Analizador

class TestAnalizador(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.archivo = "datos/sri_ventas_2024.csv"
        cls.analizador = Analizador(cls.archivo)
        cls.resultados = {}

    def test_ventas_totales_como_diccionario(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        try:
            self.assertIsInstance(resumen, dict)
            TestAnalizador.resultados["ventas_totales_como_diccionario"] = "OK"
        except AssertionError as e:
            TestAnalizador.resultados["ventas_totales_como_diccionario"] = f"FAIL: {e}"

    def test_ventas_totales_todas_las_provincias(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        try:
            self.assertEqual(len(resumen), 24)
            TestAnalizador.resultados["ventas_totales_todas_las_provincias"] = "OK"
        except AssertionError as e:
            TestAnalizador.resultados["ventas_totales_todas_las_provincias"] = f"FAIL: {e}"

    def test_ventas_totales_mayores_5k(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        try:
            self.assertTrue(all(float(v) > 5000 for v in resumen.values()))
            TestAnalizador.resultados["ventas_totales_mayores_5k"] = "OK"
        except AssertionError as e:
            TestAnalizador.resultados["ventas_totales_mayores_5k"] = f"FAIL: {e}"

    def test_ventas_por_provincia_existente(self):
        try:
            resultado = self.analizador.ventas_por_provincia("pichincha")
            self.assertGreater(resultado, 0)
            TestAnalizador.resultados["ventas_por_provincia_existente"] = "OK"
        except AssertionError as e:
            TestAnalizador.resultados["ventas_por_provincia_existente"] = f"FAIL: {e}"

    def test_ventas_por_provincia_inexistente(self):
        try:
            resultado = self.analizador.ventas_por_provincia("Narnia")
            self.assertEqual(resultado, 0.0)
            TestAnalizador.resultados["ventas_por_provincia_inexistente"] = "OK"
        except AssertionError as e:
            TestAnalizador.resultados["ventas_por_provincia_inexistente"] = f"FAIL: {e}"

    @classmethod
    def tearDownClass(cls):
        ruta = "datos/resultados_test.json"
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(cls.resultados, f, indent=4, ensure_ascii=False)
        print(f"\nLos resultados han sido guardados en: {ruta}\n")



if __name__ == "__main__":
    unittest.main(buffer=True)
