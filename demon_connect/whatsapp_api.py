# api/whatsapp_api.py
from __future__ import annotations
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from demon_connect.features.login.login_whatsapp import login_whatsapp
from demon_connect.features.send.send_message import send_message
from demon_connect.features.send.send_image import send_image
from demon_connect.features.send.send_video import send_video
from demon_connect.features.tagall.tagall import tag_all
from demon_connect.features.extras.fetch_all_unread_chats import fetch_all_unread_chats
from demon_connect.features.extras.get_list_of_messages import get_list_of_messages
from demon_connect.features.send.send_file import send_file
from demon_connect.features.logout.logout import logout
from typing import Optional
from pathlib import Path
from demon_connect.features.extras.get_list_of_messages import get_list_of_messages
from typing import Dict, List, Callable
from time import sleep
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .utils import *
from .chat import *
from .message import *

class Demon:
    driver: webdriver.Chrome

    _timeout: int
    _visible: bool
    _data_path: str
    _chrome_options: Options

    def __init__(self, timeout: int = 60, visible: bool = True, data_path: str = None, chrome_options: Options = None) -> None:
        self._timeout = timeout
        self._visible = visible
        self._data_path = data_path
        self._chrome_options = chrome_options

    _callbacks: Dict[str, Callable] = {
        "on_ready": None,
        "on_message": None
    }
    _threads: Dict[str, MyThread] = {
        "on_message": None
    }

     
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

    def _search_chat(self, chat: str) -> WebElement:
        search = self.driver.find_element(By.CSS_SELECTOR, Sorce.SEARCH_BAR)
        send_keys_slowly(search, chat)
        sleep(10)
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, Sorce.SEARCH_BAR_CLEAR))
        # )

        return search

    def _clear_search_bar(self) -> None:
        self.driver.find_element(By.CSS_SELECTOR, Sorce.SEARCH_BAR_CLEAR).click()
        self.driver.find_element(By.CSS_SELECTOR, Sorce.BACK_CHAT).click()

    def open(self, chat: str) -> (Chat | Group | None):
        """Opens a chat with the specified name or phone number

        #### Arguments
            * chat (str): The name or phone number of the chat to open

        #### Returns
            * (Chat | Group | None): The chat with the specified name or phone number. None if the chat wasn't found
        """

        if not self._is_loaded():
            raise Exception("Something went wrong while loading WhatsApp web.")

        if phone_number_regex.match(chat):
            # Remove all the non-numeric characters
            phone = "".join(filter(str.isdigit, chat))

            self.driver.get(f"https://web.whatsapp.com/send?phone={phone}")
            WebDriverWait(self.driver, 5).until(lambda driver: self._is_loaded())
        else:
            # Close the menu and the current chat
            ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
            WebDriverWait(self.driver, 5).until(lambda driver: not self._is_animating())
            ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()

            # Search for the chat
            search = self._search_chat(chat)
            search.send_keys(Keys.ENTER)

            self._clear_search_bar()

        # Open the chat info
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, Sorce.CONVERSATION_HEADER))
            )
            self.driver.find_element(By.CSS_SELECTOR, Sorce.CONVERSATION_HEADER).click()
        except TimeoutException:
            return None

        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, Sorce.INFO_DRAWER_BODY)))

        if element_exists(self.driver, By.CSS_SELECTOR, Sorce.GROUP_INFO_HEADER):
            return Group(self)

        return Chat(self)
    
    @property
    def unread_messages(self) -> List[UnreadMessage]:
        """Returns the list of unread messages in the conversations page.

        #### Returns
            * List[UnreadMessage]: List of unread messages.
        """

        return [UnreadMessage(self, element) for element in self.driver.find_elements(By.CSS_SELECTOR, Sorce.UNREAD_CONVERSATIONS)]

    def login(self):
        login_whatsapp(self)

    def send_message(self,contact_name, message):
        send_message(self.driver,contact_name, message)

    def delete_message(self, group_name, message):
        #delete_message(self.driver, group_name, message)
        raise NotImplemented

    def _add_thread(self, name: str, target: Callable, daemon: bool = True) -> None:
        self._threads[name] = MyThread(target=target, daemon=daemon)

    def _start_thread(self, name: str) -> None:
        self._threads[name].start()

    def _stop_thread(self, name: str) -> None:
        self._threads[name].stop()
        self._threads.pop(name)
    
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

    def _on_ready(self) -> None:
        """Calls the on_ready callback when the page is loaded."""

        if not self._callbacks["on_ready"]:
            return

        self._callbacks["on_ready"]()

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

    def logout(self):
        logout(self.driver)

    def close(self):
        self.driver.quit()

# Usage Example:
# You can create an instance of Demon and use its methods to interact with WhatsApp Web.
# Make sure to call close() when you're done to close the browser.
