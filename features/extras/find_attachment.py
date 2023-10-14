from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def find_attachment(driver):
        clipButton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="main"]/footer//*[@data-icon="attach-menu-plus"]/..',
                )
            )
        )
        clipButton.click()