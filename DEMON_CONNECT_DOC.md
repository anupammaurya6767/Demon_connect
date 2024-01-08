# 🚀 Demon Connect API Documentation 📱💬

Welcome to the magical world of WhatsApp Web automation using the `Demon` class! Embrace the power of the digital realm. 😎

## `Demon` Class 😈

Unleash the demon within to navigate the WhatsApp Web universe and experience the following enchanting features! 🌟

### Constructor: `__init__(self, browser: str, browser_path: str, driver_path: str)`

- **🌟 Purpose**: Create an instance of the `Demon` class and choose your portal to the browser's kingdom.

- `browser` (str): The browser of your choice (e.g., 'chrome', 'firefox').
- `browser_path` (str): The secret path to the browser's lair (user data directory).
- `driver_path` (str): The enchanted path to the browser's driver executable.

**Usage Example**:
```python
whatsapp_demon = Demon(browser='chrome', browser_path='path/to/browser', driver_path='path/to/driver')
```
<br/>

### `load_driver(self)`

- **🪄 Purpose**: Summon the Selenium driver tailored to your browser and let the magic unfold.

- Returns: A Selenium WebDriver instance ready to serve your digital incantations. 🧙

**Usage Example**:
```python
whatsapp_demon.load_driver()  # Prepare the gateway to WhatsApp Web! 🪄
```
<br/>

### `login(self)`

- **🔑 Purpose**: Initiate your grand WhatsApp Web adventure. Enter the realm of chats and connections. 👑

**Usage Example**:
```python
whatsapp_demon.login()  # Begin your epic quest! 🛡️
```
<br/>

### `send_message(self, contact_name: str, message: str)`

- **💬 Purpose**: Send text messages to your allies and friends, for words have the power to unite! 📜

- `contact_name` (str): The name of your contact or group.
- `message` (str): The message to transmit. ✉️

**Usage Example**:
```python
whatsapp_demon.send_message("Fellow Adventurers", "Brace yourselves, a new quest awaits! 🌄")
```
<br/>

### `send_image(self, contact_name: str, picture: Path, message: Optional[str] = None)`

- **📸 Purpose**: Share images with your comrades. Paint your digital canvases with memories! 🖼️🌌

- `contact_name` (str): The name of your contact or group.
- `picture` (Path): The path to your image.
- `message` (Optional[str]): A secret message accompanying your masterpiece. 🤫

**Usage Example**:
```python
whatsapp_demon.send_image("Fellow Explorers", "path/to/your/image.jpg", "A glimpse of our adventure! 📸")
```
<br/>

### `send_video(self, contact_name: str, video: Path, message: Optional[str] = None)`

- **🎥 Purpose**: Share videos to capture and relive moments with your companions. Videos are the moving art of the modern era! 🎬📖

- `contact_name` (str): The name of your contact or group.
- `video` (Path): The path to your video masterpiece.
- `message` (Optional[str]): An enchanting message to accompany your video. 🎉

**Usage Example**:
```python
whatsapp_demon.send_video("Adventurers Guild", "path/to/your/video.mp4", "Our adventures await! 🌟")
```
<br/>

### `delete_message(self, group_name: str, message: str)`

- **🔥 Purpose**: Erase unwanted messages from group chats, leaving no trace behind. Time to cleanse your story! 🗑️

- `group_name` (str): The name of the group.
- `message` (str): The text of the message to be vanquished. 💥

**Usage Example**:
```python
whatsapp_demon.delete_message("Secret Society", "This message is better left unsaid.")
```
<br/>

### `tag_all(self, group_name: str)`

- **🏷️ Purpose**: Summon all members of a group chat to heed your call, like a charismatic anime character rallying their comrades. Unite for a common cause! ⚔️🛡️

- `group_name` (str): The name of the group. 📣

**Usage Example**:
```python
whatsapp_demon.tag_all("Guild Members")  # Gather, brave souls! 🚀
```
<br/>

### `get_list_of_messages(self)`

- **📜 Purpose**: Uncover the history of your chat adventures, retrieving a list of messages from your chat kingdom. Time travel in your chat box! ⏳📚

- Returns: A list of message objects with details like sender, timestamp, and content. 🧙‍♂️

**Usage Example**:
```python
messages = whatsapp_demon.get_list_of_messages()
for message in messages:
    print(f"Sender: {message.sender}, Timestamp: {message.timestamp}, Content: {message.content}")
```
<br/>

### `send_file(self, contact_name: str, filename: Path, message: Optional[str] = None)`

- **📂 Purpose**: Dispatch magical files (documents) to your chosen contacts or groups. Share knowledge and wisdom! 📚✨

- `contact_name` (str): The name of your contact or group.
- `filename` (Path): The path to your sacred document.
- `message` (Optional[str]): A secret message to accompany your file. 🕵️

**Usage Example**:
```python
whatsapp_demon.send_file("Scroll Keepers", "path/to/ancient-scroll.pdf", "The wisdom of the ancients. 📜")
```
<br/>

### `fetch_all_unread_chats(self, limit: bool = True, top: int = 50)`

- **🔍 Purpose**: Embark on a quest to discover unread chat messages, unearthing hidden treasures. A digital adventure awaits! 🏴‍☠️

- `limit` (bool): Set to `True` to limit the number of chat messages fetched.
- `top` (int): Number of chat messages to retrieve if `limit` is set to `True. 🔎

**Usage Example**:
```python
unread_chats = whatsapp_demon.fetch_all_unread_chats(top=10)  # The uncharted chats reveal their secrets! 🌟
```
<br/>

### `logout(self)`

- **🚪 Purpose**: When your adventure reaches its conclusion, close the WhatsApp Web realm gracefully. Until the next epic quest! 👋🌄

**Usage Example**:
```python
whatsapp_demon.logout()  # Farewell, brave adventurer! Your journey continues elsewhere. 🏰
```
<br/>

### `close(self)`

- **👋 Purpose**: Close the magical gateway, freeing your browser from the spells and releasing the captive resources. Break the spell of the digital world! 👋

**Usage Example**:
```python
whatsapp_demon.close()  # Farewell, until we meet again! 👋
```

Experience the magic and explore the world of WhatsApp Web with `Demon`. Your digital adventure awaits! 🌐🌟
