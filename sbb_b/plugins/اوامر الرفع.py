from ..core.managers import edit_or_reply

from ..helpers import get_user_from_event
from userbot import jmthon


@sbb_b.on(admin_cmd(pattern="نيدو(?: |$)(.*)"))   #تكدر تغير الامر اليعجبك
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم رفعه مع سريعين الذوبان حليب نيدو 🌚♥️ "
    )                                                         # تكدر تغيره بالليعجبك 🤍
    
@sbb_b.on(admin_cmd(pattern="زقج(?: |$)(.*)"))   #تكدر تغير الامر اليعجبك
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم رفعـه في قائمة الزقوجة 🍼 "
    )                                                         # تكدر تغيره بالليعجبك 🤍
    
@sbb_b.on(admin_cmd(pattern="كيك(?: |$)(.*)"))   #تكدر تغير الامر اليعجبك
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- كيك انته شنو 🍰 "
    )                                                         # تكدر تغيره بالليعجبك 🤍
    
@sbb_b.on(admin_cmd(pattern="فضولي(?: |$)(.*)"))   #تكدر تغير الامر اليعجبك
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم رفعـه في قائمة الفضوليين 😄 "
    )                                                         # تكدر تغيره بالليعجبك 🤍
    
@sbb_b.on(admin_cmd(pattern="بخيل(?: |$)(.*)"))   #تكدر تغير الامر اليعجبك
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم رفعـه ابو كمونة $ "
    )                                                         # تكدر تغيره بالليعجبك 🤍
    
@sbb_b.on(admin_cmd(pattern="تافه(?: |$)(.*)"))   #تكدر تغير الامر اليعجبك
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم رفعـه تافه 🙂 "
    )                                                         # تكدر تغيره بالليعجبك 🤍
    
@sbb_b.on(admin_cmd(pattern="مطلق(?: |$)(.*)"))   #تكدر تغير الامر اليعجبك
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم تفعيل مود المطلقين بنجاح "
    )                                                         # تكدر تغيره بالليعجبك 🤍
    
    
@sbb_b.on(admin_cmd(pattern="مطلقة(?: |$)(.*)"))   #تكدر تغير الامر اليعجبك
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم تفعيل مود المطلقات بنجاح "
    )                                                         # تكدر تغيره بالليعجبك 🤍
    
@sbb_b.on(admin_cmd(pattern="مرتبط(?: |$)(.*)"))   #تكدر تغير الامر اليعجبك
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم رفعـه مرتبط 🌚♥️ "
    )                                                         # تكدر تغيره بالليعجبك 🤍
    
@sbb_b.on(admin_cmd(pattern="زعطوط(?: |$)(.*)"))   #تكدر تغير الامر اليعجبك
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم تفعيل مود الزعاطيط بنجاح. "
    )                                                         # تكدر تغيره بالليعجبك 🤍
    
    
@sbb_b.on(admin_cmd(pattern="زاحف(?: |$)(.*)"))   #تكدر تغير الامر اليعجبك
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم رفعـه زاحف 🦎 "
    )                                                         # تكدر تغيره بالليعجبك 🤍
    

        
    
@sbb_b.on(admin_cmd(pattern="ملبوس(?: |$)(.*)"))   #تكدر تغير الامر اليعجبك
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- ملبوس ومحد يهتملك 🙂💔 "
    )                                                         # تكدر تغيره بالليعجبك 🤍
    
@sbb_b.on(admin_cmd(pattern="حشري(?: |$)(.*)"))   #تكدر تغير الامر اليعجبك
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم رفعه حشري وغثة ☝😒 "
    )                                                         # تكدر تغيره بالليعجبك 🤍
    
@sbb_b.on(admin_cmd(pattern="طامس(?: |$)(.*)"))   #تكدر تغير الامر اليعجبك
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- طامس جدا مو يم الموضوع 🙂 "
    )                                                         # تكدر تغيره بالليعجبك 🤍
    
@sbb_b.on(admin_cmd(pattern="ثكيل(?: |$)(.*)"))   #تكدر تغير الامر اليعجبك
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- مسوي روحه ثكيل اليوم 🙃 "
    )                                                         # تكدر تغيره بالليعجبك 🤍
    
@sbb_b.on(admin_cmd(pattern="دراما(?: |$)(.*)"))   #تكدر تغير الامر اليعجبك
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        return await edit_or_reply(mention, f"[{custom}](tg://user?id={user.id})")
    tag = user.first_name.replace("\u2060", "") if user.first_name else user.username
    await edit_or_reply(
        mention, f"- المستخدم [{tag}](tg://user?id={user.id}) \n- تـم تفعيل مود الدراما بنجاح 😩 "
    )                                                         # تكدر تغيره بالليعجبك 🤍
    
    