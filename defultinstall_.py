#!/usr/bin/env python
#coding=utf-8

import os
import fileinput

hostsdir="/data/ansible/hosts/"
ansdir="/etc/ansible/hosts"
ymldir="/data/ansible_playbook/"

os.system("clear")

create_input=raw_input("输入新建hosts文件名###英文###:")
os.system("mkdir /data/ansible/hosts -p")
createstr="touch %s%s" % (hostsdir,create_input)
createfilestr="%s%s" % (hostsdir,create_input)
print createfilestr
os.system(createstr)

group_input=raw_input("输入hosts文件中的组名###英文###:")
groupstr="echo -e [%s] >> %s" % (group_input,createfilestr)
print groupstr
os.system(groupstr)

server_input=raw_input("输入hosts文件中的IP###数字###可用 | 隔开输入多个IP:")
rawip = server_input.split("|")
for i in rawip:
    ip_line="echo %s >> %s" % (i,createfilestr)
    os.system(ip_line)
    print "加入%s到hosts文件完毕" % (i)

################################################################################
yamlinput=raw_input("创建yml文件，来启动初始化，请在此输入文件名：")
yamlstr="touch %s%s.yml" % (ymldir,yamlinput)
os.system(yamlstr)
yamlheadstr="echo -e \'- hosts: %s\' >> %s%s.yml" % (group_input,ymldir,yamlinput)
os.system(yamlheadstr)
print "加入头部 host 分组信息"


print "是否将此文件加入/etc/ansible/hosts"
add_input=input("输入1为是，输入0为否")

if add_input is 1:
    for line in fileinput.input(createfilestr):
        lineaddstr="echo -e \'%s\' >> %s" % (line,ansdir)
        print lineaddstr
        os.system(lineaddstr)
    print "成功增加到/etc/ansible/hosts"
elif add_input is 0:
    print "将不增加到/etc/ansible/hosts"
else:
    print "发生错误！"

rmhosts="rm -rf %s" % (createfilestr)
#os.system(rmhosts)