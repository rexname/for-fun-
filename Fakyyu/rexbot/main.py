from telebot import TeleBot
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import time
import os
import re
import requests as req
import json
import dotenv
import xtravid
dotenv.load_dotenv()
token =  os.getenv('TOKEN')
import logging
logging.basicConfig(level=logging.INFO)

rexbot = TeleBot(token)
# @rexbot.message_handler(func=lambda message: Message)
def echo_all(message):      
    try:
        logging.info(f" {message.chat.type} Pesan dari {message.from_user.first_name + " "  + message.from_user.last_name} : \n{message.text}\n")
    except Exception as e:
        logging.error(f"Error processing message: {e}")
@rexbot.message_handler(commands=['start', 'help'])
def start(message):
    echo_all(message)
    fsad = """
*Kegunaan Bot ini*
>Membuat clash formating dengan cara langsung  dengan paste link vmess ataupun vless dan trojan
>*Contoh:*
>`vmess://`

*Untuk Donwload Sosmed juga bisa*
List link yang di support:
```
- Youtube (music/video)
- Intagram (Beta)
- Facebook (Beta)
- Mediafire
```
Langsung paste ygy
"""
    rexbot.reply_to(message, fsad, parse_mode="MarkdownV2")

youtube_regex = r'(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})'
instagram_regex = r'https?://(www\.)?instagram\.com  /(p|reel|tv|explore)/[a-zA-Z0-9._%+-]+'
facebook_regex = r'(https?://)?(www\.)?(facebook\.com|fb\.me)/(pages/[^/]+/||[^/?]+/)?([0-9]{1,15}|[a-zA-Z0-9.]+)(/.*)?'
mediafire_regex = r'https?://(www\.)?  mediafire\.com/(download|file|view)/[a-zA-Z0-9]+'

@rexbot.message_handler(func=lambda message: message.text and message.text.startswith("https"))
def downlaod(message: Message):
    link = message.text
    echo_all(message)
    api = "https://api.ryzendesu.vip/"
    ytget = req.get(url=f"{api}api/downloader/ytdl", params={"url": message.text})
    if ytget.status_code == 200:
        load = ytget.json()  # Mengambil JSON langsung
        title = load["result"]["title"]
        duration = load["result"]["duration"]
        author = load["result"]["author"]
        
        response_message = f"Title: {title}\nDuration: {duration}\nAuthor: {author}\n\n"
        
        # Membuat InlineKeyboardMarkup untuk video dan audio
        markup = InlineKeyboardMarkup()
        
        # Mengolah informasi video
        video_links = load["resultUrl"]["video"]
        if video_links:
            response_message += "Video Download Links:\n"
            for video in video_links:
                size = video["size"]
                format = video["format"]
                quality = video["quality"]
                download_link = video["download"]
                # Tambahkan tombol untuk video
                button = InlineKeyboardButton(f"{quality} ({size}, {format})", url=download_link)
                markup.add(button)
        else:
            response_message += "Tidak ada link video tersedia.\n"
        
        # Mengolah informasi audio
        audio_links = load["resultUrl"]["audio"]
        if audio_links:
            response_message += "Audio Download Links:\n"
            for audio in audio_links:
                size = audio["size"]
                format = audio["format"]
                quality = audio["quality"]
                download_link = audio["download"]
                # Tambahkan tombol untuk audio
                button = InlineKeyboardButton(f"{quality} ({size}, {format})", url=download_link)
                markup.add(button)
        else:
            response_message += "Tidak ada link audio tersedia.\n"
        
        # Mengirim pesan dengan inline keyboard
        rexbot.reply_to(message, response_message, reply_markup=markup, parse_mode='html')
    else:
        rexbot.reply_to(message, "Gagal mengunduh video, silakan coba lagi.")
    # if re.search(youtube_regex, message.text):
    #     echo_all(message)
    #     if ytget.status_code == 200:
    #         load = ytget.json()  # Mengambil JSON langsung
    #         title = load["result"]["title"]
    #         duration = load["result"]["duration"]
    #         author = load["result"]["author"]
            
    #         response_message = f"**Title:** {title}\n**Duration:** {duration}\n**Author:** {author}\n\n"
            
    #         # Mengolah informasi video
    #         video_links = load["resultUrl"]["video"]
    #         if video_links:
    #             response_message += "**Video Download Links:**\n"
    #             for video in video_links:
    #                 size = video["size"]
    #                 format = video["format"]
    #                 quality = video["quality"]
    #                 download_link = video["download"]
    #                 response_message += f"- {quality} ({size}, {format}): [Download]({download_link})\n"
    #         else:
    #             response_message += "Tidak ada link video tersedia.\n"
        
    #         # Mengolah informasi audio
    #         audio_links = load["resultUrl"]["audio"]
    #         if audio_links:
    #             response_message += "**Audio Download Links:**\n"
    #             for audio in audio_links:
    #                 size = audio["size"]
    #                 format = audio["format"]
    #                 quality = audio["quality"]
    #                 download_link = audio["download"]
    #                 response_message += f"- {quality} ({size}, {format}): [Download]({download_link})\n"
    #         else:
    #             response_message += "Tidak ada link audio tersedia.\n"
        
    #     rexbot.reply_to(message, response_message, parse_mode='MarkdownV2')
    # else:
    #     rexbot.reply_to(message, "Gagal mengunduh video, silakan coba lagi.")

