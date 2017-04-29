# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 13:50:03 2017

@author: LENOVO
"""
import os

class IndexOpt(object):
    Path = "D:\Pythonworks\SQL"
    def cindex(self,sql):
        currentP = os.getcwd()
        if sql[1] != "on":
            print("can't disinguish %s" %sql[1])
        elif not sql[3].startswith('(') and sql[3].endswith(')'):
            print("loss '(' or ')' ")
        elif currentP == IndexOpt.Path:
            print('not choose database!')
        elif not os.path.exists("%s\%s" % (currentP,sql[2])):
            print("%s was not existed!" % sql[2])
        else:
            print("create index success!")
    def dindex(self,sqlC):
        currentP = os.getcwd()
        if currentP == IndexOpt.Path:
            print('not choose database!')
        else:
            print("drop index success!")
    def cuser(self,sqlC):
        if sqlC[1] != "indentified":
            print("can't disinguish %s" %sqlC[1])
        elif sqlC[2] != "by":
            print("can't disinguish %s" %sqlC[2])
        else:
            print("create user success!")
    def grant(self,sqlC):
        if sqlC[1] != "on":
            print("can't disinguish %s" %sqlC[1])
        elif sqlC[3] != "to":
            print("can't disinguish %s" %sqlC[3])
        else:
            currentP = os.getcwd()
            if currentP == IndexOpt.Path:
                print('not choose database!')
            else:
                if os.path.exists("%s\%s" % (currentP,sqlC[2]+"_dic.txt")):
                    print("grant success!") 
                else:
                    print(sqlC[2])
                    print("%s was existed!" % sqlC[2])
    def revoke(self,sqlC):
        if sqlC[1] != "on":
            print("can't disinguish %s" %sqlC[1])
        elif sqlC[3] != "from":
            print("can't disinguish %s" %sqlC[3])
        else:
            currentP = os.getcwd()
            if currentP == IndexOpt.Path:
                print('not choose database!')
            else:
                if os.path.exists("%s\%s" % (currentP,sqlC[2]+"_dic.txt")):
                    print("revoke success!")        
                else:
                    print(sqlC[2])
                    print("%s was existed!" % sqlC[2])