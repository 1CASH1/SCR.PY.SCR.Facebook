
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from login import Login

def init():
    # Configurar las opciones de Chrome
    chrome_options = Options()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
    )
    # Descargar automáticamente el ChromeDriver y configurar el servicio
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    login = Login(driver)
    login.login()


# Puedes agregar más acciones según sea necesario
if __name__ == "__main__":
        init() 