# features/send/send_message.py

from selenium.webdriver.common.keys import Keys

def send_message(driver, contact_name, message):
    try:
        # Locate the input box
        input_box = driver.find_element_by_xpath(
            '//*[@id="main"]/footer/div/div/span[2]/div/div[2]/div/div/div'
        )

        # Clear the input box and send the message
        input_box.clear()
        input_box.send_keys(message)
        input_box.send_keys(Keys.ENTER)

        print(f"Message sent to {contact_name}: {message}")

    except Exception as e:
        print(f"Failed to send a message to {contact_name}: {str(e)}")

# Usage Example:
# send_message(driver, "Contact Name", "Hello, this is a test message!")
