# -*- coding: utf-8 -*-
import re
import regex
import chardet
import string
import collections
import sys
wordsCC=0
i=1
row=3
col=2
digit_list = '٠١٢٣٤٥٦٧٨٩'

regexx = ur'[\u0660-\u0669]+'
subst = u" "
t=""

f=open(str(sys.argv[4])+"/T1.txt","r")
text = f.read()
text = text.decode('utf-8')
text = regex.sub(ur'[\p{Latin}]', u' ', text)
text =re.sub('[A-Za-z0-9]+', ' ', text)
text = re.sub(r'[?|$|.|!]',r' ',text)
text = " ".join(re.findall(ur"[\u0617-\u061A\u064B-\u0652\u0600-\u06FF]+",text))
text = text.replace("،".decode("utf-8"), " ");
text = text.replace("؟".decode("utf-8"), " ");
text = text.replace("ـ".decode("utf-8"), " ");
text = text.replace("؛".decode("utf-8"), " ");
text = text.replace(" ".decode("utf-8"), " ");
text = text.replace("٪".decode("utf-8"), " ");

text = re.sub(regexx, subst, text)

text = re.sub(' +',' ',text)
t+=text
text = text.encode('utf-8')
out = open(str(sys.argv[4])+"/TN1.txt","w")
out.write(text)
out.close()
