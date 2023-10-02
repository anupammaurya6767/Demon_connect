# features/receive/receive_message.py

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def receive_messages(driver):
    try:
        # Set a maximum timeout for message checking
        timeout = 300  # 5 minutes (adjust as needed)

        while True:
            # Wait for the chat container to load
            chat_container = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="main"]/div[3]/div/div/div[3]/div')
                )
            )

            # Get the list of messages
            messages = chat_container.find_elements(By.XPATH, './/div[contains(@class, "message")]')

            # Process each message
            for message in messages:
                sender_name = message.find_element(By.XPATH, './/span[@class="bP"]')
                message_text = message.find_element(By.XPATH, './/span[@class="selectable-text"]').text

                print(f"Received message from {sender_name.text}: {message_text}")

            # Check for new messages every 5 seconds
            time.sleep(5)

    except KeyboardInterrupt:
        print("Receive message loop terminated.")

# Usage Example:
# Start receiving and processing messages in a separate thread or process
