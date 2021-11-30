import telegram
from buttons import tele_buttons

def main_menu_keyboard():
    keyboard=([
        [telegram.KeyboardButton(tele_buttons[0])],
        [telegram.KeyboardButton(tele_buttons[1])]
        ])
    return telegram.ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)
