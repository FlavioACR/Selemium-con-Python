# TEST  SUIT PARA EJECUTAR LA PRUEBAS DE MANERA SIMULTANEA

from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTest
from searchtests2 import SearchTests

# Paso 1: Declarar las variables para cargar los casos de prueba
# assertions.py
assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
# searchtests2.py
search_test = TestLoader().loadTestsFromTestCase(SearchTests)

# Paso 2: Construir la suite de pruebas a travez del codigo:
smoke_test = TestSuite([assertions_test, search_test])


# Otro modo de Realizarlo:
kwargs = {
    # Indica el nombre donde se guardara el reporte:
    "output": 'smoke-report'
}

# Pasar el HTMLTestRunner:
runner = HTMLTestRunner(**kwargs)
# Corremos el Runner, llamando a la suite de testing llamanda smoke_test:
runner.run(smoke_test)

