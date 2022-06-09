Resumen
¿Qué es Selenium?
Es una SUIT de herramientas para la automatización de navegadores Web.
El objetivo de Selenium NO fue para el Testing ni para el Web Scraping (aunque se puede usar para eso), por lo tanto, no es el más optimo para estas actividades.
Protocolo: WebDriver, herramienta que se conecta a un API.
Selenium WebDriver es la herramienta que utilizaremos en el curso.
-Selenium NO es un Software, ES una SUIT de Softwares.
*DDT: Data Drive Testing: Ingresar datos para que realice varias pruebas (sin intervención humana).

Selenium ID
Ventajas:
Excelente para iniciar
No requiere saber programar
Exporta scripts para Selenium RC y Selenium WebDriver
Genera reportes
Contras:
Disponible solo para Firefox y Chrome
No soporta DDT(Data Drive Test)

Selenium RC:
Ventajas:
Soporte para:
Varias plataformas, navegadores y lenguajes
Operaciones lógicas y condicionales
DDT
Posee una API madura

Contras:
Complejo de instalar
Necesita de un servidor corriendo
Comandos redundantes en su API
Navegación no tan realista

Selenium WebDriver:
Ventajas
Soporte para múltiples lenguajes
Fácil de instalar
Comunicación directa con el navegador
Interacción más realista
Contras:
No soporta nuevos navegadores tan rápido
No genera reporte o resultados de pruebas
Requiere de saber programar



Selenium Grid ( Complemento de la suite):
Ventajas
Se utiliza junto a Selenium RC
Permite correr pruebas en paralelo
Conveniente para ahorrar tiempo

Configurar un ambiente virtual para las clase 7-8.

Linux y MacOS:
#Para crear el ambiente virtual
python3 -m venv nameOfVirtualEnv

#Luego lo tienes que activar
source nameOfVirtualEnv/bin/activate

#Lo puedes desactivar así
deactivate

Windows:
#Crear
py -m venv nameOfVirtualEnv

#Activar
.\nameOfVirtualEnv\Scripts\activate

#Desactivar 
deactivate



# 6:
HOLA MUNDO!

Libreria: Unittest (Pytest)
* Test Fixture: Preparación para antes y después de la prueba.
* Test Case: Unidad de código a probar
* Test Suite: Colección de Test Cases (Fragmento de codifo para trabajar, definir o probar alguna función)
* Test Runner: Orquestador de la ejecución
* Test Report: Resumen de resultados.



# 8:
Preparar assertions y test suites:
Es un método para verificar o validar un valor esperado en la ejecución del test. Si el resultado es verdadero el test continúa, en caso contrario “falla” y termina.

Ejemplo: assertEqual(price.text,”300”)

Test suites:

Colección de test unificados en una sola prueba, permitiendo tener resultados grupales e individuales.(Similar a un árbol o diagrama)
