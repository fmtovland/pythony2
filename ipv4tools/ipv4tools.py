def onnet(*address,mask):
	'''check if an ipv4 address is on a network
	a b c and d are the octets of the ipv4 address
	mask is the subnet mask as a number between 0 and 32'''

	netmask=(2**32) - (2**(32-mask))
	masklist=[]

	for i in range(0,4):
		masklist.insert(0,netmask%256)
		netmask=int(netmask/256)


	addresslist=[]
	for i in range(0,4):
		addresslist.append(address[i] & masklist[i])

	return addresslist
