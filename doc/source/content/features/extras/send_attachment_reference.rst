send_attachment.py
=================

Documentation for `send_attachment.py` in the `Demon_connect` Repository

This file contains the code for sending attachments (such as images, videos, files) in the WhatsApp Web application. It provides a function `send_attachment()` that can be used to send attachments using the Selenium WebDriver.

Dependencies
------------

This file depends on the following modules:
- `selenium.webdriver.common.by` - Provides the `By` class for locating elements in the page
- `selenium.webdriver.support.expected_conditions` - Provides the `EC` class for defining expected conditions for waiting
- `selenium.webdriver.support.ui.WebDriverWait` - Provides the `WebDriverWait` class for waiting until certain conditions are met

Function: `send_attachment(driver: WebDriver) -> None`
------------------------------------------------------

This function sends an attachment in the WhatsApp Web application.

Arguments:

- `driver` (WebDriver): The instance of Selenium WebDriver used to interact with the browser.

Usage:

.. code:: python

   from selenium import webdriver
   from Demon_connect.features.extras.send_attachment import send_attachment

   # Create an instance of the WebDriver (e.g., ChromeDriver)
   driver = webdriver.Chrome()

   # Perform login and navigate to the desired chat

   # Call the send_attachment function to send the attachment
   send_attachment(driver)

   # Close the browser when done
   driver.quit()

Details:
--------

The `send_attachment()` function performs the following steps:

1. Waits for the pending clock icon to disappear before proceeding.
2. Find and click the send button for attachments.
3. Waits for the pending clock icon to disappear again - this is a workaround for large files or loading videos.

Note: This function assumes that the user is already logged in and has navigated to the desired chat or group in the WhatsApp Web application.

Please make sure to properly handle exceptions and take necessary precautions when using this function.

See also
--------

The following files are linked to `Demon_connect/features/extras/send_attachment.py`:
- [Demon_connect/api/whatsapp_api.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/api/whatsapp_api.py)
- [Demon_connect/drivers/chromedriver.exe](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/drivers/chromedriver.exe)
- [Demon_connect/features/extras/add_caption.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/features/extras/add_caption.py)
- [Demon_connect/features/extras/convert_bytes.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/features/extras/convert_bytes.py)