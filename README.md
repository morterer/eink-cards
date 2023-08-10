# Purpose
Generate bitmaps to be displayed on a [Adafruit 2.9" Grayscale eInk / ePaper Display FeatherWing - 4 Level Grayscale](https://www.adafruit.com/product/4777)

# Setup
1. Create a Python virtual environment

    `python3 -m venv venv`
1. Activate virtual environment

    `source ./venv/bin/activate`
1. Install dependencies

    `pip3 install -r requirements.txt`

# Usage
1. Add text to quotes.txt files.  A bitmap will be created for each line in the file
1. Run `python3 snarkcard.py`
1. Bitmaps will be created in output directory

# Notes
- Instructions were tested and verified on an Ubuntu Linux system.  Minor changes may be needed for Windows or OSX platforms