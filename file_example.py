#with open('sample.txt', 'r') as f: # this line opens the file sample.txt in read mode
#   for line in f: # for loop to print out each line
#           print(line) # prints out each line as the loop iterates over

#with open('sample.txt', 'r') as f:
#    for line in f:
#        print(line.strip()) #Prints out each line without a newline after each line 

#with open('sample.txt', 'r') as f:
#    i=1
#    for line in (f):
#        print(str(i)+":"+line.strip())
#        i=i+1

#with open('output.txt', 'w') as f: # opens the file in write mode!!!!!!
#    f.write("BOOYAHHHH!!!!.\n") #\n is for newline
#    f.write("It has two lines.\n")

#with open ('output.txt','r') as r:
#    with open ('sample.txt','w') as w:
#     for i in r:
#        w.write(i)

#import re

#pattern = r"at" # the pattern to search for
#text = "The cat sat on the mat." #

#matches = re.findall(pattern, text)# this outputs a LIST of all the matches
#print(matches)


#import re

#pattern = r"[A-Za-z]+" #This is kinda like a range for the words only!!!!
#text = "Order 123 was placed on 2023-05-01."
#print(re.findall(pattern, text))

import re

pattern = r"\d+\.\d+\.\d+\.\d+" # pattern of the ip addresses and the last \d is for time
text = "Failed login from 192.168.0.1 192.168.1.224 at 10:30"

print(re.findall(pattern, text))





