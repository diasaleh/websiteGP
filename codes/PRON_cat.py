# -*- coding: UTF-8 -*-
from __future__ import division
import re
import xlsxwriter
import sys
reload(sys)
import copy
import collections
tashkeel_patt = ur"[\u0617-\u061A\u064B-\u0652]+"

conn= {}
notconn= {}
sys.setdefaultencoding('utf-8')
from math import sqrt
from collections import Counter
from collections import defaultdict
size=int(sys.argv[3])+1
words=[0]* size
allwords=0
def createList():
    nsufff={}
    for i in range(1,size):
        with open((sys.argv[4])+'_shell_output/Farasa_details/Farasa_POS_Type_6_'+str(i)+'.txt', "r") as f:
            for line in f:
                x = line.split("&")
                if("+" in x[0]):
                    conn[x[0]]=0
                else:
                    notconn[x[0]]=0
    return conn,notconn
workbook = xlsxwriter.Workbook((sys.argv[4])+'_shell_output/'+(sys.argv[4])+(sys.argv[5])+'.xlsx')
worksheet = workbook.add_worksheet()
workbook2 = xlsxwriter.Workbook((sys.argv[4])+'_shell_output/'+(sys.argv[4])+(sys.argv[5])+'_2.xlsx')
worksheet2 = workbook2.add_worksheet()
format = workbook2.add_format()
format.set_bold()
format.set_font_color('white')
format.set_bg_color('green')
format.set_font_size(16)
format2 = workbook.add_format()
format2.set_bold()
format2.set_font_color('white')
format2.set_bg_color('#000080')
format2.set_font_size(20)
notconnallc=0
connallc=0
sentence=""
col=1
col2=1
roww=1
avgNsuff=0
connc=0
notconnc=0
m=0
connINIT ,notconnallINIT=createList()

for i in range(1,size):
    print i
    conn = copy.deepcopy(connINIT)
    notconn = copy.deepcopy(notconnallINIT)
    with open((sys.argv[4])+'_shell_output/Farasa_details/Farasa_POS_Type_6_'+str(i)+'.txt', "r") as f:
        for line in f:
            x = line.split("&")
            if("+" in x[0]):
                conn[x[0]]+=1
            else:
                notconn[x[0]]+=1    
    ff = open(sys.argv[1]+"/"+sys.argv[2]+str(i)+".txt", "r")
    sentence = ff.read()
    sentence = unicode(sentence, "utf-8")
    sentence = re.sub(tashkeel_patt,u"",sentence)
    x = sentence.split()
    words[i] += sum(len(xi) > 1 for xi in x)
    # print words[i]
    allwords += words[i] 
    ff.close()       
    # nsuff.append("+ا")
    # nsuff.append("+ان")
    # nsuff.append("+ة")
    # nsuff.append("+ات")
    # nsuff.append("+ون")
    # nsuff.append("+ين")
    # nsuff.append("+ي")
    # nsuff.append("+ان")
    # NSUFFc[i-1]+=8
    # counts = collections.OrderedDict(sorted(nsuff.items()))
       # if len(counts)<8:
    #     worksheet.write(roww, col, str(i) + "  " + "ا " + str(NSUFFc[i - 1]), format)
    #     worksheet.write(roww + 1, col, 0, format)
    #     worksheet.write(roww + 2, col,0, format)
    #     roww+=4
    connc = sum(conn.values())
    notconnc = sum(notconn.values())
    # for key in conn.keys():
    #     print key.decode("utf-8")
    # for key in notconn.keys():
    #     print key.decode("utf-8")    
    if i < 16000:
        worksheet.write(roww, col, str(i) +" & " +"conn"+ " & "+str(words[i]) , format2)
        worksheet.write(roww + 1, col,connc , format)      
        worksheet.write(roww + 2, col, 100*connc / (connc + notconnc), format)
        roww+=4
        worksheet.write(roww, col, str(i) +" & " +"conn"+ " & "+str(words[i]) , format2)
        worksheet.write(roww + 1, col,notconnc, format)      
        worksheet.write(roww + 2, col, 100*notconnc / (connc + notconnc), format)
    else:
        worksheet2.write(roww, col2, str(i) +" & " +"conn"+ " & "+str(words[i]))
        worksheet2.write(roww + 1, col2,connc )      
        worksheet2.write(roww + 2, col2, 100*connc / (connc + notconnc))
        roww+=4
        worksheet2.write(roww, col2, str(i) +" & " +"conn"+ " & "+str(words[i]) )
        worksheet2.write(roww + 1, col2,notconnc)      
        worksheet2.write(roww + 2, col2, 100*notconnc / (connc + notconnc))  
        col2+=1
    connallc +=100*connc / (connc + notconnc)
    notconnallc +=100*notconnc / (connc + notconnc)
    roww = 1
    col +=1
    conn= {}
    notconn= {}
    connc=0
    notconnc=0

    # print "======="
size=size-1 
roww =  4
for x in range(1,101):
    worksheet.write(roww, x ,connallc/size, format)
roww+=4
for x in range(1,101):
    worksheet.write(roww, x ,notconnallc/size, format)
roww =  4
for x in range(1,101):
    worksheet2.write(roww, x ,connallc/size)
roww+=4
for x in range(1,101):
    worksheet2.write(roww, x ,notconnallc/size)

workbook.close()
workbook2.close()