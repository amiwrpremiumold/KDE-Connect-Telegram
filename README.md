# KDE-Connect-Telegram
Free open source bot to control your KDE plasma desktop using Telegram

# Dependencies
1) KDE-Plasma Desktop and Apps
2) Python 3.8.5 or above
3) python-telegram-bot library
4) streamer package (to capture webcam photo). Install using 
   `sudo apt-get install streamer`

# Configuration
1) Make a new bot using [@BotFather]('https://t.me/BotFather') 
2) Copy token that BotFather gave you and edit "TOKEN" value in `config.py`
3) Send a message to [@chatIDrobot](https://t.me/chatIDrobot) to get your chat/user ID
4) edit "ADMIN_USERID" value in `config.py` with the on that @chatIDrobot sent you
5) [OPTIONAL] Line 6 to 13 in `config.py` is app directory settings. By default, it makes a folder named 
   "KDE_Connect_Telegram" in your Home directory and "Pictures", "Videos",
   "Documents", "Voices", "Audios" subfolders as you use the bot. You can
   change them with your desired path

# How To Use
To run script manually use: <br>
`python3 bot.py`

<br>

To make bot run at startup:
1) Make it executable using `sudo chmod +x bot.py`
2) Go to "System Settings" > "Startup and Shutdown" > "Autostart". Click on 
"Add Script" button. Enter `bot.py` path, and you're done
   
# Features
Currently, it has 6 different categories of commands:
1) States
2) Connections (Bluetooth to be more exact) [UNDER MAINTENANCE]
3) Brightness control
4) Volume control
5) Screenshot
6) Utilities or other

### States
1) Shutdown 
2) Reboot
3) Suspend
4) Hibernate
5) Lock screen
6) Unlock screen
7) Screen off
8) Screen on
9) Lock keyboard and mouse
10) Unlock keyboard and mouse

### Connections
1) Connect 
2) Disconnect
3) Pair
4) Remove

### Brightness control
1) Increase brightness
2) Decrease brightness
3) Maximum brightness

### Volume control
1) Increase volume
2) Decrease volume
3) Mute
4) Mute microphone

### Screenshot
1) Screenshot full screen 
2) Screenshot active screen
3) Screenshot full screen and send to telegram
4) Screenshot active screen and send to telegram

### Utilities or other
Basically, every other thing that I couldn't categorize goes here. 
I still don't know what can I add here
