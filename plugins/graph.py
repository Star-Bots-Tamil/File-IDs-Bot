import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from telegraph import upload_file, Telegraph

DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./Downloads/")

@Client.on_message(filters.media & filters.private)
async def getmedia(bot, message):
    medianame = DOWNLOAD_LOCATION + str(message.from_user.id)
    try:
        reply_message = await message.reply_text(
            text="**Processing...**",
            quote=True,
            disable_web_page_preview=True
        )
        await bot.download_media(
            message=message,
            file_name=medianame
        )
        starbots = upload_file(medianame)
        try:
            os.remove(medianame)
        except Exception as remove_error:
            print(remove_error)
    except Exception as error:
        print(error)
        text = f"**Error :-** <code>{error}</code>"
        reply_markup = InlineKeyboardMarkup(
            [[
                InlineKeyboardButton('More Help', callback_data='help')
            ]]
        )
        await reply_message.edit_text(
            text=text,
            disable_web_page_preview=True,
            reply_markup=reply_markup
        )
        return

    text = f"**Link :- https://graph.org{starbots[0]}**\n\n**Join :- [Star Bots Tamil](https://t.me/Star_Bots_Tamil)**"
    reply_markup = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton(text="Open Link", url=f"https://graph.org{starbots[0]}"),
            InlineKeyboardButton(text="Share Link", url=f"https://telegram.me/share/url?url=https://graph.org{starbots[0]}")
        ], [
            InlineKeyboardButton(text="Join Updates Channel", url="https://t.me/Star_Bots_Tamil")
        ]]
    )
    await reply_message.edit_text(
        text=text,
        disable_web_page_preview=False,
        reply_markup=reply_markup
    )

@Client.on_message(filters.text & filters.private)
async def text_handler(bot, message):
    try:
        telegraph = Telegraph()
        new_user = telegraph.create_account(short_name='1337')
        auth_url = new_user["auth_url"]
        title = message.from_user.first_name
        content = message.text
        if '|' in message.text:
            content, title = message.text.split('|', 1)
        content = content.replace("\n", "<br>")
        author_url = f'https://telegram.dog/{message.from_user.username}' if message.from_user.username else None

        try:
            starbots = Telegraph().create_page(
                title=title,
                html_content=content,
                author_name=str(message.from_user.first_name),
                author_url=author_url
            )
        except Exception as e:
            print(e)

        await message.reply_text("**https://graph.org/{}**".format(starbots["path"]))

    except Exception as e:
        print(e)
