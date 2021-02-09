#coding: utf-8

import requests
import codecs
import re
import cnvk
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

numberbase=0
with open('Good_Contents.html','r',encoding="utf-8_sig") as f:
	for line in f:
		line=line.strip()
		Len=len(line)
		numberbase+=Len
with open('Featured_Contents.html','r',encoding="utf-8_sig") as g:
	for line in g:
		line=line.strip()
		Len=len(line)
		numberbase+=Len


#漉し取り
def filt(lin,cou):
	jisx0208 = []
	with open("unicode.txt", "r", encoding="utf-8_sig") as f:
		for line in f:
			line = line.strip()
			jisx0208.append(line)
	jisx0208.append('\n')
	jisx0208.append('　')
	jisx0208.append(' ')
	jisx0208.append(' ')
	jisx0208.append('‎')
	Jisx0208 = set(jisx0208)
	h = codecs.open('Exception_R.html', 'a', 'utf-8')
	lin_list = list(lin) 
	for ind,ch in enumerate(lin_list):
		if ch not in Jisx0208:
			if cou==False:
				ch="*"
				lin_list[ind]=ch
			else:
				print(ch)
				txt = "\n".join(ch)
				Count = str(cou)
				h.write(Count+txt+'\n')
				ch = '*'+ Count+'*'
				cou = cou +1
				lin_list[ind]=ch
	lin = ''.join(lin_list)
	h.close()
	return lin,cou

#リスト作成
def list_sampling(x,y):
	entry = x.get_text('\n')
	if entry not in y:
		y.append(entry)

news_url = "https://ja.wikipedia.org/wiki/秀逸な記事"
html = requests.get(news_url)
soup = BeautifulSoup(html.content, "html.parser")
list1 = []
for i in soup.select('small'):
	catalog_sample = i.find_next('a')
	list_sampling(catalog_sample,list1)
	catalog_sample_follower = catalog_sample.find_next_siblings('a')
	for j in catalog_sample_follower:
		list_sampling(j,list1)

news_url = "https://ja.wikipedia.org/wiki/良質な記事"
html = requests.get(news_url)
soup = BeautifulSoup(html.content, "html.parser")
for i in soup.select('small'):
	catalog_sample = i.find_next('a')
	list_sampling(catalog_sample,list1)
	catalog_sample_follower = catalog_sample.find_next_siblings('a')
	for j in catalog_sample_follower:
		list_sampling(j,list1)

#余分な'wl'削除＆テキスト書き込み
list1=[i for i in list1 if i.find( 'wl')==-1]

#テキスト抽出(概要)
def sampling(http,cou,number):
	list2 = []
	html2 = requests.get(http)
	soup2 = BeautifulSoup(html2.content, "html.parser")
	[s.extract() for s in soup2('sup')]
	#[s.replace_with('削除済') for s in soup2(text =re.compile('#'))]
	title_and_trash = soup2.select('[class~=firstHeading]')
	title = title_and_trash[0].get_text()
	title = cnvk.convert(title,cnvk.Z_ASCII,cnvk.Z_KATA,{u"⋯":u"…"},{u"–":u"―"},{u"—":u"―"},{u"－":u"‐"},{u"－":u"‐"},{u"～":u"〜"},{u"·":u"・"},{u"⋅":u"・"},{u" ":u"　"},{u"›":u"〉"},{u"‹":u"〈"},{u"»":u"》"},{u"«":u"《"},{u"≥":u"≧"},{u"≤":u"≦"},{u"µ":u"μ"},{u"〝":u"“"},{u"〟":u"”"},{u"⁄":u"／"},{u"=":u"＝"})
	title,cou2 = filt(title,cou)
	starting_point = soup2.select('[class~=toclimit-3],[class~=toc]')
	if len(starting_point)==0:
		return cou,False
	fo = codecs.open('Random_Contents'+ '.txt', 'a', 'utf-8')
	fo2 = codecs.open('Random_Lists'+ '.txt', 'a', 'utf-8')
	print(title)
	ti='\n='+title+'=\n'
	line2=ti.strip()
	Len=len(line2)
	number+=Len
	fo.write(ti)			
	fo2.write(ti)			
	fo.close()	
	fo2.close()
	followers = starting_point[0].find_previous_siblings('p')
	for k in followers:
		follower = k.get_text()
		list2.append(follower)	
		list2.reverse()
	for line in list2:
		line = cnvk.convert(line,cnvk.ZAC,cnvk.ZK,{u"⋯":u"…"},{u"–":u"―"},{u"—":u"―"},{u"－":u"‐"},{u"－":u"‐"},{u"～":u"〜"},{u"·":u"・"},{u"⋅":u"・"},{u" ":u"　"},{u"›":u"〉"},{u"‹":u"〈"},{u"»":u"》"},{u"«":u"《"},{u"≥":u"≧"},{u"≤":u"≦"},{u"µ":u"μ"},{u"〝":u"“"},{u"〟":u"”"},{u"⁄":u"／"},{u"=":u"＝"})
		line,cou2 = filt(line,cou2)
		line2=line.strip()
		Len=len(line2)
		number+=Len
		fo = codecs.open('Random_Contents'+ '.txt', 'a', 'utf-8')
		fo.write(line)				
		fo.close()
	return cou2,html2
		
