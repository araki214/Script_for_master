# -*- enconding: utf-8 ^*^
import sys
File = sys.argv[1]
File_result = sys.argv[2]
sentence=[]

with open(File,"r",encoding="utf-8") as f, open(File_result,"a",encoding="utf-8") as g:
	for line in f:
		lin = line.split(" ")
		word = lin[0]
		sentence.append(word)
		#print(sentence)
		if word == "\n":
			line = " ".join(sentence)
			line += "\n"
			g.write(line)
			sentence = [] 
			#print(line)
 
