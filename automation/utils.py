# automation/utils.py
import time
from selenium.webdriver.common.action_chains import ActionChains

def human_typing(element, text, delay=0.1):
    element.click()
    for char in text:
        ActionChains(element._parent).send_keys(char).perform()
        time.sleep(delay)