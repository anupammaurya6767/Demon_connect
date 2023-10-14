# api/whatsapp_api.py
from __future__ import annotations
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
from typing import Dict, List, Callable
from utils.threads import MyThread
from utils.exceptions import InvalidEventException
from utils.handler import *
from utils.sorce import Sorce
from features.chat.unread_message import UnreadMessage
from features.extras.open import open
from features.chat.chat import Chat
from features.chat import *
from features.chat.group import Group
from time import sleep
from selenium.common.exceptions import StaleElementReferenceException

class Demon:
    _callbacks: Dict[str, Callable] = {
        "on_ready": None,
        "on_message": None
    }
    _threads: Dict[str, MyThread] = {
        "on_message": None
    }

    def __init__(self, browser, browser_path, driver_path):
        self.browser = browser
        self.browser_path = browser_path
        self.driver_path = driver_path
        self.driver = self.load_driver()
    
    def _is_loaded(self) -> bool:
        """Check if the page is loaded."""

        try:
            return element_exists(self.driver, By.CSS_SELECTOR, Sorce.SEARCH_BAR)
        except Exception:
            return False

    def _is_animating(self) -> bool:
        """Check if the page is animating."""

        return element_exists(self.driver, By.CSS_SELECTOR, Sorce.ANIMATING)


    def event(self, func: Callable) -> None:
        """Decorator to register a function as an event handler.

        #### Arguments
            * func: The function to be registered. It must be a coroutine.

        Raises:
            * InvalidEvent: If the function name is not a valid event.
        """

        if func.__name__ not in self._callbacks.keys():
            raise InvalidEventException(f"Invalid event: {func.__name__}")

        self._callbacks[func.__name__] = func

    @property
    def unread_messages(self) -> List[UnreadMessage]:
        """Returns the list of unread messages in the conversations page.

        #### Returns
            * List[UnreadMessage]: List of unread messages.
        """

        return [UnreadMessage(self, element) for element in self.driver.find_elements(By.CSS_SELECTOR, Sorce.UNREAD_CONVERSATIONS)]


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

    def _on_message(self) -> None:
        """Checks for new messages and calls the on_message callback"""

        last_check = self.unread_messages

        while True:
            if self._threads["on_message"].stopped():
                break

            if not self._callbacks["on_message"]:
                continue

            try:
                unread = self.unread_messages
            except StaleElementReferenceException:
                continue

            for chat in unread:
                if chat not in last_check and chat.message is not None:
                    self._callbacks["on_message"](chat)

            last_check = unread
            sleep(1) # Wait 1 second before checking again

    def open(self, chat: str) -> (Chat | Group | None):
        open(self, chat)

    def logout(self):
        logout(self.driver)

    def close(self):
        self.driver.quit()

# Usage Example:
# You can create an instance of Demon and use its methods to interact with WhatsApp Web.
# Make sure to call close() when you're done to close the browser.
