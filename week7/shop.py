#Program requirements: simulate a shopping cart
#Author: Liam Mc Cormick
#date: 8/11/17
#OS: Gentoo
#Kernel: 4.13.11
#python version: 3.4.5

#define type variables
productlist="productlist.txt"	#the filename of the stockfile

def getstock():
	'''import the stock list'''

	stockfile=open(productlist.txt,"r")

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

	stockfile.close()
	return mydict

def savestock(mydict):
	'''takes a list of remaining stock and saves it to file'''

	stockfile=open(productlist,"w+")
	for id in mydict:
		string="id: "+id+"\n"
		stockfile.write(string)

		string="name: "+mydict[id]["name"]+"\n"
		stockfile.write(string)

		string="stock:"+mydict[id]["stock"]+"\n"
		stockfile.write(string)

		string="price:"+str(mydict[id]["price"])+"\n"
		stockfile.write(string)

		stockfile.write("\n")

	stockfile.close()

def main():
	'''main block'''
	availableItems=getstock()	#get a list of all available items



if __name__ == "__main__":
	main()
