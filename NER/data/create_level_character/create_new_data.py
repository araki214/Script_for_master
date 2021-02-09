# -*- encoding: utf-8 =*-
import re
import sys
sentences = []
labels = []
labels_in_sentences = [] 
File_raw = sys.argv[1]
File_label = sys.argv[2] 
with open(File_raw, "r", encoding="utf-8") as f, open(File_label, "r", encoding="utf-8") as g:
	for line in f:
		if line != "\n":
			line = re.sub("\n","",line)
			line = line.split(" ")
			sentences.append(line)
	for line in g:
		if line != "\n":
			line = re.sub("\n","",line)
			line = line.split(" ")
			word_label = [line[0],line[3]]
			labels.append(word_label)
		else:
			labels_in_sentences.append(labels)
			labels = []
print(sentences)
print(labels_in_sentences)

sentence_anotation = []
sentences_anotation = []
number = 0
for sentence, labels in zip(sentences, labels_in_sentences):
	for i, word in enumerate(sentence):
		if labels[number][0] in word:
			sentence_anotation.append([word,labels[number][1]])
			number += len(word)
		else:
			print("No")
		if i == len(sentence)-1:
			sentences_anotation.append(sentence_anotation)
			sentence_anotation = []
			number = 0
print(sentences)
print(labels_in_sentences)
print(sentences_anotation)
File_result = sys.argv[3]
with open(File_result,"a",encoding="utf-8") as h:
	for sentence in sentences_anotation:
		for word_label in sentence:
			result = word_label[0] + " a a " + word_label[1] + "\n"
			#print(result)
			h.write(result)
		h.write("\n")


	
			
			
