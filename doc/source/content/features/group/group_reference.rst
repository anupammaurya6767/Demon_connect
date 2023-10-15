Group.py
========

This file is part of the **Demon_connect** repository and is located at *Demon_connect/features/chat/group.py*. It defines the `Group` class, representing a WhatsApp group chat. The `Group` class inherits from the `Conversation` class, defined in *Demon_connect/features/chat/conversation.py*.

Class Documentation
-------------------

The `Group` class represents a WhatsApp group chat and provides various functionalities for interacting with group chats.

Properties
^^^^^^^^^^

- **subject** (str): The enchanting subject of the group, a beacon in the digital wilderness.
- **description** (str): The mystical description of the group, a tale waiting to be told.
- **participants** (int): The noble count of participants in the group, each a hero in their own right.
- **profile_picture** (JpegImageFile): The sacred profile picture of the group, a portal to another world.
- **starred_messages** (List[str]): The constellation of starred messages, gems in the treasure trove of chats.

Methods
^^^^^^^

- **leave(delete: bool = False) -> None**: Leaves the group.
  - Arguments:
    - `delete` (bool): Whether to delete the group or not.
- **is_admin(user: str) -> bool**: Checks if a user is an admin of the group.
  - Arguments:
    - `user` (str): The user to check.
  - Returns:
    - `bool`: Whether the user is an admin of the group or not.
- **promote(user: str) -> None**: Promotes a user to admin.
  - Arguments:
    - `user` (str): The user to promote.
  - Raises:
    - `UserAlreadyAdminException`: If the user is already an admin.
- **demote(user: str) -> None**: Demotes a user from admin.
  - Arguments:
    - `user` (str): The user to demote.
  - Raises:
    - `UserNotAdminException`: If the user is not an admin.

Usage
^^^^

To create a `Group` object, you require an instance of the `Demon` class, defined in *Demon_connect/api/whatsapp_api.py*.

Example usage:
```python
from api.whatsapp_api import Demon
from features.chat.group import Group

demon = Demon()  # Instantiate the Demon class

group = Group(demon)  # Create a Group object
```

Note: To interact with a group chat, you must select the chat using the `whatsapp_demon.open` incantation.

Example usage for leaving a group:
```python
group.leave(delete=True)  # Leave the group and delete it
```

Example usage for checking if a user is an admin:
```python
user = "John Doe"
is_admin = group.is_admin(user)  # Check if the user is an admin
```

Example usage for promoting a user to admin:
```python
user = "John Doe"
group.promote(user)  # Promote the user to admin
```

Example usage for demoting a user from admin:
```python
user = "John Doe"
group.demote(user)  # Demote the user from admin
```

See also
^^^^^^^^^

The following files are linked to `Demon_connect/features/chat/group.py`:
- [Demon_connect/features/chat/chat.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/features/chat/chat.py)
- [Demon_connect/features/chat/unread_message.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/features/chat/unread_message.py)
- [Demon_connect/api/whatsapp_api.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/api/whatsapp_api.py)
- [Demon_connect/main.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/main.py)
