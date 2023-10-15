add_caption.py
=============

Documentation for `add_caption.py` in the `Demon_connect` Repository

The `add_caption.py` file contains the `add_caption` function, which is used to add a caption to media (image, video, or file) before sending it on WhatsApp Web.

Function
--------

`add_caption(driver, message: str, media_type: str = "image")`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adds a caption to media (image, video, or file) before sending.

Arguments
^^^^^^^^^^

- `driver` (WebDriver): The Selenium WebDriver instance used to interact with the browser.
- `message` (str): The caption text to add.
- `media_type` (str, optional): The type of media to add the caption to (image, video, or file). Defaults to "image".

Usage
^^^^^

The `add_caption` function can be used to add a caption to media before sending it on WhatsApp Web. It takes in the `driver` instance, caption `message`, and optional `media_type` as parameters. The `media_type` parameter determines the type of media to add the caption to, with "image" being the default value.

.. code:: python

   from selenium import webdriver
   from Demon_connect.features.extras.add_caption import add_caption

   # Create a Selenium WebDriver instance
   driver = webdriver.Chrome()

   # Log in to WhatsApp Web

   # Send an image with a caption
   add_caption(driver, "Check out this image!", media_type="image")

   # Send a video with a caption
   add_caption(driver, "Watch this video!", media_type="video")

   # Send a file with a caption
   add_caption(driver, "Here's a document for you.", media_type="file")

   # Close the browser
   driver.quit()

Note
^^^^

Ensure that you have logged in to WhatsApp Web using the `Demon` class from the `whatsapp_api.py` file before using the `add_caption` function.

See also
^^^^^^^^

The following files are linked to `Demon_connect/features/extras/add_caption.py`:
- [Demon_connect/api/whatsapp_api.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/api/whatsapp_api.py)
- [Demon_connect/drivers/chromedriver.exe](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/drivers/chromedriver.exe)
- [Demon_connect/features/extras/convert_bytes.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/features/extras/convert_bytes.py)
- [Demon_connect/features/extras/convert_bytes_to.py](?full_repo_name=anupammaurya6767/Demon_connect&filename=Demon_connect/features/extras/convert_bytes_to.py)
