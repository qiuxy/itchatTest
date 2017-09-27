# coding=utf8
import itchat

from itchat.content import *


# itchat.auto_login()
# 给文件传输助手发一条消息
# itchat.send('Hello', toUserName='filehelper')



# a =itchat.search_friends()#获取自己用户信息
# a =itchat.search_friends(name='老邱')#按昵称获取用户信息
# a =itchat.search_friends(nickName='老邱')#按昵称获取用户信息
# a =itchat.search_friends(remarkName='爸爸')#按备注获取用户信息
# a = itchat.search_friends(wechatAccount='littlecodersh')  # 按微信号?获取用户信息（20170926测试不好用）
# a =itchat.search_friends(userName='@9cb5b2940741208a1d0033ae2165cef48a9aa71e0ad092ad03xxxxxx')#按微信生成的id获取用户信息
# print(a)



@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    # 回复发给自己的文本消息
    msg.user.send('%s,%s' % (msg.type, msg.text))


@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    # 20170926测试手机发的视频下载完是0kb pc传的没问题
    # msg['Text'](msg['FileName'])
    return '@%s@%s' % (msg.type, msg.fileName)


@itchat.msg_register(FRIENDS)  # , isGroupChat=True
def add_friend(msg):
    msg.user.verify()
    msg.user.send('hi...')


itchat.auto_login(hotReload=True)
itchat.run(debug=True)
