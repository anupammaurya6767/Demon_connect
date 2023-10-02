# send_message.py

from selenium.webdriver.common.keys import Keys
from utils.helpers import find_element_with_retry

def send_text_message(driver, contact_name, message):
    """
    Send a text message to a contact or group on WhatsApp Web.

    :param driver: WebDriver instance
    :param contact_name: Name of the contact or group
    :param message: The text message to send
    :return: True if the message is sent successfully, False otherwise
    """
    # Find and click on the contact or group
    contact_element = find_element_with_retry(driver, f"//span[@title='{contact_name}']")
    if contact_element:
        contact_element.click()

        # Find the message input box and send the message
        message_box = find_element_with_retry(driver, "//div[@class='_2S1VP copyable-text selectable-text']")
        if message_box:
            message_box.click()
            message_box.send_keys(message)
            message_box.send_keys(Keys.RETURN)
            return True

    return False
# send_message.py

from selenium.webdriver.common.keys import Keys
from utils.helpers import find_element_with_retry

def send_text_message(driver, contact_name, message):
    """
    Send a text message to a contact or group on WhatsApp Web.

    :param driver: WebDriver instance
    :param contact_name: Name of the contact or group
    :param message: The text message to send
    :return: True if the message is sent successfully, False otherwise
    """
    # Find and click on the contact or group
    contact_element = find_element_with_retry(driver, f"//span[@title='{contact_name}']")
    if contact_element:
        contact_element.click()

        # Find the message input box and send the message
        message_box = find_element_with_retry(driver, "//div[@class='_2S1VP copyable-text selectable-text']")
        if message_box:
            message_box.click()
            message_box.send_keys(message)
            message_box.send_keys(Keys.RETURN)
            return True

    return False
