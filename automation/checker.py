from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from automation.utils import human_typing

class EmployeeChecker:
    def __init__(self, driver, log_fn, data_row):
        self.driver = driver
        self.log = log_fn
        self.data = data_row

    def wait_and_fill(self, by, value, text, delay=0.15):
        field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((by, value))
        )
        field.clear()
        human_typing(field, text, delay)

    def click_button_by_xpath(self, xpath, timeout=20):
        button = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        button.click()

    def fill_birth_date(self):
        self.wait_and_fill(By.NAME, "c_birth_date", self.data["Дата рождения"])
        self.click_button_by_xpath("//button[.//span[text()=' Продолжить ']]")
        self.log(f"🗓 Введена дата рождения: {self.data['Дата рождения']}")

    def fill_passport_info(self):
        self.wait_and_fill(By.ID, "c_series", self.data["Серия"])
        self.wait_and_fill(By.ID, "c_number", self.data["Номер"])
        self.wait_and_fill(By.NAME, "c_issue_date", self.data["Дата выдачи"])
        self.click_button_by_xpath("//button[.//span[text()=' Продолжить ']]")
        self.log("🛂 Паспортные данные введены")

    def get_result_text(self):
        result_block = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "output-html"))
        )
        return result_block.find_element(By.TAG_NAME, "h3").text

    def click_check_again(self):
        self.click_button_by_xpath("//button[.//span[text()=' Проверить ещё ']]")
        self.log("🔁 Переход к следующей проверке...")

    def run_check(self):
        try:
            self.fill_birth_date()
            self.fill_passport_info()
            comment = self.get_result_text()
            self.log(f"📄 Результат: {comment}")
            self.click_check_again()
            return comment
        except Exception as e:
            self.log(f"❌ Ошибка при проверке: {e}")
            return "Ошибка при проверке"