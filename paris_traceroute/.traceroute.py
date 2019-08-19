import csv
import os
import glob
import time
import subprocess

#traverse through the files in the directory
# using the glob.glob() function from the glob module, which allows you to filter files using a pattern
for filepath in glob.glob(os.path.join('/home/Marting/Videos/work/websites','*.txt')):
    # print (filepath)
    with open(filepath) as infile, open('/home/Marting/Videos/work/traceroute.txt', 'a') as outfile:
        copy = False
        for line in infile:
            if line.startswith("traceroute"):
                copy = True
                outfile.write(line)
            elif line.endswith("traceroute"):
                copy = False
            elif copy:
                outfile.write(line)
    with open('/home/Marting/Videos/work/traceroute.txt') as outfilez:
            # Read the file
        new_text = outfilez.readlines()

        # Create a list to keep all the words in file
        words = []
        line_break = 0

        # Add all the words in file to list
        for x in range(0, len(new_text)):
            for word in new_text[x].split(' ',1)[0]:
                words.append(word + ',')


# Write words into csv file
	
with open('/home/Marting/Videos/work/traceroute.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split("  ") for line in stripped if line)
    
    with open('/home/Marting/Videos/work/traceroute.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerows(lines)

# Add a new column to the csv file, it includes the converted ip address to country
# use Pandas to manipulate the csv file
# read the csv file
# def read_csv(csv_file):
#     df = pd.read_csv(csv_file)
#     return df

# def 

#carry out the paris traceroute
#open the traceroute.csv file which contains the websites to carry out the traceroutes
with open('/home/Marting/Videos/work/traceroute.csv', newline='') as csvfile:
	#open the file with the time stamp to store the traceroutes 
	output = open('./tracerouteOutput_'+ time.ctime(time.time())+'.txt', 'w')
	data = list(csv.reader(csvfile))
	#perform the paris traceroute on each entry in the csv file
	for row in data:
		subprocess.Popen('paris-traceroute %s' %row[0],stdout=output,shell=True)


