from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
π―ππ {}

πΎππππππ ππ π©ππ {}

π° πππ πππππππ ππππ ππππ ππππππ πππππ , ππππ ππππ ππ πππ ππππππ.

β€οΈβ¨
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("π£ Channel", url="https://t.me/Tg_Galaxy")],
        [InlineKeyboardButton(text="π  Returne Home", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("π£ Channel", url="https://t.me/Tg_Galaxy")
        ],
        [
            InlineKeyboardButton("Help π", callback_data="help"),
            InlineKeyboardButton("π About", callback_data="about")
        ],
        [InlineKeyboardButton("π€ GBS", url="https://t.me/Galaxy_bots")],
        
    ]

    # Help Message
    HELP = """
You Really Need Help ?!?!?!?!

Just send an image. Rest is on me.

Note : You can send any amount of images at once and it will work with same speed and accuracy.

More features in development. Keep track by kig jonkun
    """

    # About Message
    ABOUT = """
**About This Bot** 

Bot X 

GMX : [Click Here](https://t.me/Tgsj_Galasjjhsxy)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Thanks for using bot π
    """
