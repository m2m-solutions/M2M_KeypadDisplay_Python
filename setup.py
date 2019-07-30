from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="m2m-keypaddisplay",
    version="0.2.0",
    author="Jonny Bergdahl",
    author_email="jonny@bergdahl.it",
    description="Python module for handling the M2M Keypad/Display module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://m2msolutions.se",
    packages=find_packages(),
    install_requires=[
        "gpiozero",
        "Adafruit-Blinka",
        "CircuitPython_LCD"
    ],
    classifiers=[
        "Development Status :: 4 - Beta"
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License"
        "Operating System :: OS Independent",
    ]
)
