from pyrogram import filters, Client
from pyromod.helpers import ikb
from PIL import Image, ImageDraw, ImageFont, ImageSequence
import random

ID = int(os.environ.get('ID'))
HASH = os.environ.get('HASH')
TOKEN = os.environ.get('TOKEN)

gif = "utils/sayu.gif"
fnt = "utils/dafont.ttf"

app = Client('bot',api_id=ID,api_hash=HASH,bot_token=TOKEN)

keyboard = ikb([
    [('Support', 't.me/ShinobuSupport', 'url'), ('Repo', 'github.com/ItzKakarotto/sayu-chan', 'url')],
    [('Add Me', f"http://t.me/{(await app.get_me()).username}?startgroup=true", 'url')]
])

txt = [
"I'm Alive OwO!",
"Hewwo Senpai",
"*peeks*"
]



#def _gif(chatname, username):


@app.on_message(filters.private)
async def rstart(_, message):
    await app.send_chat_action(message.chat.id, 'typing')
    text = f"*Hewwo ~{}-Kun!* I'm Sayu[\u2063](https://telegra.ph/file/c330dd3c5770ae2da66c1.jpg)\nAdd me to Groups OwO and I'll welcome new Users OwO!"
    await message.reply_text(text, reply_markup=keyboard)

@app.on_message(filters.command('start') & filters.regex('sayu'))
async def _owo(_, message):
    chat_id = message.chat.id
    await app.send_message(chat_id, random.choice(txt))


