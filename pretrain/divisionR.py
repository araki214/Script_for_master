number=0
with open("WARA_result.txt","r") as f,open("WARA_result_1.txt","a") as g,open("WARA_result_2.txt","a") as h:
	number_based=12901479
	flag = False
	for line in f:
		if number<=number_based//2:
			g.write(line)
		else:
			if line == "\n":
				if flag == False:
					g.write("\n")
				flag = True
			if flag:
				h.write(line)
			else:
				g.write(line)
		number+=1


