def getstock():
	'''import the stock list'''

	stockfile=open("productlist.txt","r")

	mydict={}

	for line in stockfile.readlines():
		if line[0:2].strip() == "id":
			id=line.strip()[-4:]
			mydict[id]={}
		elif line[0:4].strip() == "name":
			mydict[id]["name"]=line.strip()[6:]
		elif line[0:5].strip() == "stock":
			mydict[id]["stock"]=line.strip()[7:]
		elif line[0:5].strip() == "price":
			mydict[id]["price"]=line.strip()[7:]
			mydict[id]["price"]=float(mydict[id]["price"])

	return mydict
