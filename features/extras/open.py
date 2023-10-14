from utils.threads import *
from features.chat.chat import Chat
from utils.exceptions import *
from utils.sorce import Sorce
from features.chat.group import Group
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from utils.handler import *
from selenium.webdriver.support import expected_conditions as EC

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
