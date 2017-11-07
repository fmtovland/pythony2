def mask2list(mask):
	'''convert a network mask between 1 and 32 to a list in
	the form 255.255.0.0'''

	netmask=(2**32) - (2**(32-mask))
	masklist=[]

	for i in range(0,4):
		masklist.insert(0,netmask%256)
		netmask=int(netmask/256)

	return masklist

def list2mask(*masklist):
	'''convert a masklist back to a number between 1 and 32'''
	from math import log2
	mask=32

	for i in range(0,4):
		mask=mask-log2(256-masklist[i])

	return int(mask)

def onnet(*address,mask):
	'''check if an ipv4 address is on a network
	*address is the octets of the ipv4 address
	mask is the subnet mask as a number between 0 and 32'''

	masklist=mask2list(mask)

	addresslist=[]
	for i in range(0,4):
		addresslist.append(address[i] & masklist[i])

	return addresslist

#def broadcast(*address,mask):
#	'''generate a broadcast from any address on a network'''
#
#	masklist=mask2list(mask)
#
#	i=0
#	addresslist=[]
#	while(masklist[i]==255 and i<=3):
#		addresslist.insert(i,address[i])
#		i=i+1
#
#
#	while i<=3:
#		addresslist.insert(i,address[i] & masklist[i])
#		addresslist[i]=addresslist[i] + ((masklist[i]-1)%256)
#		while addresslist[i]>255:
#			addresslist[i-1]=addresslist[i-1]+1
#			addresslist[i]=addresslist[i]-256
#		i=i+1
#
#
#	return addresslist

def netaddr(*address,mask):
	'''find the network address of a given ip address'''

	masklist=mask2list(mask)
	addresslist=[]
	for i in range(0,4):
		addresslist.append(address[i] & masklist[i])

	return addresslist
