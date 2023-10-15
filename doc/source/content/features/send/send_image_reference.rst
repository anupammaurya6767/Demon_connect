`Demon_connect/features/send/send_image.py` Documentation
======================================================

This file contains the code for sending an image to a contact or group on WhatsApp. The `send_image` function allows you to send an image to a specific contact or group and optionally add a message to it.

Function Signature
------------------

```python
def send_image(driver, contact_name, picture: Path, message: Optional[str] = None):
```

Parameters
----------

- `driver`: WebDriver - The selenium webdriver instance used for interacting with the browser.
- `contact_name`: str - The name of the contact or group to send the image to.
- `picture`: Path - The path to the image file to be sent.
- `message`: str (optional) - An optional message to be added along with the image.

Usage Example
-------------

```python
from pathlib import Path
from selenium import webdriver
from features.send.send_image import send_image

# Create a webdriver instance
driver = webdriver.Chrome()

# Login to WhatsApp Web

# Send an image to a contact
contact_name = "John Doe"
image_file = Path("/path/to/image.jpg")
send_image(driver, contact_name, image_file, message="Check out this cool image!")

# Close the browser
driver.quit()
```

Detailed Description
--------------------

The `send_image` function performs the following steps:
1. Searches for the contact or group using the specified `contact_name` and selects it.
2. Finds the input element for the image and sends the file path of the image to it.
3. If a `message` is provided, it adds the message as a caption to the image.
4. Calls the `send_attachment` function to send the image.
5. Waits for the message to be sent successfully by checking the presence and disappearance of the pending clock icon.
6. Prints a success message if the message was sent successfully or an error message if an exception occurred.

Note: Make sure to have the appropriate permissions to access the image file and that the file path is correct.

See also
--------

The following files are linked to `Demon_connect/features/send/send_image.py`:
- [Demon_connect/api/whatsapp_api.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/api/whatsapp_api.py)
- [Demon_connect/features/login/login_whatsapp.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/features/login/login_whatsapp.py)
- [Demon_connect/features/send/send_message.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/features/send/send_message.py)
- [Demon_connect/main.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/main.py)