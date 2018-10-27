# Flipkart-auto_buy_Bot

Automates purchases for Flpkart.com, this is a python script for auto add product in flipkart cart

# Usage:

#### STEP ONE
```
$ git clone https://github.com/Dipeshpal/Flipkart-auto_buy_Bot
$ cd supreme-bot
$ virtualenv venv --python=python3.7
$ pip install -r requirements.txt
```

#### STEP TWO
Create a config.py file in the local directory that looks similar to this for each order you are placing.

```
keys = {
        "product_url": "Flipkart Product Url Only",
        "email": "youremail@domain",
        "password": "Your_Password",       
}
```

#### STEP THREE
You may have to download the correct chromedriver for you operating system (Linux/OSX/Windows), put the chromedriver.exe in the Flipkart-auto_buy_Bot directory with the script.

chromdriver: http://chromedriver.chromium.org/downloads

#### STEP FOUR
```
$ python bot.py
```
