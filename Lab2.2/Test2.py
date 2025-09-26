from collections import defaultdict

counts = defaultdict(int)           # Creating a dictionary to keep track of IPs

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
print(counts)