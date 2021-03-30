#!/usr/bin/env python3

from myCommands import *
from config import *

from os import system, popen, mkdir, path
from datetime import datetime
from time import sleep
from re import findall

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
from telegram import error


ADMIN: int = ADMIN_USERID
file_name_regex = r'.*\/(.*)(?=)'


def dir_maker(parent_folder: str, folder_name: str):
    if not path.isdir(f"{parent_folder}/{folder_name}"):
        mkdir(f"{parent_folder}/{folder_name}")


def file_name_generator():
    return str(datetime.now().strftime('%Y%m%d_%H%M%S'))


def passer(uid: int):
    if uid == ADMIN:
        return True
    else:
        return False


class Keyboards:
    def __init__(self):
        self.home_keyboard = [
            ['🎛️ States', '⚡️ Bluetooth'],
            ['💡 Brightness', '🔈 Volume'],
            ['📸 Capture', '⚙️ Utilities']
        ]
        self.home_markup = ReplyKeyboardMarkup(self.home_keyboard)

        self.states_keyboard = [
            ['📴 Shutdown', '🔄 Reboot'],
            ['⏸️ Suspend', '💤 Hibernate'],
            ['🔒 Lock Screen', '🔓Unlock Screen'],
            ['⚪ ️Screen On', '⚫️ Screen Off'],
            ['🔒 Lock keyboard & Mouse', '🔓Unlock keyboard & Mouse'],
            ['🏠 Home'],
        ]
        self.states_markup = ReplyKeyboardMarkup(self.states_keyboard, resize_keyboard=True)

        self.brightness_keyboard = [
            ['🔆 Up', '🔅 Down'],
            ['📈 Maximum'],
            ['🏠 Home']
        ]
        self.brightness_markup = ReplyKeyboardMarkup(self.brightness_keyboard, one_time_keyboard=False)

        self.volume_keyboard = [
            ['🔊 Up', '🔉 Down'],
            ['🔇 Mute', '🎙 Mute Mic'],
            ['🏠 Home']
        ]
        self.volume_markup = ReplyKeyboardMarkup(self.volume_keyboard, one_time_keyboard=False)

        self.screenshot_keyboard = [
            ['🖥 Fullscreen', '🖥 Active window'],
            ['🖥 Fullscreen Here', '🖥 Active window Here'],
            ['📸 Webcam'],
            ['🏠 Home']
        ]
        self.screenshot_markup = ReplyKeyboardMarkup(self.screenshot_keyboard, one_time_keyboard=False)


keyboards = Keyboards()


dir_maker(HOME_DIR, APP_FOLDER_NAME)


