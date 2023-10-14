from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def send_group_message(driver, group_name, message):
    try:
        # Find the search input box to locate the group
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@id="side"]/div[1]/div/label/div/div[2]'))
        )
        search_box.clear()
        search_box.send_keys(group_name)
        search_box.send_keys(Keys.ENTER)


        #finding the name of the group from the list
        name_find = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="_21S-L"]/span'))
        )
        if name_find.get_attribute("title") == contact_name:
            name_find.click()


        # Locate the message input box
        message_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="to2l77zo gfz4du6o ag5g9lrv bze30y65 kao4egtt"]/p'))
        )
        message_box.click()
        
        # Type your message
        message_box.send_keys(message)

        # Send the message
        message_box.send_keys(Keys.ENTER)

        print(f"Message sent to group {group_name}: {message}")


                #now we are verifing if the message is sent in the group or not 
        
        #finding the last msg from the message container
        latest_message = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'//*[@id="main"]/div[2]/div/div[2]/div[3]/div[34]/div/div')))
        #verifing if the message is sent or not
        double_tick = WebDriverWait(latest_message,20).until(EC.presence_of_element_located((By.XPATH,'//*[@id="main"]/div[2]/div/div[2]/div[3]/div[34]/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div')))

        if double_tick:
            print(f"message sent successfully to {contact_name}")
        else:
            print(f"failed to send a message to {contact_name}")
            

    except Exception as e:
        print(f"An error occurred while sending the message: {str(e)}")

# Usage Example:
# Create a WebDriver instance and log in to WhatsApp Web
# group_name = "Your Group Name"  # Replace with the name of your group
# message = "Hello, this is a test message!"
# send_message(driver, group_name, message)

# Don't forget to handle login and initialize the WebDriver before using this function.
