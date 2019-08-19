from geoip import geolite2
import csv
import re


regex = re.compile(".*?\((.*?)\)")
r = re.compile("([\s0-9]+(?:\.[0-9]+)?)(?:\s)")

#file to write to the location and the ip addess
outfile = open('/home/Marting/Videos/work/ex/MTNTCP.txt', 'w')

# return the country where the ip address is found
def getLocation(ipaddress):
    match = geolite2.lookup(ipaddress)
    if(match is not None):
        #print (match.country)
        ip_loc = str(match.country)
        return ip_loc
        # outfile.write(ip_loc)

#validate the ip adress
def validate_ip(ipaddress):
    a = ipaddress.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True

#reading the csv file, return the column with the ip addresses
#afterwards parse the ip address to getlocation
#@return ip address
with open('/home/Marting/Videos/work/ex/logMTN.csv') as infile:
    file_csv = csv.reader(infile)
    
    str1 = '('
    str2 = ')'
    
    
    for row in file_csv:
        delay = ""
        location = ""
        destLocation = ""
        sourceIP2 = ""
        # destIP = ""
        if(row):
            ip_address_list = row[1]
            #get the ip address between the braces
            ip_address = ip_address_list[ip_address_list.find(str1)+1 : ip_address_list.find(str2)]

            # validate the ip address
            if(validate_ip(ip_address)):
                location = getLocation(ip_address)

            result = re.findall(regex, row[0])
            if(result):
                # print (result)
                sourceIP2 = result[0]
                sourceIP = re.findall(r'[0-9]+(?:\.[0-9]+){3}', sourceIP2)
                destinationIP = result[1]
                destIP = re.findall(r'[0-9]+(?:\.[0-9]+){3}', destinationIP)
            else:
                sourceIP =" "
                destinationIP = " "
            # print (ip_address)

            for x in range(2,5):
                
                match = re.match(r,row[x])
                if(match):
                    # print (format(match.group(0)))
                    delay += ""+format(match.group(0)) +"," 
                else:
                    # print ("*")
                    delay += "" +","
                # print ("end of row")
            # print (delay +"\n")

            # validate the destination ip
            
            if(destIP):
                destIP2 = destIP[0]
            # else:
            #     destIP2 ="*"
            if(validate_ip(destIP2)):
                destLocation = getLocation(destIP2)
            # else:
            #     destLocation = "*"

            line = str(sourceIP[0]) +","+str(destIP2)+","+str(destLocation)+","+ip_address+","+str(location)+","+ delay+"\n"

            #check if the destination address is not empty and also if belongs to Uganda
            # if(destLocation == 'UG'):
                
            # print (sourceIP[0])
            outfile.write(line)
            

            #     print ("<"+delay+">")
            #get the ip address between the braces
            # ip_address = ip_address_list[ip_address_list.find(str1)+1 : ip_address_list.find(str2)]
            # if validate_ip(ip_address):
            #     getLocation(ip_address)
    infile.close
#outfile.close
#convert_to_csv('/home/Marting/Documents/traceroute analysis/new analysis/AirtelLocation.txt')
