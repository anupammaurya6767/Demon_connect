# api/whatsapp_api.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from features.login.login_whatsapp import login_whatsapp
from features.send.send_message import send_message
from features.send.send_image import send_image
from features.send.send_video import send_video
from features.delete.delete_message import delete_message
from features.tagall.tagall import tag_all
from features.extras.fetch_all_unread_chats import fetch_all_unread_chats
from features.extras.get_list_of_messages import get_list_of_messages
from features.send.send_file import send_file
from features.logout.logout import logout
from typing import Optional
from pathlib import Path
from features.extras.get_list_of_messages import get_list_of_messages



class Demon:
    def __init__(self, browser, browser_path, driver_path):
        self.browser = browser
        self.browser_path = browser_path
        self.driver_path = driver_path
        self.driver = self.load_driver()


    def load_driver(self):
        """
        Load the Selenium driver depending on the browser
        (Edge and Safari are not running yet)
        """
        driver = None
        if self.browser == 'firefox':
            firefox_profile = webdriver.FirefoxProfile(
                self.browser_path)
            driver = webdriver.Firefox(firefox_profile)
        elif self.browser == 'Chrome':
            chrome_options = webdriver.ChromeOptions()
            if self.browser_path:
                chrome_options.add_argument('user-data-dir=' +
                                            self.browser_path)
            driver = webdriver.Chrome(executable_path=f"{self.driver_path}", options=chrome_options)
        elif self.browser == 'safari':
            pass
        elif self.browser == 'edge':
            pass

        return driver

    def login(self):
        login_whatsapp(self.driver)

    def send_message(self,contact_name, message):
        send_message(self.driver,contact_name, message)

    def send_image(self,contact_name, image_path):
        send_image(self.driver,contact_name, image_path)

    def send_video(self,contact_name, video_path):
        send_video(self.driver,contact_name, video_path)

    def delete_message(self, group_name, message):
        delete_message(self.driver, group_name, message)
    
    def tag_all(self, group_name):
        tag_all(self.driver, group_name)

    def get_list_of_messages(self):
        get_list_of_messages(self.driver)

    def send_file(self, contact_name, filename: Path, message: Optional[str] = None):
        send_file(self.driver, contact_name, filename, message)

    def send_image(self,contact_name, picture: Path, message: Optional[str] = None):
        send_image(self.driver,contact_name, picture, message)
    
    def send_video(self,contact_name, video: Path, message: Optional[str] = None):
        send_video(self.driver,contact_name, video, message)
    
    def fetch_all_unread_chats(self, limit=True, top=50):
        fetch_all_unread_chats(self.driver, limit, top)

    def logout(self):
        logout(self.driver)

    def close(self):
        self.driver.quit()

# Usage Example:
# You can create an instance of Demon and use its methods to interact with WhatsApp Web.
# Make sure to call close() when you're done to close the browser.
