# login_whatsapp.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class WhatsAppLogin:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def wait_for_login(self):
        # Open WhatsApp Web
        self.driver.get("https://web.whatsapp.com/")

        # Wait for the user to scan the QR code manually for 20 seconds
        input("Scan the QR code manually and press Enter after scanning...")

    def login(self):
        # Check if already logged in
        if "WhatsApp" in self.driver.title:
            print("Already logged in.")
        else:
            self.wait_for_login()
            print("Logged in successfully.")

    def logout(self):
        # Close the browser
        self.driver.quit()

# Example usage
if __name__ == "__main__":
    # Provide the path to the Chrome WebDriver executable
    chrome_driver_path = "path/to/chromedriver.exe"  # Update with the correct path

    # Initialize WhatsAppLogin and log in
    whatsapp_login = WhatsAppLogin(chrome_driver_path)
    whatsapp_login.login()
