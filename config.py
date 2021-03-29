from os import path

ADMIN_USERID: int = int('YOUR-USER-ID-HERE')
TOKEN: str = 'YOUR-BOT-TOKEN-HERE'

APP_FOLDER_NAME: str = 'KDE_Connect_Telegram'
HOME_DIR = path.expanduser("~")
APP_PATH: str = f"{HOME_DIR}/{APP_FOLDER_NAME}"
PIC_PATH: str = f'{APP_PATH}/Pictures'
VIDEO_PATH: str = f'{APP_PATH}/Videos'
FILE_PATH: str = f'{APP_PATH}/Documents'
VOICE_PATH: str = f'{APP_PATH}/Voices'
AUDIO_PATH: str = f'{APP_PATH}/Audios'
