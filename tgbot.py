import os
import random
import time
from pyrogram import filters, Client
from pyromod.helpers import ikb
from PIL import Image, ImageDraw, ImageFont, ImageSequence

ID = int(os.environ.get('ID'))
HASH = os.environ.get('HASH')
TOKEN = os.environ.get('TOKEN')

app = Client('bot',api_id=ID,api_hash=HASH,bot_token=TOKEN)

keyboard = ikb([
    [('Support', 't.me/ShinobuSupport', 'url'), ('Repo', 'github.com/ItzKakarotto/sayu-chan', 'url')],
    [('Add Me', f"http://t.me/SayuChan_Robot?startgroup=true", 'url')]
])

TEXTS = [
"I'm Alive OwO!",
"~Hewwo Senpai~",
"*peeks*",
"~blushes~"
]


@app.on_message(filters.private)
async def rstart(_, message):
    text = f"Hewwo ~{message.from_user.first_name}-Kun! I'm Sayu[\u2063](https://telegra.ph/file/c330dd3c5770ae2da66c1.jpg)\nAdd me to Groups and I'll welcome new Members OwO!"
    await message.reply_text(text, reply_markup=keyboard)

@app.on_message(filters.group & filters.regex(['Sayu', 'SAYU', 'sayu']))
async def start(_, message):
    chat_id = message.chat.id
    await app.send_chat_action(chat_id, 'typing')
    time.sleep(1)
    await app.send_message(chat_id, random.choice(TEXTS))


@app.on_message(filters.new_chat_members)
async def welcome(_, message):
    user = message.from_user
    chat_id = message.chat.id
    username = user.first_name
    chatname = message.chat.title

    gif = Image.open("utils/sayuchan.gif")
    txt = Image.new("RGBA", gif.size)

    if len(chatname)>16:
        try:
            chatname = chatname.split(" ", 1)[0]
        except:
            print("Chatname too long")
    
    text = f"Welcome to {chatname}! {username}-Kun!"
 
    ft = 200
    f = ft//len(text)
    fnt = ImageFont.truetype("utils/dafont.ttf", 18+f)

    ImageDraw.Draw(txt).text((35+f*10, 300), text, font=fnt,fill=(255, 255, 255), stroke_width=1, stroke_fill='black')
    
    frames = []
    for frame in ImageSequence.Iterator(gif):
        frame = frame.copy()
        if len(frames)>20:
            frame.paste(txt, mask=txt)
        frames.append(frame)
    
    frames[0].save(f"output{chat_id}{user.id}.gif", save_all=True, optimize=False, append_images=frames[1:])

    await message.reply_animation(f"output{chat_id}{user.id}.gif", caption=f"{username}-san just joined!")


def main():
    app.run()
    app.send_message(720518864, "Hewoo I'm back Senpai!")

main()
