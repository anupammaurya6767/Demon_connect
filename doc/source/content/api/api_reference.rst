whatsapp_api.py Documentation
============================

This file contains the implementation of the `Demon` class, which is responsible for interacting with the WhatsApp Web API.

Class: Demon
------------

The `Demon` class represents an instance of the WhatsApp Web API. It provides methods for logging in, sending messages, sending images and videos, deleting messages, tagging all members in a group, and more.

Constructors
~~~~~~~~~~~~

- ``__init__(self, browser: str, browser_path: str, driver_path: str, timeout: int = 60, visible: bool = True) -> None``

  Parameters:
  - ``browser`` (str): The browser to be used. Currently supports "firefox" and "Chrome".
  - ``browser_path`` (str): The path to the browser profile directory.
  - ``driver_path`` (str): The path to the driver executable.
  - ``timeout`` (int, optional): The maximum time (in seconds) to wait for a page to load. Defaults to 60.
  - ``visible`` (bool, optional): Specifies whether the browser window should be visible or not. Defaults to True.

Methods
~~~~~~~

- ``event(self, func: Callable) -> None``

  Decorator to register a function as an event handler.
  Arguments:
  - ``func`` (Callable): The function to be registered. It must be a coroutine.

- ``open(self, chat: str) -> (Chat | Group | None)``

  Opens a chat with the specified name or phone number.
  Arguments:
  - ``chat`` (str): The name or phone number of the chat to open.
  Returns:
  - ``(Chat | Group | None)``: The chat with the specified name or phone number. Returns `None` if the chat is not found.

- ``@property``
- ``unread_messages(self) -> List[UnreadMessage]``

  Returns the list of unread messages in the conversations page.
  Returns:
  - ``List[UnreadMessage]``: List of unread messages.

- ``login(self) -> None``

  Logs in to WhatsApp Web.

- ``send_message(self, contact_name: str, message: str) -> None``

  Sends a message to the specified contact.
  Arguments:
  - ``contact_name`` (str): The name of the contact.
  - ``message`` (str): The message to send.

- ``delete_message(self, group_name: str, message: str) -> None``

  Deletes a message from the specified group.
  Arguments:
  - ``group_name`` (str): The name of the group.
  - ``message`` (str): The message to delete.

- ``tag_all(self, group_name: str) -> None``

  Tags all members in the specified group.
  Arguments:
  - ``group_name`` (str): The name of the group.

- ``send_file(self, contact_name: str, filename: Path, message: Optional[str] = None) -> None``

  Sends a file to the specified contact.
  Arguments:
  - ``contact_name`` (str): The name of the contact.
  - ``filename`` (Path): The path to the file to send.
  - ``message`` (Optional[str], optional): An optional message to accompany the file. Defaults to None.

- ``send_image(self, contact_name: str, picture: Path, message: Optional[str] = None) -> None``

  Sends an image to the specified contact.
  Arguments:
  - ``contact_name`` (str): The name of the contact.
  - ``picture`` (Path): The path to the image to send.
  - ``message`` (Optional[str], optional): An optional message to accompany the image. Defaults to None.

- ``send_video(self, contact_name: str, video: Path, message: Optional[str] = None) -> None``

  Sends a video to the specified contact.
  Arguments:
  - ``contact_name`` (str): The name of the contact.
  - ``video`` (Path): The path to the video to send.
  - ``message`` (Optional[str], optional): An optional message to accompany the video. Defaults to None.

- ``fetch_all_unread_chats(self, limit: bool = True, top: int = 50) -> None``

  Fetches all unread chats.
  Arguments:
  - ``limit`` (bool, optional): If `True`, limits the number of unread chats to `top`. Defaults to True.
  - ``top`` (int, optional): The maximum number of unread chats to fetch. Defaults to 50.

- ``load_driver(self) -> WebDriver``

  Loads the Selenium driver depending on the browser.

- ``_is_loaded(self) -> bool``

  Checks if the page is loaded.

- ``_is_animating(self) -> bool``

  Checks if the page is animating.

- ``_search_chat(self, chat: str) -> WebElement``

  Searches for a chat and returns the search element.
  Arguments:
  - ``chat`` (str): The name or phone number of the chat.
  Returns:
  - ``WebElement``: The search element.

- ``_clear_search_bar(self) -> None``

  Clears the search bar.

- ``_on_ready(self) -> None``

  Calls the `on_ready` callback when the page is loaded.

- ``_on_message(self) -> None``

  Checks for new messages and calls the `on_message` callback.

- ``logout(self) -> None``

  Logs out of WhatsApp Web.

- ``close(self) -> None``

  Closes the browser.

Example Usage
~~~~~~~~~~~~~

```python
whatsapp_demon = Demon("Chrome", "path/to/browser/profile", "path/to/driver")
whatsapp_demon.login()
chat = whatsapp_demon.open("John Doe")
whatsapp_demon.send_message(chat, "Hello, John!")
whatsapp_demon.logout()
whatsapp_demon.close()
```

Note: Make sure to call `close()` when you're done to close the browser.

See also
~~~~~~~~

The following files are linked to Demon_connect/api/whatsapp_api.py:
- [Demon_connect/main.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/main.py)
- [Demon_connect/features/login/login_whatsapp.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/features/login/login_whatsapp.py)
- [Demon_connect/features/send/send_image.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/features/send/send_image.py)
- [Demon_connect/features/send/send_message.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/features/send/send_message.py)
