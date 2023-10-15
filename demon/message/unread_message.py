from __future__ import annotations
"""
🔔 Enchanted Unread Chat 📩

Behold, a chat cloaked in the mystique of unread messages, a realm of secrets and surprises in WhatsApp! 🪄📜 Do not seek to awaken it directly; invoke the 'whatsapp_whatsapp_api.demon.unread_messages' spell instead. 🧙‍♂️🔮

This class unveils the tales of unread chats, their names, the count of their unread scrolls, and the echoes of their last messages. A world of digital mysteries awaits! 🌟📩

### 🌠 Properties
- **name** (str): The magical name of the unread chat, a title that hints at the untold. 🌌📜
- **count** (int): The count of unread messages, a measure of the secrets hidden within. 🔢🔐
- **message** (str): The last message, a whisper of the chat's lingering voice. 💬🌟
"""



from dataclasses import dataclass, field
from typing import List, Literal

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from .. import whatsapp_api
from .. import chat
from ..utils import *

@dataclass(init=False)
class UnreadMessage:
  _whatsapp: whatsapp_api.Demon = field(repr=False)
  _element: WebElement = field(repr=False)
  name: str
  count: int
  message: str

  def __init__(self, _whatsapp: whatsapp_api.Demon, _element: WebElement) -> None:
        self._whatsapp = _whatsapp
        self._element = _element

        self.name = _element.find_element(By.CSS_SELECTOR, Sorce.UNREAD_TITLE).get_attribute("title")
        self.count = int(_element.find_element(By.CSS_SELECTOR, Sorce.UNREAD_BADGE).text) or 1

        try:
            self.message = _element.find_element(By.CSS_SELECTOR, Sorce.UNREAD_LAST_MESSAGE).get_attribute("title")
            self.message = self.message[1:-1]
        except NoSuchElementException:
            self.message = None

  def reply(self, 
            message: str, 
            attatchments: List[str] = None, 
            type: Literal["auto", "document", "midia", "contact"] = "auto"
    ) -> chat.Chat | chat.Group:
        """Reply to the unread chat.

        #### Arguments
            * message (str): The message to reply with.
            * attatchments (List[str], optional): The attatchments to reply with. Defaults to None.
            * type (Literal["auto", "document", "midia", "contact"], optional): The type of the attatchments. Defaults to "auto".

        #### Returns
            * Chat | Group: The chat or group that the message was sent to.
        """

        chat = self._whatsapp.open(self.name)
        chat.send(message, attatchments, type)

        return chat



