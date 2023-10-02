# send_video.py

import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from utils.helpers import find_element_with_retry

def send_video(driver, contact_name, video_path):
    """
    Send a video to a contact or group on WhatsApp Web.

    :param driver: WebDriver instance
    :param contact_name: Name of the contact or group
    :param video_path: Path to the video file to send
    :return: True if the video is sent successfully, False otherwise
    """
    # Find and click on the contact or group
    contact_element = find_element_with_retry(driver, f"//span[@title='{contact_name}']")
    if contact_element:
        contact_element.click()

        # Find the attachment button and click it to open the menu
        attachment_button = find_element_with_retry(driver, "//div[@title='Attach']")
        if attachment_button:
            attachment_button.click()

            # Find and click on the 'Photo & Video Library' option
            photo_video_option = find_element_with_retry(driver, "//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']")
            if photo_video_option:
                photo_video_option.send_keys(video_path)
                time.sleep(2)  # Wait for the video to upload
                send_button = find_element_with_retry(driver, "//span[@data-icon='send']")
                if send_button:
                    send_button.click()
                    return True

    return False