#テキスト抽出(詳細)
def sampling_detail(http,cou,number):
	List = []
	soup2 = BeautifulSoup(http.content, "html.parser")
	[s.extract() for s in soup2('sup')]
	[s.extract() for s in soup2('annotation')]
	[s.extract() for s in soup2('.mw-editsection')]
	[s.extract() for s in soup2.select('.gallerybox')]
	[s.extract() for s in soup2.select('.mbox-text')]
	[s.extract() for s in soup2.select('.geo-multi-punct')]
	[s.extract() for s in soup2.select('.geo-nondefault')]	
	[s.extract() for s in soup2.select('.geo-default')]
	[s.extract() for s in soup2.select('.plainlist')]	
	block = soup2.select('h2 > span[class~=mw-headline]')
	for i in block:
		over = i.prettify()
		if over.find('id="出典"')>-1 or over.find('id="注釈"')>-1 or over.find('id="脚注"')>-1 or over.find('id="註釈"')>-1 or over.find('id="外部リンク"')>-1:
			break
		item1 = i.get_text()
		item1 = cnvk.convert(item1,cnvk.ZAC,cnvk.ZK,{u"⋯":u"…"},{u"–":u"―"},{u"—":u"―"},{u"－":u"‐"},{u"－":u"‐"},{u"～":u"〜"},{u"·":u"・"},{u"⋅":u"・"},{u" ":u"　"},{u"›":u"〉"},{u"‹":u"〈"},{u"»":u"》"},{u"«":u"《"},{u"≥":u"≧"},{u"≤":u"≦"},{u"µ":u"μ"},{u"〝":u"“"},{u"〟":u"”"},{u"⁄":u"／"},{u"=":u"＝"})
		item1,cou = filt(item1,cou)
		if item1.find('注釈')>-1 or item1.find('脚注')>-1 or item1.find('註釈')>-1:
			break
		List.append('\n=='+item1+'==\n')
		texts = i.find_all_next(['h2','h3','h4','p','li','dd','dt','blockquote'])
		overlap = []
		temp2_prev = texts[0].prettify()
		temp2_tx_prev=''
		for j in texts:
			temp2 = j.prettify()
			if temp2.find('h2')>-1:
				break 
			elif temp2.find('h3')>-1 and temp2.find('mw-headline')>-1:
				heading2 = j.select('.mw-headline')
				item2 = heading2[0].get_text()
				item2 = cnvk.convert(item2,cnvk.ZAC,cnvk.ZK,{u"⋯":u"…"},{u"–":u"―"},{u"—":u"―"},{u"－":u"‐"},{u"－":u"‐"},{u"～":u"〜"},{u"·":u"・"},{u"⋅":u"・"},{u" ":u"　"},{u"›":u"〉"},{u"‹":u"〈"},{u"»":u"》"},{u"«":u"《"},{u"≥":u"≧"},{u"≤":u"≦"},{u"µ":u"μ"},{u"〝":u"“"},{u"〟":u"”"},{u"⁄":u"／"},{u"=":u"＝"})
				item2,cou = filt(item2,cou)
				if item2 not in overlap:
					List.append('\n==='+item2+'===\n')
					overlap.append(item2)
				temp2_prev=temp2
			elif temp2.find('h4')>-1 and temp2.find('mw-headline')>-1:
				heading3 = j.select('.mw-headline')
				item3 = heading3[0].get_text()
				item3 = cnvk.convert(item3,cnvk.ZAC,cnvk.ZK,{u"⋯":u"…"},{u"–":u"―"},{u"—":u"―"},{u"－":u"‐"},{u"－":u"‐"},{u"～":u"〜"},{u"·":u"・"},{u"⋅":u"・"},{u" ":u"　"},{u"›":u"〉"},{u"‹":u"〈"},{u"»":u"》"},{u"«":u"《"},{u"≥":u"≧"},{u"≤":u"≦"},{u"µ":u"μ"},{u"〝":u"“"},{u"〟":u"”"},{u"⁄":u"／"},{u"=":u"＝"})
				item3,cou = filt(item3,cou)
				if temp2_prev.find('h3')==-1 and item3 not in overlap:
					List.append('\n==='+item3+'===\n')
					overlap.append(item3)
				if temp2_prev.find('h3')>-1 and item3 not in overlap:
					List.append('\n===='+item3+'====\n')
					overlap.append(item3)
				temp2_prev=temp2
			elif temp2.find('blockquote')>-1:
				text0 = j.get_text()
				text0 = cnvk.convert(text0,cnvk.ZAC,cnvk.ZK,{u"⋯":u"…"},{u"–":u"―"},{u"—":u"―"},{u"－":u"‐"},{u"－":u"‐"},{u"～":u"〜"},{u"·":u"・"},{u"⋅":u"・"},{u" ":u"　"},{u"›":u"〉"},{u"‹":u"〈"},{u"»":u"》"},{u"«":u"《"},{u"≥":u"≧"},{u"≤":u"≦"},{u"µ":u"μ"},{u"〝":u"“"},{u"〟":u"”"},{u"⁄":u"／"},{u"=":u"＝"})
				text0,cou=filt(text0,cou)
				if text0 not in overlap:
					List.append('<block>'+text0+'<block>\n')
					overlap.append(text0)
				temp2_tx_prev=text0
				temp2_prev=temp2
			elif temp2.find('<dt>')>-1:
				item4 = j.get_text()
				item4 = cnvk.convert(item4,cnvk.ZAC,cnvk.ZK,{u"⋯":u"…"},{u"–":u"―"},{u"—":u"―"},{u"－":u"‐"},{u"－":u"‐"},{u"～":u"〜"},{u"·":u"・"},{u"⋅":u"・"},{u" ":u"　"},{u"›":u"〉"},{u"‹":u"〈"},{u"»":u"》"},{u"«":u"《"},{u"≥":u"≧"},{u"≤":u"≦"},{u"µ":u"μ"},{u"〝":u"“"},{u"〟":u"”"},{u"⁄":u"／"},{u"=":u"＝"})
				item4,cou = filt(item4,cou)
				if temp2_tx_prev.find(item4)==-1:
					if temp2_prev.find('h3')==-1 and item4 not in overlap:
						List.append('\n==='+item4+'===\n')
						overlap.append(item4)
					if temp2_prev.find('h3')>-1 and item4 not in overlap:
						List.append('\n===='+item4+'====\n')
						overlap.append(item4)
					temp2_prev=temp2
			elif temp2.find('<p>')>-1 or temp2.find('<li>')>-1 or temp2.find('<dd>')>-1:
				if temp2.find('mwe-math-element')==-1:
					text = j.get_text()
					text = cnvk.convert(text,cnvk.ZAC,cnvk.ZK,{u"⋯":u"…"},{u"–":u"―"},{u"—":u"―"},{u"－":u"‐"},{u"－":u"‐"},{u"～":u"〜"},{u"·":u"・"},{u"⋅":u"・"},{u" ":u"　"},{u"›":u"〉"},{u"‹":u"〈"},{u"»":u"》"},{u"«":u"《"},{u"≥":u"≧"},{u"≤":u"≦"},{u"µ":u"μ"},{u"〝":u"“"},{u"〟":u"”"},{u"⁄":u"／"},{u"=":u"＝"})
					text,cou=filt(text,cou)
					if temp2_tx_prev.find(text)==-1:
						if text not in overlap:
							List.append(text)
							overlap.append(text)
				elif temp2.find('mwe-math-element')>-1:			
					text = '<math-element>\n'
					if temp2_tx_prev.find(text)==-1:
						List.append(text)
				temp2_prev=temp2
	fo = codecs.open('Random_Contents'+ '.txt', 'a', 'utf-8')
	for line in List:
		print(line)
		line2=line.strip()
		Len=len(line2)
		number+=Len
		fo.write(line)				
	fo.write('\n')
	fo.close()	
	return cou

