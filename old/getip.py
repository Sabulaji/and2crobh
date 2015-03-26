import socket
import fcntl

def get_ip_address(ifname):
	skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	pktString = fcntl.ioctl(skt.fileno(), 0x8915, struct.pack('256s', ifname[:15]))
	ipString  = socket.inet_ntoa(pktString[20:24])
	return ipString


ip = get_ip_address('eth0')
print 'Your ip is : %s' % (ip)