import re
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from telegram.ext import(
    CallbackContext,
    Updater,
    CommandHandler,
    PicklePersistence,
    MessageHandler,
    Filters,
    CallbackQueryHandler
)
from ssylka import PTT
from menu import main_menu_keyboard
from buttons import tele_buttons
from spisok_knig import (
    detektiv1,
    fantastika1,
    priklucheniya1,
    sovremennyi1,
    amerikanskaya1,
    britanskaya1,
    zarubeznaya1,
    russkaya1,
    detektiv2,
    fantastika2,
    priklucheniya2,
    sovremennyi2,
    amerikanskaya2,
    britanskaya2,
    zarubeznaya2,
    russkaya2,
    detektiv3,
    fantastika3,
    priklucheniya3,
    sovremennyi3,
    amerikanskaya3,
    britanskaya3,
    zarubeznaya3,
    russkaya3
)
from otzyvy import(
    d1, 
    d2,
    d3,
    f1,
    f2,
    f3,
    p1,
    p2,
    p3,
    s1,
    s2,
    s3,
    a1,
    a2,
    a3,
    b1,
    b2,
    b3,
    z1,
    z2,
    z3,
    r1,
    r2,
    r3,
)

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Добро пожаловать, {username}, выберите опцию: '.format(
            username=update.effective_user.first_name \
                if update.effective_user.first_name is not None \
                    else update.effective_user.username
        ),
        reply_markup=main_menu_keyboard()
    )

JANR_REGEX=r"(?=("+(tele_buttons[0])+r"))"
OTZYV_REGEX=r"(?=("+(tele_buttons[1])+r"))"


# def janr_inline_menu(update: Update, context: CallbackContext):
#     msg = update.message.text
#     if msg in spisok_knig:

def janr_inline_menu(update: Update, context: CallbackContext):
    info=re.match(JANR_REGEX, update.message.text)
    keyboard=[
        [InlineKeyboardButton('Детектив', callback_data='detektiv')],
        [InlineKeyboardButton('Фантастика', callback_data='fantastika')],
        [InlineKeyboardButton('Приключения', callback_data='priklucheniya')],
        [InlineKeyboardButton('Современный Роман', callback_data='sovremennyi')],
        [InlineKeyboardButton('Амаериканская классика', callback_data='amerikanskaya')],
        [InlineKeyboardButton('Британская классика', callback_data='britanskaya')],
        [InlineKeyboardButton('Зарубежная классика', callback_data='zarubeznaya')],
        [InlineKeyboardButton('Русская классика', callback_data='russkaya')]
    ]
    reply_markup=InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'Выберите жанр:', 
        reply_markup=reply_markup
    )

