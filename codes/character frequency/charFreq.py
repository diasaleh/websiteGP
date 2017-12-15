# -*- coding: UTF-8 -*-
from __future__ import division
import xlsxwriter
import sys
import collections
row = 3
row2 = 3
col = 1
col2 = 1
j=0
size=int(sys.argv[3])+1
avgcat1=0
avgcat2=0
workbook = xlsxwriter.Workbook(str(sys.argv[4])+'_shell_output/'+str(sys.argv[4])+'RowCharFeq.xlsx')
worksheet = workbook.add_worksheet()
workbook2 = xlsxwriter.Workbook(str(sys.argv[4])+'_shell_output/'+str(sys.argv[4])+'RowCharFeq_2.xlsx')
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
        if not "?@-:*&^%$#@!;\"()‍ ×  ,ـ.-؛_«»[]}{= \\/~`–،؟".__contains__(n) and not n.isdigit() and not n.isalnum():
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
    a1,n=char_frequency(sentence)
    # d_view = [ (v,k) for k,v in d.iteritems() ]
    # d_view.sort(reverse=True)

    # print d
    # print n


    worksheet.write(row, col, str(i) + "",format)
    # a1_sorted_keys = sorted(a1, key=a1.get)
    for r in sorted(a1):
        print r, a1[r]        
        #print "%s : %d" % (k,v)
        sentence = unicode(r, "utf-8")
        if i<16000:
            worksheet.write(row+1, col, sentence,format)
            worksheet.write(row+1, col+1, float((a1[r] * 100) / (n * 1.0)),format)
        else:
            worksheet2.write(row+1, col2, sentence)
            worksheet2.write(row+1, col2+1, float((a1[r] * 100) / (n * 1.0)))
            col2 = col2+2
        row+=1
        
        print i
        print float((a1[r] * 100) / (n * 1.0))
        print "\n=============\n"
   
    col = col+2
    row = 3
    # for k, v in od2.items():
    #
    #     #print "%s : %d" % (k,v)
    #     sentence = unicode(k, "utf-8")
    #
    #     worksheet.write(row, col, sentence)
    #     worksheet.write(row, col + 1, float((v*100)/(n* 1.0)), format)
    #     row+=1


workbook.close()
workbook2.close()