`main.py` Documentation
=======================

Description
-----------

The `main.py` file is the entry point of the Demon_connect repository. It demonstrates the usage of the `Demon` class from the `whatsapp_api.py` file to interact with WhatsApp Web.

Dependencies
------------

- `BROWSER`: The browser name (e.g., `'Chrome'`) to be used by the Demon.
- `USR_DIR`: The user data directory path for the Demon's browser.
- `CHROME_DRIVER_PATH`: The path to the Chrome driver executable.

Example:
```python
from utils.constants import BROWSER
from utils.constants import USR_DIR
from utils.constants import CHROME_DRIVER_PATH
```

Usage
-----

1. Create an instance of the `Demon` class by providing the necessary arguments - `browser`, `browser_path`, and `driver_path`.

   - `browser`: The browser to be used by the Demon (e.g., `'Chrome'`).
   - `browser_path`: The path to the user data directory for the browser.
   - `driver_path`: The path to the driver executable for the browser.

   Example:
   ```python
   whatsapp_demon = Demon(BROWSER, USR_DIR, CHROME_DRIVER_PATH)
   ```

2. Log in to WhatsApp Web using the `login()` method of the `Demon` class.

   Example:
   ```python
   whatsapp_demon.login()
   ```

3. Use the available methods of the `Demon` class to interact with WhatsApp. Some of the available methods are:

   - `send_message(contact_name, message)`: Sends a message to a specified contact.
   - `delete_message(group_name, message)`: Deletes a specific message in a group (Not implemented).
   - `send_image(contact_name, picture, message)`: Sends an image to a specified contact.
   - `send_video(contact_name, video, message)`: Sends a video to a specified contact.
   - `tag_all(group_name)`: Tags all members in a group (group mention).

   Example (Sending a message):
   ```python
   message = "hello"
   contact = "bot test"
   whatsapp_demon.send_message(contact, message)
   ```

4. Close the browser by calling the `close()` method when done with the interactions.

   Example:
   ```python
   whatsapp_demon.close()
   ```

Example Usage
-------------

```python
from utils.constants import BROWSER
from utils.constants import USR_DIR
from utils.constants import CHROME_DRIVER_PATH
from api.whatsapp_api import Demon

def main():
    whatsapp_demon = None
    try:
        whatsapp_demon = Demon(BROWSER, USR_DIR, CHROME_DRIVER_PATH)
        whatsapp_demon.login()

        message = "hello"
        contact = "bot test"
        whatsapp_demon.send_message(contact, message)
        whatsapp_demon.delete_message(contact, message)

        # Other operations

    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        if whatsapp_demon is not None:
            whatsapp_demon.close()

if __name__ == "__main__":
    main()
```

Note
----

- Some methods like `delete_message` are marked with a `NotImplemented` comment indicating that the method is not implemented yet.

See also
--------

The following files are linked to `Demon_connect/main.py`:
- [Demon_connect/api/whatsapp_api.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/api/whatsapp_api.py)
- [Demon_connect/features/login/login_whatsapp.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/features/login/login_whatsapp.py)
- [Demon_connect/features/send/send_image.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/features/send/send_image.py)
- [Demon_connect/features/send/send_message.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/features/send/send_message.py)
