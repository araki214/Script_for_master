# -*- encoding: utf-8 -*-

import sys
import re
Input_1 = sys.argv[1]
Input_2 = sys.argv[2]
word_seg = []
word_NER = []
with open(Input_1,"r",encoding="utf-8") as f:
	for line in f:
		if line != "\n":
			#print(line)
			line = re.sub(" ","",line)
			line = re.sub("\n","",line)
			word_seg.append(line)

with open(Input_2,"r",encoding="utf-8") as g:
	for line in g:
		if line != "\n":
			#print(line)
			line = re.sub(" ","",line)
			line = re.sub("\n","",line)
			word_NER.append(line)

count_Yes = 0
count_No = 0
for sen in word_seg:
	if sen in word_NER:
		#print("Yes")
		count_Yes += 1
	else:
		#print("No")
		print(sen)
		count_No += 1
tag = sys.argv[3]
with open("result_same_NER_pretrain.txt","a",encoding="utf-8") as h:
	result = tag+ "\n"
	h.write(result)
	result = "#All: "+str(len(word_seg))+"\n"
	h.write(result)
	result = "#Yes: "+str(count_Yes)+"\n"
	h.write(result)
	result = "#No: "+str(count_No)+"\n"
	h.write(result)
