# coding=utf8
import itchat
import requests
from itchat.content import *


@itchat.msg_register(TEXT)
def text_reply(msg):
    defaultReply = 'I received: ' + msg.text
    reply = get_response(msg.text)
    re = reply or defaultReply
    print('%s say:%s,me reply %s' % (msg['User']['NickName'], msg.text, re))
    return re


KEY = 'xxxx'


def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': KEY,
        'info': msg,
        'userid': 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('url') or r.get('text')
    except:
        return


itchat.auto_login(hotReload=True)
itchat.run(debug=True)
