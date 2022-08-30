from telegram import ReplyKeyboardMarkup
from telegram.keyboardbutton import KeyboardButton

from . import static_text


def make_keyboard_for_language() -> ReplyKeyboardMarkup:
    buttons = [
        [static_text.UZBEK, static_text.RUSSIAN],
    ]

    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)


def make_keyboard_for_anonymous_ru() -> ReplyKeyboardMarkup:
    buttons = [
        [static_text.stay_anonymous_ru]
    ]

    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)


def make_keyboard_for_anonymous_uz() -> ReplyKeyboardMarkup:
    buttons = [
        [static_text.stay_anonymous_uz]
    ]

    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)


def send_contact_keyboard_uz() -> ReplyKeyboardMarkup:
    # resize_keyboard=False will make this button appear on half screen (become very large).
    # Likely, it will increase click conversion but may decrease UX quality.
    return ReplyKeyboardMarkup(
        [[KeyboardButton(text=static_text.share_number_uz, request_contact=True)]],
        resize_keyboard=True
    )


def send_contact_keyboard_ru() -> ReplyKeyboardMarkup:
    # resize_keyboard=False will make this button appear on half screen (become very large).
    # Likely, it will increase click conversion but may decrease UX quality.
    return ReplyKeyboardMarkup(
        [[KeyboardButton(text=static_text.share_number_ru, request_contact=True)]],
        resize_keyboard=True
    )
