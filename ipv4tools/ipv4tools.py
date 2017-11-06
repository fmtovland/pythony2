def mask2list(mask):
	'''convert a network mask between 1 and 32 to a list in
	the form 255.255.0.0'''

	netmask=(2**32) - (2**(32-mask))
	masklist=[]

	for i in range(0,4):
		masklist.insert(0,netmask%256)
		netmask=int(netmask/256)

	return masklist


def onnet(*address,mask):
	'''check if an ipv4 address is on a network
	a b c and d are the octets of the ipv4 address
	mask is the subnet mask as a number between 0 and 32'''

	masklist=mask2list(mask)

	addresslist=[]
	for i in range(0,4):
		addresslist.append(address[i] & masklist[i])

	return addresslist
