import os
from typing import Optional
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    NoSuchElementException,
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from demon_connect.features.extras.send_attachment import send_attachment
from demon_connect.features.extras.add_caption import add_caption
from demon_connect.features.extras.find_attachment import find_attachment
import time



def send_image(driver,contact_name, picture: Path, message: Optional[str] = None):
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

        filename = os.path.realpath(picture)
        find_attachment(driver)
        # Find the input element for the image
        imgButton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[1]/div/div/span/div/ul/div/div[2]/li/div/input',
                )
            )
        )
        imgButton.send_keys(filename)
        if message:
            # Add an optional message
            add_caption(driver,message, media_type="image")
        send_attachment(driver)
         # Wait for the pending clock icon to show and disappear
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
    except (NoSuchElementException, Exception) as bug:
        print(f"❌ Failed to send a message to {contact_name} - {bug}")
    finally:
        print("🏁 send_picture() finished running!")
