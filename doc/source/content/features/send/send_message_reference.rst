`send_message.py` Documentation
==============================

The `send_message.py` file contains a function `send_message` that is responsible for sending a message to a contact on WhatsApp Web.

Function Details
----------------

send_message(driver, contact_name, message, _2vDPL=None)

This function sends a message to a contact on WhatsApp Web.

Arguments
---------

- `driver`: The Selenium driver used to interact with the browser.
- `contact_name`: The name of the contact to send the message to.
- `message`: The message to send.

Usage Example
-------------

```python
send_message(driver, "Contact Name", "Hello, this is a test message!")
```

Implementation Details
----------------------

1. **Finding the contact to send the message**

   The function first searches for the contact in the search box by entering the `contact_name` and pressing ENTER.

2. **Locating the contact in the search results**

   After searching, the function locates the contact name in the search results and clicks on it.

3. **Finding the input box**

   The function locates the input box where the message is typed.

4. **Sending the message**

   The input box is cleared, and the `message` is sent by entering it in the input box and pressing ENTER.

5. **Confirmation**

   The function waits for the message to be sent successfully and displays a confirmation message.

Note: If an exception occurs during the process, a failure message is displayed.

Please refer to the usage example provided above for understanding how to use the `send_message` function.

See also
--------

The following files are linked to `Demon_connect/features/send/send_message.py`:
- [Demon_connect/api/whatsapp_api.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/api/whatsapp_api.py)
- [Demon_connect/features/login/login_whatsapp.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/features/login/login_whatsapp.py)
- [Demon_connect/features/send/send_image.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/features/send/send_image.py)
- [Demon_connect/main.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/main.py)