# features/delete/delete_message.py
from __future__ import annotations
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

def delete_message(driver, group_name, message):
    try:
        action = ActionChains(driver)
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="to2l77zo gfz4du6o ag5g9lrv bze30y65 kao4egtt qh0vvdkp"]/p'))
        )
        search_box.clear()
        search_box.send_keys(group_name)
        search_box.send_keys(Keys.ENTER)

        name_find = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="_21S-L"]/span'))
        )
        if name_find.get_attribute("title") == group_name:
            name_find.click()

        # locate the sent message and delete it
        sent_message_list = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, f'//*[@id="main"]/div[2]/div/div[2]/div[3]'))
        )

        for msg in sent_message_list:
            print(msg.text)
            if message in msg.text:
                action.move_to_element(msg).perform()
                sleep(5)
                dropdown = WebDriverWait(driver,10).until(
                    EC.presence_of_element_located((By.XPATH,'//*[@id="main"]/div[2]/div/div[2]/div[3]/div[128]/div/div/div[1]/div[1]/span[2]/div/div')))

                dropdown.click()

                delete_button = WebDriverWait(driver ,10).until(
                    EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/span[4]/div/ul/div/li[5]/div'))
                )

                delete_button.click()

                delete_for_everyone = WebDriverWait(driver ,10).until(
                    EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/button[1]'))
                )

                delete_for_everyone.click()

                ok_button = WebDriverWait(driver,10).until(
                    EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/button[2]/div/div'))
                    )

                ok_button.click()
                print(f"Message deleted in group {group_name}: {message}")
            else:
                print("failed to delete msg")



    except Exception as e:
        print(f"An error occurred while deleting the message: {str(e)}")

