# -*- coding: UTF-8 -*-
from __future__ import division
import xlrd
import xlsxwriter
from collections import Counter
from collections import defaultdict
import sys
size=int(sys.argv[3])+1
# book = xlrd.open_workbook('/Users/diasaleh/Desktop/GP/neg.xlsx')
# sheet = book.sheet_by_name('Sheet1')
workbook = xlsxwriter.Workbook((sys.argv[4])+'_shell_output/'+(sys.argv[4])+'NegCat_New.xlsx')
worksheet = workbook.add_worksheet()
workbook2 = xlsxwriter.Workbook((sys.argv[4])+'_shell_output/'+(sys.argv[4])+'NegCat_New_2.xlsx')
worksheet2 = workbook2.add_worksheet()
o=open((sys.argv[4])+'_shell_output/'+(sys.argv[4])+'NegCat_New.txt',"w")
format = workbook.add_format()
format.set_bold()
format.set_font_color('white')
format.set_bg_color('green')
format.set_font_size(16)
neg = defaultdict(list)
avgNegCount = [0] * 3
col=1
col2=1
roww=1
j=0
negCounti=0
cat=[0]*3
negCount=[0]*3
# for i in range(0,sheet.ncols):
#     for row in range(0, sheet.nrows):
#         if sheet.cell_value(row, i) != "":
#             neg[i].append(sheet.cell_value(row, i))
#             j+=1
#     j=0
neg[0].append("حاشا")    
neg[0].append("خلا") 
neg[1].append("غير")       
neg[1].append("سوى")       
neg[1].append("سواء")       
neg[1].append("سوا")       
neg[1].append("سواي")       
neg[2].append("إلا")    
# print neg
# print "\n ==============="
nsuff={}
for i in range(1,size):
    with open((sys.argv[4])+'_shell_output/Farasa_details/Farasa_POS_Type_2_'+str(i)+'.txt', "r") as f:
        for line in f:
            x = line.split("&")
            if x[0] in nsuff:
                nsuff[x[0]]+=1
            else:
                nsuff[x[0]]=1   

    # print neg[0][0]
    print "i="+str(i)
    # print '\n'    
    for j in range(0,3):
        for p in range(0,len(neg[j])):
                # print neg[j][p]
                # print x[k]
                if neg[j][p] in nsuff:
                    # print "j="+str(j)
                    # print nsuff[neg[j][p]]
                    negCount[j]+=nsuff[neg[j][p]]
                else:
                    nsuff[neg[j][p]] = 0 
            # print nsuff
            # print x[k]
            # print "111"

    # cat[0] += nsuff["غير"]
    # cat[0] += nsuff["خلا"]
    # cat[1] += nsuff["سواء"]
    # cat[1] += nsuff["سوى"]
    # cat[1] += nsuff["غير"]
    # cat[2] += nsuff["إلا"]
    # print cat        
    # negCount[j]+=nsuff["غير"]
    for j in range(0,len(negCount)):
        negCounti +=(negCount[j]) 
    for j in range(0,len(negCount)):
        if negCounti !=0:
            avgNegCount[j]+=(100*negCount[j]/negCounti)
    if i < 16000:
        for j in range(0,3):
            worksheet.write(roww, col, str(i) +"  "+neg[j][0].decode("UTF-8") , format)
            worksheet.write(roww+1, col, negCount[j], format)
            if (negCounti) !=0:
                worksheet.write(roww + 2, col, 100*negCount[j]/negCounti, format)
            else:
                worksheet.write(roww + 2, col, "zero", format)
            roww +=4
    else:
        for j in range(0,3):
            worksheet2.write(roww, col2, str(i) +"  "+neg[j][0].decode("UTF-8") )
            worksheet2.write(roww+1, col2, negCount[j])
            if (negCounti) !=0:
                worksheet2.write(roww + 2, col2, 100*negCount[j]/negCounti)
            else:
                worksheet2.write(roww + 2, col2, "zero")
            roww +=4   
        col2+=1         
    o.write(str(i))
    # print negCount
    # print "\n ==============="
    negCount=[]
    negCount = [0] * 3
    negCounti=0
    roww = 1
    col +=1
    nsuff={}
roww = 4
for j in range(0, 3):
    for b in range(1,size):
        if sum(avgNegCount) !=0:
            worksheet.write(roww, b, avgNegCount[j]/(size-1), format)
        else:
            worksheet.write(roww,  b, "zero", format)
    roww += 4
roww = 4
for j in range(0, 3):
    for b in range(1,size):
        if sum(avgNegCount) !=0:
            worksheet2.write(roww, b, avgNegCount[j]/(size-1))
        else:
            worksheet2.write(roww,  b, "zero")
    roww += 4    
workbook.close()
workbook2.close()
o.close()
