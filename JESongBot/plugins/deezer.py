import os
from random import randint

import aiofiles
import aiohttp
from pyrogram import filters

from JESongBot import Jebot as app

ARQ = "https://thearq.tech/"

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            try:
                data = await resp.json()
            except:
                data = await resp.text()
    return data

async def download_song(url):
    song_name = f"{randint(6969, 6999)}.mp3"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                f = await aiofiles.open(song_name, mode="wb")
                await f.write(await resp.read())
                await f.close()
    return song_name


@app.on_message(filters.command("deezer"))
async def deezer(_, message):
    if len(message.command) < 2:
        await message.reply_text("İndirmek istediğiniz şarkı nedir?🧐")
        return
    text = message.text.split(None, 1)[1]
    query = text.replace(" ", "%20")
    m = await message.reply_text("araştırıcı...")
    try:
        r = await fetch(f"{ARQ}deezer?query={query}&count=1")
        title = r[0]["title"]
        url = r[0]["url"]
        artist = r[0]["artist"]
    except Exception as e:
        await m.edit(str(e))
        return
    await m.edit("Indiriyor...")
    song = await download_song(url)
    await m.edit("Yükleme...")
    await message.reply_audio(audio=song, title=title, performer=artist)
    os.remove(song)
    await m.delete()
