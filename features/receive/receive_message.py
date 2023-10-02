# receive_message.py

import time
from selenium.webdriver.common.by import By
from utils.helpers import find_element_with_retry

def receive_messages(driver):
    """
    Receive and process incoming messages on WhatsApp Web.

    :param driver: WebDriver instance
    """
    while True:
        try:
            # Find all message elements in the chat
            message_elements = driver.find_elements(By.XPATH, "//div[@class='copyable-text']")

            for message_element in message_elements:
                message_text = message_element.text
                # Process the message text as needed (e.g., reply, store, analyze)

            # Wait briefly before checking for new messages again
            time.sleep(2)
        except Exception as e:
            print(f"An error occurred while receiving messages: {str(e)}")

# Example usage
if __name__ == "__main__":
    from selenium import webdriver

    # Initialize the WebDriver (e.g., Chrome)
    driver = webdriver.Chrome()
    driver.get("https://web.whatsapp.com/")

    # Wait for the user to scan the QR code manually for 10 seconds
    input("Scan the QR code manually and press Enter after scanning...")

    # Call the receive_messages function to start monitoring messages
    receive_messages(driver)
