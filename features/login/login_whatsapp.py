from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import qrcode

def login_whatsapp(driver):
    try:
        # Open WhatsApp Web
        driver.get("https://web.whatsapp.com/")

        # Wait for the QR code to be scanned by the user
        qr_code_element = WebDriverWait(driver, 600).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div/div[1]/div[2]/div/div[2]'))
        )
        
        # Get the QR code image source
        qr_code_image_src = qr_code_element.get_attribute("src")

        # Generate a QR code and display it in the terminal
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_code_image_src)
        qr.make(fit=True)

        qr_code = qr.make_image(fill_color="black", back_color="white")

        # Display the QR code in the terminal
        print(qr_code.terminal(module_color="black", background="white"))

        print("Scan the QR code to log in to WhatsApp Web.")
        
        # Wait for the user to scan the QR code manually
        WebDriverWait(driver, 600).until(
            EC.url_contains("web.whatsapp.com")
        )
        
        print("Successfully logged in to WhatsApp Web!")

    except TimeoutException:
        print("QR code scan timed out. Please try again.")
