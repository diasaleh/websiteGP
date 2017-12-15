# -*- coding: UTF-8 -*-
from __future__ import division
import re
import xlsxwriter
from math import sqrt
import sys
tashkeel_patt = ur"[\u0617-\u061A\u064B-\u0652]+"
col2=1

size=int(sys.argv[3])+1
V=[0] * size
PREP=[0]* size
PART=[0]* size
DET=[0]* size
NOUN=[0]* size
NSUFF=[0]* size
ADJ=[0]* size
PRON=[0]* size
NUM=[0]* size
CONJ=[0]* size
FUT_PART=[0]*size
CASE=[0]*size
ADV=[0]*size
FOREIGN=[0]*size
ABBREV=[0]*size
words=[0]* size
avgV=[0]* size
sentence=""
row = 4
col = 2

allwords=0
j=0
workbook = xlsxwriter.Workbook((sys.argv[4])+'_shell_output/'+(sys.argv[4])+'POS.xlsx')
worksheet = workbook.add_worksheet()
workbook2 = xlsxwriter.Workbook((sys.argv[4])+'_shell_output/'+(sys.argv[4])+'POS_2.xlsx')
worksheet2 = workbook2.add_worksheet()
format = workbook.add_format()
format.set_bold()
format.set_font_color('white')
format.set_bg_color('green')
format.set_font_size(20)

format2 = workbook.add_format()
format2.set_bold()
format2.set_font_color('white')
format2.set_bg_color('#000080')
format2.set_font_size(20)
for t in range(2,size+1):
    worksheet.write(row, t , "Verbs",format2)
    row=row+4
    worksheet.write(row, t , "PREP",format2)
    row = row + 4
    worksheet.write(row, t , "PART",format2)
    row=row+4
    worksheet.write(row, t  ,  "DET",format2)
    row=row+4
    worksheet.write(row, t , "NOUN",format2)
    row=row+4
    worksheet.write(row, t , "NSUFF",format2)
    row=row+4
    worksheet.write(row, t ,"PRON",format2)
    row=row+4
    worksheet.write(row, t ,"NUM",format2)
    row=row+4
    worksheet.write(row, t ,"CONJ",format2)
    row=row+4
    worksheet.write(row, t , "ADJ",format2)
    row=row+4
    worksheet.write(row, t , "FUT_PART",format2)
    row=row+4
    worksheet.write(row, t , "CASE",format2)
    row=row+4
    worksheet.write(row, t , "ADV",format2)
    row=row+4
    worksheet.write(row, t , "ABBREV",format2)
    row=row+4
    worksheet.write(row, t , "FOREIGN",format2)
    row=row+4
    worksheet.write(row, t , "words",format2)
    row=4
pos =[]
avgVs=[0]*16
fil=[0]*16

