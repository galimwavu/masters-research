import csv
import time

search_string = "20294"

#open a file for writing the results
outputfile = open('rv_27_ug','w')

#with open('routeviews-rv2-20180124-1600.csv', 'rb') as f, open('file2.csv', 'wb') as g:
with open('routeviews-rv2-20180227-1200.csv', 'rb') as f:
    reader = csv.reader(f)
    
    for row in reader:
        if row[2] == search_string:
            out = row[0] + ' '+row[1]+' '+row[2]+ '\n'
            outputfile.write(out) 
        elif row[2]  == "21491":
            out2 = row[0] + ' '+row[1]+' '+row[2] +'\n'
            outputfile.write(out2)
        elif row[2]  == "29032":
            out3 = row[0] + ' '+row[1]+' '+row[2] +'\n'
            outputfile.write(out3)
        elif row[2]  == "29039":
            out4 = row[0] + ' '+row[1]+' '+row[2] +'\n'
            outputfile.write(out4)
        elif row[2]  == "36991":
            out5 = row[0] + ' '+row[1]+' '+row[2] +'\n'
            outputfile.write(out5)
        elif row[2]  == "36997":
            out6 = row[0] + ' '+row[1]+' '+row[2] +'\n'
            outputfile.write(out6)
        elif row[2]  == "37063":
            out7 = row[0] + ' '+row[1]+' '+row[2] +'\n'
            outputfile.write(out7)
        elif row[2]  == "37075":
            out8 = row[0] + ' '+row[1]+' '+row[2] +'\n'
            outputfile.write(out8)
        elif row[2]  == "37113":
            out9 = row[0] + ' '+row[1]+' '+row[2] +'\n'
            outputfile.write(out9)
        elif row[2]  == "37122":
            out10 = row[0] + ' '+row[1]+' '+row[2] +'\n'
            outputfile.write(out10)
        elif row[2]  == "37273":
            out11 = row[0] + ' '+row[1]+' '+row[2] +'\n'
            outputfile.write(out11)
        elif row[2]  == "37610":
            out12 = row[0] + ' '+row[1]+' '+row[2] +'\n'
            outputfile.write(out12)
        elif row[2]  == "37679":
            out13 = row[0] + ' '+row[1]+' '+row[2] +'\n'
            outputfile.write(out13)
        elif row[2]  == "64520":
            out14 = row[0] + ' '+row[1]+' '+row[2] +'\n'
            outputfile.write(out14)
        elif row[2]  == "327687":
            out15 = row[0] + ' '+row[1]+' '+row[2] +'\n'
            outputfile.write(out15)
        elif row[2]  == "327724":
            out16 = row[0] + ' '+row[1]+' '+row[2] +'\n'
            outputfile.write(out16)
        elif row[2]  == "328015":
            out17 = row[0] + ' '+row[1]+' '+row[2] +'\n'
            outputfile.write(out17)
