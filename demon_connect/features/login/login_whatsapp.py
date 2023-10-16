from __future__ import annotations
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from demon_connect.utils.constants import WHATSAPP_WEB_URL
from demon_connect.utils.sorce import Sorce
from demon_connect.utils.handler import *
from typing import Self
from selenium.webdriver.chrome.options import Options
from qrcode import QRCode
from time import sleep
import os

def login_whatsapp(self) -> Self:
        self._chrome_options = self._chrome_options or Options()
        self._chrome_options.add_argument("--start-maximized")

        if not self._visible:
            self._chrome_options.add_argument("--headless")
            self._chrome_options.add_argument("--window-size=1920,1080")

        if self._data_path:
            self._chrome_options.add_argument(f"--user-data-dir={self._data_path}")

        # Disable the logging
        self._chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

        # Open the browser
        self.driver = webdriver.Chrome(service=Service(), options=self._chrome_options)

        # Open the WhatsApp web page
        self.driver.get(WHATSAPP_WEB_URL)

        # Wait until the page is loaded
        WebDriverWait(self.driver, self._timeout).until(lambda driver: (
            element_exists(self.driver, By.CSS_SELECTOR, Sorce.QR_CODE) or
            element_exists(self.driver, By.CSS_SELECTOR, Sorce.SEARCH_BAR)
        ))

        qr_code = find_element_if_exists(self.driver, By.CSS_SELECTOR, Sorce.QR_CODE)

        if qr_code:
            if not self._visible:
                data_ref = qr_code.get_attribute("data-ref")

                os.system("cls||clear")

                qr = QRCode(version=1, border=2)
                qr.add_data(data_ref)
                qr.make(fit=True)
                qr.print_ascii(invert=True)

            print("Scan the QR code with your phone to log in.")

        WebDriverWait(self.driver, self._timeout).until(lambda driver: self._is_loaded())
        sleep(10) # Sometimes the page is not loaded correctly

        # Create the threads
        self._add_thread("on_ready", self._on_ready)
        self._add_thread("on_message", self._on_message)

        # Start the threads
        for thread in self._threads.values():
            thread.start()

        return self