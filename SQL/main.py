# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 10:34:45 2017

@author: LENOVO
"""

#import os
import DatabaseOpt as dbs
import TableOpt as tabe
import IndexOpt as idx

print("\nWelcome to my SQL!")
command = ''

while (1):
    command = input("SQL>>")    #写命令
    
    if command == "quit":
        break
                   
    cmd = command.split(' ',command.count(' '))
    db = dbs.DatabaseOpt()
    tl = tabe.TableOpt()
    ix = idx.IndexOpt()

    #判断是空语句
    if len(command) == 0:
        continue
    
    #判断是否以';'结尾
    if len(cmd)>0 and not cmd[len(cmd)-1].endswith(';'):
        print("error : loss ';'")
        continue
    cmd[len(cmd)-1] = cmd[len(cmd)-1][:-1]
    
    #create
    if cmd[0] == 'create' and len(cmd) >= 3:
        if cmd[1] == 'database':
            db.createdb(cmd[2])
        elif cmd[1] == 'table':
            tl.createtb(cmd[2:])
        elif cmd[1] == "index":
            ix.cindex(cmd[2:])
        elif cmd[1] == 'user':
            ix.cuser(cmd[2:])
        else:
            print('error:can not create %s' % cmd[1])
            
    #drop
    elif cmd[0] == 'drop':
        if cmd[1] == 'database':
            db.dropdb(cmd[2])
        elif cmd[1] == 'table':
            tl.droptb(cmd[2:])
        elif cmd[1] == 'index':
            ix.dindex(cmd[2:])
        else:
            print('error:can not drop %s' % cmd[1])
    
    #例如use student
    elif cmd[0] == 'use':
        db.usedb(cmd[1])
    
    #alter
    elif cmd[0] == 'alter':
        if cmd[1] == 'table':
            tl.alter(cmd[2:])
        else:
            print('error:only can alter table')
            
    #insert
    elif cmd[0] == 'insert':
        if cmd[1] == 'into':
            tl.insert(cmd[2:])
        else:
            print("error:can not distinguish '%s'" % cmd[1])
    
    #delete
    elif cmd[0] == 'delete':
        if cmd[1] == 'from':
            tl.delete(cmd[2:])
        else:
            print('error:can not distinggush % s' % cmd[2])
            
    #updata
    elif cmd[0] == 'update':
        tl.update(cmd[1:])
    
    #select
    elif cmd[0] == "select":
        tl.select(cmd[1:])
       
    #grant
    elif cmd[0] == "grant":
        ix.grant(cmd[1:])
        
    elif cmd[0] == "revoke":
        ix.revoke(cmd[1:])
        
    else:
        print('错误命令')