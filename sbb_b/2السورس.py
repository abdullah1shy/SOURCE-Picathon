#by Abdullah salhy
import os
from datetime import datetime

from j64jj import j64jj

#
from . import hmention, reply_id

surce_TEXT = os.environ.get("surce_TEXT") or (
    "https://telegra.ph/file/35ed418f21911e5cbb9bc.mp4"
)

Py_TXT = os.environ.get("surce_TEXT") or "  .šŖšššš¢š š š§š¢ š£ššš§šš¢š” ššæš®šÆš¶š° . š¤"


@j64jj.ar_cmd(pattern="Ų§ŁŲ³ŁŲ±Ų³$")
async def _(event):
    reply_to_id = await reply_id(event)
    start = datetime.now()
    cat = await edit_or_reply(
        event, "<b><i>  ā¤ļøāāāāāāāāŲ§ŁŁŲ§ ŁŲ³ŁŁŲ§ ŲØŁ </b></i>", "html"
    )
    end = datetime.now()
    await cat.delete()
    ms = (end - start).microseconds / 1000
    if PING_PIC:
        caption = f"<b><i>{JM_TXT}<i><b>\n<code>________ššš²šæ šš¼š____________\nā ā¦ <b> @Pegatho</b> Ų§ŁŁŁŲ§Ų© \nā----------------| ā¦ <b>{hmention}</b>\n___________š£š²šš®ššµš¼š»________"
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
            event, "<code>ŁŲ¬ŁŲØ Ų§Ų¶ŁŲ§ŁŲ© ŁŲŖŁŲŗŁŲ± `surce_TEXT`  Ų§ŁŁŲ§  f<code>", "html"
        )
