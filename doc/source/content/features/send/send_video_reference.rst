`send_video.py` Documentation
=============================

This module contains a function `send_video` that is responsible for sending a video to a target user in WhatsApp.

Function Signature
------------------

```python
def send_video(driver, contact_name, video: Path, message: Optional[str] = None)
```

Parameters
----------

- `driver`: WebDriver - The Selenium WebDriver instance that is used to interact with the WhatsApp Web page.
- `contact_name`: str - The name of the contact to whom the video should be sent.
- `video`: Path - The path to the video file that needs to be sent.
- `message`: Optional[str] - An optional message to include with the video (default: None).

Description
-----------

The `send_video` function sends a video file to a target user if the video size is less than 14MB. It performs the following steps:

1. Searches for the contact by entering the contact name in the search box.
2. Clicks on the contact name from the search results.
3. Checks if the video size is less than 14MB.
4. Finds the attachment button to upload the video.
5. Enters the video file path and adds an optional message if provided.
6. Sends the video attachment.
7. Waits for the pending clock icon to show and disappear, indicating that the message has been sent successfully.

Exceptions
----------

- `NoSuchElementException`: This exception is raised if any required element is not found on the WhatsApp Web page.
- `Exception`: This exception is raised for any other unexpected error that occurs during the video sending process.

Usage Example
-------------

```python
from selenium import webdriver
from pathlib import Path
from Demon_connect.features.send.send_video import send_video

# Create a Selenium WebDriver instance
driver = webdriver.Chrome()

# Login and perform other necessary steps

# Path to the video file
video_path = Path("path_to_video/video.mp4")

# Send the video to a contact
send_video(driver, "John Doe", video_path, "Check out this video!")

# Close the browser
driver.quit()
```

**Note:** Make sure to log in and perform any necessary steps before calling the `send_video` function.

See also
--------

The following files are linked to `Demon_connect/features/send/send_video.py`:
- [Demon_connect/api/whatsapp_api.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/api/whatsapp_api.py)
- [Demon_connect/features/login/login_whatsapp.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/features/login/login_whatsapp.py)
- [Demon_connect/features/send/send_image.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/features/send/send_image.py)
- [Demon_connect/features/send/send_message.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/features/send/send_message.py)