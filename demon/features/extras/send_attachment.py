from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def send_attachment(driver):
        # Waiting for the pending clock icon to disappear
        WebDriverWait(driver, 10).until_not(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="main"]//*[@data-icon="msg-time"]')
            )
        )

        sendButton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div[1]/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div/span',
                )
            )
        )
        sendButton.click()

        # Waiting for the pending clock icon to disappear again - workaround for large files or loading videos.
        # Appropriate solution for the presented issue. [nCKbr]
        WebDriverWait(driver, 10).until_not(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="main"]//*[@data-icon="msg-time"]')
            )
        )