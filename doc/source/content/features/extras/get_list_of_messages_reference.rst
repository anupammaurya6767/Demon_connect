get_list_of_messages.py
=======================

Documentation for `get_list_of_messages.py` in the `Demon_connect` Repository

This file contains the function `get_list_of_messages` which is responsible for retrieving the list of messages in the WhatsApp web page.

Function Details
----------------

`get_list_of_messages(driver)`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This function takes a `driver` object as its parameter, representing the Selenium WebDriver instance. It retrieves the list of messages in the page and returns a clean list of messages with specific details.

Parameters
^^^^^^^^^^^

- `driver`: The Selenium WebDriver instance for interacting with the web page.

Returns
^^^^^^^

- A list of dictionaries representing the messages in the page. Each dictionary contains the following keys:

  - `sender`: The name of the message sender.
  - `time`: The timestamp of the message.
  - `message`: The content of the message.
  - `unread`: A boolean value indicating if the message is unread or not.
  - `no_of_unread`: The number of unread messages in a group chat.
  - `group`: A boolean value indicating if the message belongs to a group chat.

Example Usage
^^^^^^^^^^^^^

.. code:: python

   from selenium import webdriver
   from features.extras.get_list_of_messages import get_list_of_messages

   # Create a WebDriver instance
   driver = webdriver.Chrome()

   # Perform necessary actions to load the WhatsApp web page

   # Call the get_list_of_messages function
   messages = get_list_of_messages(driver)

   # Print the retrieved messages
   for message in messages:
       print(message)

   # Close the WebDriver
   driver.quit()

Note: This function relies on Selenium WebDriver functionality and should be called after performing necessary actions to load the WhatsApp web page using the WebDriver instance.

See also
^^^^^^^^^

The following files are linked to `Demon_connect/features/extras/get_list_of_messages.py`:
- [Demon_connect/api/whatsapp_api.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/api/whatsapp_api.py)
- [Demon_connect/drivers/chromedriver.exe](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/drivers/chromedriver.exe)
- [Demon_connect/features/extras/add_caption.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/features/extras/add_caption.py)
- [Demon_connect/features/extras/convert_bytes.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/features/extras/convert_bytes.py)