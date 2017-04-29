# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 10:50:24 2017

@author: LENOVO
"""
import os

class DatabaseOpt(object):
    Path = "D:\PythonWorks\SQL"
    def createdb(self,dbname):
        if os.path.exists("%s\%s" % (DatabaseOpt.Path,dbname)):
            print("%s was existed!" % dbname)
        else:
            os.mkdir("%s\%s" % (DatabaseOpt.Path,dbname))
            print("create success!")
    def dropdb(self,dbname):
        if os.path.exists("%s\%s" % (DatabaseOpt.Path,dbname)):
            os.rmdir("%s\%s" % (DatabaseOpt.Path,dbname))
            print("drop success!")
        else:
            print('%s not exists' % dbname)
    def usedb(self,dbname):
        if os.path.exists("%s\%s" % (DatabaseOpt.Path,dbname)):
            os.chdir("%s\%s" % (DatabaseOpt.Path,dbname))
            print("into success!")
        else:
            print('%s not exists' % dbname)