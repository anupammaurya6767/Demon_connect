from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def tag_all(driver, group_name):
     #finding the contact we have to send msg to -
        #finding the search box for the contacts
        time.sleep(2)
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="to2l77zo gfz4du6o ag5g9lrv bze30y65 kao4egtt qh0vvdkp"]/p'))
        )
        search_box.clear()
        search_box.send_keys(group_name)
        search_box.send_keys(Keys.ENTER)

        
        #finding the name of the contact from the list after searching 
        name_find = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="_21S-L"]/span'))
        )
        if name_find.get_attribute("title") == group_name:
            name_find.click()

        

    # Wait for the chat to load
        time.sleep(2)

        # Find the message input box
        message_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="to2l77zo gfz4du6o ag5g9lrv bze30y65 kao4egtt"]/p'))
        )

        message_box.click()
        message_box.clear()
        # Find all the <span> elements that match the specified attributes
        time.sleep(10)
        span_elements = driver.find_elements(By.CSS_SELECTOR,'span[title][aria-label].selectable-text')
        
        segregated_items = []
        # Loop through the span elements and print their text content
        for span in span_elements:
            items = span.text.split(',')
        # Remove leading and trailing spaces from each item and add it to the segregated_items list
            segregated_items.extend([item.strip() for item in items])

        # Remove the "You" element from the list
        segregated_items = [item for item in segregated_items if item != "You"]


    # Now, the 'segregated_items' list contains all items separated by ','
        for item in segregated_items:
            member_name = item
            message_box.send_keys(f"@{member_name}")  # Mention the member
            time.sleep(0.5)
            message_box.send_keys(Keys.ENTER)
            time.sleep(0.5)  # Add a delay to avoid rate limiting (adjust as needed) 
    
        # Send the message
        message_box.send_keys(Keys.ENTER)
        
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

