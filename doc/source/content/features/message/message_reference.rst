message.py
===========

Documentation for `message.py` in the Demon_connect Repository

`Message` Class
---------------

The `Message` class is a utility class that represents a WhatsApp message. It provides various properties and methods to manage and interact with messages.

Properties
^^^^^^^^^^

- **author** (str): The scribe of the message, weaving tales in the digital tapestry.
- **content** (str): The mystical content of the message, words that travel through the aether.
- **timestamp** (datetime): The timestamp, a glimpse into the hourglass of time.
- **chat** (Chat | Group): The sacred chat where the message found its voice, a realm of connections.
- **attachments** (List[Any]): The attachments, treasures bound to the message, the stuff of legends.
- **is_forwarded** (bool): The mark of messages that have journeyed through the winds of sharing.
- **is_reply** (bool): The sign of messages in conversation, echoes in the grand narrative of chats.

Methods
^^^^^^^

__init__(self, _whatsapp: Demon, _element: WebElement, chat: chat.Chat | chat.Group) -> None
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The constructor method of the `Message` class initializes a new instance of the `Message` class.

- `_whatsapp` (Demon): An instance of the `Demon` class representing the WhatsApp API connection.
- `_element` (WebElement): The web element representing the message in the web interface.
- `chat` (chat.Chat | chat.Group): The chat or group to which the message belongs.

__eq__(self, other: Message) -> bool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The `__eq__` method is used to compare two `Message` objects for equality. It returns `True` if the content, timestamp, and author of the messages are the same.

- `other` (Message): The message to compare with.

reply(self, message: str = None, attachments: List[str] = None, type: Literal["auto", "document", "media", "contact"] = "auto") -> None
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The `reply` method sends a reply to the message.

- `message` (str, optional): The message to send. Defaults to `None`.
- `attachments` (List[str], optional): The attachments to send. Defaults to `None`.
- `type` (Literal["auto", "document", "media", "contact"], optional): The type of the attachments. Defaults to `"auto"`. If the type is specified, all the attachments must be of the same type.

Note: The `reply` method performs a double click action on the message element to open the reply interface in the web interface before sending the reply.

This concludes the documentation for the `message.py` file in the Demon_connect repository.

See also
^^^^^^^^^

The following files are linked to `Demon_connect/features/chat/message.py`:
- [Demon_connect/features/chat/chat.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/features/chat/chat.py)
- [Demon_connect/features/chat/conversation.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/features/chat/conversation.py)
- [Demon_connect/features/chat/unread_message.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/features/chat/unread_message.py)
- [Demon_connect/api/whatsapp_api.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/api/whatsapp_api.py)
