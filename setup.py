from os import path
from setuptools import setup, find_packages

# read the contents of your description file

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="demon_connect",
    version="1.0.0",
    description= "Welcome to Demon Connect - WhatsApp API, your powerful tool for unleashing the potential of WhatsApp in your applications. This API allows you to integrate WhatsApp messaging into your projects with ease.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anupammaurya6767/Demon_connect",
    download_url="https://github.com/anupammaurya6767/Demon_connect/archive/refs/tags/latest.zip",
    author="Anupam Maurya",
    author_email="anupammaurya981@gmail.com",
    license="GNU general public license",
    packages=find_packages(),
    keywords=[
        "demon_connect",
        "python-whatsapp",
        "PyWhatsApp",
        "pywhatsapp",
        "python-whatsapp-wrapper",
        "whatsapp API",
        "automate whatsapp"
    ],
    install_requires=[
        "qrcode",
        "selenium",
        "webdriver-manager",
        "typing-extensions",
        "pathlib2",
        "moviepy",
        "imageio[ffmpeg]",
        "bs4",
        "colorama"
    ],
    include_package_data=False,
    python_requires=">=3.10",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: GNU general public License",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11"
    ],
)