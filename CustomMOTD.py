# -*- coding: utf-8 -*-

help='''=======§6CustomMOTD§r=======
使用§6!!motd <内容>§r即可修改MOTD
§a可以使用&颜色代码来更改颜色和格式
§a会自动替换成§
§d需要CarpetMOD支持！
'''

def on_info(server,info):
    if(info.content == '!!motd'):
        server.tell(info.player,help)
    if ('!!motd ' in info.content):
        motd=info.content[7:].replace('&','§')
        server.execute('carpet setDefault customMOTD {}'.format(motd))
        server.execute('say §e[MOTD]§r{}已经将MOTD修改为{}'.format(info.player,motd))

def on_load(server, old_module):
    server.add_help_message('!!motd', '§f获取CustomMOTD使用方法')