@rexbot.message_handler(func=lambda message: message.text and message.text.lower().startswith(('trojan', 'vmess', 'vless')))
def xray(message: Message):
    echo_all(message)
    if message.chat.type == 'private':
        # Create InlineKeyboardMarkup object
        markup = InlineKeyboardMarkup()
        # Create buttons
        xray_button = InlineKeyboardButton("Clash", callback_data="clash")
        singbox_button = InlineKeyboardButton("Singbox", callback_data="singbox")
        cancel_button = InlineKeyboardButton("Batal", callback_data="cancel_clash")
        # Add buttons to markup
        markup.row(xray_button, singbox_button)
        markup.row(cancel_button)
        # Store the original message text for later use
        rexbot.reply_to(message, "Pilih opsi:", reply_markup=markup)
    else:
        rexbot.reply_to(message, "Gunakan Chat Private.")

# handle callback inline keytboard
# Handle callback queries
@rexbot.callback_query_handler(func=lambda call: True)
def xray_callback(call):
    try:
        options = {
    "clash" : "clash",
    "back_clash" : "clash",
    "singbox" : "singbox",
    # "back_singbox" : "singbox",
    "cancel_clash" : "cancel_clash",
    "back" : "back",
    "xl" : "xl",
    "xlvidio" : "xlvidio",
    "xldobleyt" :  "xldobleyt",
    "tsel" : "tsel" 
}
        if call.data in options:
            handle_format(call)
        else :
            pass
    except Exception as e:
        logging.error(f"Error in callback handler: {e}")
def handle_format(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    format_type = call.data  # Ambil data dari callback query
    if format_type == "clash": # xl, tsel, back
        markup = InlineKeyboardMarkup()
        xl = InlineKeyboardButton("xl", callback_data="xl")
        tsel = InlineKeyboardButton("tsel", callback_data="tsel")
        back_button = InlineKeyboardButton("Kembali", callback_data="back")
        
        # Tambahkan button ke markup
        markup.row(xl, tsel)
        markup.row(back_button)
        
        # Edit pesan dengan pilihan baru
        rexbot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="Pilih format yang diinginkan:",
            reply_markup=markup
        )
    elif call.data == "xl": # xlvidio, xldobleyt, back_clash
        # Buat markup baru untuk pilihan xl
        markup = InlineKeyboardMarkup()
        xlvid = InlineKeyboardButton("Vidio", callback_data="xlvidio")
        xldobel = InlineKeyboardButton("Doble Youtube", callback_data="xldobleyt")
        # xldobel = InlineKeyboardButton("", callback_data="xldobleyt")
        back_button = InlineKeyboardButton("Kembali", callback_data="back_clash")
        # Tambahkan button ke markup
        markup.row(xlvid, xldobel)
        markup.row(back_button)
        # Handle pilihan xl
        rexbot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Pilih paket:", reply_markup=markup
        )
    elif format_type == "singbox": # singbox
        # Handle pilihan Sing-Box
        rexbot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="Format Sing-Box akan segera hadir!"
        )
    elif format_type == "back":  # clash, singbox, cancel_clash
        # Handle pilihan awal
        markup = InlineKeyboardMarkup()
        # Create buttons
        xray_button = InlineKeyboardButton("Clash", callback_data="clash")
        singbox_button = InlineKeyboardButton("Singbox", callback_data="singbox")
        cancel_button = InlineKeyboardButton("Batal", callback_data="cancel_clash")
        # Add buttons to markup
        markup.row(xray_button, singbox_button)
        markup.row(cancel_button)
        rexbot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="Pilih opsi:",
            reply_markup=markup
        )
    elif format_type == "cancel_clash": # cancel_clash
        # Handle cancel_clash
        rexbot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="Permintaan di tangguhkan!"
        )
    elif format_type == "xlvidio": #xlvidio
        convert = xtravid.xtravid(call.message.reply_to_message.text) #xtc.convert_link(call.message.reply_to_message.text)
        rexbot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text=f'ini Detail nya:\n{convert}',
            parse_mode='MarkdownV2'
        )
@rexbot.message_handler(func=lambda message: message.text and message.text.lower() == 'ping')
def ping(message: Message):
    echo_all(message)
    start_time = time.time()
    sent_message = rexbot.reply_to(message, "Pong!")
    end_time = time.time()
    
    duration = round((end_time - start_time)  * 1000 / 3, 2)
    spinner = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿" , f"Pong! 🏓\nResponse time: {duration}ms"]
    for chat in range(len(spinner)):
        rexbot.edit_message_text(f'{
            spinner[chat]
            }', chat_id=message.chat.id,  message_id=sent_message.message_id)
    # rexbot.edit_message_text(f"Pong! 🏓\nResponse time: {duration}ms", chat_id=message.chat.id, message_id=sent_message.message_id)
    # echo_all(message)


def runBot():
    rexbot.infinity_polling()

if  __name__ == "__main__":
    runBot()
