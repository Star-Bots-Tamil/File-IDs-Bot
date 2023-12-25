import os
from telegraph import upload_file, Telegraph
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(filters.private & (filters.photo | filters.video))
async def direct_upload(bot, update):
    text = await update.reply_text(text="<b>Downloading to graph.org Server ...</b>", quote=True)
    media = await update.download()

    await text.edit_text(text="<b>Downloading Completed. Now I am Uploading to graph.org Link...</b>")

    try:
        response = upload_file(media)
    except Exception as error:
        print(error)
        await text.edit_text(text=f"**Error :- {error}**")
        return

    try:
        os.remove(media)
    except Exception as error:
        print(error)
        return

    await text.edit_text(
        text=f"<b>Your Photo or Video Link :-</b>\n\n<b>https://graph.org{response[0]}</b>",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text="Open Link", url=f"https://graph.org{response[0]}"),
             InlineKeyboardButton(text="Share Link", url=f"https://telegram.me/share/url?url=https://graph.org{response[0]}")],
            [InlineKeyboardButton(text="✗ Close ✗", callback_data="close")]
        ])
    )

telegraph = Telegraph()
telegraph.create_account(short_name='Graph-Star-Bots')

@Client.on_message(filters.text & filters.private)
async def text_handler(bot, message):
    try:
        title = message.from_user.first_name
        content = message.text

        if '|' in message.text:
            content, title = message.text.split('|', 1)

        content = content.replace("\n", "<br>")
        author_url = f'https://telegram.dog/{message.from_user.username}' if message.from_user.username else None

        try:
            page = telegraph.create_page(
                title=title,
                html_content=content,
                author_name=str(message.from_user.first_name),
                author_url=author_url
            )
        except Exception as e:
            print(e)
            return

        await message.reply_text(
            text=f"<b>Your Text Link:</b>\n\n<b>https://graph.org/{page['path']}</b>", quote=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(text="Open Link", url=f"https://graph.org/{page['path']}"),
                 InlineKeyboardButton(text="Share Link", url=f"https://telegram.me/share/url?url=https://graph.org/{page['path']}")],
                [InlineKeyboardButton(text="✗ Close ✗", callback_data="close")]
            ])
        )

    except Exception as e:
        print(e)
