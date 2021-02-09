import sys

vocab={}
databefore=sys.argv[1]
dataafter=sys.argv[2]
maximum=64000
with open(databefore,'r') as f:
	for line in f:
		line=line.split()
		for i in line:
			vocab[i]=vocab.get(i,0)+1
count=0
with open(dataafter,'w') as g:
	g.write("[PAD]\n")
	g.write("[UNK]\n")
	g.write("[CLS]\n")
	g.write("[SEP]\n")
	g.write("[MASK]\n")
	for voc,v in sorted(vocab.items(),key=lambda x:-x[1]):
		if count <maximum:
			g.write(voc+'\n')
			count+=1
