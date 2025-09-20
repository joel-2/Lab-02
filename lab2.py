import re

#with open("auth.log",'r') as line:
#    for i in line:
#            print(i.strip())


list_ip= r"\d+\.\d+\.\d+\.\d+" #BEWARE THERE IS NO SPACE BETWEEN
ips=[]
with open("auth.log",'r') as line:
    for i in line:
        s=i.strip()
        t=re.findall(list_ip,s)
        for m in t:
            ips.append(m) #Remember you FOOL its not LINUX  or JAVA anymore!!!
b=set(ips)
with open("unique_ips.txt", 'w+') as k:
    for i in b:
        k.write(i +'\n')
print("Everything is Successfully done!!!")







