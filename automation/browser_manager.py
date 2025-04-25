from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException

def get_browser():
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        return driver
    except WebDriverException as e:
        raise RuntimeError(f"❌ Chrome не запущен: {e}")