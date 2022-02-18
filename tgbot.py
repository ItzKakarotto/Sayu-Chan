from pyrogram import filters, Client
from pyromod.helpers import ikb
import os
from PIL import Image, ImageDraw, ImageFont, ImageSequence
import random

ID = int(os.environ.get('ID'))
HASH = os.environ.get('HASH')
TOKEN = os.environ.get('TOKEN')

gif = Image.open("utils/sayu.gif")
txt = Image.new("RGBA", gif.size)

app = Client('bot',api_id=ID,api_hash=HASH,bot_token=TOKEN)

keyboard = ikb([
    [('Support', 't.me/ShinobuSupport', 'url'), ('Repo', 'github.com/ItzKakarotto/sayu-chan', 'url')],
    [('Add Me', f"http://t.me/SayuChan_Robot?startgroup=true", 'url')]
])

txt = [
"I'm Alive OwO!",
"Hewwo Senpai",
"*peeks*"
]


#def _gif(chatname, username):


@app.on_message(filters.private)
async def rstart(_, message):
    text = f"*Hewwo ~{message.from_user.first_name}-Kun!* I'm Sayu[\u2063](https://telegra.ph/file/c330dd3c5770ae2da66c1.jpg)\nAdd me to Groups OwO and I'll welcome new Users OwO!"
    await message.reply_text(text, reply_markup=keyboard)

@app.on_message(filters.command('start') & filters.regex('sayu') & ~filters.private)
async def start(_, message):
    chat_id = message.chat.id
    await app.send_chat_action(message.chat.id, 'typing')
    await app.send_message(chat_id, random.choice(txt))

@app.on_message(filters.new_chat_members)
async def welcome(_, message):
    user = message.from_user
    chat_id = message.chat.id
    username = user.first_name
    chatname = message.chat.title
    if len(chatname)>16:
        try:
            chatname = chatname.split(" ", 1)[0]
        except:
            print("Chatname too long")
    
    text = f"Welcome to {chatname}! {username}-Kun!"
 
    ft = 200
    f = ft//len(text)
    font = ImageFont.truetype("utils/dafont.ttf", 20+f)

    draw = ImageDraw.Draw(txt).text((60+f*18, 410), text, font=font,fill=(255, 255, 255), stroke_width=1, stroke_fill='black')
    
    frames = []
    for frame in ImageSequence.Iterator(gif):
        frame = frame.copy()
        if len(frames)>40:
            frame.paste(txt, mask=txt)
        frames.append(frame)
        
    frames[0].save(f"output{chat_id}.gif", save_all=True, append_images=frames[1:])

    message.reply_animation(f"output{chat_id}.gif")


app.run()
