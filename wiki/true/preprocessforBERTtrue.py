import re

jisx0208 = []
with open("unicode.txt", "r", encoding="utf-8_sig") as f:
	for line in f:
		line = line.strip()
		jisx0208.append(line)
jisx0208.append('\n')
Jisx0208 = set(jisx0208)

F='Featured_Contents.html'
G='Good_Contents.html'
R='Random_Contentsadjust.txt'
WB='Wikitexttrueb.txt'
RB='Random_Contentsadjusttrueb.txt'
def preprocess(before,after):
	with open(before,'r') as f,open(after,'a') as g:
		for line in f:
			if re.search(r'=[^=]+=',line) is None:
				line=re.sub(' ','　',line)	
				#line=re.sub('[0-9０-９]+','*',line)
				#line=re.sub("\*[\*]+","*",line)
				line=re.sub('<math-element>','',line)	
				line=re.sub('<block>','',line)
				line=re.sub('[=]+[^=][\S]+[=]+','',line)					
				line=line.split('。')
				line=[i for i in line if i!='']
				count=0
				for i,lin in enumerate(line):
					lin2=lin.strip()
					if lin2 !="":
						line[i]=line[i]+'。\n' 
						if i==len(line)-1:
							line[i]=line[i]+'\n' 
				sentence=''.join(line)
				g.write(sentence)

preprocess(F,WB)
preprocess(G,WB)
preprocess(R,RB)

