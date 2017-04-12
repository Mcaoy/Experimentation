# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 10:34:45 2017

@author: LENOVO
"""

#import os
import DatabaseOpt as dbs
import TableOpt as tabe

print("Welcome to my SQL!")
command = ''

#while command != 'quit':
i=0
while i<5:
    i += 1
    command = input("SQL>>")    #写命令
    cmd = command.split(' ',command.count(' '))
    db = dbs.DatabaseOpt()
    tl = tabe.TableOpt()

    #判断是空语句
    if len(command) == 0:
        continue
    
    #判断是否以';'结尾
    if len(command)>0 and not cmd[len(cmd)-1].endswith(';'):
        print("error : loss ';'")
        continue
    cmd[len(cmd)-1] = cmd[len(cmd)-1][:-1]
    
    #create
    if cmd[0] == 'create' and len(cmd) >= 3:
        if cmd[1] == 'database':
            db.createdb(cmd[2])
        elif cmd[1] == 'table':
            if cmd[2].startswith("'") and cmd[2].endswith("'"):     #或者只含英文和数字
                tl.createtb(cmd[2][1:-1],cmd[3:])
            else:
                print("loss '\'' or '\'' ")
        else:
            print('error:command1')
            
    #drop
    elif cmd[0] == 'drop':
        if cmd[1] == 'database':
            db.dropdb(cmd[2])
        elif cmd[1] == 'table':
            tl.droptb(cmd[2])
        else:
            print('error:command2')
    
    #例如use student
    elif cmd[0] == 'use':
        db.usedb(cmd[1])
    
    #alter
    elif cmd[0] == 'alter':
        if cmd[1] == 'table':
            tl.alter(cmd[2:])
        else:
            print('error:command3')
            
    #insert
    elif cmd[0] == 'insert':
        if cmd[1] == 'into':
            tl.insert(cmd[2:])
        else:
            print("error:can not distinguish '%s'" % cmd[1])
    
    #delete
    elif cmd[0] == 'delete':
        if cmd[1] == 'from':
            tl.delete(cmd[2],cmd[3:])
        else:
            print('error:can not distinggush % s' % cmd[2])
    elif cmd[0] == 'update':
        tl.update(cmd[1:])
    else:
        print('错误命令')