from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from JESongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from JESongBot import Jebot as app
from JESongBot import LOGGER

pm_start_text = """
Merhaba [{}](tg://user?id={}), Ben Mp3 İndirme Botu 🎵

Basınız >> /help komutlarımı bilmek için 😎

Destek Kanalı @SohbetDestek 🏷️
"""

help_text = """
Komutlarım👇

- /bul <şarkı İsmi>: Youtube üzerinden şarkı indirme (Demet Akalın - Çalkala) gibi yazınız. 
- Ses formatında indirmek için pm'ime youtube url'si gönder.. 

Destek Kanalı @SohbetDestek 🏷️
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
                        text="Kanal 📣", url="https://t.me/Sohbetdestek"
                    ),
                    InlineKeyboardButton(
                        text="Müzik Kanalı 🎶", url="https://t.me/kanalEfsanestar"
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
LOGGER.info("Mp3 Dowlander Hazır.")
idle()
