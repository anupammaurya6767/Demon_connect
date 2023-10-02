# features/login/login_whatsapp.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def login_whatsapp(driver):
    try:
        # Open WhatsApp Web
        driver.get("https://web.whatsapp.com/")

        # Wait for the QR code to be scanned by the user
        WebDriverWait(driver, 600).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div/div[1]/div[2]/div/div[2]'))
        )
        
        print("Successfully logged in to WhatsApp Web!")

    except TimeoutException:
        print("QR code scan timed out. Please try again.")

# Usage Example:
# Call login_whatsapp(driver) function in your main.py script to log in to WhatsApp Web.
