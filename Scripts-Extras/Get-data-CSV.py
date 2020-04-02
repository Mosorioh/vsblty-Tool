import csv
import codecs

file = "C:/Users/Mijail/Documents/vsblty-Tool/Scripts-Extras/ListadoSoftware.csv"

""" 
with open('C:/Users/Mijail/Documents/vsblty-Tool/Scripts-Extras/ListadoSoftware.csv', newline='') as File:  
    reader = csv.reader(File)
    for row in reader:
        print(row)




with open(file, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print (', '.join(row))
"""

print (repr(open(file, 'rb').read(200))) # dump 1st 200 bytes of file
data = open(file, 'rb').read()
print (data.find('\x00'))
print (data.count('\x00'))