from __future__ import annotations
"""
🌟 A Majestic WhatsApp Group 🏰

This, dear traveler, is not just any WhatsApp group; it's a realm of magic, conversation, and camaraderie! 🪄⚔️✨

Beware, for you must not summon it directly. Instead, wield the 'whatsapp_whatsapp_api.demon.open' spell. 🧙‍♂️🌌

### 🌈 Properties
- **subject** (str): The enchanting subject of the group, a beacon in the digital wilderness. 🌈
- **description** (str): The mystical description of the group, a tale waiting to be told. 📜
- **profile_picture** (JpegImageFile): The sacred profile picture of the group, a portal to another world. 🖼️
- **participants** (int): The noble count of participants in the group, each a hero in their own right. ⚔️👥
- **starred_messages** (List[str]): The constellation of starred messages, gems in the treasure trove of chats. 💎🌟
"""



import requests
from PIL import Image
from PIL.JpegImagePlugin import JpegImageFile
from dataclasses import dataclass, field
from typing import List
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from .. import chat
from .. import whatsapp_api
from ..utils import *

@dataclass(init=False)
class Group(chat.Conversation):
    _whatsapp: whatsapp_api.Demon = field(repr=False)
    
    name: str
    description: str
    participants: int
    profile_picture: JpegImageFile
    
    def __init__(self, _whatsapp: whatsapp_api.Demon) -> None:
        super().__init__(_whatsapp)
        
        driver = self._whatsapp.driver
        
        # Group name
        self.name = emoji_to_text(driver.find_element(By.CSS_SELECTOR, Sorce.GROUP_SUBJECT))

        # Group description
        if read_more_btn := find_element_if_exists(driver, By.CSS_SELECTOR, Sorce.GROUP_READ_MORE):
            read_more_btn.click()

        if description_element := find_element_if_exists(driver, By.CSS_SELECTOR, Sorce.GROUP_DESCRIPTION):
            self.description = description_element.text
        else:
            self.description = None

        # Wait for the group participants to load
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, Sorce.GROUP_PARTICIPANTS)))
        
        # Group participants
        self.participants = int(driver.find_element(By.CSS_SELECTOR, Sorce.GROUP_PARTICIPANTS).text.split()[0])

        # Group profile picture
        if not element_exists(driver, By.CSS_SELECTOR, Sorce.GROUP_DEFAULT_PIC):
            pfp_url = driver.find_element(By.CSS_SELECTOR, Sorce.CHAT_INFO_PIC).get_attribute("src")
            self.profile_picture = Image.open(requests.get(pfp_url, stream=True).raw)
        else:
            self.profile_picture = None

        self._start_threads()

    def leave(self, delete: bool = False) -> None:
        """Leaves the group.

        #### Arguments
            * delete (bool): Whether to delete the group or not.
        """

        if self._whatsapp.current_chat != self.name:
            raise NotSelectedException(f"The group \"{self.name}\" is not selected.")

        driver = self._whatsapp.driver
        driver.find_element(By.CSS_SELECTOR, Sorce.GROUP_LEAVE).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, Sorce.POPUP_CONFIRM)))

        driver.find_element(By.CSS_SELECTOR, Sorce.POPUP_CONFIRM).click()

        WebDriverWait(driver, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, Sorce.POPUP)))

        if delete:
            self.leave(delete=False)

    def is_admin(self, user: str) -> bool:
        """Checks if a user is an admin of the group.

        #### Arguments
            * user (str): The user to check.

        #### Returns
            * bool: Whether the user is an admin of the group or not.
        """
        
        driver = self._whatsapp.driver

        admin, _ = self._is_admin(user)    
        driver.find_element(By.CSS_SELECTOR, Sorce.CLOSE).click()

        return admin

    def promote(self, user: str) -> None:
        """Promotes a user to admin.

        #### Arguments
            * user (str): The user to promote.

        #### Raises
            * UserAlreadyAdminException: If the user is already an admin.
        """

        driver = self._whatsapp.driver

        admin = self._is_admin(user)
        if admin:
            driver.find_element(By.CSS_SELECTOR, Sorce.CLOSE).click()
            raise UserAlreadyAdminException(f"The user \"{user}\" is already an admin.")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, Sorce.GROUP_SEARCH_RESULT)))

        driver.find_element(By.CSS_SELECTOR, Sorce.GROUP_SEARCH_RESULT).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, Sorce.GROUP_PROMOTE_ADMIN)))

        driver.find_element(By.CSS_SELECTOR, Sorce.GROUP_PROMOTE_ADMIN).click()
        driver.find_element(By.CSS_SELECTOR, Sorce.CLOSE).click()

    def demote(self, user: str) -> None:
        """Demotes a user from admin.

        #### Arguments
            * user (str): The user to demote.

        #### Raises
            * UserNotAdminException: If the user is not an admin.
        """

        driver = self._whatsapp.driver

        admin = self._is_admin(user)
        if not admin:
            driver.find_element(By.CSS_SELECTOR, Sorce.CLOSE).click()
            raise UserNotAdminException(f"The user \"{user}\" is not an admin.")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, Sorce.GROUP_SEARCH_RESULT)))

        driver.find_element(By.CSS_SELECTOR, Sorce.GROUP_SEARCH_RESULT).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, Sorce.GROUP_DEMOTE_ADMIN)))

        driver.find_element(By.CSS_SELECTOR, Sorce.GROUP_DEMOTE_ADMIN).click()
        driver.find_element(By.CSS_SELECTOR, Sorce.CLOSE).click()

    def _is_admin(self, user: str) -> bool:
        if self._whatsapp.current_chat != self.name:
            raise NotSelectedException(f"The group \"{self.name}\" is not selected.")

        driver = self._whatsapp.driver

        if len(self._search_user(user)) == 0:
            raise UserNotFoundException(f"The user \"{user}\" was not found.")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, Sorce.GROUP_SEARCH_RESULT)))

        result = driver.find_element(By.CSS_SELECTOR, Sorce.GROUP_SEARCH_RESULT)

        try:
            return result.find_element(By.CSS_SELECTOR, Sorce.GROUP_ADMIN_BADGE).is_displayed()
        except NoSuchElementException:
            return False

    def _search_user(self, user: str) -> List[WebElement]:
        driver = self._whatsapp.driver
        driver.find_element(By.CSS_SELECTOR, Sorce.GROUP_SEARCH).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, Sorce.GROUP_SEARCH_INPUT)))

        search_box = driver.find_element(By.CSS_SELECTOR, Sorce.GROUP_SEARCH_INPUT)
        search_box.click()

        search_box.send_keys(user)

        return driver.find_elements(By.CSS_SELECTOR, Sorce.GROUP_SEARCH_RESULT)
