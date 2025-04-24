# automation/browser_manager.py
import shutil
import platform
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.common.exceptions import WebDriverException

def get_browser():
    # Chrome
    if shutil.which("chromedriver"):
        try:
            options = ChromeOptions()
            options.add_argument("--start-maximized")
            return webdriver.Chrome(service=ChromeService(), options=options)
        except WebDriverException as e:
            print(f"❌ Ошибка Chrome: {e}")

    # Edge
    if shutil.which("msedgedriver"):
        try:
            options = EdgeOptions()
            options.add_argument("--start-maximized")
            return webdriver.Edge(service=EdgeService(), options=options)
        except WebDriverException as e:
            print(f"❌ Ошибка Edge: {e}")

    # Safari (только macOS)
    if platform.system() == "Darwin":
        try:
            return webdriver.Safari()
        except WebDriverException as e:
            print(f"❌ Ошибка Safari: {e}")

    raise RuntimeError("❌ Не найден доступный браузерный WebDriver: Chrome, Edge или Safari")