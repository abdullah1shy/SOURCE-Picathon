import time
import re
from ..Config import Config
from ..sql_helper.bank import add_bank, del_bank, get_bank, update_bank, des_bank
from telethon import Button, events
import glob, os
import os.path
from ..helpers import get_user_from_event
from telethon import types
from random import randint
import random
from . import jmthon
from ..core.managers import edit_delete, edit_or_reply

import asyncio
#Written By Reda .. 
#كتابة الملف من الصفر من قبل بيكاثون
#ممنوع تاخذه وتنسبه الك خليك مطور واصنع بنفسك 👍🏻
plugin_category = "utils"
#----Timers----#
t = {}
#--------------#
def convert(seconds): 

    seconds = seconds % (24 * 3600) 

    seconds %= 3600

    minutes = seconds // 60

    seconds %= 60

    return "%02d:%02d" % (minutes, seconds)

@jmthon.ar_cmd(pattern="tdata")

async def td(event):
    return await edit_or_reply(event, str(t))

@jmthon.ar_cmd(pattern="توب الفلوس?([\s\S]*)")
   
async def d(message):
    users = des_bank()
    if not users:
        return edit_or_reply(message, "لا يوجد حسابات في المصرف")
    list = '**قائمة اغنى عشرة**\n'
    count = 0
    for i in users:
        count += 1
        list += f'**{count} -** [{i.first_name}](tg://user?id={i.user_id}) {i.balance} 💵\n'
        
    await edit_or_reply(message, list)
    #return await edit_or_reply(message, str(des_bank()))

@jmthon.ar_cmd(pattern="مسح حسابي?([\s\S]*)")
   
async def d(message):
    me = await message.client.get_me()
    acc = get_bank(me.id)
    if acc is None:
        await edit_delete(message, "لا تملك حساب مصرفي لحذفه")
    else:
        row = del_bank(me.id)
        await message.delete()
        await message.client.send_message(message.chat_id, "تم حذف حسابك المصرفي")

@jmthon.ar_cmd(
    pattern="البنك?([\s\S]*)")",
    command=("البنك", plugin_category),
)
async def start(event):
    me = await event.client.get_me()
    sta = await edit_or_reply(event, f"""<strong>



👋  {me.first_name} مرحبًا
 ━━━━━━━━━━━━━━━━━
- يمكنك استعمال الاوامر في اي مكان

- المصرف. 

- لاضهار المساعدة فيما يخص المصرف
 ━━━━━━━━━━━━━━━━━
ارسل .انشاء حساب
لانشاء حساب في المصرف

</strong>""",parse_mode="html")



@jmthon.on(admin_cmd(pattern="(فلوسي|اموالي) ?([\s\S]*)"))
async def a(message):
    me = await message.client.get_me()
    if get_bank(me.id) is None:
         noa = await edit_or_reply(message, f"<strong>انت لا تملك حساب في البنك</strong>", parse_mode="html")
    else:
         acc = get_bank(me.id)
         mo = int(acc.balance)
         ba = await edit_or_reply(message,f"<strong>اموالك : {mo}  💵</strong>",parse_mode="html")



@jmthon.on(admin_cmd(pattern="(بنكي|مصرفي) ?([\s\S]*)"))
async def myb(message):

    me = await message.client.get_me()
    
    if get_bank(me.id) is not None:
         acc = get_bank(me.id)
         nn = acc.first_name
         balance = acc.balance
         ba = acc.bank
         ifn = f"""
- ================= -
• الاسم : {nn} 
• رقم الحساب : {me.id} 
• الاموال : {balance} 💵
• اسم المصرف : {ba} 
- ================= -
          """
         acinfo = await edit_or_reply(message,f"<strong>{ifn}</strong>",parse_mode="html")

    else:
         ca = await edit_or_reply(message,f"<strong>ليس لديك حساب في البنك!</strong>",parse_mode="html")


