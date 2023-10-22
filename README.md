# 🌟 Demon Connect - WhatsApp API 🌟

<img align='right' src="https://github.com/anupammaurya6767/Demon_connect/blob/main/main.png" width="230">

<p align="center">
  <a href="#Overview">Overview</a> •
  <a href="#Features">Features</a> •
  <a href="#Usage">Usage</a> •
  <a href="#Installation">Installation</a> •
  <a href="#Contributing">Contributing</a> •
  <a href="#License">License</a>
</p>
<br/>
<p align="center">
<a href="https://pypi.org/project/demon-connect/">
  <img src="https://img.shields.io/badge/demon-connect?logo=pypi&logoColor=blue&label=demon-connect&labelColor=white&color=black" alt="Demon" />
</a>
<img src="https://readthedocs.org/projects/demon_connect/badge/?version=latest" alt="Docs" ><a href="https://demon-connect.readthedocs.io/" /></img>
<img src="https://img.shields.io/github/license/anupammaurya6767/Demon_connect" alt="License" ><a href="#" /></img>
<a href="https://chat.whatsapp.com/FGV7ef4d9tNGtfN8HDvbim"><img src="https://badges.aleen42.com/src/whatsapp.svg" alt="Whatsapp" /></a>
</p>

## Overview 👹

Welcome to **Demon Connect - WhatsApp API**, your powerful tool for unleashing the potential of WhatsApp in your applications. This API allows you to integrate WhatsApp messaging into your projects with ease.

<p align="center">
  <img src="https://github.com/anupammaurya6767/Demon_connect/blob/main/sc1.jpeg" alt="Demon Connect Screenshot">
</p>

Unleash the demon within as you explore the capabilities of this WhatsApp API. Transform your digital experience with the magic of **Demon Connect**.

## Features ✨

📲 **WhatsApp Integration**: Seamlessly integrate WhatsApp messaging into your applications.

📩 **Message Sending**: Send text messages, images, and videos programmatically.

🚀 **Group Messaging**: Engage with WhatsApp group chats via the API.

🪄 **Customization**: Customize and extend the API to suit your project's needs.

## Usage 📱

1. Install **Demon Connect - WhatsApp API** in your Python project.

2. Initialize the API and connect to WhatsApp Web.

3. Send messages and media programmatically to your WhatsApp contacts.

4. Explore advanced features and customization options.

<p align="center">
  <img src="https://github.com/anupammaurya6767/Demon_connect/blob/main/sc2.jpeg" alt="Demon Connect Demo">
</p>

## Installation 🧙‍♂️

1. Install Demon Connect via pip:
   ```bash
   pip install demon-connect
   ```

2. Include Demon Connect in your Python project:
   ```python
    from demon_connect.whatsapp_api import Demon

    # Initialize the API
    whatsapp_demon = Demon()

    # Log in to WhatsApp Web
    whatsapp_demon.login()

    # Send a message
     message = "heyy"
     contact = "Grp"
     whatsapp_demon.send_message(contact,message)
     whatsapp_demon.delete_message(contact,message)

    # Send an image (provide the path to the image file)
     image_path = r"C:\Users\raman\Downloads\aatman.jpg"
     contact = "Grp"
     whatsapp_demon.send_image(contact,image_path)


    # Send a video (provide the path to the video file)
     video_path = "path/to/your/video.mp4"
     whatsapp_demon.send_video(contact,video_path)

    # tag all in group
     group_name = "Grp"
     whatsapp_demon.tag_all(group_name)

    @whatsapp_demon.event
    def on_message(chat):
        print(f"New message from {chat.name}: {chat.message}")

    @whatsapp_demon.event
    def on_ready():
    print("Demon is ready!")
  
    chat = whatsapp_demon.open("Anupam Maurya")
    chat.send("HI")

   ```

## Contributing 🌟

Contributions are welcome! Feel free to open issues and pull requests to enhance the API's power.

## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
<a href="https://github.com/anupammaurya6767/Demon_connect/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=anupammaurya6767/Demon_connect" />
</a>

## License 📜

This project is licensed under the **WhatsApp API License**. See the [LICENSE](LICENSE) file for details.

<p align="center">
  <img src="https://github.com/anupammaurya6767/Demon_connect/blob/main/image.png" alt="API License Seal">
</p>

Unlock the potential of WhatsApp in your applications with **Demon Connect - WhatsApp API**!
