# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 10:50:24 2017

@author: LENOVO
"""
import os

class DatabaseOpt(object):
    def createdb(self,dbname):
        if os.path.exists("D:\Pythonworks\SQL\%s" % dbname):
            print("%s was existed!" % dbname)
        else:
            os.mkdir("D:\Pythonworks\SQL\%s" % dbname)
            print("create success!")
    def dropdb(self,dbname):
        if os.path.exists("D:\Pythonworks\SQL\%s" % dbname):
            os.rmdir("D:\Pythonworks\SQL\%s" % dbname)
            print("drop success!")
        else:
            print('%s not exists' % dbname)
    def usedb(self,dbname):
        if os.path.exists("D:\Pythonworks\SQL\%s" % dbname):
            os.chdir("D:\Pythonworks\SQL\%s" % dbname)
            print("into success!")
        else:
            print('%s not exists' % dbname)