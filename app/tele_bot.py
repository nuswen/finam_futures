from tele_bot_tools import *
from tools import *
from app import models
from app import bot
from app import db
import json
import re
import requests
from time import sleep


"""rawData = models.data.query.filter_by(Id = 1).first()
data = rawData.Data
data = json.loads(data)"""

@bot.message_handler(commands=['prepare'])
def contentToFileId(msg):
    i = 'http://tg.lfinco.ru/ED.txt'
    rawDoc = requests.get(i,stream = True)
    doc = rawDoc.raw
    postMsg = bot.send_document(msg.chat.id, doc, None)
    poster(bot, msg.chat.id, text=postMsg)
    
    """rawData = models.data.query.filter_by(Id = 1).first()
    data = rawData.Data
    data = json.loads(data)
    if rawData.Prepare == False or rawData.Prepare == None:
        s = rawData.Data
        result = re.findall(r'http.+?jpg', s)
        result = set(result)
        for i in result:
            rawImg = requests.get(i,stream = True)
            img = rawImg.raw
            postMsg = bot.send_photo(msg.chat.id, img, None)
            # А теперь отправим вслед за файлом его file_id
            fileId = postMsg.json['photo']
            fileId = fileId[len(fileId)-1]['file_id']
            s = s.replace(i,fileId)
        rawData.Data = s
        rawData.Prepare = True
        db.session.commit()"""


@bot.message_handler(commands=['start'])
def hi_msg(msg):
    poster(bot, msg.chat.id, text='text')
    """start(msg.chat.id, data)
    text, keys, img = message(msg.chat.id, data)
    poster(bot, msg.chat.id, text=text, buttons=keys, img=img)
    user = models.teleusers.query.filter_by(Id = msg.chat.id).first()
    divert = True
    b = 0
    while divert:
        b = b + 1
        for i in data['data']['stitches'][user.Point]['content'][1:]:
            if 'divert' in i:
                b = 0
                nextPoint = i['divert']
                user.Point = nextPoint
                db.session.commit()
                text, keys, img = message(msg.chat.id, data)
                sleep(2)
                poster(bot, msg.chat.id, text=text, buttons=keys, img=img)
        if b == 2:
            divert = False"""
  
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    pass