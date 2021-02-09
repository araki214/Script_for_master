# -*- coding: utf-8 -*-

import sys
import re
target_file = sys.argv[1]
vocab_file = sys.argv[2]
all_words = []
vocab = []
with open(target_file,"r",encoding="utf-8") as f:
	for line in f:
		line = re.sub("\n","",line)
		#line = line.split(" ")
		all_words.append(line)

all_words = set(all_words)
with open(vocab_file,"r",encoding="utf-8") as g:
	for line in g:
		line = re.sub("\n","",line)
		vocab.append(line)
vocab = set(vocab)
intersection = all_words & vocab
difference = vocab - all_words
print(difference)
not_coverage = len(difference)/len(vocab)
print(not_coverage)
match = vocab - difference
coverage = len(match)/len(vocab)
tag = sys.argv[3]

with open("result_coverage.txt","a",encoding="utf-8") as h:
	result = tag +": "+str(coverage)+"\n"
	h.write(result)



