Documentation - `login_whatsapp.py`
==================================

This file contains the implementation of the `login_whatsapp` function, which is used to log in to the WhatsApp Web platform. This function is called from the `Demon` class in the `Demon_connect/api/whatsapp_api.py` file.

Dependencies
------------

This function requires the following dependencies:

- `selenium.webdriver.common.by`
- `selenium.webdriver.support.ui`
- `selenium.webdriver.support.expected_conditions`
- `selenium.common.exceptions.TimeoutException`
- `utils.constants.WHATSAPP_WEB_URL`
- `utils.sorce.Sorce`
- `utils.handler`
- `qrcode_terminal` (commented out in the code snippet)

Function Signature
------------------

```python
def login_whatsapp(self)
```

Parameters
----------

- `self`: The instance of the `Demon` class.

Usage
-----

To use this function, create an instance of the `Demon` class and call the `login_whatsapp` method on that instance. For example:

```python
demon = Demon(browser='Chrome', browser_path='path/to/browser', driver_path='path/to/driver')
demon.login_whatsapp()
```

Function Details
----------------

The `login_whatsapp` function performs the following steps:

1. Navigates to the WhatsApp Web URL.
2. Waits for either the QR code element or the search bar element to become visible.
3. If the QR code is visible, it prints the QR code on the console (if the browser is not set to visible mode).
4. Prints a message asking the user to scan the QR code with their phone to log in.
5. Waits for the page to finish loading.
6. Creates and starts threads for handling the `on_ready` and `on_message` events.

Please note that this function uses some utility functions and classes from the `utils` module, such as `element_exists`, `find_element_if_exists`, and `Sorce`. These are used to interact with the Selenium WebDriver and perform various operations on the web elements.

See also
--------

The following files are linked to `Demon_connect/features/login/login_whatsapp.py`:
- [Demon_connect/api/whatsapp_api.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/api/whatsapp_api.py)
- [Demon_connect/features/send/send_image.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/features/send/send_image.py)
- [Demon_connect/features/send/send_message.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/features/send/send_message.py)
- [Demon_connect/main.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/main.py)