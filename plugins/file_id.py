from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.private & filters.text & ~filters.forwarded)
async def handle_new_user_text(bot, message: Message):
    new_user_info = {
        "id": message.from_user.id,      
        "is_bot": message.from_user.is_bot,
        "first_name": message.from_user.first_name,
        "username": message.from_user.username,
        "language_code": message.from_user.language_code
    }
    chat_info = {
        "id": message.chat.id,
        "type": message.chat.type,
        "username": message.chat.username,
        "first_name": message.chat.first_name
    }
    info_text = f"User Info:\n\n{new_user_info}\n\nChat Info:\n\n{chat_info}"
    await message.reply_text(info_text)

# Define handlers for different types of messages
@Client.on_message(filters.video)
async def handle_video(bot, message: Message):
    # Handle video message
    await message.reply_text(f"Video file ID: {message.video.file_id}")

@Client.on_message(filters.sticker)
async def handle_sticker(bot, message: Message):
    # Handle sticker message
    await message.reply_text(f"Sticker file ID: {message.sticker.file_id}")

@Client.on_message(filters.photo)
async def handle_photo(bot, message: Message):
    # Handle photo message
    await message.reply_text(f"Photo file ID: {message.photo.file_id}")

@Client.on_message(filters.document)
async def handle_document(bot, message: Message):
    # Handle document message
    await message.reply_text(f"Document file ID: {message.document.file_id}")

# Define handlers for voice and audio messages
@Client.on_message(filters.voice)
async def handle_voice(bot, message: Message):
    # Handle voice message
    await message.reply_text(f"Voice file ID: {message.voice.file_id}")

@Client.on_message(filters.audio)
async def handle_audio(bot, message: Message):
    # Handle audio message
    await message.reply_text(f"Audio file ID: {message.audio.file_id}")
