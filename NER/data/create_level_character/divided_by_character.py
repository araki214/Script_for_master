# -*- enconding: utf-8 ^*^

import sys
File = sys.argv[1]
File_result = sys.argv[2]

with open(File,"r",encoding="utf-8") as f, open(File_result,"a",encoding="utf-8") as g:
	for line in f:
		lin = line.split(" ")
		word = lin[0]
		print(word)
		if len(word) <=1:
			g.write(line)
			print(line)
		elif len(word) > 1:
			words = list(word)
			for i,cha in enumerate(words):
				if i != 0 and "B-" in lin[3]:
					label = lin[3]
					label = label[2:]
					label = "I-" + label
					print(label)
					line = cha + " "+ lin[1]+" "+lin[2]+" "+label
				else:	
					line = cha + " "+ lin[1]+" "+lin[2]+" "+lin[3]
				g.write(line)
				print(line)
 
