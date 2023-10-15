from typing import List, Literal
import re
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from threading import Thread, Event, Lock
import mimetypes

class MyThread(Thread):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._stop_event = Event()
        self.lock = Lock()  # Lock to ensure thread safety for WebDriver operations

    def stop(self) -> None:
        self._stop_event.set()

    def stopped(self) -> bool:
        return self._stop_event.is_set()

    @staticmethod
    def get_attachment_type(attachment: str) -> str:
        if "." not in attachment:
            return "contact"

        mime = mimetypes.guess_type(attachment)[0]

        if mime is None:
            return "document"
        elif mime.split("/")[0] in ["image", "video", "audio"]:
            return "media"
        else:
            return "document"


phone_number_regex = re.compile(r'\+?\d{1,3}[-.\s]?\d{1,14}[-.\s]?\d{1,14}[-.\s]?\d{1,14}')
url_regex = re.compile(r'(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z0-9]{2,}(\.[a-zA-Z0-9]{2,})(\.[a-zA-Z0-9]{2,})?')