import re
import sys
def analysis2(text,result,name):
	num_sen = 0
	Dict=dict()
	num_word=0
	num_cha=0
	num_cha_sen=0
	with open(text, "r", encoding="utf-8_sig") as f:
		for line in f:
			line2=line
			line=re.sub('\n','',line)
			line=line.split(' ')
			line=[i.strip() for i in line]
			line=[i for i in line if i]
			num_word+=len(line)
			for i in line:
				num_cha+=len(i) 
			for k in line:
				Dict[k]=Dict.get(k,0)+1
			#line2="".join(line)
			num_sen += line2.count('。')
			line2=re.sub('！！！','！',line2) 
			line2=re.sub('！！','！',line2)
			line2=re.sub(" ","",line2) 
			line2=re.sub("\n","",line2)
			num_sen += line2.count('！')
			num_sen += line2.count('？')
			num_sen += line2.count('♪')
			line3="".join(line2)
			#print(line3)
			sentences = re.split('[。！？♪]',line3)
			#print(sentences)
			for sen in sentences:
				num_cha_sen+=len(sen)
				num_cha_sen+=1
	#num_kind_word=len(Dict)
	ave_sen_lengh = num_cha_sen/num_sen
	num_sen = str(num_sen)
	num_cha_sen = str(num_cha_sen)
	with open(result, "a", encoding="utf-8_sig") as g:
		g.write(name+'\n')
		g.write('文の数='+str(num_sen)+'\n')
		#g.write('単語数='+str(num_word)+'\n')
		g.write('文字数='+str(num_cha)+'\n')
		g.write('文字数2='+str(num_cha_sen)+'\n')
		g.write("平均文長="+str(ave_sen_lengh)+"\n")
		#g.write('語彙数='+str(num_kind_word)+'\n\n')


analysis2(sys.argv[1],sys.argv[2],sys.argv[3])
