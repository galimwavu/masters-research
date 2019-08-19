import socket
from cymruwhois import Client

ip = '100.10.1.63'
ip_2 = '102.164.120.10'
ip_3 = '102.80.10.106'
ip_4 = '102.80.101.132'

c= Client()
#instead of puting lookup(ip) in the loop and get weird results, instead use lookupmany(ips) to return the results
for r in c.lookupmany([ip,ip_2,ip_3,ip_4]):
	print r.owner
	

#using cymruwhois to convert ips to asn and country code on the commandline
#cymruwhois /home/Marting/Videos/work/ips.txt -f asn,cc > /home/Marting/Videos/work/cyrmu_output.txt 
