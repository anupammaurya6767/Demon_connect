logout.py
=========

This file contains the implementation of the `logout` function, which is responsible for logging out of the WhatsApp Web application.

Functions
---------

.. function:: logout(driver)

   This function is used to log out of the WhatsApp Web application.

   Arguments
   ~~~~~~~~~
   - `driver` (WebDriver): The Selenium WebDriver instance.

   Returns
   ~~~~~~~
   - None

   Usage Example
   ~~~~~~~~~~~~~
   .. code:: python

      from selenium import webdriver
      from features.logout import logout

      # Create a WebDriver instance
      driver = webdriver.Chrome()

      # Call the logout function
      logout(driver)

      # Close the WebDriver instance
      driver.quit()

   This function performs the following steps to log out:

   1. Find the dots button element, which is used to open the menu, by waiting for it to be clickable using the XPath expression `//div[@id='side']/header/div[2]/div/span/div[3]/div[@role='button']`.
   2. Click on the dots button element to open the menu.
   3. Find the logout item element in the menu by waiting for it to be clickable using the XPath expression `//div[@id='side']/header/div[2]/div/span/div[3]/span/div[1]/ul/li[last()]/div[@role='button']`.
   4. Click on the logout item element to log out of the WhatsApp Web application.

See also
--------

The following files are linked to `Demon_connect/features/logout/logout.py`:
- [Demon_connect/api/whatsapp_api.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/api/whatsapp_api.py)
- [Demon_connect/drivers/chromedriver.exe](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/drivers/chromedriver.exe)
- [Demon_connect/features/extras/add_caption.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/features/extras/add_caption.py)
- [Demon_connect/features/extras/convert_bytes.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/features/extras/convert_bytes.py)