import re
def statistic(file1,file2,name):
	number=0
	Dict={}
	with open(file1,"r") as f:
		for line in f:
			if "a a"in line:
				number+=1
				line=re.sub("[^a]+a a ","",line)
				if re.search("[B,I]+-",line):
					line=re.sub("[B,I]+-","",line)
				print(line)
				Dict[line]=Dict.get(line,0)+1
	with open(file2,"a") as g:
		g.write(name+"\n")
		g.write("tokens="+str(number)+"\n")
		g.write("tags="+str(len(Dict))+"\n")
		for key,value in Dict.items():
			g.write(f"{key} {value}\n")
		g.write("\n\n")

statistic("train.txt","statNER-R.txt","train")
statistic("dev.txt","statNER-R.txt","dev") 
statistic("test.txt","statNER-R.txt","test")					
