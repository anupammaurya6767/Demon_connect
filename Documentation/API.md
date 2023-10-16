# WhatsApp API Documentation

This documentation provides information on how to use the WhatsApp API to interact with WhatsApp Web. The API is implemented in the `whatsapp_api.py` module.

## Demon Class

The `Demon` class represents the API for interacting with WhatsApp web. It provides various methods to perform different actions such as logging in, sending messages, sending images or videos, tagging all members in a group, and more.

### Constructor

```python
def __init__(self, timeout: int = 60, visible: bool = True, data_path: str = None, chrome_options: Options = None) -> None:
```

**Arguments:**
- `timeout` (int): The maximum amount of time (in seconds) to wait for WhatsApp web to load. Default is 60 seconds.
- `visible` (bool): Whether the browser should be visible or run in the background. Default is True.
- `data_path` (str): The path to the data directory where WhatsApp web data will be stored. Default is None.
- `chrome_options` (Options): Additional options to customize the Chrome browser. Default is None.

### Methods

- `login()`: Logs in to WhatsApp web using the provided credentials.
- `send_message(contact_name: str, message: str)`: Sends a text message to the specified contact.
- `delete_message(group_name: str, message: str)`: Deletes a message from the specified group (Not implemented).
- `tag_all(group_name: str)`: Tags all members in the specified group.
- `get_list_of_messages()`: Fetches and returns a list of all messages in the current chat.
- `send_file(contact_name: str, filename: Path, message: Optional[str] = None)`: Sends a file (document, audio, etc.) to the specified contact.
- `send_image(contact_name: str, picture: Path, message: Optional[str] = None)`: Sends an image to the specified contact.
- `send_video(contact_name: str, video: Path, message: Optional[str] = None)`: Sends a video to the specified contact.
- `fetch_all_unread_chats(limit: bool = True, top: int = 50)`: Fetches and returns a list of all unread chats.
- `logout()`: Logs out from WhatsApp web.
- `close()`: Closes the browser window.

### Events

```python
event(func: Callable)
```

Decorator to register a function as an event handler. The following events are supported:
- `on_ready`: Called when the page is loaded and ready to use.
- `on_message`: Called when a new message is received.

### Properties

- `unread_messages`: Returns a list of unread messages in the conversations page.

## Example Usage

```python
# Create an instance of Demon
d = Demon()

# Login to WhatsApp web
d.login()

# Send a message
d.send_message("John Doe", "Hello!")

# Fetch all unread chats
unread_chats = d.fetch_all_unread_chats()

# Tag all members in a group
d.tag_all("Group Name")

# Register event handlers
@d.event
def on_ready():
    print("WhatsApp web is ready")

@d.event
def on_message(chat):
    print("New message received:", chat.message)

# Close the browser when done
d.close()
```
