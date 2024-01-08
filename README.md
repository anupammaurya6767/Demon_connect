# 🌟 Demon Connect - WhatsApp API 🌟

<img align='right' src="https://github.com/anupammaurya6767/Demon_connect/blob/main/assets/main.png" width="230">

<p align="center">
  <a href="#overview-">Overview</a> •
  <a href="#features-">Features</a> •
  <a href="#usage-">Usage</a> •
  <a href="#installation">Installation</a> •
  <a href="#contributing-">Contributing</a> •
  <a href="#license-">License</a>
</p>
<br/>
<p align="center">
<a href="https://pypi.org/project/demon-connect/">
  <img src="https://img.shields.io/badge/demon-connect?style=plastic&logo=pypi&logoColor=blue&label=demon-connect&labelColor=white&color=black" alt="Demon" />
</a>&nbsp;
<a href="https://demon-connect.readthedocs.io">
    <img alt="Static Badge" src="https://img.shields.io/badge/Docs-Demon-rgb?style=plastic&labelColor=black" alt="Docs">
</a>&nbsp;
<a href="LICENSE">
    <img src="https://img.shields.io/github/license/anupammaurya6767/Demon_connect?style=plastic&labelColor=black&color=yellow" alt="License">
</a>&nbsp;
<img alt="GitHub forks" src="https://img.shields.io/github/forks/anupammaurya6767/Demon_connect?style=plastic&labelColor=black&color=blue">&nbsp;
<a href="https://chat.whatsapp.com/FGV7ef4d9tNGtfN8HDvbim">&nbsp;
<img src="https://badges.aleen42.com/src/whatsapp.svg?style=plastic&labelColor=black" alt="Whatsapp" /></a>
</p>

## Overview 👹

**Demon Connect - WhatsApp API** is the ultimate tool for WhatsApp magic. 🧙‍♂️

With this API, you can:

- Send and receive texts, images, and videos through WhatsApp
- Join WhatsApp group chats and interact with other users
- Customize the API to fit your project’s needs

**Demon Connect** is perfect for any app that wants to improve customer engagement, automate messaging, or just have fun with WhatsApp API.

Ready to start your adventure with **Demon Connect**? Join us today and unleash the power of WhatsApp in your apps!🔥

<br/>

## API Documentation 📚

This project provides a powerful API for interacting with WhatsApp Web. The API is implemented in the `whatsapp_api.py` module and is documented in detail in the [API Documentation]((Documentation/API.md)).

<br/>

## Features ✨

📲 **WhatsApp Integration**: Seamlessly integrate WhatsApp messaging into your applications.

📩 **Message Sending**: Send text messages, images, and videos programmatically.

🚀 **Group Messaging**: Engage with WhatsApp group chats via the API.

🔧 **Customization**: Customize and extend the API to suit your project's needs.

<br/>

## Usage 📱

1. Install **Demon Connect - WhatsApp API** in your Python project.

2. Initialize the API and connect to WhatsApp Web.

3. Send messages and media programmatically to your WhatsApp contacts.

4. Explore advanced features and customization options.

<p align="center">
   <img src="https://github.com/anupammaurya6767/Demon_connect/blob/main/assets/sc2.jpeg" alt="Demon Connect Demo">
</p>

<br/>

## Installation <a name="installation"></a>🧙‍♂️

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

<br/>

## Contributing 🌟
First off, thank you for considering contributing to our project! 🎉 We value all our contributors and we’re excited to see how you can make this project even better.

Before you start, we ask everyone to adhere to our [Code of Conduct](CODE_OF_CONDUCT.md). It’s important to us that we maintain a positive and inclusive environment for everyone in our community.

Next, take a moment to familiarize yourself with our [API Documentation](Documentation/API.md). Understanding the API is key to making meaningful contributions.

We also have a specific [workflow for contributions](WORKFLOW.md). This will give you an understanding of how we like to do things and make it easier for us to integrate your contributions.

Now, you’re ready to start contributing! Whether it’s enhancing features, fixing bugs, or improving documentation, every contribution counts. Remember, the best way to contribute is to start small. Find a task in the project that you feel comfortable with and start there.

If you ever get stuck or need help, don’t hesitate to reach out. We’re a community, and we’re here to help each other. You can join our community [WhatsApp group](https://chat.whatsapp.com/FGV7ef4d9tNGtfN8HDvbim). Happy coding! 😊

<br/>

## Security Policy 🔒

We take the security of our project seriously. For details on which versions of the project are currently being supported with security updates and how to report a vulnerability, please see our [Security Policy](SECURITY.md).

<br/>

## Contributors 🤝

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
<a href="https://github.com/anupammaurya6767/Demon_connect/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=anupammaurya6767/Demon_connect" />
</a>

<br/>

## License 📜

This project is licensed under the **WhatsApp API License**. See the [LICENSE](LICENSE) file for details.

<p align="center">
   <img src="https://github.com/anupammaurya6767/Demon_connect/blob/main/assets/image.png" alt="API License Seal">
</p>

Unlock the potential of WhatsApp in your applications with **Demon Connect - WhatsApp API**!
