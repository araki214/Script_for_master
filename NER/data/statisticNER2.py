import re
def statistic(file1,file2,name):
	number_word=0
	number_sen=0
	number_NE=0
	Dict={}
	with open(file1,"r") as f:
		for line in f:
			if line=="\n":
				number_sen+=1
			if "a a"in line:
				number_word+=1
				line=re.sub("[^a]+a a ","",line)
				if re.search("[B]+-",line):
					number_NE+=1
					#line=re.sub("[B,I]+-","",line)
				print(line)
				#Dict[line]=Dict.get(line,0)+1
	with open(file2,"a") as g:
		g.write(name+"\n")
		g.write("#Word="+str(number_word)+"\n")
		g.write("#sen.="+str(number_sen)+"\n")
		g.write("#NE="+str(number_NE)+"\n")   
		g.write("\n\n")

statistic("train.txt","statNER-Recipe.txt","train")
statistic("dev.txt","statNER-Recipe.txt","dev") 
statistic("test.txt","statNER-Recipe.txt","test")					
