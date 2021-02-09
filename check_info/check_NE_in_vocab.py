# -*- encoding:utf-8 -*-

import sys
import re

Input_NE = sys.argv[1]
Input_vocab = sys.argv[2]
Dict_NER = {}
Vocab = []
count_tag = 0
count_NE = 0
with open(Input_NE, "r", encoding="utf-8") as f:
	for line in f:
		if line != "\n":
			lin = line.split(" ")
			word = lin[0]
			tag = lin[3]
			tag = re.sub("\n","",tag)
			count_tag += 1
			if tag != "O":
				count_NE += 1
				Dict_NER[word] = Dict_NER.get(word, 0)+1
				#print(tag)
				#print(word)
print(Dict_NER)
with open(Input_vocab, "r", encoding="utf-8") as g:
	for i,line in enumerate(g):
		if i > 4:
			line = re.sub("\n","",line)
			Vocab.append(line)
#print(count_tag)
#print(count_NE)
#print(Vocab)

count_Yes = 0
count_No = 0
count_all = 0
for word in Dict_NER.keys():
	count_all += 1
	if word in Vocab:
		#print("Yes")
		count_Yes += 1
	else:
		#print("No")
		count_No += 1
TAG = sys.argv[3]

with open("result_NE_in_vocab_shogi.txt","a",encoding="utf-8") as h:
	result = TAG + "\n"
	h.write(result)
	result = "ALL: "+str(count_all)+"\n"
	h.write(result)
	result = "Yes: "+str(count_Yes)+"\n"
	h.write(result)
	result = "No: "+str(count_No)+"\n"
	h.write(result)
