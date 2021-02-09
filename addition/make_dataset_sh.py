# -*- encoding: utf-8 -*-
import re
import random
import sys

text_shogi = sys.argv[1]
text_recipe = sys.argv[2]
maximum = 0
count_cha = 0
with open(text_shogi, "r") as f:
	for line in f:
		line = line.strip()
		line = re.sub("\n","",line)
		line = line.replace(" ","")
		if line:
			maximum +=len(line)

text_recipe_after = text_recipe+"_same_size_shogi"
with open(text_recipe, "r") as f,open(text_recipe_after, "a") as g:
	for line in f:
		if line =="\n" and count_cha >= maximum:
			g.write(line)
			break
		g.write(line)
		line = line.strip()
		line = re.sub("\n","",line)
		line = line.replace(" ","")
		if line:
			count_cha += len(line)		
print(maximum)
print(count_cha)

