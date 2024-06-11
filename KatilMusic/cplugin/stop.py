from pyrogram import filters, Client
from pyrogram.types import Message

from KatilMusic import app
from KatilMusic.core.call import Hotty
from KatilMusic.utils.database import set_loop
from KatilMusic.utils.decorators import AdminRightsCheck
from KatilMusic.utils.inline import close_markup
from config import KATIL_USERS


@Client.on_message(
    filters.command(
        ["end", "stop", "cend", "cstop"],
        prefixes=["/", "!", "%", ",", "", ".", "@", "#"],
    )
    & filters.group
    & ~KATIL_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return
    await Hotty.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_5"].format(message.from_user.mention), reply_markup=close_markup(_)
    )
