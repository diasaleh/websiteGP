# -*- coding: UTF-8 -*-
from __future__ import division
import xlsxwriter
import sys



row = 3
row2 = 3
col = 1
col2 = 1
j=0
size=int(sys.argv[3])+1
import collections
avgcat1=0
avgcat2=0
workbook = xlsxwriter.Workbook(str(sys.argv[4])+'_shell_output/'+str(sys.argv[4])+'all_Mjhor_Mhmos_details.xlsx')
worksheet = workbook.add_worksheet()
workbook2 = xlsxwriter.Workbook(str(sys.argv[4])+'_shell_output/'+str(sys.argv[4])+'all_Mjhor_Mhmos_details_2.xlsx')
worksheet2 = workbook2.add_worksheet()
format = workbook.add_format()
format.set_bold()
format.set_font_color('white')
format.set_bg_color('green')
format.set_font_size(16)

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
    for k, v in od.items():
        #print "%s : %d" % (k,v)
        sentence = unicode(k, "utf-8")
        # مجهورة ( Voiced )(ب، ج، د، ر، ز، ط، ع، غ، ص، ل، م، ن، و، ي)
        if(k =="ع"or k=="غ" or k == "ق"or k=="ج"  or k=="ب"  or k=="ض"  or k=="ل"  or k=="ن"  or k=="ر"   or k=="د"  or k=="ز"  or k=="ذ"  or k=="ظ"  or k=="و"  or k=="م"  or k=="ي" ):
            cat1+= float((v*100)/(n* 1.0))

        # مهموسة ( Voiceless ) حروفها : (ف، ح، ث، هـ، ش، خ، ص، س، ك، ت، ق، ط، ء) - عند المحدثين
        elif k == "ت" or k == "س" or k == "ش" or k == "ك" or k == "خ" or k == "ه" or k == "ح" or k == "ص" or k == "ث"  or k ==  "ف" :
            cat2 += float((v * 100) / (n * 1.0))
        else:
            print v, k
            cat3 += float((v * 100) / (n * 1.0))
    avgcat1 += cat1
    avgcat2+=cat2
    print i
    print "\nMjhor: " + str(cat1)
    print "\nMhmos: " + str(cat2)
    print "\n=============\n"
    if i < 16000:
        worksheet.write(row, col, str(i) + " Mjhor",format)
        worksheet.write(row+1, col, cat1,format)

        print cat3

        worksheet.write(row+3, col, str(i) +" Mhmos",format)
        worksheet.write(row + 4, col , cat2,format)
        worksheet.write(row+6, col, cat3,format)
    else:
        worksheet2.write(row, col2, str(i) + " Mjhor")
        worksheet2.write(row+1, col2, cat1)

        print cat3

        worksheet2.write(row+3, col2, str(i) +" Mhmos")
        worksheet2.write(row + 4, col2 , cat2)
        worksheet2.write(row+6, col2, cat3)
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
size = size-1
for k in range(0,size+1):
    worksheet.write(5, k, avgcat1/size,format)
    worksheet.write(8, k, avgcat2/size,format)

workbook.close()
for k in range(0,size+1):
    worksheet2.write(5, k, avgcat1/size)
    worksheet2.write(8, k, avgcat2/size)

workbook2.close()