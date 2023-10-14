from __future__ import annotations

import requests
from PIL import Image
from PIL.JpegImagePlugin import JpegImageFile
from dataclasses import dataclass, field
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

from features import chat
from api.whatsapp_api import Demon
from utils.exceptions import *
from utils.handler import *

@dataclass(init=False)
class Chat(chat.Conversation):
    """A chat in WhatsApp. Should not be initialized directly, use `whatsappy.Whatsapp.open` instead.

    #### Properties
        * name (str): The name of the chat.
        * number (str): The number of the chat.
        * about (str): The about of the chat.
        * profile_picture (JpegImageFile): The profile picture of the chat.
        * starred_messages (List[str]): The starred messages of the chat.
    """

    _whatsapp: Demon = field(repr=False)

    name: str
    number: str
    about: str
    profile_picture: JpegImageFile

    def __init__(self, _whatsapp: Demon) -> None:
        super().__init__(_whatsapp)

        driver = self._whatsapp.driver

        info = driver.find_elements(By.CSS_SELECTOR, '#app > div > div > div:nth-child(6) span[dir="auto"].copyable-text.selectable-text')

        self.name = emoji_to_text(info[0])
        self.number = info[1].text
        self.about = info[2].get_attribute("title") if len(info) > 2 else None

        if self.number.startswith("~"):
            self.name, self.number = self.number[1:], self.name

        if self.name == self.number:
            self.number = None # Official bussiness accounts

        if element_exists(driver, By.CSS_SELECTOR, '#app > div > div > div:nth-child(6) span[data-icon="default-user"]'):
            self.profile_picture = None
        else:
            pfp_url = driver.find_element(By.CSS_SELECTOR, '#app > div > div > div:nth-child(6) section > div img').get_attribute("src")
            self.profile_picture = Image.open(requests.get(pfp_url, stream=True).raw)

        self._start_threads()

    @property
    def is_blocked(self) -> bool:
        """Returns whether the chat is blocked or not."""

        if self._whatsapp.current_chat != self.name:
            raise NotSelectedException(f"The chat \"{self.name}\" is not selected.")

        return element_exists(self._whatsapp.driver, By.CSS_SELECTOR, '#app > div > div > div:nth-child(6) div[title="Unblock "]')
            
    def block(self) -> None:
        """Blocks the chat."""

        if self._whatsapp.current_chat != self.name:
            raise NotSelectedException(f"The chat \"{self.name}\" is not selected.")

        if self.is_blocked:
            return

        driver = self._whatsapp.driver
        driver.find_element(By.CSS_SELECTOR, '#app > div > div > div:nth-child(6) div[title="Block "]').click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-animate-modal-popup="true"]')))

        driver.find_element(By.CSS_SELECTOR, 'div[data-animate-modal-popup="true"] button:last-child').click()

        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, 'div[data-animate-modal-popup="true"]')))

    def unblock(self) -> None:
        """Unblocks the chat."""

        if self._whatsapp.current_chat != self.name:
            raise NotSelectedException(f"The chat \"{self.name}\" is not selected.")

        if not self.is_blocked:
            return

        driver = self._whatsapp.driver
        driver.find_element(By.CSS_SELECTOR, '#app > div > div > div:nth-child(6) div[title="Unblock "]').click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-animate-modal-popup="true"]')))

        driver.find_element(By.CSS_SELECTOR,'div[data-animate-modal-popup="true"] button:last-child').click()

        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, 'div[data-animate-modal-popup="true"]')))

    def delete(self) -> None:
        """Deletes the chat."""

        if self._whatsapp.current_chat != self.name:
            raise NotSelectedException(f"The chat \"{self.name}\" is not selected.")

        driver = self._whatsapp.driver
        driver.find_element(By.CSS_SELECTOR, '#app > div > div > div:nth-child(6) div[title="Delete chat"]').click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-animate-modal-popup="true"] button:last-child')))

        driver.find_element(By.CSS_SELECTOR,'div[data-animate-modal-popup="true"] button:last-child').click()

        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, 'div[data-animate-modal-popup="true"]')))