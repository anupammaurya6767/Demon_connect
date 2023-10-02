# sample_usage.py

from selenium import webdriver
from features.login.login_whatsapp import WhatsAppLogin
from features.send.send_message import send_text_message
from features.send.send_image import send_image
from features.send.send_video import send_video
from features.receive.receive_message import receive_messages

def main():
    try:
        # Initialize the Chrome WebDriver (you may need to specify the driver path)
        driver = webdriver.Chrome(executable_path="path/to/chromedriver.exe")

        # Initialize WhatsAppLogin and log in
        whatsapp_login = WhatsAppLogin(driver)
        whatsapp_login.login()

        # Example: Send a text message
        send_text_message(driver, "Contact Name", "Hello, this is a test message!")

        # Example: Send an image
        send_image(driver, "Contact Name", "path/to/image.jpg")

        # Example: Send a video
        send_video(driver, "Contact Name", "path/to/video.mp4")

        # Example: Receive and process messages (this should run in a separate thread)
        # Note: You may need to implement more advanced logic for message handling
        receive_messages(driver)

    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        # Log out and close the browser
        whatsapp_login.logout()

if __name__ == "__main__":
    main()
