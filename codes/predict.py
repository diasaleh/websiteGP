# -*- coding: utf-8 -*-
from __future__ import division
import codecs
import xlrd
import xlsxwriter
from collections import Counter
from collections import defaultdict
import sys
import numpy as np
import pickle
import random


cat1=(sys.argv[1])
wordC=int(sys.argv[2])
# print wordC
fn=12
farasaFeat = [6,18,26,38,42,54]
charOut = [7,10]
mhmj=[4,7]
book1_1 = xlrd.open_workbook(str(cat1)+'_shell_output/'+str(cat1)+'POS.xlsx')
sheet1_1 = book1_1.sheet_by_name('Sheet1')

book1_2 = xlrd.open_workbook(str(cat1)+'_shell_output/'+str(cat1)+'avgWordL.xlsx')
sheet1_2 = book1_2.sheet_by_name('Sheet1')

book1_3 = xlrd.open_workbook(str(cat1)+'_shell_output/'+str(cat1)+'all_charOut.xlsx')
sheet1_3 = book1_3.sheet_by_name('Sheet1')

book1_4 = xlrd.open_workbook(str(cat1)+'_shell_output/'+str(cat1)+'all_Mjhor_Mhmos_details.xlsx')
sheet1_4 = book1_4.sheet_by_name('Sheet1')

book1_5 = xlrd.open_workbook(str(cat1)+'_shell_output/'+str(cat1)+'all_entifakh_details.xlsx')
sheet1_5 = book1_5.sheet_by_name('Sheet1')

# book1_6 = xlrd.open_workbook(str(cat1)+'_shell_output/'+str(cat1)+'PRON_cat.xlsx')
# sheet1_6 = book1_6.sheet_by_name('Sheet1')
size1 = 1
# print size1
featuresCat1 = np.zeros(shape=(fn,size1))
# print featuresCat1
col=2
row=0
i=0
for col in range(1,2):
	# print col
	# print sheet1_2.cell_value(4, col)
	featuresCat1[row][i] = (float(sheet1_2.cell_value(4, col)))
	i+=1
i=0
# print featuresCat1

for row in range(1,len(farasaFeat)+1):
	# print row
	# print farasaFeat[row]
	for col in range(2, 3):
		# print sheet1_1.cell_value(farasaFeat[row], col)
		featuresCat1[row][i] = (float(sheet1_1.cell_value(farasaFeat[row-1], col)))
		i+=1
	i=0
i=0
# print featuresCat1

for row in range(7,9):
	# print row
	# print charOut[row-7]
	for col in range(1, 2):
		# print col
		# print sheet1_3.cell_value(charOut[row-7], col)
		featuresCat1[row][i] = (float(sheet1_3.cell_value(charOut[row-7], col)))
		i+=1
	i=0
i=0
# print featuresCat1

for row in range(9,11):
	# print row
	# print charOut[row-7]
	for col in range(1, 2):
		# print col
		# print sheet1_4.cell_value(mhmj[row-9], col)
		featuresCat1[row][i] = (float(sheet1_4.cell_value(mhmj[row-9], col)))
		i+=1
	i=0
i=0
# print featuresCat1

row = 11
for col in range(1, 2):
	# print col
	# print sheet1_4.cell_value(mhmj[row-9], col)
	featuresCat1[row][i] = (float(sheet1_5.cell_value(4, col)))
	i+=1
row = 12
i=0
# print featuresCat1

# for col in range(1, 2):
# 	# print col
# 	# print sheet1_4.cell_value(mhmj[row-9], col)
# 	featuresCat1[row][i] = (float(sheet1_6.cell_value(3, col)))
# 	i+=1
# print featuresCat1
# from sklearn import svm
# from sklearn.ensemble import GradientBoostingClassifier
# from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
# clf = svm.SVC(probability=True)
if wordC > 1700:
	f = open('NB_100_1000_hindawi_D1500_finalSVM.pickle', 'rb')
	print "predict 1500 2500"
elif wordC > 999:
	f = open('NB_100_1000_hindawi_D1500_finalSVM.pickle', 'rb')
	print "predict 1500"
else:
	f = open('NB_100_1000_hindawi_D500_finalSVM.pickle', 'rb')
	print "predict 500"
clf = pickle.load(f)
f.close()

# print xCat1test

xCat1test=np.dstack((featuresCat1)).reshape(-1,fn)
print xCat1test
# print "hi"
oo = open(cat1+"_P.txt","w")	
print ( clf.predict(xCat1test)[0])
predic =  (clf.predict_proba(xCat1test))
print predic
print predic[0][0]*100
print predic[0][1]*100
print predic[0][2]*100

oo.write(str(clf.predict(xCat1test)[0])+"\n")
oo.write(str(predic[0][0]*100)+"\n")
oo.write(str(predic[0][1]*100)+"\n")
oo.write(str(predic[0][2]*100)+"\n")
oo.close()
# print (clf.predict_proba(xCat1test))





