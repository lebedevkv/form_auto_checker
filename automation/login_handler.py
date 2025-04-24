# automation/login_handler.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

LOGIN_URL = "https://www.gosuslugi.ru/655781/1/form?_=1745411643396"

def login_with_mfa(driver, log_fn):
    driver.get(LOGIN_URL)
    log_fn("🌐 Ожидаем логина и MFA...")

    try:
        # Ждём, пока кнопка "Начать" появится в DOM и станет видимой
        WebDriverWait(driver, 300).until(
            EC.visibility_of_element_located((By.XPATH, "//button[.//span[text()='Начать']]"))
        )
        start_button = driver.find_element(By.XPATH, "//button[.//span[text()='Начать']]")

        # Клик через JavaScript — обход защиты UI
        driver.execute_script("arguments[0].click();", start_button)
        log_fn("✅ Кнопка 'Начать' нажата через JS.")
        return True

    except Exception as e:
        log_fn(f"❌ Ошибка при нажатии на кнопку 'Начать': {e}")
        return False