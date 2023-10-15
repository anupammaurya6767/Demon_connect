===============================
🌟 Demon Connect - WhatsApp API 🌟
===============================

.. image:: https://github.com/anupammaurya6767/Demon_connect/blob/main/assets/main.png
   :align: right
   :width: 230px

.. contents::
   :local:
   :backlinks: none

Overview 👹
==========

Welcome to **Demon Connect - WhatsApp API**, your powerful tool for unleashing the potential of WhatsApp in your applications. This API allows you to integrate WhatsApp messaging into your projects with ease.

.. image:: https://github.com/anupammaurya6767/Demon_connect/blob/main/assets/sc1.jpeg
   :alt: Demon Connect Screenshot
   :align: center

Unleash the demon within as you explore the capabilities of this WhatsApp API. Transform your digital experience with the magic of **Demon Connect**.

Features ✨
==========

📲 **WhatsApp Integration**: Seamlessly integrate WhatsApp messaging into your applications.

📩 **Message Sending**: Send text messages, images, and videos programmatically.

🚀 **Group Messaging**: Engage with WhatsApp group chats via the API.

🪄 **Customization**: Customize and extend the API to suit your project's needs.

Usage 📱
========

1. Install **Demon Connect - WhatsApp API** in your Python project.

2. Initialize the API and connect to WhatsApp Web.

3. Send messages and media programmatically to your WhatsApp contacts.

4. Explore advanced features and customization options.

.. image:: https://github.com/anupammaurya6767/Demon_connect/blob/main/assets/sc2.jpeg
   :alt: Demon Connect Demo
   :align: center

Installation 🧙‍♂️
=================

1. Install Demon Connect via pip:

   .. code-block:: bash

      pip install demon-connect

2. Include Demon Connect in your Python project:

   .. code-block:: python

      from api.whatsapp_api import Demon

      # Initialize the API
      whatsapp_api = Demon()

      # Log in to WhatsApp Web
      whatsapp_demon.login()
    
      @whatsapp_demon.event
      def on_message(chat):
          print(f"New message from {chat.name}: {chat.message}")

      @whatsapp_demon.event
      def on_ready():
          print("Demon is ready!")
    
      chat = whatsapp_demon.open("Anupam Maurya")
      chat.send("HI")

Contributing 🌟
===============

Contributions are welcome! Feel free to open issues and pull requests to enhance the API's power.

Contributors
------------

See the list of contributors `here <https://github.com/anupammaurya6767/Demon_connect/graphs/contributors>`_.

License 📜
===========

This project is licensed under the **WhatsApp API License**. See the :doc:`LICENSE` file for details.

.. image:: https://github.com/anupammaurya6767/Demon_connect/blob/main/assets/sc3.jpeg
   :alt: API License Seal
   :align: center

Unlock the potential of WhatsApp in your applications with **Demon Connect - WhatsApp API**!
