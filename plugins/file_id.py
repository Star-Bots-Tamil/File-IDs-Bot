from pyrogram import Client, filters, enums
from pyrogram.types import Message

language_names = {
    "ab": "Abkhazian",
    "aa": "Afar",
    "af": "Afrikaans",
    "ak": "Akan",
    "sq": "Albanian",
    "am": "Amharic",
    "ar": "Arabic",
    "an": "Aragonese",
    "hy": "Armenian",
    "as": "Assamese",
    "av": "Avaric",
    "ae": "Avestan",
    "ay": "Aymara",
    "az": "Azerbaijani",
    "bm": "Bambara",
    "ba": "Bashkir",
    "eu": "Basque",
    "be": "Belarusian",
    "bn": "Bengali",
    "bh": "Bihari languages",
    "bi": "Bislama",
    "bs": "Bosnian",
    "br": "Breton",
    "bg": "Bulgarian",
    "my": "Burmese",
    "ca": "Catalan, Valencian",
    "km": "Central Khmer",
    "ch": "Chamorro",
    "ce": "Chechen",
    "ny": "Chichewa, Chewa, Nyanja",
    "zh": "Chinese",
    "cu": "Church Slavonic, Old Bulgarian, Old Church Slavonic",
    "cv": "Chuvash",
    "kw": "Cornish",
    "co": "Corsican",
    "cr": "Cree",
    "hr": "Croatian",
    "cs": "Czech",
    "da": "Danish",
    "dv": "Divehi, Dhivehi, Maldivian",
    "nl": "Dutch, Flemish",
    "dz": "Dzongkha",
    "en": "English",
    "eo": "Esperanto",
    "et": "Estonian",
    "ee": "Ewe",
    "fo": "Faroese",
    "fj": "Fijian",
    "fi": "Finnish",
    "fr": "French",
    "ff": "Fulah",
    "gd": "Gaelic, Scottish Gaelic",
    "gl": "Galician",
    "lg": "Ganda",
    "ka": "Georgian",
    "de": "German",
    "ki": "Gikuyu, Kikuyu",
    "el": "Greek (modern)",
    "kl": "Greenlandic, Kalaallisut",
    "gn": "Guarani",
    "gu": "Gujarati",
    "ht": "Haitian, Haitian Creole",
    "ha": "Hausa",
    "he": "Hebrew",
    "hz": "Herero",
    "hi": "Hindi",
    "ho": "Hiri Motu",
    "hu": "Hungarian",
    "is": "Icelandic",
    "io": "Ido",
    "ig": "Igbo",
    "id": "Indonesian",
    "ia": "Interlingua (International Auxiliary Language Association)",
    "ie": "Interlingue",
    "iu": "Inuktitut",
    "ik": "Inupiaq",
    "ga": "Irish",
    "it": "Italian",
    "ja": "Japanese",
    "jv": "Javanese",
    "kn": "Kannada",
    "kr": "Kanuri",
    "ks": "Kashmiri",
    "kk": "Kazakh",
    "rw": "Kinyarwanda",
    "kv": "Komi",
    "kg": "Kongo",
    "ko": "Korean",
    "kj": "Kuanyama, Kwanyama",
    "ku": "Kurdish",
    "ky": "Kyrgyz",
    "lo": "Lao",
    "la": "Latin",
    "lv": "Latvian",
    "lb": "Letzeburgesch, Luxembourgish",
    "li": "Limburgan, Limburger, Limburgish",
    "ln": "Lingala",
    "lt": "Lithuanian",
    "lu": "Luba-Katanga",
    "mk": "Macedonian",
    "mg": "Malagasy",
    "ms": "Malay",
    "ml": "Malayalam",
    "mt": "Maltese",
    "gv": "Manx",
    "mi": "Maori",
    "mr": "Marathi",
    "mh": "Marshallese",
    "mn": "Mongolian",
    "na": "Nauru",
    "nv": "Navajo, Navaho",
    "nd": "Northern Ndebele",
    "ng": "Ndonga",
    "ne": "Nepali",
    "se": "Northern Sami",
    "no": "Norwegian",
    "nb": "Norwegian Bokmål",
    "nn": "Norwegian Nynorsk",
    "ii": "Nuosu, Sichuan Yi",
    "oc": "Occitan (post 1500)",
    "oj": "Ojibwa",
    "or": "Oriya",
    "om": "Oromo",
    "os": "Ossetian, Ossetic",
    "pi": "Pali",
    "pa": "Panjabi, Punjabi",
    "ps": "Pashto, Pushto",
    "fa": "Persian",
    "pl": "Polish",
    "pt": "Portuguese",
    "qu": "Quechua",
    "ro": "Romanian, Moldavian, Moldovan",
    "rm": "Romansh",
    "rn": "Rundi",
    "ru": "Russian",
    "sm": "Samoan",
    "sg": "Sango",
    "sa": "Sanskrit",
    "sc": "Sardinian",
    "sr": "Serbian",
    "sn": "Shona",
    "ii": "Sichuan Yi, Nuosu",
    "sd": "Sindhi",
    "si": "Sinhala, Sinhalese",
    "sk": "Slovak",
    "sl": "Slovenian",
    "so": "Somali",
    "st": "Sotho, Southern",
    "nr": "South Ndebele",
    "es": "Spanish, Castilian",
    "su": "Sundanese",
    "sw": "Swahili",
    "ss": "Swati",
    "sv": "Swedish",
    "tl": "Tagalog",
    "ty": "Tahitian",
    "tg": "Tajik",
    "ta": "Tamil",
    "tt": "Tatar",
    "te": "Telugu",
    "th": "Thai",
    "bo": "Tibetan",
    "ti": "Tigrinya",
    "to": "Tonga (Tonga Islands)",
    "ts": "Tsonga",
    "tn": "Tswana",
    "tr": "Turkish",
    "tk": "Turkmen",
    "tw": "Twi",
    "ug": "Uighur, Uyghur",
    "uk": "Ukrainian",
    "ur": "Urdu",
    "uz": "Uzbek",
    "ve": "Venda",
    "vi": "Vietnamese",
    "vo": "Volapük",
    "wa": "Walloon",
    "cy": "Welsh",
    "fy": "Western Frisian",
    "wo": "Wolof",
    "xh": "Xhosa",
    "yi": "Yiddish",
    "yo": "Yoruba",
    "za": "Zhuang, Chuang",
    "zu": "Zulu",
}

