# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 14:15:15 2017

@author: LENOVO
"""
import os
from itertools import islice 

class TableOpt(object):
    Path = "D:\PythonWorks\SQL"
    def createtb(self,tabename,tableCon):
        currentP = os.getcwd()
        if currentP == TableOpt.Path:
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
    def alter(self,sqlC):  #传入语句    可以合并
        sql = " ".join(str(i) for i in sqlC)
        sql = sql.split(' ',2)            

        if sql[1] == 'add' and sql[2].startswith('(') and sql[2].endswith(')'):
            currentP = os.getcwd()
            if currentP == TableOpt.Path:
                print('not choose databse!')
            elif not os.path.exists("%s\%s" % (currentP,sql[0]+'_dic.txt')):
                print("%s was not existed!" % sql[0])
            else:
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
        elif sql[1] == 'drop':
            list = sql[2].split(',')
            currentP = os.getcwd()
            if currentP == TableOpt.Path:
                print('not choose databse!')
            elif not os.path.exists("%s\%s" % (currentP,sql[0]+'_dic.txt')):
                print("%s was not existed!" % sql[0])
            else:
                temp_f = open('tempfile.txt','a+')
                with open(sql[0]+'_dic.txt','r+') as f:
                    lines = f.readlines()
                    for line in lines:
                        if line.split("\t")[0] in list:
                            continue
                        temp_f.write(line)
                f.close()
                temp_f.close()
                os.remove(sql[0]+'_dic.txt')
                os.rename('tempfile.txt',sql[0]+'_dic.txt')
                print('alter drop success!')
        else:
            print('error:sql wrong!')
    def insert(self,sqlC):
        currentP = os.getcwd()
        sql = " ".join(str(i) for i in sqlC)
        sql = sql.split(' ',3)
        if currentP == TableOpt.Path:
            print('not choose databse!')
        elif sql[2] != "values":
            print("can't disinguish2 %s" %sql[2])
        elif not (sql[1].startswith('(') and sql[1].endswith(')') and sql[3].startswith('(') and sql[3].endswith(')')):
            print("loss '(' or ')' ")
        elif not os.path.exists("%s\%s" % (currentP,sql[0]+'_dic.txt')):
            print("%s was not existed!" % sql[0])
        else:
            list = []  #存字段名  
            input_file = open(sql[0]+'_dic.txt')  
            for line in islice(input_file, 1, None):  
                list.append(line.split("\t")[0])
            input_file.close()
           
            key = sql[1][1:-1].split(",")
            value = sql[3][1:-1].split(",")
            if len(key) != len(value):
                print("number is wrong!")
                return
            for k in key:
                if not k in list:
                    print("wrong:%s" % k)
                    return
            #检测对应属性类型
            fo = open(sql[0]+'.txt','a+')
            for l in list:
                if l in key:
                    for index in range(0,len(key)):
                        if key[index] == l:
                            fo.write(value[index]+"\t")
                else:
                     fo.write("\t")
            fo.write("\n")
            fo.close()
            print('insert success!')
    def delete(self,sqlC):
        ope = ["and","or","=","≠","≤","≥","<",">"]
        currentP = os.getcwd()
        sql = " ".join(str(i) for i in sqlC)
        sql = sql.split(' ',2)
        if currentP == TableOpt.Path:
            print('not choose database!')
        elif sql[1] != "where":
            print("can't disinguish %s 1" %sql[1])
        elif not sql[2].split(" ")[1] in ope:
            print("wrong:%s" % sql[2].split(" ")[1])
        elif not os.path.exists("%s\%s" % (currentP,sql[0]+'.txt')):
            print("%s was not existed!" % sql[0])
        else:
            list = []  #存字段名  
            input_file = open(sql[0]+'_dic.txt')  
            for line in islice(input_file, 1, None):  
                list.append(line.split("\t")[0])
            input_file.close()
            
            if not sql[2].split(" ")[0] in list:
                print("wrong:%s not existed" % sql[2].split(" ")[0])
            
            temp_f = open('tempfile.txt','a+')
            with open(sql[0]+'.txt','r+') as f:
                lines = f.readlines()
                for line in lines:
                    if line.split("\t")[list.index(sql[2].split(" ")[0])] == sql[2].split(" ")[2]:
                        continue
                    temp_f.write(line)
            f.close()
            temp_f.close()
            os.remove(sql[0]+'.txt')
            os.rename('tempfile.txt',sql[0]+'.txt')
            print('delete success!')
    def update(self,sqlC):
        if sqlC[1] != "set":
            print("error:%s" % sqlC[1])
        elif sqlC[3] != "where":
            print("error:%s" % sqlC[3])
        else:
            tl = TableOpt()
            currentP = os.getcwd()
            sql = " ".join(str(i) for i in sqlC)
            sql = sql.split(' ',3)
            if currentP == TableOpt.Path:
                print('not choose databse!')
            list = []  #存字段名  
            input_file = open(sqlC[0]+'_dic.txt')  
            for line in islice(input_file, 1, None):  
                list.append(line.split("\t")[0])
            input_file.close()
            
            re = []
            with open(sqlC[0]+'.txt','r+') as f:
                lines = f.readlines()
                for line in lines:
                    if line.split()[list.index(sqlC[4])] == sqlC[6]:
                        re.append(line)
            f.close()
            
            insertsql = []
            for setting in sql[2].split(","):        
                for i in range(0,len(re)):
                    li = re[i].split()
                    li[list.index(setting.split("=")[0])] = setting.split("=")[1]
            
                    list = ",".join(str(i) for i in list)
                    li = ",".join(str(i) for i in li)
                    insertsql.append(sql[0]+" ("+ list +")"+" values "+"("+li+")")
                    list = list.split(",")    
            
            delli = " ".join(str(i) for i in sqlC[4:])
            delsql = sql[0]+" where "+delli
            tl.delete(delsql.split())
            
            for ins in insertsql:
                tl.insert(ins.split())
                    
            print("update success!")
            
    def select(self,sqlC):
        ope = ["and","or","=","≠","≤","≥","<",">"]
        currentP = os.getcwd()
        
        list = []  #存字段名  
        input_file = open(sqlC[2]+'_dic.txt')  
        for line in islice(input_file, 1, None):  
            list.append(line.split("\t")[0])
        input_file.close()
        
        if currentP == TableOpt.Path:
            print('not choose database!')
            return
        elif sqlC[1] != "from":
            print("can't disinguish %s" %sqlC[1])
            return
        elif len(sqlC) > 3:
            if sqlC[3] != "where":
                print("can't disinguish %s" %sqlC[3])
                return
            elif not sqlC[5] in ope:
                print("wrong:%s" % sqlC[5])
                return
            elif not sqlC[4] in list:
                print("wrong:%s not existed" % sqlC[4])            
                return
        if sqlC[0] == "*":
            for l in list:
                print(l+"\t",end="")
            print()
            with open(sqlC[2]+'.txt','r') as f:         #读文件去换行
                lines = f.readlines()
                if len(sqlC) > 3:
                    for line in lines:
                        if line.split("\t")[list.index(sqlC[4])] == sqlC[6]:
                             print(line,end="")
                else:
                    for line in lines:
                        print(line,end="")
            f.close()
        else:
            it = sqlC[0].split(",")
            for item in it:
                if not (item in list):
                    print("wrong:%s" % item)
                    return
            for item in it:
                print(list[list.index(item)]+"\t",end="")
            print()
            
            with open(sqlC[2]+'.txt','r') as f:         #读文件去换行
                lines = f.readlines()
                if len(sqlC) > 3:
                    for line in lines:
                        if line.split("\t")[list.index(sqlC[4])] == sqlC[6]:
                            for item in it:
                                print(line.split("\t")[list.index(item)]+"\t",end="")
                else:
                    for line in lines:
                        for item in it:
                            print(line.split("\t")[list.index(item)]+"\t",end="")
                        print("\n")
            f.close()