class Bot:
    def __init__(self):
        self.main()

    @staticmethod
    def start_command(update: Update, context: CallbackContext) -> None:
        if passer(update.message.from_user.id):
            update.message.reply_text('Welcome Boss', reply_markup=keyboards.home_markup)
        else:
            update.message.reply_text('Fuck Off')
        return

    @staticmethod
    def states(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            update.message.reply_text('🔹 Choose One 🔹', reply_markup=keyboards.states_markup)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def shutdown(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            keyboard = [
                [
                    InlineKeyboardButton("✅ Yea", callback_data='YES SHUTDOWN'),
                    InlineKeyboardButton('❌ No', callback_data="NO SHUTDOWN")
                ]
            ]
            update.message.reply_text(
                'Are You Sure You Want To Shutdown?',
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def reboot(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            keyboard = [
                [
                    InlineKeyboardButton("✅ Yea", callback_data='YES REBOOT'),
                    InlineKeyboardButton('❌ No', callback_data="NO REBOOT")
                ]
            ]
            update.message.reply_text(
                'Are You Sure You Want To Reboot?',
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def suspend(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            update.message.reply_text('Suspended', reply_markup=keyboards.states_markup)
            system(Suspend)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def hibernate(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            update.message.reply_text('Hibernated', reply_markup=keyboards.states_markup)
            system(Hibernate)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def lock_screen(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            update.message.reply_text('Screen Locked', reply_markup=keyboards.states_markup)
            system(Lock_screen)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def unlock_screen(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            update.message.reply_text('Screen Unlocked', reply_markup=keyboards.states_markup)
            system(Unlock_screen)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def turn_off_screen(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            update.message.reply_text('Screen Turned Off', reply_markup=keyboards.states_markup)
            system(Turn_off_screen)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def turn_on_screen(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            update.message.reply_text('Screen Turned On', reply_markup=keyboards.states_markup)
            system(Turn_on_screen)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def lock_keyboard_and_mouse(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            update.message.reply_text('Keyboard & Mouse Locked', reply_markup=keyboards.states_markup)
            system(Lock_keyboard_and_mouse)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def unlock_keyboard_and_mouse(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            update.message.reply_text('Keyboard & Mouse Unlocked', reply_markup=keyboards.states_markup)
            system(Unlock_keyboard_and_mouse)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def bluetooth(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            keyboard = [
                ['Connect', 'Disconnect'],
                ['Pair', 'Remove']
            ]
            update.message.reply_text('🔹 Choose One 🔹',
                                      reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True))
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def brightness(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            update.message.reply_text('Up And Down', reply_markup=keyboards.brightness_markup)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def brightness_up(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            system(Brightness_Up)
            update.message.reply_text('🔆 Brightness Increased', reply_markup=keyboards.brightness_markup)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def brightness_down(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            system(Brightness_Down)
            update.message.reply_text('🔅 Brightness Decreased', reply_markup=keyboards.brightness_markup)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def brightness_max(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            system(Brightness_Maximum)
            update.message.reply_text('📈 Maximum Brightness', reply_markup=keyboards.brightness_markup)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def volume(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            update.message.reply_text('Up And Down', reply_markup=keyboards.volume_markup)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def volume_up(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            system(Volume_up)
            update.message.reply_text('🔊 Volume Increased', reply_markup=keyboards.volume_markup)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def volume_down(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            system(Volume_down)
            update.message.reply_text('🔉 Volume Decreased', reply_markup=keyboards.volume_markup)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def mute(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            system(Mute)
            update.message.reply_text('🔇 Muted', reply_markup=keyboards.volume_markup)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def mute_mic(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            system(Mute_microphone)
            update.message.reply_text('🎙 Microphone Muted', reply_markup=keyboards.volume_markup)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def capture(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            update.message.reply_text('🔹 Choose One 🔹',
                                      reply_markup=keyboards.screenshot_markup)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def screen_shot_fullscreen(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            system(f'spectacle -b')
            update.message.reply_text('Captured', reply_markup=keyboards.screenshot_markup)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def screen_shot_active(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            system(f'spectacle -a -b')
            update.message.reply_text('Captured', reply_markup=keyboards.screenshot_markup)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def screen_shot_fullscreen_to_phone(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            file_name = f"/home/amiwr/Pictures/Screenshot/Screenshot_{file_name_generator()}.png"
            system(f'spectacle -b -n -o {file_name}')
            sleep(0.5)
            update.message.reply_photo(photo=open(file_name, 'rb'),
                                       caption=str(file_name),
                                       reply_markup=keyboards.screenshot_markup)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def screen_shot_active_to_phone(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            file_name = f"/home/amiwr/Pictures/Screenshot/Screenshot_{file_name_generator()}.png"
            system(f'spectacle -a -n -b -o {file_name}')
            sleep(0.5)
            update.message.reply_photo(photo=open(file_name, 'rb'),
                                       caption=str(file_name),
                                       reply_markup=keyboards.screenshot_markup)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def webcam(update: Update, context: CallbackContext):
        if passer(update.message.from_user.id):
            file_name = f"{APP_PATH}/{PIC_PATH}/{file_name_generator()}.jpeg"
            system(f'streamer -f jpeg -o {file_name}')
            try:
                update.message.reply_photo(file_name, caption=file_name)
            except Exception as e:
                update.message.reply_text(f'⚠️ Failed To Complete The Task Due To Below Error:\n\n'
                                          f'<code>{str(e)}</code>',
                                          parse_mode=ParseMode.HTML)
        else:
            update.message.reply_text('Fuck Off')

    @staticmethod
    def button(update: Update, context: CallbackContext):
        query = update.callback_query
        query.answer()
        chose = query.data

        if chose == 'YES SHUTDOWN':
            query.edit_message_text('Hope You Thought This Through!\n\n'
                                    '✅ Shutting Down...')
            system(Shutdown)
        if chose == 'NO SHUTDOWN':
            query.edit_message_text('❌ Canceled')
        if chose == 'YES REBOOT':
            query.edit_message_text('Hope You Thought This Through!\n\n'
                                    '✅ Rebooting...')
            system(Reboot)
        if chose == 'NO REBOOT':
            query.edit_message_text('❌ Canceled')

    @staticmethod
    def photo(update: Update, context: CallbackContext):
        try:
            media = update.message.photo[-1].file_id
            pic_file = context.bot.get_file(media)
            file_path = pic_file.file_path
            file_name = findall(file_name_regex, file_path)[0]
            dir_maker(APP_PATH, "Pictures")
            pic_file.download(custom_path=f"{PIC_PATH}/{file_name}")

            update.message.reply_text(f'Saved in {PIC_PATH} as: {file_name}')
        except Exception as e:
            update.message.reply_text(f'⚠️ Failed To Complete The Task Due To Below Error:\n\n'
                                      f'<code>{str(e)}</code>',
                                      parse_mode=ParseMode.HTML)

    @staticmethod
    def video(update: Update, context: CallbackContext):
        try:
            media = update.message.video.file_id
            pic_file = context.bot.get_file(media)
            file_path = pic_file.file_path
            file_name = findall(file_name_regex, file_path)[0]
            dir_maker(APP_PATH, "Videos")
            pic_file.download(custom_path=f"{VIDEO_PATH}/{file_name}")

            update.message.reply_text(f'Saved in {VIDEO_PATH} as: {file_name}')
        except Exception as e:
            update.message.reply_text(f'⚠️ Failed To Complete The Task Due To Below Error:\n\n'
                                      f'<code>{str(e)}</code>',
                                      parse_mode=ParseMode.HTML)

    @staticmethod
    def file(update: Update, context: CallbackContext):
        try:
            media = update.message.document.file_id
            pic_file = context.bot.get_file(media)
            file_path = pic_file.file_path
            file_name = findall(file_name_regex, file_path)[0]
            dir_maker(APP_PATH, "Documents")
            pic_file.download(custom_path=f"{FILE_PATH}/{file_name}")

            update.message.reply_text(f'Saved in {FILE_PATH} as: {file_name}')
        except Exception as e:
            update.message.reply_text(f'⚠️ Failed To Complete The Task Due To Below Error:\n\n'
                                      f'<code>{str(e)}</code>',
                                      parse_mode=ParseMode.HTML)

    @staticmethod
    def voice(update: Update, context: CallbackContext):
        try:
            media = update.message.voice.file_id
            pic_file = context.bot.get_file(media)
            file_path = pic_file.file_path
            file_name = findall(file_name_regex, file_path)[0]
            dir_maker(APP_PATH, "Voices")
            pic_file.download(custom_path=f"{VOICE_PATH}/{file_name}")

            update.message.reply_text(f'Saved in {VOICE_PATH} as: {file_name}')
        except Exception as e:
            update.message.reply_text(f'⚠️ Failed To Complete The Task Due To Below Error:\n\n'
                                      f'<code>{str(e)}</code>',
                                      parse_mode=ParseMode.HTML)

    @staticmethod
    def audio(update: Update, context: CallbackContext):
        try:
            media = update.message.audio.file_id
            pic_file = context.bot.get_file(media)
            file_path = pic_file.file_path
            file_name = findall(file_name_regex, file_path)[0]
            dir_maker(APP_PATH, "Audios")
            pic_file.download(custom_path=f"{AUDIO_PATH}/{file_name}")

            update.message.reply_text(f'Saved in {AUDIO_PATH} as: {file_name}')
        except Exception as e:
            update.message.reply_text(f'⚠️ Failed To Complete The Task Due To Below Error:\n\n'
                                      f'<code>{str(e)}</code>',
                                      parse_mode=ParseMode.HTML)

    def main(self):
        updater = Updater(TOKEN, use_context=True)
        dpa = updater.dispatcher.add_handler

        dpa(CommandHandler('start', self.start_command))

        dpa(MessageHandler(Filters.regex('^🏠 Home$'), self.start_command))

        dpa(MessageHandler(Filters.regex('^🎛️ States$'), self.states))
        dpa(MessageHandler(Filters.regex('^📴 Shutdown$'), self.shutdown))
        dpa(MessageHandler(Filters.regex('^🔄 Reboot$'), self.reboot))
        dpa(MessageHandler(Filters.regex('^⏸️ Suspend$'), self.suspend))
        dpa(MessageHandler(Filters.regex('^💤 Hibernate$'), self.hibernate))
        dpa(MessageHandler(Filters.regex('^🔒 Lock Screen$'), self.lock_screen))
        dpa(MessageHandler(Filters.regex('^🔓 Unlock Screen$'), self.unlock_screen))
        dpa(MessageHandler(Filters.regex('^⚪ ️Screen On$'), self.turn_on_screen))
        dpa(MessageHandler(Filters.regex('^⚫️ Screen Off$'), self.turn_off_screen))
        dpa(MessageHandler(Filters.regex('^🔒 Lock keyboard & Mouse$'), self.lock_keyboard_and_mouse))
        dpa(MessageHandler(Filters.regex('^🔓 Unlock keyboard & Mouse$'), self.unlock_keyboard_and_mouse))

        dpa(MessageHandler(Filters.regex('^⚡️ Bluetooth$'), self.bluetooth))

        dpa(MessageHandler(Filters.regex('^💡 Brightness$'), self.brightness))
        dpa(MessageHandler(Filters.regex('^🔆 Up$'), self.brightness_up))
        dpa(MessageHandler(Filters.regex('^🔅 Down$'), self.brightness_down))
        dpa(MessageHandler(Filters.regex('^📈 Maximum$'), self.brightness_max))

        dpa(MessageHandler(Filters.regex('^🔈 Volume$'), self.volume))
        dpa(MessageHandler(Filters.regex('^🔊 Up$'), self.volume_up))
        dpa(MessageHandler(Filters.regex('^🔉 Down$'), self.volume_down))
        dpa(MessageHandler(Filters.regex('^🔇 Mute$'), self.mute))
        dpa(MessageHandler(Filters.regex('^🎙 Mute Mic$'), self.mute_mic))

        dpa(MessageHandler(Filters.regex('^📸 Capture$'), self.capture))
        dpa(MessageHandler(Filters.regex('^🖥 Fullscreen$'), self.screen_shot_fullscreen))
        dpa(MessageHandler(Filters.regex('^🖥 Active window$'), self.screen_shot_active))
        dpa(MessageHandler(Filters.regex('^🖥 Fullscreen Here$'), self.screen_shot_fullscreen_to_phone))
        dpa(MessageHandler(Filters.regex('^🖥 Active window Here$'), self.screen_shot_active_to_phone))
        dpa(MessageHandler(Filters.regex('^📸 Webcam$'), self.webcam))

        dpa(CallbackQueryHandler(self.button))

        dpa(MessageHandler(Filters.photo, self.photo))
        dpa(MessageHandler(Filters.video, self.video))
        dpa(MessageHandler(Filters.document, self.file))
        dpa(MessageHandler(Filters.voice, self.voice))
        dpa(MessageHandler(Filters.audio, self.audio))

        updater.start_polling()
        updater.idle()


def main():
    try:
        Bot()
    except error.TimedOut:
        print('Exception 1')
        main()
    except error.NetworkError:
        print('Exception 2')
        main()


if __name__ == '__main__':
    try:
        main()
    except error.TimedOut:
        print('Exception 3')
        main()
    except error.NetworkError:
        print('Exception 4')
        main()


# TODO Add notification sender
# TODO Add speed test
# TODO Add Battery Percentage