def TITLEs(url,cou):
	html2 = requests.get(url)
	soup2 = BeautifulSoup(html2.content, "html.parser")
	[s.extract() for s in soup2('sup')]
	title_and_trash = soup2.select('[class~=firstHeading]')
	title = title_and_trash[0].get_text()
	title = cnvk.convert(title,cnvk.Z_ASCII,cnvk.Z_KATA,{u"⋯":u"…"},{u"–":u"―"},{u"—":u"―"},{u"－":u"‐"},{u"－":u"‐"},{u"～":u"〜"},{u"·":u"・"},{u"⋅":u"・"},{u" ":u"　"},{u"›":u"〉"},{u"‹":u"〈"},{u"»":u"》"},{u"«":u"《"},{u"≥":u"≧"},{u"≤":u"≦"},{u"µ":u"μ"},{u"〝":u"“"},{u"〟":u"”"},{u"⁄":u"／"},{u"=":u"＝"})
	title,_ = filt(title,cou)
	return title

number=0
with open("Random_Contents.txt","r",encoding="utf-8_sig") as f:
	for line in f:
		line=line.strip()
		Len=len(line)
		number+=Len
http = list1
count= 1
for i in range(10000):
	url="http://ja.wikipedia.org/wiki/%E7%89%B9%E5%88%A5:Random"
	TITLE=TITLEs(url,False)
	while TITLE in http:
		url="http://ja.wikipedia.org/wiki/%E7%89%B9%E5%88%A5:Random"
		TITLE=TITLEs(url,False)
	print(url)
	count,html2=sampling(url,count,number)
	while html2==False:
		url="http://ja.wikipedia.org/wiki/%E7%89%B9%E5%88%A5:Random"
		count,html2=sampling(url,count,number)
		if html2!=False:
			TITLE=TITLEs(url,False)
			if TITLE in http:
				html2=False
	count=sampling_detail(html2,count,number)
	http.append(TITLE)
	if number>numberbase:
		break
