MercadoLibre Scraper

Proyecto de un script en Python que utiliza Selenium para automatizar la búsqueda de productos en MercadoLibre. 
Permite aplicar filtros (como "solo productos nuevos") y extraer información de los primeros 5 resultados obtenidos.

 En el ejemplo proporcionado, el script busca una PlayStation 5, filtrando solo productos nuevos.

Tecnologías utilizadas
    - Python 3.x
    - Selenium
    - ChromeDriver (WebDriver para Google Chrome)
    - Librerías estándar: time

Instalación

Clona este repositorio:

    - git clone <URL_DEL_REPOSITORIO>
    - cd <NOMBRE_DEL_REPOSITORIO>

Instala las dependencias:

    - pip install selenium


Descarga ChromeDriver:

Descarga la versión compatible con tu navegador desde:
    - https://googlechromelabs.github.io/chrome-for-testing/

Asegúrate de que el ejecutable esté incluido en tu variable de entorno PATH.


Instrucciones

Edita las siguientes variables dentro del script principal para personalizar la búsqueda:

    - PRODUCTO = 'PlayStation 5'
    - URL = 'https://www.mercadolibre.com.mx/'


Luego ejecuta el script:

python automatizacion.py


El script abrirá una ventana del navegador, realizará la búsqueda, aplicará los filtros y mostrará por consola los primeros 5 resultados.# ML-Scraper
