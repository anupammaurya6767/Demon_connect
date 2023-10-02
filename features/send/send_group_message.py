from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def send_message(driver, group_name, message):
    try:
        # Find the search input box to locate the group
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@id="side"]/div[1]/div/label/div/div[2]'))
        )
        search_box.clear()
        search_box.send_keys(group_name)
        search_box.send_keys(Keys.ENTER)

        # Wait for the chat to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/header/div[2]/div[1]/div[1]/span'))
        )

        # Locate the message input box
        message_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'))
        )
        
        # Type your message
        message_box.send_keys(message)

        # Send the message
        message_box.send_keys(Keys.ENTER)

        print(f"Message sent to group {group_name}: {message}")

    except Exception as e:
        print(f"An error occurred while sending the message: {str(e)}")

# Usage Example:
# Create a WebDriver instance and log in to WhatsApp Web
# group_name = "Your Group Name"  # Replace with the name of your group
# message = "Hello, this is a test message!"
# send_message(driver, group_name, message)

# Don't forget to handle login and initialize the WebDriver before using this function.