@Client.on_message(filters.private & filters.text & ~filters.forwarded)
async def handle_new_user_text(bot, message: Message):
    button = InlineKeyboardMarkup([[
        InlineKeyboardButton('🔒 Close', callback_data='close')
    ]])
    language_name = language_names.get(message.from_user.language_code, "Unknown")
    chat_type_str = {
        enums.ChatType.PRIVATE: "🔐 Private",
        enums.ChatType.GROUP: "🗨️ Group",
        enums.ChatType.SUPERGROUP: "💬 Supergroup",
        enums.ChatType.CHANNEL: "📡 Channel"
    }.get(message.chat.type, "🫴🏻 Unknown")
    info_text = f"**--User Info :---\n\n👦🏻 User ID :- `{message.from_user.id}`\n🤖 Is Bot :- {message.from_user.is_bot}\n💳 Name :- {message.from_user.first_name}\n📛 Username :- @{message.from_user.username}\n🔠 Language :- {language_name}\n\n--Chat Info :---\n\n🆔 Chat ID :- `{message.chat.id}`\n🗨️ Chat Type :- {chat_type_str}\n📛 Chat Username :- @{message.chat.username}\n💳 Chat Name :- {message.chat.first_name}\n\n©️ [Star Bots Tamil](https://t.me/Star_Bots_Tamil)**"
    await message.reply_text(info_text, quote=True, reply_markup=button)

# Define handlers for different types of messages
@Client.on_message(filters.video)
async def handle_video(bot, message: Message):
    # Handle video message
    await message.reply_text(f"**File ID Genrated Successfully..!\n\nVideo's File ID :- `{message.video.file_id}`\n\n©️ [Star Bots Tamil](https://t.me/Star_Bots_Tamil)**", quote=True)

@Client.on_message(filters.sticker)
async def handle_sticker(bot, message: Message):
    # Handle sticker message
    await message.reply_text(f"**File ID Genrated Successfully..!\n\nSticker's File ID :- `{message.sticker.file_id}`\n\n©️ [Star Bots Tamil](https://t.me/Star_Bots_Tamil)**", quote=True)

@Client.on_message(filters.photo)
async def handle_photo(bot, message: Message):
    # Handle photo message
    await message.reply_text(f"**File ID Genrated Successfully..!\n\nPhoto's File ID :- `{message.photo.file_id}`\n\n©️ [Star Bots Tamil](https://t.me/Star_Bots_Tamil)**", quote=True)

@Client.on_message(filters.document)
async def handle_document(bot, message: Message):
    # Handle document message
    await message.reply_text(f"**File ID Genrated Successfully..!\n\nDocument's File ID :- `{message.document.file_id}`\n\n©️ [Star Bots Tamil](https://t.me/Star_Bots_Tamil)**", quote=True)

# Define handlers for voice and audio messages
@Client.on_message(filters.voice)
async def handle_voice(bot, message: Message):
    # Handle voice message
    await message.reply_text(f"**File ID Genrated Successfully..!\n\nVoice's File ID :- `{message.voice.file_id}`\n\n©️ [Star Bots Tamil](https://t.me/Star_Bots_Tamil)**", quote=True)

@Client.on_message(filters.audio)
async def handle_audio(bot, message: Message):
    # Handle audio message
    await message.reply_text(f"**File ID Genrated Successfully..!\n\nAudio's File ID :- `{message.audio.file_id}`\n\n©️ [Star Bots Tamil](https://t.me/Star_Bots_Tamil)**", quote=True)
