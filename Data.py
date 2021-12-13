from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
𝑯𝒆𝒚 {}

𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝒕𝒐 𝑩𝒐𝒕 {}

𝑰 𝒄𝒂𝒏 𝒆𝒙𝒕𝒓𝒂𝒄𝒕 𝒕𝒆𝒙𝒕 𝒇𝒓𝒐𝒎 𝒊𝒎𝒂𝒈𝒆𝒔 𝒖𝒔𝒊𝒏𝒈 , 𝒋𝒖𝒔𝒕 𝒔𝒆𝒏𝒅 𝒎𝒆 𝒕𝒉𝒆 𝒊𝒎𝒂𝒈𝒆 😉.

❤️✨
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("♦️♦️ MDG ♦️♦️", url="https://t.me/Studjjddj")],
        [InlineKeyboardButton(text="🏠 Return Home", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("📣 Channel", url="https://t.me/Tg_Galaxy")
        ],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🆘 About", callback_data="about")
        ],
        [InlineKeyboardButton("🔻CJ7🔻", url="https://t.me/Stajdjdjjdj")],
        [InlineKeyboardButton("👥Group", url="https://t.me/Stsijdjjdjd")],
    ]

    # Help Message
    HELP = """
You Really Need Help ?!?!?!?!

Just send an image. Rest is on me.

Note : You can send any amount of images at once and it will work with same speed and accuracy.

More features in development.
    """

    # About Message
    ABOUT = """
**About This Bot** 

Bot world

Source Code : [Click Here](https://github.com/Soulgoodustries/Cj7Bot)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Thanks for using the Bot 😊😅
    """
