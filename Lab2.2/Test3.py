from collections import defaultdict
import time

start = time.time()          # start the timer
counts = defaultdict(int)           # Creating a dictionary to keep track of IPs

def top_n(counts, n=5): #I have no idea what this does but knows it just sortes the dictionary
    return sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:n]

def ip_parse(line): #this is the functionto extract the ip from the line

    
    parts = line.split() # splits the line into tokens, seperates by spaces by default
    try:
        anchor = parts.index("from")    # Find the position of the token "port", our anchor
        port = parts[anchor+1]          # the port value will be next token, anchor+1
        return port.strip()             # strip any trailing punctuation
            
                    
           
                        

    except (ValueError, IndexError):
        return None

    return None

with open("sample_auth_small.log",'r') as f:
    for line in f:
        if (" Failed password " or " Invalid User ")in line:
            # extract ip
            ip = ip_parse(line) # passing over the line that meets the criteria to the fuction up
            if ip:
                counts[ip] += 1



print("Top 5 Attacker Ip :")
for ip, count in top_n(counts, n=5):
        print(f"{ip} - {count}")

# we gotta open a file now and write this to file and add time parsed
with open("failed_counts.txt",'w+') as k:
    k.write("Top 5 Attacker Ip :\n")
    for ip, count in top_n(counts, n=5):
        k.write(f"{ip} - {count}\n")
        k.write("\n")

print("Wrote failed_counts.txt")

# timer
end = time.time()
print("Elapsed:", end-start, "seconds")