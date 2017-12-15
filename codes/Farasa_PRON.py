# -*- coding: UTF-8 -*-
from __future__ import division
import re
import xlsxwriter
import sys
reload(sys)
import collections
import copy
tashkeel_patt = ur"[\u0617-\u061A\u064B-\u0652]+"
col2=1
nsuff= {}
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
                nsufff[x[0]]=0
    return nsufff
workbook = xlsxwriter.Workbook((sys.argv[4])+'_shell_output/'+(sys.argv[4])+(sys.argv[5])+'.xlsx')
worksheet = workbook.add_worksheet()
workbook2 = xlsxwriter.Workbook((sys.argv[4])+'_shell_output/'+(sys.argv[4])+(sys.argv[5])+'_2.xlsx')
worksheet2 = workbook2.add_worksheet()
format = workbook.add_format()
format.set_bold()
format.set_font_color('white')
format.set_bg_color('green')
format.set_font_size(16)
format2 = workbook.add_format()
format2.set_bold()
format2.set_font_color('white')
format2.set_bg_color('#000080')
format2.set_font_size(20)
NSUFFc=[0]* 1000
NSUFFall={}
sentence=""
col=1
roww=1
avgNsuff=0
m=0

NSUFFallINIT=createList()
NSUFFall = copy.deepcopy(NSUFFallINIT)    

for i in range(1,size):
    print i
    nsuff = copy.deepcopy(NSUFFallINIT)    
    with open((sys.argv[4])+'_shell_output/Farasa_details/Farasa_POS_Type_6_'+str(i)+'.txt', "r") as f:
        for line in f:
            x = line.split("&")
            nsuff[x[0]]+=1
    allPron = sum(nsuff.values())
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
    roww = 1
    if i < 16000:
        for key in sorted(nsuff):
            worksheet.write(roww, col, str(i) +" & " +key+ " & "+str(words[i]) , format2)
            worksheet.write(roww + 1, col, nsuff[key], format)      
            worksheet.write(roww + 2, col, 100*nsuff[key]/allPron, format)
            NSUFFall[key] +=100*nsuff[key]/ allPron
            roww +=4
    else:
        
        for key in sorted(nsuff):
            worksheet2.write(roww, col2, str(i) +" & " +key+ " & "+str(words[i]) )
            worksheet2.write(roww + 1, col2, nsuff[key])      
            worksheet2.write(roww + 2, col2, 100*nsuff[key]/allPron)
            NSUFFall[key] +=100*nsuff[key]/ allPron
            roww +=4
        col2+=1    
    
    col +=1
    nsuff= {}
    allPron=0
    # print "======="
size=size-1 
roww =  4
for key in sorted(NSUFFall):
    for x in range(1,101):
        worksheet.write(roww, x ,NSUFFall[key]/size, format)
    roww+=4    
roww =  4
for key in sorted(NSUFFall):
    for x in range(1,101):
        worksheet2.write(roww, x ,NSUFFall[key]/size)
    roww+=4   

workbook.close()
workbook2.close()