l=0
o = open((sys.argv[4])+'_shell_output/'+str(sys.argv[4])+'POS.txt',"w")
wordcf = open((sys.argv[4])+'_shell_output/'+(sys.argv[4])+'wordsCount.txt',"w")
for i in range(1,size):
    for fi in range(0,len(fil)):
        fil[fi] = open((sys.argv[4])+'_shell_output/'+'Farasa_details/' + 'Farasa_POS_Type_' +str(fi)+'_'+str(i) + ".txt", 'w')
    f = open(sys.argv[1]+"/"+sys.argv[2]+str(i)+".txt", "r")
    sentence = f.read()
    sentence = unicode(sentence, "utf-8")
    sentence = re.sub(tashkeel_patt,u"",sentence)
    x = sentence.split()
    words[i] += sum(len(xi) > 1 for xi in x)
    print words[i]
    allwords += words[i]
    print sys.argv[2]+str(i)+""
    with open((sys.argv[4])+'_shell_output/'+'Farasa/'+(sys.argv[4])+'F2_'+str(i)+'.txt', "r") as ff:
        for line in ff:
            x = line.split("&")
            if len(x) > 2:
                if x[1] == "V":
                    V[i]+=  1
                    fil[0].write(line)
                elif x[1] == "PREP":
                    fil[1].write(line)
                    PREP[i] = PREP[i] + 1
                elif x[1] == "PART":
                    PART[i] = PART[i] + 1
                    fil[2].write(line)
                elif x[1] == "DET":
                    DET[i] = DET[i] + 1
                    fil[3].write(line)
                elif x[1] == "NOUN":
                    NOUN[i] = NOUN[i] + 1
                    fil[4].write(line)
                elif x[1] == "NSUFF":
                    NSUFF[i] = NSUFF[i] + 1
                    fil[5].write(line)
                elif x[1] == "PRON":
                    PRON[i] = PRON[i] + 1
                    fil[6].write(line)
                elif x[1] == "NUM":
                    NUM[i] = NUM[i] + 1
                    fil[7].write(line)
                elif x[1] == "CONJ":
                    CONJ[i] = CONJ[i] + 1
                    fil[8].write(line)
                elif x[1] == "ADJ":
                    ADJ[i] = ADJ[i] + 1
                    fil[9].write(line)
                elif x[1] == "FUT_PART":
                    FUT_PART[i] = FUT_PART[i] + 1
                    fil[10].write(line)
                elif x[1] == "CASE":
                    CASE[i] = CASE[i] + 1
                    fil[11].write(line)
                elif x[1] == "ADV":
                    ADV[i] = ADV[i] + 1
                    fil[12].write(line)
                elif x[1] == "ABBREV":
                    ABBREV[i] = ABBREV[i] + 1
                    fil[13].write(line)
                elif x[1] == "FOREIGN":
                    FOREIGN[i] = FOREIGN[i] + 1
                    fil[14].write(line)
                else:
                    print line

    o.write(str(sys.argv[2])+str(i)+'.txt'+"\n")
    o.write(str(words[i])+"\n")
    o.write(str(V[i])+"\n")
    o.write(str(PREP[i])+"\n")
    o.write(str(PART[i])+"\n")
    o.write(str(DET[i])+"\n")
    o.write(str(NOUN[i])+"\n")
    o.write(str(NSUFF[i])+"\n")
    o.write(str(PRON[i])+"\n")
    o.write(str(NUM[i])+"\n")
    o.write(str(CONJ[i])+"\n")
    o.write(str(ADJ[i])+"\n")
    o.write(str(FUT_PART[i])+"\n")
    o.write(str(CASE[i])+"\n")
    o.write(str(ADV[i])+"\n")
    o.write(str(ABBREV[i])+"\n")
    o.write(str(FOREIGN[i])+"\n")
    o.write("=========================================\n")
    pos.append(V[i])
    pos.append(PREP[i])
    pos.append(PART[i])
    pos.append(DET[i])
    pos.append(NOUN[i])
    pos.append(NSUFF[i])
    pos.append(PRON[i])
    pos.append(NUM[i])
    pos.append(CONJ[i])
    pos.append(ADJ[i])
    pos.append(FUT_PART[i])
    pos.append(CASE[i])
    pos.append(ADV[i])
    pos.append(ABBREV[i])
    pos.append(FOREIGN[i])
    pos.append(words[i])
    if i < 16000:
        row = 2
        worksheet.write(row, col, i , format)
        row=3
        worksheet.write(row, col, words[i],format)
        row=4
        for item in (pos):
            worksheet.write(row+1, col, item,format)
            worksheet.write(row+2, col, (100*item)/words[i],format)
            avgVs[l] = (100*item)/words[i] +avgVs[l]
            l=l+1
            row += 4
    else:
        
        row = 2
        worksheet2.write(row, col2, i)
        row=3
        worksheet2.write(row, col2, words[i])
        row=4
        for item in (pos):
            worksheet2.write(row+1, col2, item)
            worksheet2.write(row+2, col2, (100*item)/words[i])
            avgVs[l] = (100*item)/words[i] +avgVs[l]
            l=l+1
            row += 4 
        col2 = col2 + 1           
    l=0
    pos=[]
    col = col + 1
    print col

wordcf.write("allwords = "+ str(allwords)+"\n")
wordcf.close()

row=7

size=size-1
for k in range(0,len(avgVs)):
    for i in range(2,size+2):
        worksheet.write(row, i , avgVs[k]/size ,format)
    row+=4

row=7
for k in range(0,len(avgVs)):
    for i in range(1,size+2):
        worksheet2.write(row, i , avgVs[k]/size )
    row+=4    
workbook.close()
workbook2.close()