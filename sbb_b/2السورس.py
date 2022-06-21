#by Abdullah salhy
import os
from datetime import datetime

from j64jj import j64jj

#
from . import hmention, reply_id

surce_TEXT = os.environ.get("surce_TEXT") or (
    "https://telegra.ph/file/35ed418f21911e5cbb9bc.mp4"
)

Py_TXT = os.environ.get("surce_TEXT") or "  .𝗪𝗘𝗟𝗖𝗢𝗠𝗘 𝗧𝗢 𝗣𝗘𝗚𝗧𝗛𝗢𝗡 𝗔𝗿𝗮𝗯𝗶𝗰 . 🖤"


@j64jj.ar_cmd(pattern="السورس$")
async def _(event):
    reply_to_id = await reply_id(event)
    start = datetime.now()
    cat = await edit_or_reply(
        event, "<b><i>  ❤️⃝⃝⃝⃝⃝⃝⃝⃝اهلا وسهلا بك </b></i>", "html"
    )
    end = datetime.now()
    await cat.delete()
    ms = (end - start).microseconds / 1000
    if PING_PIC:
        caption = f"<b><i>{JM_TXT}<i><b>\n<code>________𝘂𝘀𝗲𝗿 𝗕𝗼𝘁____________\n┃ ✦ <b> @Pegathon</b> القناة \n┃ ✦ <b>{hmention}</b>\n___________𝗣𝗲𝗚𝗮𝘁𝗵𝗼𝗻________"
        await event.client.send_file(
            event.chat_id,
            PING_PIC,
            caption=caption,
            parse_mode="html",
            reply_to=reply_to_id,
            link_preview=False,
            allow_cache=True,
        )
    else:
        await event.edit_or_reply(
            event, "<code>يجـب اضـافة متـغير `surce_TEXT`  اولا  f<code>", "html"
        )
