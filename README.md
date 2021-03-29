# KDE-Connect-Telegram
Free open source bot to control your KDE plasma desktop using Telegram

# Dependencies
1) KDE-Plasma Desktop and Apps
2) Python 3.8.5 or above
3) python-telegram-bot library

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
