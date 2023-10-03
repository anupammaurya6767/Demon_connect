# api/whatsapp_api.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from features.login.login_whatsapp import login_whatsapp
from features.send.send_message import send_message
from features.send.send_image import send_image
from features.send.send_video import send_video
from features.receive.receive_message import receive_message
from features.send.send_group_message import send_group_message
from features.delete.delete_message import delete_message

class Demon:
    def __init__(self):
        self.driver = self.initialize_driver()

    def initialize_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--user-data-dir=./User_Data")  # Modify this path as needed
        return webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    def login(self):
        login_whatsapp(self.driver)

    def send_message(self, message):
        send_message(self.driver, message)

    def send_image(self, image_path):
        send_image(self.driver, image_path)

    def send_video(self, video_path):
        send_video(self.driver, video_path)

    def receive_message(self):
        return receive_message(self.driver)

    def send_group_message(self, group_name, message):
        send_group_message(self.driver, group_name, message)

    def delete_message(self, group_name, message):
        delete_message(self.driver, group_name, message)

    def close(self):
        self.driver.quit()

# Usage Example:
# You can create an instance of Demon and use its methods to interact with WhatsApp Web.
# Make sure to call close() when you're done to close the browser.
