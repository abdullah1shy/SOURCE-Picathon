import asyncio

from . import edit_or_reply, sbb_b

plugin_category = "fun"

@sbb_b.ar_cmd(
    pattern="شمس سطعت$",
    command=("انيم", plugin_category),
    info={
        "الامر": "امر تسليه قم بالتجربه بنفسك",
        "الاستخدام": "{tr}شمس سطعت",
    },
)
async def _(event):
    "animation command"
    animation_interval = 1
    animation_ttl = range(20)
    event = await edit_or_reply(event, "😢")
    animation_chars = [
        "شمس سطعت والجو",
        "جميل هذا اليوم",
        "وفرشات قد قالت ",
        "هذا فصل الصيف",
        "‎تنصيب بيكاثون",
        "ورفيقاتي قلنا هيا ",
        "للنزهة هيا ",
        "ما اجمل هذا رحله",
        "يا اصحاب",
        "[المطور....",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 10])
    },
)
@sbb_b.ar_cmd(
    pattern="تجربه$",
    command=("تجربه", plugin_category),
    info={
        "الامر": "امر تسليه قم بالتجربه بنفسك",
        "الاستخدام": "{tr}تجربه",
    },
)
async def _(event):
    "animation command"
    animation_interval = 1
    animation_ttl = range(20)
    event = await edit_or_reply(event, "😢")
    animation_chars = [
        "شمس سطعت والجو",
        "جميل هذا اليوم",
        "وفرشات قد قالت ",
        "هذا فصل الصيف",
        "‎تنصيب بيكاثون",
        "ورفيقاتي قلنا هيا ",
        "للنزهة هيا ",
        "ما اجمل هذا رحله",
        "يا اصحاب",
        "[المطور....",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 10])