from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from document.models import Document
from . import static_text


def make_keyboard_menu() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(static_text.products, callback_data=static_text.products)],
        [InlineKeyboardButton(static_text.location, callback_data=static_text.location),
         InlineKeyboardButton(static_text.phone_number, callback_data=static_text.phone_number)],
        [InlineKeyboardButton(static_text.telegram_channel, callback_data=static_text.telegram_channel),
         InlineKeyboardButton(static_text.website, callback_data=static_text.website)],
    ]

    return InlineKeyboardMarkup(buttons)


def make_keyboard_for_products() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(static_text.school, callback_data=f"{static_text.products} {static_text.school}"),
         InlineKeyboardButton(static_text.kindergarten,
                              callback_data=f"{static_text.products} {static_text.kindergarten}")],
        [InlineKeyboardButton(static_text.BACK, callback_data=static_text.MENU)],
    ]
    return InlineKeyboardMarkup(buttons)


def make_keyboard_for_kindergarten() -> InlineKeyboardMarkup:
    docs_count = Document.objects.filter(type='kindergarten').count()
    buttons = [
        [InlineKeyboardButton(static_text.all_kindergartens,
                              callback_data=f"{static_text.kindergarten} {static_text.all_kindergartens}")],
        [InlineKeyboardButton(static_text.placates, callback_data=f"{static_text.kindergarten} {static_text.placates}"),
         InlineKeyboardButton(static_text.materials,
                              callback_data=f"{static_text.kindergarten} {static_text.materials}")],
        [InlineKeyboardButton(static_text.documents.format(docs_count),
                              callback_data=f"{static_text.kindergarten} {static_text.documents}"),
         InlineKeyboardButton(static_text.lepbuks, callback_data=f"{static_text.kindergarten} {static_text.lepbuks}")],
        [InlineKeyboardButton(static_text.buklets, callback_data=f"{static_text.kindergarten} {static_text.buklets}"),
         InlineKeyboardButton(static_text.imgs, callback_data=f"{static_text.kindergarten} {static_text.imgs}")],
        [InlineKeyboardButton(static_text.masks, callback_data=f"{static_text.kindergarten} {static_text.masks}"),
         InlineKeyboardButton(static_text.makets, callback_data=f"{static_text.kindergarten} {static_text.makets}")],
        [InlineKeyboardButton(static_text.decorations,
                              callback_data=f"{static_text.kindergarten} {static_text.decorations}")],
        [InlineKeyboardButton(static_text.BACK, callback_data=f'{static_text.products} {static_text.BACK}')],
    ]
    return InlineKeyboardMarkup(buttons)


def make_keyboard_for_school() -> InlineKeyboardMarkup:
    docs_count = Document.objects.filter(type='school').count()
    buttons = [
        [InlineKeyboardButton(static_text.all_schools,
                              callback_data=f"{static_text.school} {static_text.all_schools}")],
        [InlineKeyboardButton(static_text.placates, callback_data=f"{static_text.school} {static_text.placates}"),
         InlineKeyboardButton(static_text.materials,
                              callback_data=f"{static_text.school} {static_text.materials}")],
        [InlineKeyboardButton(static_text.documents.format(docs_count),
                              callback_data=f"{static_text.school} {static_text.documents}"),
         InlineKeyboardButton(static_text.lepbuks, callback_data=f"{static_text.school} {static_text.lepbuks}")],
        [InlineKeyboardButton(static_text.buklets, callback_data=f"{static_text.school} {static_text.buklets}"),
         InlineKeyboardButton(static_text.imgs, callback_data=f"{static_text.school} {static_text.imgs}")],
        [InlineKeyboardButton(static_text.masks, callback_data=f"{static_text.school} {static_text.masks}"),
         InlineKeyboardButton(static_text.makets, callback_data=f"{static_text.school} {static_text.makets}")],
        [InlineKeyboardButton(static_text.decorations,
                              callback_data=f"{static_text.kindergarten} {static_text.decorations}")],
        [InlineKeyboardButton(static_text.BACK, callback_data=f'{static_text.products} {static_text.BACK}')],
    ]
    return InlineKeyboardMarkup(buttons)


def make_keyboard_for_kindergarten_documents() -> InlineKeyboardMarkup:
    documents = Document.objects.filter(type='kindergarten').all()
    buttons = []
    for doc in documents:
        buttons.append([InlineKeyboardButton(
            text=f'{doc.title[:20].capitalize()}... | ID: {doc.id}' if len(doc.title) > 20 else f'{doc.title.capitalize()} | ID: {doc.id}',
            callback_data=f'{static_text.kindergarten} {static_text.documents} {doc.id}')])
    buttons.append(
        [InlineKeyboardButton(text=static_text.BACK, callback_data=f"{static_text.school} {static_text.BACK}")])
    return InlineKeyboardMarkup(buttons)


def make_keyboard_for_school_documents() -> InlineKeyboardMarkup:
    documents = Document.objects.filter(type='school').all()
    buttons = []
    for doc in documents:
        buttons.append([InlineKeyboardButton(
            text=f'{doc.title[:20].capitalize()}... | ID: {doc.id}' if len(doc.title) > 20 else f'{doc.title.capitalize()} | ID: {doc.id}',
            callback_data=f'{static_text.school} {static_text.documents} {doc.id}')])
    buttons.append([InlineKeyboardButton(text=static_text.BACK, callback_data=f"{static_text.kindergarten} {static_text.BACK}")])
    return InlineKeyboardMarkup(buttons)
