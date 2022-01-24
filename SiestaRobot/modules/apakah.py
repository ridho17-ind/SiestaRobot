import random
from SiestaRobot.events import register
from SiestaRobot import telethn

APAKAH_STRING = ["Iya Lah", 
                 "Tidak", 
                 "Mungkin", 
                 "Mungkin Tidak", 
                 "Bisa Jadi", 
                 "Mungkin Tidak",
                 "Tidak Mungkin",
                 "YNTKTS NJING",
                 "Pala Bapak Kau Pecah",
                 "Apa Iya?",
                 "Tanya Aja Sama Mamak Kau Tu Pler 😁"
                 ]


@register(pattern="^/apakah ?(.*)")
async def apakah(event):
    quew = event.pattern_match.group(1)
    if not quew:
        await event.reply('Berikan Saya Pertanyaan Lah Bodo 😐')
        return
    await event.reply(random.choice(APAKAH_STRING))
