Demon_connect/features/chat/conversation.py
=========================================

This file contains the `Conversation` class, which is a utility class for managing conversations and groups in WhatsApp.

Conversation Class
-------------------

The `Conversation` class represents a conversation or group in WhatsApp.

Properties
^^^^^^^^^^

- **name** (str): The name of the conversation.

Methods
^^^^^^^

- **__init__(self, _whatsapp: Demon) -> None**: Initializes a new instance of the `Conversation` class.

- **last_message(self) -> Message | None**: Returns the last message in the conversation.

- **is_muted(self) -> bool**: Returns whether the conversation is muted or not.

- **is_pinned(self) -> bool**: Returns whether the conversation is pinned or not.

- **event(self, func: Callable) -> None**: Decorator to register a function as an event handler.

- **open(self) -> Conversation**: Opens the conversation.

- **send(self, message: str = None, attatchments: List[str] = None, type: Literal["auto", "document", "midia", "contact"] = "auto") -> None**: Sends a message to the conversation.

- **clear(self, keep_starred: bool = False) -> None**: Clears the conversation messages.

- **mute(self, time: Literal["8 hours", "1 week", "Always"]) -> None**: Mutes the conversation notifications.

- **unmute(self) -> None**: Unmutes the conversation's notifications.

- **pin(self) -> None**: Pins the conversation.

- **unpin(self) -> None**: Unpins the conversation.

Additional Details
^^^^^^^^^^^^^^^^^^

The `Conversation` class is used to interact with individual conversations or groups in WhatsApp. It provides methods for sending messages, clearing messages, muting and unmuting notifications, and pinning and unpinning conversations.

To use the `Conversation` class, you need to create an instance by calling the `open` method of the `whatsapp_demon` object with the name of the conversation as the argument. This will return an instance of the `Conversation` class.

Example:

```python
whatsapp = whatsapp_demon.open("John Doe")
conversation = Conversation(whatsapp)
conversation.send("Hello!")
```

The `Conversation` class also supports event handling. You can register a function as an event handler using the `event` decorator. Currently, only the `on_message` event is supported. The registered function will be called whenever a new message is received in the conversation.

Example:

```python
@conversation.event
async def on_message(message: Message):
    print(f"New message: {message.text}")

conversation.open()
```

Note: The `Conversation` class should not be initialized directly. Instead, use the `open` method of the `whatsapp_demon` object to create an instance.

Exceptions
^^^^^^^^^^

The following exceptions can be raised by the methods of the `Conversation` class:

- `NotSelectedException`: Raised if the conversation is not selected.

- `ValueError`: Raised if no attachments or messages are specified while sending a message, or if an invalid type is specified for attachments.

- `TypeError`: Raised if any of the attachments is not a string.

- `FileNotFoundError`: Raised if any of the attachments is a file that does not exist.

- `ContactNotFoundException`: Raised if any of the specified contacts does not exist.

- `MaxPinnedChatsException`: Raised if the maximum number of pinned chats is reached.

See also
^^^^^^^^^

The following files are linked to `Demon_connect/features/chat/conversation.py`:
- [Demon_connect/features/chat/chat.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/features/chat/chat.py)
- [Demon_connect/features/chat/message.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/features/chat/message.py)
- [Demon_connect/features/chat/unread_message.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/features/chat/unread_message.py)
- [Demon_connect/api/whatsapp_api.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/api/whatsapp_api.py)