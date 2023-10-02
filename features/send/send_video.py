# features/send/send_video.py

from selenium.webdriver.common.keys import Keys

def send_video(driver, contact_name, video_path):
    try:
        # Locate the attachment button
        attachment_button = driver.find_element_by_xpath(
            '//*[@id="main"]/footer/div/div/span[1]/div[1]/div/span'
        )
        attachment_button.click()

        # Select the photo/video option
        photo_video_option = driver.find_element_by_xpath(
            '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]'
        )
        photo_video_option.send_keys(video_path)

        # Wait for the video to be attached
        driver.implicitly_wait(5)

        # Click the send button
        send_button = driver.find_element_by_xpath(
            '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div'
        )
        send_button.click()

        print(f"Video sent to {contact_name}: {video_path}")

    except Exception as e:
        print(f"Failed to send a video to {contact_name}: {str(e)}")

# Usage Example:
# send_video(driver, "Contact Name", "path/to/video.mp4")
