import asyncio
from collections import deque

@sbb_b.ar_cmd(pattern="كومبي$") 
 async def _(event): 
     animation_interval = 0.8 
     animation_ttl = range(5) 
     event = await edit_or_reply(event, "wtf") 
     animation_chars = [ 
         "كواد", 
         "منيوج", 
         "تعال مصهةة", 
         "كلك فرخ مال تلي", 
         "\n هاكك https://telegra.ph/file/5e890d649776d79468051.jpg", 
     ] 
     for i in animation_ttl: 
         await asyncio.sleep(animation_interval) 
         await event.edit(animation_chars[i % 5], link_preview=True)