@jmthon.ar_cmd(func=lambda m:"راتب?([\s\S]*)"")
async def ga(message):
    mee = await message.client.get_me()
    ms = message.text
    acc = get_bank(mee.id)
 
    if ms == ".المصرف" or ms == ".البانك" or ms == ".مصرف":


        help = """
•| قائمة المساعدة |•
.انشاء حساب (لانشاء حساب مصرفي)
- مثال: .انشاء حساب الرافدين او بيكاثون الاسلامي
1- .استثمار (مبلغ) 
- مثال : استثمار 18276
2- .حظ (المبلغ)
- مثال : حظ 17267
3- .راتب
4- .كنز
5- .بخشيش
6- .فلوسي | لرؤية فلوسك
7- .اسرق | لسرقة اموال من شخص
-بالرد على الشخص المُراد سرقته
8- .بنكي او .مصرفي | لاضهار معلومات حسابك في المصرف
9- .مسح حسابي | لحذف حسابك البنكي
10- .توب الفلوس | لعرض اغنى ١٠ اشخاص
      """


        hr = await edit_or_reply(message,f"<strong>{help}</strong>",parse_mode="html")


    if ms == "$كنز":
        if "كنز" in t:
              tii = t["كنز"] - time.time()
              return await edit_or_reply(message,"<strong> ليس هنالك كنز لقد اخذته بالفعل انتضر {}</strong>".format(convert(tii)),parse_mode="html")
     
        else:
              rt = randint(50,3000)
              acca = get_bank(mee.id).balance
              ga = int(rt) + int(acca)
              update_bank(mee.id, ga)
              tx = await edit_or_reply(message,f"<strong>💸 لقد حصلت على الكنز!🤩\n- حصلت على {rt} 💵.\n- اموالك الان : {ga} 💵 .</strong>",parse_mode="html")
              t["كنز"] = time.time() + 600 
              await asyncio.sleep(600)
              del t["كنز"]
     
    if ".استثمار" in ms:
        value = message.text.replace("$استثمار","")
        if "استثمار" in t:
            ti2 = t["استثمار"] - time.time()
            return await edit_or_reply(message,"<strong> للاستثمار مجدداً انتضر {}</strong>".format(convert(ti2)),parse_mode="html")
        lss = ["Done","Fail"]
        ls = random.choice(lss)
        ppe = acc.balance
        if int(value) > int(ppe):
            return await edit_delete(message, "<strong>! انت لا تملك هذا القدر من الاموال للاستثمار</strong>", parse_mode="html")
        #isv = value.isnumeric()
        #if not isv:
         #    return await edit_delete(message, "<strong>!ادخل رقم صالِح للاستثمار</strong>", parse_mode="html")
        if "Done" in ls:
            kf = int(value) + int(randint(int(ppe),int(ppe)))
            update_bank(mee.id, kf)
            d = ["1%","2%","4%","8%","9%"]
            ra = random.choice(d)
            ma = await edit_or_reply(message,f"""<strong>
===================
• استثمار ناجح  💰
• نسبة الربح  ↢ {ra}
• مبلغ الربح  ↢ ( {ppe} 💵 )
• اموالك الان  ↢ ( {kf}  💵 )
===================
</strong>""",parse_mode="html")
            t["استثمار"] = time.time() + 600
            await asyncio.sleep(600)
            del t["استثمار"]
        if "Fail" in ls:
             await edit_or_reply(message, "استثمار فاشل لم تحصل على اي ارباح")
             t["استثمار"] = time.time() + 600
             await asyncio.sleep(600)
             del t["استثمار"]
             

    if f"$حظ"in message.text:
        value = message.text.replace(".حظ","")
        ppe = acc.balance
        if "حظ" in t:
            ti2 = t["حظ"] - time.time()
            return await edit_or_reply(message,"<strong> للعب الحظ مجدداً انتضر {}</strong>".format(convert(ti2)),parse_mode="html")

        if int(value) > int(ppe):
            return await edit_delete(message, "<strong>! انت لا تملك هذا القدر من الاموال للحظ</strong>", parse_mode="html")
        ls = ["Done","Fail"]
        sv = random.choice(ls)
        if "Done" in sv:
        
            kf = int(value) + int(randint(int(ppe),int(ppe)))
            update_bank(mee.id, kf)
            cong = await edit_or_reply(message,f"""<strong>          
======================
• مبارك لقد ربحت بالحظ
• اموالك السابقة  ↢ ( {ppe}  💵 ) .
• اموالك الان  ↢ ( {kf}  💵 ) .
======================
</strong>""",parse_mode="html")
            t["حظ"] = time.time() + 600
            await asyncio.sleep(600)
            del t["حظ"]
        else:
            pa = acc.balance
            pop = int(pa) - int(value)
            update_bank(mee.id, pop)
            heh = await edit_or_reply(message,f"""<strong>
=======================
• لسوء الحظ , خسرت في الحظ 
• اموالك السابقة  ↢ ( {pa} 💵 ) .
• اموالك الان  ↢ ( {pop} 💵 ) .
========================
</strong>""",parse_mode="html")

            t["حظ"] = time.time() + 600
            await asyncio.sleep(600)
            del t["حظ"]
    if ms == "$بخشيش":
        ppe = acc.balance
        if "بخشيش" in t:
            ti2 = t["بخشيش"] - time.time()
            return await edit_or_reply(message,"<strong> لقد اخذت بخشيش انتضر {}</strong>".format(convert(ti2)),parse_mode="html")
        else:
              rt = randint(70,2000)
              ga = int(rt) + int(ppe)
              tp = await edit_or_reply(message,f"<strong>=================\n- •تم ايداع البخشيش 💸\n- • حصلت على  {rt} 💵.\n- • أموالك الان : {ga} 💵\n=================</strong>",parse_mode="html")
              update_bank(mee.id, ga)
              t["بخشيش"] = time.time() + 600
              await asyncio.sleep(600)
              del t["بخشيش"]
    
    if ms == ".راتب":
        ba = acc.balance
        if "راتب" in t:
            ti2 = t["راتب"] - time.time()
            return await edit_or_reply(message,"<strong> لأخذ راتب مجدداً انتضر {}</strong>".format(convert(ti2)),parse_mode="html")

        else:


              list = ["مبرمج 💻-1000","ملك 🤴-10000","قاضي 👨‍⚖-20000","عامل 🧑‍🔧-1000","روبوت 🤖-2300","سائق 🚓-4000","تاجر مخدرات 🚬-5000","تاجر اسلحة 🔫-9000","طيار ✈️-7000","قبطان 🛳-8000"]

              rt = random.choice(list)
              name = rt.split("-")[0]
              ratb = rt.split("-")[1]
              ga = int(ratb) + int(ba)
              update_bank(mee.id, ga)
              sal = await edit_or_reply(message,f"<strong>==================\n- • تم ايداع راتبك! 💸🤩\n- • حصلت على {ratb} 💵\n- • لأنك {name}.\n- • اموالك الان : {ga} 💵 \n==================</strong>",parse_mode="html")
              t["راتب"] = time.time() + 600
              await asyncio.sleep(600)
              del t["راتب"]

@jmthon.ar_cmd(
    pattern="اسرق?([\s\S]*)",
    command=("اسرق", plugin_category),
)
async def thief(message):
    mee = await message.client.get_me()
    user, custom = await get_user_from_event(message)
    accu = get_bank(user.id)
    acc = get_bank(mee.id)
    if "اسرق" in t:
        ti2 = t["اسرق"] - time.time()
        return await edit_or_reply(message,"<strong> لقد سرقت قبل قليل انتظر {}</strong>".format(convert(ti2)),parse_mode="html")
    else:
        if not user:
            return await edit_or_reply(message,"<strong> يجب عليك الرد على شخص لسرقته </strong>", parse_mode="html")
        if get_bank(user.id) is None:
            return await edit_or_reply(message,"<strong> لا يمكنك سرقة شخص لا يمتلك حساب مصرفي </strong>", parse_mode="html")
        if get_bank(mee.id) is None:
            return await edit_or_reply(message,"<strong> لا يمكنك السرقة لانك لا تملك حساب مصرفي </strong>", parse_mode="html")
        if int(accu.balance) < 5000:
            return await edit_or_reply(message,"<strong> لا يمكنك سرقته لان امواله اقل من 5000$ </strong>", parse_mode="html")
    rt = randint(70,2000)
    ppe = int(acc.balance)
    be = int(accu.balance)
    jep = int(be) - int(rt)
    update_bank(user.id, jep)
    jepthon = mee.first_name.replace("\u2060", "") if mee.first_name else mee.username
    ga = int(rt) + int(ppe)
    update_bank(mee.id, ga)
    await jmthon.send_file(
                message.chat_id,
                "https://telegra.ph/file/9c4007ca621cc01a3c650.jpg",
                caption=f"سرق [{jepthon}](tg://user?id={mee.id}) من [{user.first_name}](tg://user?id={user.id})\n المبلغ: {rt} 💵",
                )
    t["اسرق"] = time.time() + 600
    await asyncio.sleep(600)
    del t["اسرق"]
    
    
@jmthon.ar_cmd(pattern="انشاء حساب ?([\s\S]*)"")
async def bankar(message):
    input = message.pattern_match.group(1)
    mee = await message.client.get_me()
    if get_bank(mee.id) is not None:
        return await edit_or_reply(message, f"<strong>لديك حساب مصرفي بالفعل</strong>",parse_mode="html")
    if input == "بيكاثون الاسلامي":
        bankn = "مصرف بيكاثون الاسلامي"
    elif input == "الرافدين":
    	bankn = "مصرف الرافدين"
    elif input != "الرافدين" or "بيكاثون الاسلامي":
         return await edit_or_reply(message, "لا يوجد هكذا مصرِف !")
    add_bank(mee.id, mee.first_name, 50, bankn)
    cbs = await edit_or_reply(message,f"<strong>تم انشاء حساب مصرفي بالمعلومات التالية:\nاسم صاحب الحساب:{mee.first_name}|\nايدي الحساب:{mee.id}|\nاسم المصرف:{bankn}|\nالاموال المودعة:50$</strong>", parse_mode="html")


@jmthon.ar_cmd(pattern="تحويل ?([\s\S]*)"")

async def transmoney(event):
    me = await event.client.get_me()
    inp = event.pattern_match.group(1)
    user, custom = await get_user_from_event(event)
    acc = get_bank(me.id)
    accu = get_bank(user.id)
    if inp is None:
        return await edit_delete(event, "ادخل المبلغ الذي تريد تحويله")
    if not user:
        return await edit_delete(event, "يجب ان ترد على الشخص الذي تريد ان تحول له")
    if acc is None:
        return await edit_delete(event, "ليس لديك حساب مصرفي للتحويل")
    if accu is None:
        return await edit_delete(event, "الشخص الذي تحاول التحويل له لا يملك حساب مصرفي")
    if "-" in inp:
        inp = inp.replace("-", "")
    if int(inp) > int(acc.balance):
        return await edit_delete(event, "انت لا تملك هذا القدر من الاموال لتحويله")
    if int(inp) < 2000:
        return await edit_delete(event, "لا يمكنك تحويل مبلغ اقل من 2000$")
    if int(inp) > int(acc.balance):
        return await edit_delete(event, "انت لا تملك هذا القدر من الاموال لتحويله")
    if int(inp) < 0:
        return await edit_delete(event, "ادخل قيمة صحيحة للتحويل!")
    tra = int(acc.balance) - int(inp)
    rec = int(accu.balance) + int(inp)
    update_bank(me.id, tra)
    update_bank(user.id, rec)
    don = await edit_or_reply(event, f"تم تحويل {inp} لحساب [{user.first_name}](tg://user?id={user.id})")