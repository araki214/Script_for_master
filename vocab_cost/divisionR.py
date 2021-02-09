number=0
with open("WikiArecipeAtrue.full","r") as f,open("WARAresult_1.txt","a") as g,open("WARAresult_2.txt","a") as h:
	number_based=12624551
	for line in f:
		if number<=number_based//2:
			g.write(line)
		else:
			h.write(line)
		number+=1


