vocab={}
databefore=input()
dataafter=input()
maximum=int(input())
with open(databefore,'r') as f:
	for line in f:
		line=line.split()
		for i in line:
			vocab[i]=vocab.get(i,0)+1
count=0
with open(dataafter,'w') as g:
	for voc,v in sorted(vocab.items(),key=lambda x:-x[1]):
		if count <maximum:
			g.write(voc+'\n')
			count+=1

