count=0
#enwiki-latest-pages-articles.xml
with open("D:\\MSbyResearch\\webMining\\Assignment4\\as4\\wikixmlj-r43\\sample.xml","r") as dataDump:
	for line in dataDump:
		data=[]
		if "<page>" in line:
			count+=1
			while "</page>" not in line:
				data.append(line)
				line=dataDump.next()
			data.append('</page>')
			name="D:\\MSbyResearch\\webMining\\Assignment4\\as4\\wikixmlj-r43\\Pages\\page"+str(count)+".xml"
			f=open(name,"w")
			f.write("".join(data))
			f.close()
dataDump.close()
print count
