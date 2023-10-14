from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.constants import WHATSAPP_WEB_URL
from utils.sorce import Sorce
from utils.handler import *
# import qrcode_terminal
from qrcode import QRCode
from time import sleep
import os

def login_whatsapp(self):
    self.driver.get(WHATSAPP_WEB_URL)
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
    sleep(1) # Sometimes the page is not loaded correctly

    # Create the threads
    self._add_thread("on_ready", self._on_ready)
    self._add_thread("on_message", self._on_message)

    # Start the threads
    for thread in self._threads.values():
        thread.start()

    return self
