from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from JESongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from JESongBot import Jebot as app
from JESongBot import LOGGER

pm_start_text = """
Heya [{}](tg://user?id={}), Ben Mp3 İndirme Botu 🎵

yapmak /help komutlarımı bilmek için

A Sahip by @EfsaneStar
"""

help_text = """
Komutlarım👇

- /bul <song name>: Youtube üzerinden şarkı indirme
- /saavn <song name>: JioSaavn üzerinden şarkı indirme
- /deezer <song name>: Deezer aracılığıyla şarkı indirmek
- Ses formatında indirmek için pm'ime youtube url'si gönder

A Sahip by @EfsaneStar
"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Owner", url="https://t.me/EfsaneStar"
                    ),
                    InlineKeyboardButton(
                        text="Dev Mp3", url="https://t.me/kanalEfsanestar"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)

@app.on_message(filters.command("help"))
async def start(client, message):
    await message.reply(help_text)

app.start()
LOGGER.info("EfsaneStar yayında.")
idle()
