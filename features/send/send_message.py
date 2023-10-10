# features/send/send_message.py

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
def send_message(driver, contact_name, message, _2vDPL=None):
    try:

        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="to2l77zo gfz4du6o ag5g9lrv bze30y65 kao4egtt qh0vvdkp"]/p'))
        )
        search_box.clear()
        search_box.send_keys(contact_name)
        search_box.send_keys(Keys.ENTER)

        name_find = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="_21S-L"]/span'))
        )
        if name_find.get_attribute("title") == contact_name:
            name_find.click()
        # Locate the input box
        # list_msgs = driver.find_elements(By.XPATH,'//*[@id="main"]/div[2]/div/div[2]/div[3]/div')
        input_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="to2l77zo gfz4du6o ag5g9lrv bze30y65 kao4egtt"]/p'))
        )
        input_box.click()
        # input_box = driver.find_element_by_xpath(
        #     '//div[@class="to2l77zo gfz4du6o ag5g9lrv bze30y65 kao4egtt"]/p'
        # )
        # input_box = driver.find_element("By.XPATH,'//div[@class = 'to2l77zo gfz4du6o ag5g9lrv bze30y65 kao4egtt qh0vvdkp']'")
        # Clear the input box and send the message
        input_box.clear()
        input_box.send_keys(message)
        input_box.send_keys(Keys.ENTER)

        # sleep(10)




        # list_msgs_new = driver.find_elements(By.XPATH,'//*[@id="main"]/div[2]/div/div[2]/div[3]/div')
        # print(list_msgs_new[-1])
        latest_message = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'//*[@id="main"]/div[2]/div/div[2]/div[3]/div[34]/div/div')))

        double_tick = WebDriverWait(latest_message,20).until(EC.presence_of_element_located((By.XPATH,'//*[@id="main"]/div[2]/div/div[2]/div[3]/div[34]/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div')))

        if double_tick:
            print(f"message sent successfully to {contact_name}")
        else:
            print("not sent")

    except Exception as e:
        print(f"Failed to send a message to {contact_name}: {str(e)}")

# Usage Example:
# send_message(driver, "Contact Name", "Hello, this is a test message!")
