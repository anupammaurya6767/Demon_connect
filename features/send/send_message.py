# features/send/send_message.py

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def send_message(driver, contact_name, message, _2vDPL=None):
    try:
        #finding the contact we have to send msg to -
        #finding the search box for the contacts
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="to2l77zo gfz4du6o ag5g9lrv bze30y65 kao4egtt qh0vvdkp"]/p'))
        )
        search_box.clear()
        search_box.send_keys(contact_name)
        search_box.send_keys(Keys.ENTER)

        
        #finding the name of the contact from the list after searching 
        name_find = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="_21S-L"]/span'))
        )
        if name_find.get_attribute("title") == contact_name:
            name_find.click()

        
        # Locate the input box
        input_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="to2l77zo gfz4du6o ag5g9lrv bze30y65 kao4egtt"]/p'))
        )
        input_box.click()

        # Clear the input box and send the message
        input_box.clear()
        input_box.send_keys(message)
        input_box.send_keys(Keys.ENTER)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="main"]//*[@data-icon="msg-time"]')
            )
        )
        WebDriverWait(driver, 10).until_not(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="main"]//*[@data-icon="msg-time"]')
            )
        )
        print("✅ Message sent successfully.")

    except Exception as e:
        print(f"Failed to send a message to {contact_name}: {str(e)}")

# Usage Example:
# send_message(driver, "Contact Name", "Hello, this is a test message!")
