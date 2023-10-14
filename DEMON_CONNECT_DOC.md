# 🚀 Demon_Connect API Documentation 📱💬

## `Demon` Class 😈

Welcome to the exciting world of automating WhatsApp Web using the `Demon` class! 😎

### Constructor: `__init__(self, browser: str, browser_path: str, driver_path: str)`

- **🌟 Purpose**: Initializes an instance of the `Demon` class with the power to wield your favorite browser and unleash your digital sorcery!

- `browser` (str): The browser to use (e.g., 'chrome', 'firefox').
- `browser_path` (str): The secret path to the browser's lair (user data directory).
- `driver_path` (str): The enchanted path to your browser driver executable.

### `load_driver(self)`

- **🪄 Purpose**: Summons the Selenium driver, crafting it to obey your command. Select the right one for your browser magic.

- Returns: A Selenium WebDriver instance suitable for the specified browser. 🧙

### `login(self)`

- **🔑 Purpose**: Initiates your grand WhatsApp Web adventure. Get ready to login to your chat kingdom! 👑

- Usage: `demon_instance.login()` (Click this to enter the WhatsApp realm!)

### `send_message(self, contact_name: str, message: str)`

- **💬 Purpose**: Casts a spell to send a text message to a chosen contact or group. The words shall flow like a river! 🌊

- `contact_name` (str): The name of the contact or group.
- `message` (str): The message incantation. ✉️

### `send_image(self, contact_name: str, picture: Path, message: Optional[str] = None)`

- **📸 Purpose**: Sends an image to your chosen ally or a fierce group. Make your messages a masterpiece! 🖼️

- `contact_name` (str): The name of the contact or group.
- `picture` (Path): The sacred path to the image artifact.
- `message` (Optional[str]): A secret message to accompany your image. 🤫

### `send_video(self, contact_name: str, video: Path, message: Optional[str] = None)`

- **🎥 Purpose**: Unleashes a video to amaze your friends or dazzle a group. Videos, the moving art of the modern era! 📽️

- `contact_name` (str): The name of the contact or group.
- `video` (Path): The path to the video reel.
- `message` (Optional[str]): An enchanting message to go with the video. 🎉

### `delete_message(self, group_name: str, message: str)`

- **🔥 Purpose**: Commands the deletion of a troublesome message within a group chat. Out of sight, out of mind! 🙈

- `group_name` (str): The name of the group.
- `message` (str): The text of the message to be vanquished. 💥

### `tag_all(self, group_name: str)`

- **🏷️ Purpose**: Summons all members of a group chat to heed your call. Tag them all! A royal decree. 👑

- `group_name` (str): The name of the group. 📣

### `get_list_of_messages(self)`

- **📜 Purpose**: Retrieves a list of messages, unearthing the chronicles of your chat history. Time travel in your chat box! ⏳📚

- Returns: List of message objects with details like sender, timestamp, and content. 🧙‍♂️

### `send_file(self, contact_name: str, filename: Path, message: Optional[str] = None)`

- **📂 Purpose**: Dispatches a magical file (document) to a specific contact or group. Share knowledge! 📚✨

- `contact_name` (str): The name of the contact or group.
- `filename` (Path): The path to the sacred document.
- `message` (Optional[str]): A secret message to accompany your file. 🕵️

### `fetch_all_unread_chats(self, limit: bool = True, top: int = 50)`

- **🔍 Purpose**: Embarks on a quest to find unread chat messages. Retrieve hidden treasures! 🏴‍☠️

- `limit` (bool): Set to `True` to limit the number of chat messages fetched.
- `top` (int): Number of chat messages to retrieve if `limit` is set to `True. 🔎

### `logout(self)`

- **🚪 Purpose**: It's time to exit the WhatsApp Web realm. Logout gracefully and save your progress for the next adventure! 🚶

- Usage: `demon_instance.logout()` (Click here to exit the realm!)

### `close(self)`

- **👋 Purpose**: Closes the magical gateway, freeing your browser from the spells and releasing the captive resources. Farewell! 👋

- Usage: `demon_instance.close()` (Click here to break the spell!)

Experience the magic and explore the world of WhatsApp Web with `Demon`. Your digital adventure awaits! 🌐🌟
