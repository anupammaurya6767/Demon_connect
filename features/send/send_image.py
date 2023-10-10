# features/send/send_image.py

from selenium.webdriver.common.keys import Keys

def send_image(driver, contact_name, image_path):
    try:
        # Locate the attachment button
        attachment_button = driver.find_element_by_xpath(
            '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div'
        )
        attachment_button.click()

        # Select the photo/video option
        photo_video_option = driver.find_element_by_xpath(
            '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[2]/li'
        )
        photo_video_option.send_keys(image_path)

        # Wait for the image to be attached
        driver.implicitly_wait(5)

        # Click the send button
        send_button = driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div'
        )
        send_button.click()

        print(f"Image sent to {contact_name}: {image_path}")

    except Exception as e:
        print(f"Failed to send an image to {contact_name}: {str(e)}")

# Usage Example:
# send_image(driver, "Contact Name", "path/to/image.jpg")
