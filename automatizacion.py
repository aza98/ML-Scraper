from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# Configuración
PRODUCTO = 'PlayStation 5'
URL = 'https://www.mercadolibre.com.mx/'

# Inicializar navegador
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Buscar producto
    driver.get(URL)
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'as_word'))
    )
    search_box.send_keys(PRODUCTO)
    search_box.submit()
    
    # Aplicar filtro "Nuevo" 
    filtro_nuevo = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@title, 'Nuevo')]"))
    )
    filtro_nuevo.click()
    
    # Obtener primeros 5 productos
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'li.ui-search-layout__item'))
    )
    productos = driver.find_elements(By.CSS_SELECTOR, 'li.ui-search-layout__item')[:5]
    
    print(f"Primeros 5 resultados para '{PRODUCTO}' (solo NUEVOS):\n")
    
    for i, item in enumerate(productos, 1):
        try:
            title = item.find_element(By.CSS_SELECTOR, 'a.poly-component__title').text
            link = item.find_element(By.CSS_SELECTOR, 'a.poly-component__title').get_attribute('href')
            price = item.find_element(By.CSS_SELECTOR, '.poly-price__current .andes-money-amount__fraction').text
            print(f"{i}. {title} - ${price}")
            print(f"   {link}\n")
        except:
            print(f"{i}. No se pudo extraer información del producto\n")

except Exception as e:
    print(f"Error: {e}")

finally:
    time.sleep(3)
    driver.quit()