def otzyv_inline_menu(update: Update, context: CallbackContext):
    info=re.match(OTZYV_REGEX, update.message.text)
    keyboard1=[
        [InlineKeyboardButton('ТАИНСТВЕННЫЙ ПРОТИВНИК', callback_data='d1')],
        [InlineKeyboardButton('ОБОРОТНАЯ СТОРОНА ПОЛУНОЧИ', callback_data='d2')],
        [InlineKeyboardButton('ГОЛОС НОЧНОЙ ПТИЦЫ', callback_data='d3')],
        [InlineKeyboardButton('ГАРРИ ПОТТЕР И ФИЛОСОФСКИЙ КАМЕНЬ', callback_data='f1')],
        [InlineKeyboardButton('ХРОНИКИ НАРНИИ: ЛЕВ, КОЛДУНЬЯ И ПЛАТЯНОЙ ШКАФ', callback_data='f2')],
        [InlineKeyboardButton('ВЛАСТЕЛИН КОЛЕЦ', callback_data='f3')],
        [InlineKeyboardButton('ГРАФ МОНТЕ-КРИСТО', callback_data='p1')],
        [InlineKeyboardButton('ТАИНСТВЕННЫЙ ОСТРОВ', callback_data='p2')],
        [InlineKeyboardButton('СОКРОВИЩЕ ДЖУНАИДА', callback_data='p3')],
        [InlineKeyboardButton('ВРЕМЯ СВИНГА', callback_data='s1')],
        [InlineKeyboardButton('ОСЕНЬ', callback_data='s2')],
        [InlineKeyboardButton('МЕДВЕЖИЙ УГОЛ', callback_data='s3')],
        [InlineKeyboardButton('МОБИ ДИК', callback_data='a1')],
        [InlineKeyboardButton('МАРТИН ИДЕН', callback_data='a2')],
        [InlineKeyboardButton('ПРОЩАЙ, ОРУЖИЕ!', callback_data='a3')],
        [InlineKeyboardButton('ГРОЗОВОЙ ПЕРЕВАЛ', callback_data='b1')],
        [InlineKeyboardButton('АЛИСА В СТРАНЕ ЧУДЕС И ЗАЗЕРКАЛЬЕ', callback_data='b2')],
        [InlineKeyboardButton('ЛУННЫЙ КАМЕНЬ', callback_data='b3')],
        [InlineKeyboardButton('СТО ЛЕТ ОДИНОЧЕСТВА', callback_data='z1')],
        [InlineKeyboardButton('1984', callback_data='z2')],
        [InlineKeyboardButton('ТРИ МУШКЕТЕРА', callback_data='z3')],
        [InlineKeyboardButton('ОТЦЫ И ДЕТИ', callback_data='r1')],
        [InlineKeyboardButton('БЕЛЫЕ НОЧИ', callback_data='r2')],
        [InlineKeyboardButton('ТИХИЙ ДОН', callback_data='r3')]
    ]
    reply_markup1=InlineKeyboardMarkup(keyboard1)
    update.message.reply_text(
        'Оставить отзыв на книгу:', 
        reply_markup=reply_markup1
    )



