from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.constants import WHATSAPP_WEB_URL
import qrcode_terminal
from time import sleep

def login_whatsapp(driver):
    driver.get(WHATSAPP_WEB_URL)
    try:

        WebDriverWait(driver,20).until(
                EC.presence_of_element_located((By.XPATH,"//div[@class='_2Ts6i _3RGKj']/header"))            #finding the whatsapp header element if the whatsapp is already logged in 
            )
        
        print("Successfully logged in to WhatsApp Web!")
        
    except:

        try:
            # Open WhatsApp Web

            WebDriverWait(driver,50).until(
                EC.presence_of_element_located((By.XPATH,'//div[@class="_10aH-"]/span'))
            )
            logged_in = False

            qr_code_element = WebDriverWait(driver, 600).until(                                    
                EC.presence_of_element_located((By.XPATH, '//div[@class="_19vUU"]'))
            )

            print("Scan the QR code to log in to WhatsApp Web.")

            while True:
                # Wait for the QR code to be scanned by the user
                try:
                # Get the QR code image source
                    qr_code_image_dataref = qr_code_element.get_attribute("data-ref")
                    qrcode_terminal.draw(qr_code_image_dataref)                #printing the qr in the terminal so that the user can scan from terminal directly
                except:
                    pass
                # Generate and display the QR code in the terminal

                try:
                    header_element = driver.find_element(By.XPATH, "//div[@class='_2Ts6i _3RGKj']/header")
                    print("Successfully logged in to WhatsApp Web!")
                    return  # Exit the function since the element is found
                except:
                    pass

                # Sleep for a few seconds before checking the QR code again
                sleep(20)

        except TimeoutException:
            print("QR code scan timed out. Please try again.")

