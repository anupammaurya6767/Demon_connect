fetch_all_unread_chats.py
=========================

Documentation for `fetch_all_unread_chats.py` in the `Demon_connect` Repository

This module provides the functionality to fetch all unread chats in WhatsApp.

Functions
---------

`fetch_all_unread_chats(driver, limit=True, top=50)`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This function fetches all unread chats in WhatsApp.

Arguments
^^^^^^^^^^

- `driver` (WebDriver): The Selenium driver instance.
- `limit` (bool): Specifies whether to limit the counting to a certain number of chats (default: True).
- `top` (int): The approximate number of chats to consider when `limit` is True (default: 50).

Returns
^^^^^^^

- `names_data` (List[dict]): A list of dictionaries containing information about each unread chat, including the name of the sender and whether the message is unread.

Usage Example
^^^^^^^^^^^^^

.. code:: python

   from selenium import webdriver
   from fetch_all_unread_chats import fetch_all_unread_chats

   # Create a Selenium driver instance
   driver = webdriver.Chrome()

   # Fetch all unread chats
   unread_chats = fetch_all_unread_chats(driver)

   # Print the list of unread chats
   for chat in unread_chats:
       print(chat['sender'], chat['unread'])

   # Close the driver
   driver.quit()

Notes
^^^^^

- The functionality of `fetch_all_unread_chats` is tested and works on most updated browser versions.
- If the function fails to work, updating the browser to the latest version is recommended.
- If the problem persists, consider updating the browser while an alternative solution for non-updated browsers is being developed.

See also
^^^^^^^^

The following files are linked to `Demon_connect/features/extras/fetch_all_unread_chats.py`:
- [Demon_connect/api/whatsapp_api.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/api/whatsapp_api.py)
- [Demon_connect/main.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/main.py)
- [Demon_connect/features/chat/chat.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/features/chat/chat.py)
- [Demon_connect/features/chat/conversation.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/features/chat/conversation.py)
