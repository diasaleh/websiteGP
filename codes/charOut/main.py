# -*- coding: UTF-8 -*-
from __future__ import division
import xlsxwriter
import sys
import re
tashkeel_patt = ur"[\u0617-\u061A\u064B-\u0652]+"

row = 3
row2 = 3
col = 1
col2 = 3
j=0
size=int(sys.argv[3])+1
import collections
avgcat1=0
avgcat2=0
avgcat3=0
avgcat4=0
avgcat5=0
col2=1
workbook = xlsxwriter.Workbook((sys.argv[4])+'_shell_output/'+(sys.argv[4])+'all_charOut.xlsx')
worksheet = workbook.add_worksheet()
workbook2 = xlsxwriter.Workbook((sys.argv[4])+'_shell_output/'+(sys.argv[4])+'all_charOut_2.xlsx')
worksheet2 = workbook2.add_worksheet()
format = workbook.add_format()
format.set_bold()
format.set_font_color('white')
format.set_bg_color('green')
format.set_font_size(16)
unk={}
def char_frequency(str1):
    dict = {}
    lett = 0
    for n in str1:
        keys = dict.keys()
        n = n.encode("utf-8")
        if not "?@-:*&^%$#@!;\"()‍ ×  ,ـ.-؛_«»[]}{= \\/~`–،؟".__contains__(n) and not n.isalpha() and not n.isdigit() and not n.isalnum():
            lett = lett+1
            if n in keys:
                dict[n] += 1
            else:
                dict[n] = 1
    return dict,lett
for i in range(1,size):
    f = open(sys.argv[1]+"/"+sys.argv[2]+str(i)+".txt", "r")
    sentence = f.read()
    sentence = unicode(sentence, "utf-8")
    sentence = re.sub(tashkeel_patt,u"",sentence)
    d,n=char_frequency(sentence)
    # d_view = [ (v,k) for k,v in d.iteritems() ]
    # d_view.sort(reverse=True)

    # print d
    # print n
    od = collections.OrderedDict(sorted(d.items()))
    u=0
    cat1=0
    cat2=0
    cat3=0
    cat4 = 0
    cat5 = 0
    for k, v in od.items():
        #print "%s : %d" % (k,v)
        sentence = unicode(k, "utf-8")
        if(k =="ء"or k=="أ" or k=="إ"  or k=="ئ"  or k=="ؤ"  or k=="ه"  or k=="ع"  or k=="غ"   or k=="ح"  or k=="خ"   ):
            cat1+= float((v*100)/(n* 1.0))
        elif k == "ق" or k == "ك" or k == "ج" or k == "ش" or k == "ي" or k == "ت" or k == "ط" or k == "د" or k == "ث" or k == "ظ" or k == "ذ"or k=="ن" or k == "ر" or k == "ز" or k == "ص"or k=="س"  or k == "ض"or k=="ل":
            cat2 += float((v * 100) / (n * 1.0))
        elif k == "ب" or k == "م" or k == "و" or k == "ف":
            cat3 += float((v * 100) / (n * 1.0))
        elif k == "و" or k == "ي" or k == "ا" or k == "آ" or k == "ى":
            cat4 += float((v * 100) / (n * 1.0))
        else:
            unkKeys = unk.keys()
            if k in unkKeys:
                unk[k] += 1
            else:
                unk[k] = 1
            cat5 += float((v * 100) / (n * 1.0))
    avgcat1 += cat1
    avgcat2+=cat2
    avgcat3+=cat3
    avgcat4+=cat4
    avgcat5+=cat5
    print i
    print "\nhulk: " + str(cat1)
    print "\nlesan: " + str(cat2)
    print "\nshefa: " + str(cat3)
    print "\njuff: " + str(cat4)
    print "\nUnknown: " + str(cat5)
    for ke in unk.keys():
        print ke
    print "\n=============\n"
    if i < 16000:
        worksheet.write(row, col, str(i) + " hulk",format)
        worksheet.write(row+1, col, cat1,format)

        worksheet.write(row+3, col, str(i) + " lesan", format)
        worksheet.write(row + 4, col, cat2, format)

        worksheet.write(row+6, col, str(i) + " shefa", format)
        worksheet.write(row + 7, col, cat3, format)

        worksheet.write(row+9, col, str(i) +" juff",format)
        worksheet.write(row + 10, col , cat4,format)
    else:
        worksheet2.write(row, col2, str(i) + " hulk")
        worksheet2.write(row+1, col2, cat1)

        worksheet2.write(row+3, col2, str(i) + " lesan")
        worksheet2.write(row + 4, col2, cat2)

        worksheet2.write(row+6, col2, str(i) + " shefa")
        worksheet2.write(row + 7, col2, cat3)

        worksheet2.write(row+9, col2, str(i) +" juff")
        worksheet2.write(row + 10, col2 , cat4)
        col2+=1
    col += 1
    row=3
    # for k, v in od2.items():
    #
    #     #print "%s : %d" % (k,v)
    #     sentence = unicode(k, "utf-8")
    #
    #     worksheet.write(row, col, sentence)
    #     worksheet.write(row, col + 1, float((v*100)/(n* 1.0)), format)
    #     row+=1
size=size-1
row = 3
for k in range(1,size+1):
    worksheet.write(row+2, k, avgcat1/size,format)
    worksheet.write(row+5, k, avgcat2/size,format)
    worksheet.write(row+8, k, avgcat3/size,format)
    worksheet.write(row+11, k, avgcat4/size,format)
for k in range(1,size+1):
    worksheet2.write(row+2, k, avgcat1/size)
    worksheet2.write(row+5, k, avgcat2/size)
    worksheet2.write(row+8, k, avgcat3/size)
    worksheet2.write(row+11, k, avgcat4/size)
workbook2.close()
workbook.close()