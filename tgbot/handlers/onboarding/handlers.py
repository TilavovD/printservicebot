import datetime

from django.utils import timezone
from telegram import ParseMode, Update
from telegram.ext import CallbackContext

from document.models import Document
from tgbot.handlers.onboarding import static_text
from tgbot.handlers.utils.info import extract_user_data_from_update
from tgbot.models import User
from . import keyboards
from . import static_text


def callback_query_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    data = query.data
    if data == static_text.products:
        update.callback_query.edit_message_text(static_text.products)
        update.callback_query.edit_message_reply_markup(keyboards.make_keyboard_for_products())
    elif data == static_text.MENU:
        update.callback_query.edit_message_text('Bizning mahsulotlar:')
        update.callback_query.edit_message_reply_markup(keyboards.make_keyboard_menu())
    elif data == f"{static_text.products} {static_text.school}":
        update.callback_query.edit_message_reply_markup(keyboards.make_keyboard_for_school())
    elif data == f"{static_text.products} {static_text.kindergarten}":
        update.callback_query.edit_message_reply_markup(keyboards.make_keyboard_for_kindergarten())
    elif data == f"{static_text.kindergarten} {static_text.BACK}":
        update.callback_query.edit_message_text('Bizning mahsulotlar:')
        update.callback_query.edit_message_reply_markup(keyboards.make_keyboard_for_kindergarten())
    elif data == f"{static_text.school} {static_text.BACK}":
        update.callback_query.edit_message_text('Bizning mahsulotlar:')
        update.callback_query.edit_message_reply_markup(keyboards.make_keyboard_for_school())

    elif data == f"{static_text.products} {static_text.BACK}":
        update.callback_query.edit_message_reply_markup(keyboards.make_keyboard_for_products())
    elif data == f'{static_text.kindergarten} {static_text.documents}':
        update.callback_query.edit_message_text('Xujjatlar')
        update.callback_query.edit_message_reply_markup(keyboards.make_keyboard_for_kindergarten_documents())
    elif data == f'{static_text.school} {static_text.documents}':
        update.callback_query.edit_message_text('Xujjatlar')
        update.callback_query.edit_message_reply_markup(keyboards.make_keyboard_for_school_documents())
    elif data.startswith(f'{static_text.kindergarten} {static_text.documents}') or \
            data.startswith(f'{static_text.school} {static_text.documents}'):
        id = data.split()[3]
        doc = Document.objects.filter(id=id).first()
        if doc:
            context.bot.send_photo(
                chat_id=update.effective_user.id,
                photo=doc.cover_photo,
                caption=f'<b>ID</b>: {id}\n\n'
                        f'<b>Xujjat nomi</b>: {doc.title.capitalize()}\n\n'
                        f'Xujjat haqida: <i>{doc.content}</i>',
                parse_mode=ParseMode.HTML
            )
            context.bot.send_document(chat_id=update.effective_user.id, document=doc.file)
