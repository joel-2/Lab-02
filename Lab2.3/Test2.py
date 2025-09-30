# lab2.3_starter.py
import json
from collections import defaultdict
from datetime import datetime
from datetime import timedelta

LOGFILE = "sample_auth_small.log"
sorted_list=[]
output={}


def parse_auth_line(line):
    """
    Parse an auth log line and return (timestamp, ip, event_type)
    Example auth line:
    Mar 10 13:58:01 host1 sshd[1023]: Failed password for invalid user admin from 203.0.113.45 port 52344 ssh2
    We will:
     - parse timestamp (assume year 2025)
     - extract IP (token after 'from')
     - event_type: 'failed' if 'Failed password', 'accepted' if 'Accepted password', else 'other'
    """
    parts = line.split()
    # timestamp: first 3 tokens 'Mar 10 13:58:01'
    ts_str = " ".join(parts[0:3]) # this joins the first three parts i.e month, day, time
    try:
        ts = datetime.strptime(f"2025 {ts_str}", "%Y %b %d %H:%M:%S") # assume 2025 is the year year, month, day, hour, minute, second
    except Exception: # return none if timestamp parsing fails
        ts = None
    ip = None
    event_type = "other" # default event type
    if "Failed password" in line:
        event_type = "failed" #setting condition for failed event
    elif "Accepted password" in line or "Accepted publickey" in line:
        event_type = "accepted" #setting condition for accepted event
    if " from " in line: #parsing the ip address
        try:
            idx = parts.index("from") # all the usual things
            ip = parts[idx+1]
        except (ValueError, IndexError):
            ip = None
    return ts, ip, event_type

if __name__ == "__main__":
    per_ip_timestamps = defaultdict(list) # dictionary declaration
    with open(LOGFILE) as f: #opening the file
        for line in f: #chopping it line by line
            ts, ip, event = parse_auth_line(line) # calling the function and returning the values
            if ts and ip and event == "failed":   # checks that ts and ip are not null, and that event=="failed"
                per_ip_timestamps[ip].append(ts)

    for ip, ts in per_ip_timestamps.items():
        sorted_ts = sorted(ts) # sorting the timestamps
        formatted_ts = [t.strftime("%Y-%b-%d %H:%M:%S") for t in sorted_ts] # formatting the timestamps and putting int a list
        output[ip] = formatted_ts # storing the formatted timestamps in the output dictionary
    
incidents = [] # make a list called incidents to store the results
window = timedelta(minutes=10) #define the time delta window of 10 minutes
for ip, times in per_ip_timestamps.items(): #iterate through the dictionary
    times.sort() #sort timestamps
    n = len(times) #get the length of the timestamps list
    i = 0
    while i < n:
        j = i
        while j + 1 < n and (times[j+1] - times[i]) <= window:
            j += 1
        count = j - i + 1
        if count >= 5: # if there are 5 or more failed attempts in the window
            incidents.append({
                "ip": ip,
                "count": count,
                "first": times[i].isoformat(),
                "last": times[j].isoformat()
            })
            # advance i past this cluster to avoid duplicate overlapping reports:
            i = j + 1
        else:
            i += 1
print(f"{len(incidents)} brute-force incidents found:")
for i in incidents:
    print(i)