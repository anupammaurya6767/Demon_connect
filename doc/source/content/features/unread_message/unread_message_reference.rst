unread_message.py
================

Documentation for `unread_message.py` in the `Demon_connect` Repository

Enchanted Unread Chat
----------------------

Behold, a chat cloaked in the mystique of unread messages, a realm of secrets and surprises in WhatsApp! Do not seek to awaken it directly; invoke the 'whatsapp_demon.unread_messages' spell instead.

This class unveils the tales of unread chats, their names, the count of their unread scrolls, and the echoes of their last messages. A world of digital mysteries awaits!

Properties
----------

- **name** (str): The magical name of the unread chat, a title that hints at the untold.
- **count** (int): The count of unread messages, a measure of the secrets hidden within.
- **message** (str): The last message, a whisper of the chat's lingering voice.

Methods
-------

reply(message: str, attachments: List[str] = None, type: Literal["auto", "document", "media", "contact"] = "auto") -> chat.Chat | chat.Group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Reply to the unread chat.

Arguments
^^^^^^^^^^

- `message` (str): The message to reply with.
- `attachments` (List[str], optional): The attachments to reply with. Defaults to None.
- `type` (Literal["auto", "document", "media", "contact"], optional): The type of the attachments. Defaults to "auto".

Returns
^^^^^^^

- `Chat | Group`: The chat or group that the message was sent to.

See also
--------

The following files are linked to `Demon_connect/features/chat/unread_message.py`:
- [Demon_connect/features/chat/chat.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/features/chat/chat.py)
- [Demon_connect/features/chat/conversation.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/features/chat/conversation.py)
- [Demon_connect/features/chat/message.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/features/chat/message.py)
- [Demon_connect/features/chat/group.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/features/chat/group.py)