def inline_buttons(update: Update, context: CallbackContext):
    query=update.callback_query
    query.answer()
    keyboard=[
        [InlineKeyboardButton('Детектив', callback_data='detektiv')],
        [InlineKeyboardButton('Фантастика', callback_data='fantastika')],
        [InlineKeyboardButton('Приключения', callback_data='priklucheniya')],
        [InlineKeyboardButton('Современный Роман', callback_data='sovremennyi')],
        [InlineKeyboardButton('Амаериканская классика', callback_data='amerikanskaya')],
        [InlineKeyboardButton('Британская классика', callback_data='britanskaya')],
        [InlineKeyboardButton('Зарубежная классика', callback_data='zarubeznaya')],
        [InlineKeyboardButton('Русская классика', callback_data='russkaya')]
    ]
    reply_markup=InlineKeyboardMarkup(keyboard)

    if query.data=='detektiv':
        query.message.reply_text(
            text=detektiv1
        )
        query.message.reply_photo(
           open('d1.jpeg', 'rb')
        )
        query.message.reply_text(
            text=detektiv2
        )
        query.message.reply_photo(
            open('d2.jpeg', 'rb')
        )
        query.message.reply_text(
            text=detektiv3
        )
        query.message.reply_photo(
            open('d3.jpeg', 'rb')
        )
    if query.data=='fantastika':
        query.message.reply_text(
            text=fantastika1
        )
        query.message.reply_photo(
           open('f1.jpeg', 'rb')
        )
        query.message.reply_text(
            text=fantastika2
        )
        query.message.reply_photo(
            open('f2.jpeg', 'rb')
        )
        query.message.reply_text(
            text=fantastika3
        )
        query.message.reply_photo(
            open('f3.jpeg', 'rb')
        )
    if query.data=='priklucheniya':
        query.message.reply_text(
            text=priklucheniya1
        )
        query.message.reply_photo(
           open('p1.jpeg', 'rb')
        )
        query.message.reply_text(
            text=priklucheniya2
        )
        query.message.reply_photo(
            open('p2.jpeg', 'rb')
        )
        query.message.reply_text(
            text=priklucheniya3
        )
        query.message.reply_photo(
            open('p3.jpeg', 'rb')
        )
    if query.data=='sovremennyi':
        query.message.reply_text(
            text=sovremennyi1
        )
        query.message.reply_photo(
           open('s1.jpeg', 'rb')
        )
        query.message.reply_text(
            text=sovremennyi2
        )
        query.message.reply_photo(
            open('s2.jpeg', 'rb')
        )
        query.message.reply_text(
            text=sovremennyi3
        )
        query.message.reply_photo(
            open('s3.jpeg', 'rb')
        )
    if query.data=='amerikanskaya':
        query.message.reply_text(
            text=amerikanskaya1
        )
        query.message.reply_photo(
           open('a1.jpeg', 'rb')
        )
        query.message.reply_text(
            text=amerikanskaya2
        )
        query.message.reply_photo(
            open('a2.jpeg', 'rb')
        )
        query.message.reply_text(
            text=amerikanskaya3
        )
        query.message.reply_photo(
            open('a3.jpeg', 'rb')
        )
    if query.data=='britanskaya':
        query.message.reply_text(
            text=britanskaya1
        )
        query.message.reply_photo(
           open('b1.jpeg', 'rb')
        )
        query.message.reply_text(
            text=britanskaya2
        )
        query.message.reply_photo(
            open('b2.jpeg', 'rb')
        )
        query.message.reply_text(
            text=britanskaya3
        )
        query.message.reply_photo(
            open('b3.jpeg', 'rb')
        )
    if query.data=='zarubeznaya':
        query.message.reply_text(
            text=zarubeznaya1
        )
        query.message.reply_photo(
           open('z1.jpeg', 'rb')
        )
        query.message.reply_text(
            text=zarubeznaya2
        )
        query.message.reply_photo(
            open('z2.jpeg', 'rb')
        )
        query.message.reply_text(
            text=zarubeznaya3
        )
        query.message.reply_photo(
            open('z3.jpeg', 'rb')
        )
    if query.data=='russkaya':
        query.message.reply_text(
            text=russkaya1
        )
        query.message.reply_photo(
           open('r1.jpeg', 'rb')
        )
        query.message.reply_text(
            text=russkaya2
        )
        query.message.reply_photo(
            open('r2.jpeg', 'rb')
        )
        query.message.reply_text(
            text=russkaya3
        )
        query.message.reply_photo(
            open('r3.jpeg', 'rb')
        )
    if query.data=='d1':
        query.edit_message_text(
            text=d1
        )
    if query.data=='d2':
        query.edit_message_text(
            text=d2
        )
    if query.data=='d3':
        query.edit_message_text(
            text=d3
        )
    if query.data=='f1':
        query.edit_message_text(
            text=f1
        )
    if query.data=='f2':
        query.edit_message_text(
            text=f2
        )
    if query.data=='f3':
        query.edit_message_text(
            text=f3
        )
    if query.data=='p1':
        query.edit_message_text(
            text=p1
        )
    if query.data=='p2':
        query.edit_message_text(
            text=p2
        )
    if query.data=='p3':
        query.edit_message_text(
            text=p3
        )
    if query.data=='s1':
        query.edit_message_text(
            text=s1
        )
    if query.data=='s2':
        query.edit_message_text(
            text=s2
        )
    if query.data=='s3':
        query.edit_message_text(
            text=s3
        )
    if query.data=='a1':
        query.edit_message_text(
            text=a1
        )
    if query.data=='a2':
        query.edit_message_text(
            text=a2
        )
    if query.data=='a3':
        query.edit_message_text(
            text=a3
        )
    if query.data=='b1':
        query.edit_message_text(
            text=b1
        )
    if query.data=='b2':
        query.edit_message_text(
            text=b2
        )
    if query.data=='b3':
        query.edit_message_text(
            text=b3
        )
    if query.data=='z1':
        query.edit_message_text(
            text=z1
        )
    if query.data=='z2':
        query.edit_message_text(
            text=z2
        )
    if query.data=='z3':
        query.edit_message_text(
            text=z3
        )
    if query.data=='r1':
        query.edit_message_text(
            text=r1
        )
    if query.data=='r2':
        query.edit_message_text(
            text=r2
        )
    if query.data=='r3':
        query.edit_message_text(
            text=r3
        )

updater=Updater(PTT, persistence=PicklePersistence(filename='bot_data'))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(JANR_REGEX), janr_inline_menu))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(OTZYV_REGEX), otzyv_inline_menu))
updater.dispatcher.add_handler(CallbackQueryHandler(inline_buttons))
updater.start_polling()
updater.idle()