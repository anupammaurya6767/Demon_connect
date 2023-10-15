`send_file.py` Documentation
===========================

The `send_file.py` module is responsible for sending a file to a target user in the WhatsApp chat.

Functions
---------

`send_file(driver, contact_name, filename: Path, message: Optional[str] = None)`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This function sends a file to a target user.

Arguments
~~~~~~~~~

- `driver`: The Selenium WebDriver instance that controls the browser.
- `contact_name`: The name of the target user to send the file to.
- `filename: Path`: The path of the file to be sent.
- `message: Optional[str]`: An optional message to accompany the file.

Exceptions
~~~~~~~~~~~

- `NoSuchElementException`: If any elements required for sending the file are not found.
- `Exception`: If there is any other error while sending the file.

Returns
~~~~~~~

None

The function performs the following steps:

1. It searches for the contact by entering the name in the search box.
2. It clicks on the contact's name after finding it in the list.
3. It obtains the absolute path of the file.
4. It finds the attachment button and clicks on it.
5. It finds the document button and sends the file path to it.
6. If a message is provided, it adds a caption to the file.
7. It sends the attachment.
8. It waits for the pending clock icon to appear and disappear, indicating that the message has been sent successfully.
9. It handles any exceptions that may occur during the process and prints relevant error messages.

Usage Example:
~~~~~~~~~~~~~~~

```python
send_file(driver, "John Doe", '/path/to/file.pdf', "Check out this document!")
```

Note: Make sure to have a valid Selenium WebDriver instance (`driver`) before calling this function.

See also
--------

The following files are linked to `Demon_connect/features/send/send_file.py`:
- [Demon_connect/api/whatsapp_api.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/api/whatsapp_api.py)
- [Demon_connect/drivers/chromedriver.exe](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/drivers/chromedriver.exe)
- [Demon_connect/features/extras/add_caption.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/features/extras/add_caption.py)
- [Demon_connect/features/extras/convert_bytes.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/features/extras/convert_bytes.py)