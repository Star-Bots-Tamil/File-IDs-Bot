from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.private & filters.text & ~filters.forwarded)
async def handle_new_user_text(bot, message: Message):
    new_user_info = {
        "id": ,      
        "is_bot": ,
        "first_name": ,
        "username": ,
        "language_code": message.from_user.language_code
    }
    chat_info = {
        "id": message.chat.id,
        "type": message.chat.type,
        "username": message.chat.username,
        "first_name": message.chat.first_name
    }
    info_text = f"User Info:\n\n👦🏻 User ID :- {message.from_user.id}\n🤖 Is Bot:- {message.from_user.is_bot}\n💳 Name :- {message.from_user.first_name}\n📛 Username :- {message.from_user.username}\n🔠 Language :-\nChat Info:\n\n{chat_info}"
    await message.reply_text(info_text)

# Define handlers for different types of messages
@Client.on_message(filters.video)
async def handle_video(bot, message: Message):
    # Handle video message
    await message.reply_text(f"**Video's File ID :- `{message.video.file_id}`\n\n©️ [Star Bots Tamil](https://t.me/Star_Bots_Tamil)**", quote=true)

@Client.on_message(filters.sticker)
async def handle_sticker(bot, message: Message):
    # Handle sticker message
    await message.reply_text(f"**Sticker's File ID :- `{message.sticker.file_id}`\n\n©️ [Star Bots Tamil](https://t.me/Star_Bots_Tamil)**", quote=true)

@Client.on_message(filters.photo)
async def handle_photo(bot, message: Message):
    # Handle photo message
    await message.reply_text(f"**Photo's File ID :- `{message.photo.file_id}`\n\n©️ [Star Bots Tamil](https://t.me/Star_Bots_Tamil)**", quote=true)

@Client.on_message(filters.document)
async def handle_document(bot, message: Message):
    # Handle document message
    await message.reply_text(f"**Document's File ID :- `{message.document.file_id}`\n\n©️ [Star Bots Tamil](https://t.me/Star_Bots_Tamil)**", quote=true)

# Define handlers for voice and audio messages
@Client.on_message(filters.voice)
async def handle_voice(bot, message: Message):
    # Handle voice message
    await message.reply_text(f"**Voice's File ID :- `{message.voice.file_id}`\n\n©️ [Star Bots Tamil](https://t.me/Star_Bots_Tamil)**", quote=true)

@Client.on_message(filters.audio)
async def handle_audio(bot, message: Message):
    # Handle audio message
    await message.reply_text(f"**Audio's File ID :- `{message.audio.file_id}`\n\n©️ [Star Bots Tamil](https://t.me/Star_Bots_Tamil)**", quote=true)
