# ======================================================================================================================================
# ping -> edited ping with pic by  @RR7PP
# كتابة الملف لسورس جمثون فقط ممنوع نسبه لنفسك
# تخمط دليل فشلك اخمط وكول اني مطور 😂😂

import os
from datetime import datetime

from sbb_b import sbb_b

#
from . import hmention, reply_id

PING_PIC = os.environ.get("PING_PIC") or (
    "https://telegra.ph/file/0232addc09f30daba0eb4.mp4"
)

JM_TXT = os.environ.get("PING_TEXT") or " تذكر بأن الأيام الصعبة التي تمر بها ستصنع منك شخصاً قوياً ،،، لا ينكسر . . 🖤"


@sbb_b.ar_cmd(pattern="بنك$")
async def _(event):
    reply_to_id = await reply_id(event)
    start = datetime.now()
    cat = await edit_or_reply(
        event, "<b><i>  ❤️⃝⃝⃝⃝⃝⃝⃝⃝⃝⃝⃝⃝⃝⃝⃟✨ تحميل البـنك... 🍀⃝⃝⃟🍂 </b></i>", "html"
    )
    end = datetime.now()
    await cat.delete()
    ms = (end - start).microseconds / 1000
    if PING_PIC:
        caption = f"<b><i>{JM_TXT}<i><b>\n<code>________𝘂𝘀𝗲𝗿 𝗕𝗼𝘁____________\n┃ ✦ {ms}\n┃ ✦ <b>{hmention}</b>\n___________𝗣𝗲𝗚𝗮𝘁𝗵𝗼𝗻________"
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
            event, "<code>يجـب اضـافة متـغير `PING_PIC`  اولا  f<code>", "html"
        )


# ======================================================================================================================================
