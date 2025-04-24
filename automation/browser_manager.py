# automation/browser_manager.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import platform

def get_browser():
    try:
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        return driver
    except Exception as chrome_error:
        print(f"⚠️ Не удалось запустить Chrome: {chrome_error}")

        try:
            options = EdgeOptions()
            options.add_argument("--start-maximized")
            driver = webdriver.Edge(EdgeChromiumDriverManager().install(), options=options)
            return driver
        except Exception as edge_error:
            print(f"❌ Не удалось запустить Edge: {edge_error}")
            raise RuntimeError("❌ Не удалось запустить ни один браузер. Установи Chrome или Edge.")