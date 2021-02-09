import re
import cnvk
jisx0208 = []
with open("unicode.txt", "r", encoding="utf-8_sig") as f:
	for line in f:
		line = line.strip()
		jisx0208.append(line)
jisx0208.append('\n')
jisx0208.append(" ")
Jisx0208 = set(jisx0208)
"""
with open("Wikitexttrueb.full","r") as f, open("Wikitexttruea.full","a") as g:
	for line in f:
		#line = cnvk.convert(line,cnvk.Z_ASCII,cnvk.Z_KATA)
		line=re.sub('[0-9０-９]+','*',line)
		#line=re.sub("\*[\*]+","*",line)
		g.write(line)
"""
with open("Random_Contentsadjusttrueb.full","r") as f, open("Random_Contentsadjusttrueaver2.full","a") as g:
	for line in f:
		line = cnvk.convert(line,cnvk.Z_ASCII,cnvk.Z_KATA)
		line=re.sub('[0-9０-９]+','*',line)
		#line=re.sub("\*[\*]+","*",line)
		g.write(line)
