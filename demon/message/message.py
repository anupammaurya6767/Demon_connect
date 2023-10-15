from __future__ import annotations

import datefinder
from datetime import datetime
from dataclasses import dataclass, field
from typing import Any, List, Literal

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from ..utils import *
from .. import chat
from .. import whatsapp_api


@dataclass(init=False)
class Message:
    """
💌 Magical Message Utility Class 🚀

This, my fellow wanderer, is the secret scroll for managing messages in the realm of WhatsApp! 🧙‍♂️🪄 Do not attempt to conjure it directly; use the 'whatsapp_whatsapp_api.demon.open' incantation. 📱💬

This enchanting class is your key to deciphering the language of messages, from authors and timestamps to attachments and the mysteries of forwarding and replies.

May your messages be swift and your adventures legendary! 🌟📜

### 📜 Properties
- **author** (str): The scribe of the message, weaving tales in the digital tapestry. 🧙‍♀️📜
- **content** (str): The mystical content of the message, words that travel through the aether. 🪄✨
- **timestamp** (datetime): The timestamp, a glimpse into the hourglass of time. 🕰️🌌
- **chat** (Chat | Group): The sacred chat where the message found its voice, a realm of connections. 🏰👥
- **attachments** (List[Any]): The attachments, treasures bound to the message, the stuff of legends. 📦🌟
- **is_forwarded** (bool): The mark of messages that have journeyed through the winds of sharing. 💌🌬️
- **is_reply** (bool): The sign of messages in conversation, echoes in the grand narrative of chats. 💬🌊
"""


    _element: WebElement = field(repr=False)
    _whatsapp: whatsapp_api.Demon = field(repr=False)
    
    chat: chat.Chat | chat.Group = None
    author: str = None
    content: str = None
    timestamp: datetime = None
    attatchments: List[Any] = None
    is_forwarded: bool = False
    is_reply: bool = False
    
    def __init__(self, _whatsapp: whatsapp_api.Demon, _element: WebElement, chat: chat.Chat | chat.Group) -> None:
        self._whatsapp = _whatsapp
        self._element = _element
        self.chat = chat

        # TODO: Add support for attatchments.
        container = _element.find_element(By.CSS_SELECTOR, Sorce.MESSAGE_CONTAINER)

        self.author = container.find_element(By.CSS_SELECTOR, Sorce.MESSAGE_AUTHOR).get_attribute("aria-label")[:-1]

        if content := find_element_if_exists(container, By.CSS_SELECTOR, Sorce.MESSAGE_CONTENT):
            self.content = emoji_to_text(content)

        if info := find_element_if_exists(container, By.CSS_SELECTOR, Sorce.MESSAGE_INFO):
            dates = list(datefinder.find_dates(info.text))
            self.timestamp = dates[0] if dates else datetime(1900, 1, 1, 0, 0)
        else:
            self.timestamp = list(datefinder.find_dates(container.find_element(By.CSS_SELECTOR, Sorce.MESSAGE_META).text))[0]
            self.timestamp = self.timestamp.replace(year=1900, month=1, day=1)

        self.is_forwarded = element_exists(container, By.CSS_SELECTOR, Sorce.MESSAGE_FORWARDED)
        self.is_reply = element_exists(container, By.CSS_SELECTOR, Sorce.MESSAGE_QUOTE)

    def __eq__(self, other: Message) -> bool:
        if not isinstance(other, Message):
            return False

        return self.content == other.content and self.timestamp == other.timestamp and self.author == other.author

    def reply(self,
              message: str = None,
              attatchments: List[str] = None,
              type: Literal["auto", "document", "midia", "contact"] = "auto"
        ) -> None:
        """Replies to the message.

        #### Arguments
            * message (str, optional): The message to send. Defaults to None.
            * attatchments (List[Any], optional): The attatchments to send. Defaults to None.
            * type (Literal["auto", "document", "midia", "contact"], optional): The type of the attatchments. Defaults to "auto".
            If the type is specified, all the attatchments must be of the same type.
        """

        action = ActionChains(self._whatsapp.driver)
        action.double_click(self._element).perform()

        self.chat.send(message, attatchments, type)
