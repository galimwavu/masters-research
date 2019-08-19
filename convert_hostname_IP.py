import csv, os, subprocess, time, socket
with open('/home/Marting/Documents/python programs/masters/data/Uganda_top_sites_edit.csv', newline='') as csvfile:
	output = open('/home/Marting/Videos/work/trial/ipaddress.txt', 'w')
	data = list(csv.reader(csvfile))
	for row in data:
		ipd = str(row[0])
		ip = socket.gethostbyname(ipd)
		print (ip)
