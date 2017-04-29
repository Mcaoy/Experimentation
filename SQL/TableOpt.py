
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 14:15:15 2017

@author: LENOVO
"""
import os
from itertools import islice 

class TableOpt(object):
    Path = "D:\Pythonworks\SQL"
    Dic_list = "字段名"+'\t'+"类型"+"主键"+"索引"
    
    def checking1(self,name):
        currentP = os.getcwd()
        if currentP == TableOpt.Path:
            print('not choose database!')
            return 0
        elif os.path.exists("%s\%s" % (currentP,name+'_dic.txt')):
            print("%s was existed!" % name)
            return 0
    def checking2(self,name):
        currentP = os.getcwd()
        if currentP == TableOpt.Path:
            print('not choose database!')
            return 0
        elif not os.path.exists("%s\%s" % (currentP,name+'_dic.txt')):
            print("%s was not existed!" % name)
            return 0
                
    def createtb(self,sql):
        to = TableOpt()
        Con = " ".join(str(i) for i in sql[1:])
        
        if not sql[0].isalpha():
            print("error:lose name!")
            return
        
        if Con.startswith('(') and Con.endswith(')'):
            if to.checking1(sql[0]) == 0:
                return
            Con = Con[1:-1].split(',')
            fo = open(sql[0]+'_dic.txt','a+')
            fo.write(TableOpt.Dic_list+'\n')
            for line in Con:
                pre = ''
                for item in line.split():
                    if not pre == '':
                        fo.write('\t')
                    pre = item
                    fo.write(item)
                fo.write('\n')
            fo.close()
            print('create table success!')
        else:
            print("loss '(' or ')' ")

    def droptb(self,sql):
        if len(sql) > 1:
            print("error:only can be one!")
            return

        to = TableOpt()

        if to.checking2(sql[0]) == 0:
            return
        else:
            os.remove(sql[0]+'_dic.txt')
            if os.path.exists("%s\%s" % (os.getcwd(),sql[0]+'.txt')):
                os.remove(sql[0]+'.txt')
            print('drop table success!')
        
    def alter(self,sql):  #传入语句    可以合并
        sql = " ".join(str(i) for i in sql)
        sql = sql.split(' ',2)     
        
        if "add" in sql[0] or "drop" in sql[0]:
            print("error:lose name!")
            return
        
        to = TableOpt()
        if to.checking2(sql[0]) == 0:
            return
        if sql[1] == 'add' and sql[2].startswith('(') and sql[2].endswith(')'):
            fo = open(sql[0]+'_dic.txt','a+')
            sqlcon = sql[2][1:-1].split(',')        #添加的属性  增加列
            for con in sqlcon:
                pre = ''
                for l in con.split():
                    if not pre == '':
                        fo.write('\t')
                    pre = l
                    fo.write(l)
                fo.write('\n')
            fo.close()
            
            temp_f = open('tempfile.txt','a+')
            with open(sql[0]+'.txt','r+') as f:
                lines = f.readlines()
                for line in lines:
                    line = line.strip("\n")
                    for num in range(0,len(sqlcon)):
                        temp_f.write(line+""+"\t")
                    temp_f.write("\n")
            f.close()
            temp_f.close()
            os.remove(sql[0]+'.txt')
            os.rename('tempfile.txt',sql[0]+'.txt')
            
            print('alter add success!')
        elif sql[1] == 'drop':              #可以drop多个
            lx = []  #存字段名
            input_file = open(sql[0]+'_dic.txt')
            for line in islice(input_file, 1, None):  
                lx.append(line.split("\t")[0])
            input_file.close()
            
            list = sql[2].split(',')
            droplist = []
            for item in list:
                if item in lx:
                    droplist.append(lx.index(item))
                else:
                    print("%s is not existed" % item)
                    return
        
            temp_f = open('tempfile.txt','a+')
            with open(sql[0]+'_dic.txt','r+') as f:
                lines = f.readlines()
                for line in lines:
                    line = line.strip("\n")
                    if line.split("\t")[0] in list:
                        continue
                    temp_f.write(line+"\n")
            f.close()
            temp_f.close()
            os.remove(sql[0]+'_dic.txt')
            os.rename('tempfile.txt',sql[0]+'_dic.txt')
            
            if os.path.exists("%s\%s" % (os.getcwd(),sql[0]+'.txt')):
                temp_f = open('tempfile.txt','a+')
                with open(sql[0]+'.txt','r+') as f:
                    lines = f.readlines()
                    for line in lines:
                        line = line.strip("\n").rstrip("\t")
                        templine = line.split("\t")
                        for num in range(0,len(templine)):
                            if num in droplist:
                                continue
                            temp_f.write("\t"+templine[num])
                        temp_f.write("\n") 
                f.close()
                temp_f.close()
                os.remove(sql[0]+'.txt')
                os.rename('tempfile.txt',sql[0]+'.txt')
            print('alter drop success!')
        else:
            print('error:sql wrong,loss add or drop!')
    def insert(self,sql):
        to = TableOpt()
        if not sql[0].isalpha():
            print("error:lose name!")
            return
        if sql[2] != "values":
            print("can't disinguish2 %s,must be values!" %sql[2])
            return
        if not (sql[1].startswith('(') and sql[1].endswith(')') and sql[3].startswith('(') and sql[3].endswith(')')):
            print("loss '(' or ')' ")
            return
        if to.checking2(sql[0]) == 0:
            return
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
        str = ""
        for l in list:
            if l in key:
                for index in range(0,len(key)):
                    if key[index] == l:
                        str += value[index]+"\t"
            else:
                str += ""+"\t"
        fo.write(str.rstrip("\t")+"\n")
        fo.close()
        print('insert success!')
    def delete(self,sql):
        ope = ["and","or","=","≠","≤","≥","<",">"]
        to = TableOpt()
        if not sql[0].isalpha():
            print("error:lose name!")
        elif sql[1] != "where":
            print("can't disinguish2 %s,must be 'where'!" %sql[1])
        elif to.checking2(sql[0]) == 0:
            return
        else:
            mark = ""
            for s in sql[2]:
                if s in ope:
                    mark = s
                    break
            if mark == "":
                print("loss condition!")
                return
            list = []  #存字段名  
            input_file = open(sql[0]+'_dic.txt')  
            for line in islice(input_file, 1, None):  
                list.append(line.split("\t")[0])
            input_file.close()
            
            if not sql[2].split(mark)[0] in list:
                print("wrong:%s not existed" % sql[2].split(mark)[0])
            
            temp_f = open('tempfile.txt','a+')
            with open(sql[0]+'.txt','r+') as f:
                lines = f.readlines()
                for line in lines:
                    if line.rstrip("\n").split("\t")[list.index(sql[2].split(mark)[0])] == sql[2].split(mark)[1]:
                        continue
                    temp_f.write(line)
            f.close()
            temp_f.close()
            os.remove(sql[0]+'.txt')
            os.rename('tempfile.txt',sql[0]+'.txt')
            print('delete success!')
    def update(self,sql):
        to = TableOpt()
        ope = ["and","or","=","≠","≤","≥","<",">"]
        if sql[1] != "set":
            print("error:%s" % sql[1])
        elif sql[3] != "where":
            print("error:%s" % sql[3])
        elif to.checking2(sql[0]) == 0:
            return
        else:
            tl = TableOpt()
            list = []  #存字段名  
            input_file = open(sql[0]+'_dic.txt')  
            for line in islice(input_file, 1, None):  
                list.append(line.split("\t")[0])
            input_file.close()
            
            mark = ""
            for s in sql[4]:
                if s in ope:
                    mark = s
                    break
            if mark == "":
                print("loss condition!")
                return
            
            re = []
            with open(sql[0]+'.txt','r+') as f:
                lines = f.readlines()
                for line in lines:
                    line = line.rstrip("\n")
                    if line.split("\t")[list.index(sql[4].split(mark)[0])] == sql[4].split(mark)[1]:
                        re.append(line)
            f.close()
            
            insertsql = []
            for setting in sql[2].split(","):        
                for i in range(0,len(re)):
                    li = re[i].split("\t")
                    li[list.index(setting.split("=")[0])] = setting.split("=")[1]
            
                    list = ",".join(str(i) for i in list)
                    li = ",".join(str(i) for i in li)
                    insertsql.append(sql[0]+" ("+ list +")"+" values "+"("+li+")")
                    list = list.split(",")    
            
            delsql = sql[0]+" where "+sql[4]
            tl.delete(delsql.split())
            
            for ins in insertsql:
                tl.insert(ins.split())
                    
            print("update success!")
            
    def select(self,sql):
        ope = ["and","or","=","≠","≤","≥","<",">"]
        to = TableOpt()
        
        list = []  #存字段名  
        input_file = open(sql[2]+'_dic.txt')  
        for line in islice(input_file, 1, None):  
            list.append(line.split("\t")[0])
        input_file.close()
        
        if sql[1] != "from":
            print("can't disinguish %s" %sql[1])
        elif len(sql) > 3:
            if sql[3] != "where":
                print("can't disinguish %s" %sql[3])
                return
            else:
                mark = ""
                for s in sql[4]:
                    if s in ope:
                        mark = s
                        break
                if mark == "":
                    print("loss condition!")
                    return
        elif to.checking2(sql[2]) == 0:
            return
            
        if sql[0] == "*":
            str = ""
            for l in list:
                str += l+"\t"
            print(str.rstrip("\t"))
            with open(sql[2]+'.txt','r') as f:
                lines = f.readlines()
                for line in lines:
                    line = line.rstrip("\n")
                    if len(sql) > 3:
                        if line.split("\t")[list.index(sql[4].split(mark)[0])] == sql[4].split(mark)[1]:
                             print(line)
                    else:
                        print(line)
            f.close()
        else:
            it = sql[0].split(",")
            head = ""
            for item in it:
                if not (item in list):
                    print("wrong:%s" % item)
                    return
                head += item+"\t"
            print(head.rstrip("\t"))
            
            with open(sql[2]+'.txt','r') as f:
                lines = f.readlines()
                for line in lines:
                    line = line.rstrip("\n")
                    tmpl = ""
                    if len(sql) > 3:
                        if line.split("\t")[list.index(sql[4].split(mark)[0])] == sql[4].split(mark)[1]:
                            for item in it:
                                tmpl += line.split("\t")[list.index(item)]+"\t"
                            print(tmpl.rstrip("\t"))
                    else:
                        for item in it:
                            tmpl += line.split("\t")[list.index(item)]+"\t"
                            print(tmpl.rstrip("\t"))
            f.close()