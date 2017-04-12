# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 14:15:15 2017

@author: LENOVO
"""
import os

class TableOpt(object):
    def createtb(self,tabename,tableCon):
        currentP = os.getcwd()
        if currentP == 'D:\Pythonworks\SQL':
            print('not choose databse!')
        else:
            if os.path.exists("%s\%s" % (currentP,tabename)):
                print("%s was existed!" % tabename)
            else:
                tableCon = " ".join(str(i) for i in tableCon)
                if tableCon.startswith('(') and tableCon.endswith(')'):
                    Con = tableCon[1:-1].split(',')
                    fo = open(tabename+'_dic.txt','a+')
                    fo.write('字段名'+'\t'+'类型'+'\t'+'可空'+'\n')
                    for line in Con:
                        pre = ''
                        for l in line.split(' '):
                            if not pre == '':
                                fo.write('\t')
                            pre = l
                            fo.write(l)
                        fo.write('\n')
                    fo.close()
                    print('create table success!')
                else:
                    print("loss '(' or ')' ")
    def droptb(self,tabename):
        currentP = os.getcwd()
        if os.path.exists("%s\%s" % (currentP,tabename+'_dic.txt')):
            os.remove(tabename+'_dic.txt')
            if os.path.exists("%s\%s" % (currentP,tabename+'.txt')):
                os.remove(tabename+'.txt')
            print('drop table success!')
        else:
            print('not exist')
    def alter(self,sqlC):  #传入语句
        sql = " ".join(str(i) for i in sqlC)
        sql = sql.split(' ',2)

        if sql[1] == 'add' or sql[1] == 'drop' and sql[2].startswith('(') and sql[2].endswith(')'):
            currentP = os.getcwd()
            if currentP == 'D:\Pythonworks\SQL':
                print('not choose databse!')
            elif not os.path.exists("%s\%s" % (currentP,sql[0]+'_dic.txt')):
                print("%s was not existed!" % sql[0])
            elif sql[1] == 'add':
                fo = open(sql[0]+'_dic.txt','a+')
                sqlcon = sql[2][1:-1].split(' ')        #添加的属性的各项
                pre = ''
                for l in sqlcon:
                    if not pre == '':
                        fo.write('\t')
                    pre = l
                    fo.write(l)
                fo.write('\n')
                fo.close()
                print('alter add success!')
            else:
                print('alter drop success!')
        else:
            print('error:sql wrong!')
    def insert(self,sqlC):
        sql = " ".join(str(i) for i in sqlC)
        sql = sql.split(' ',3)
        print('insert操作:',sql)
    def delete(self,tabename,sqlC):
        print('delete操作:',sqlC)
    def update(self,sqlC):
        print('update操作:',sqlC)