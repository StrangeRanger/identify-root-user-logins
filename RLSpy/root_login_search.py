import re
from datetime import datetime, timedelta
from itertools import islice
import subprocess
import os

N = 7 
def root_users():
    N_days_ago = datetime.now() - timedelta(days=N) # determines what days in the auth.log will be scanned, starting from 7 to 0 days prior to the current day 
    # the two lines below changes date to unix/linux format(e.g. March  1 "or" March 20)
    date2 = N_days_ago.strftime("%b  %-d")
    date1 = N_days_ago.strftime("%b %d")
    tmp = open("tmp.txt", "w+") 

    with open("/var/log/auth.log", "r") as txt: 
        for line in txt:
            if re.match("^%s.+" % date1, line) or re.match("^%s.+" % date2, line): # 1. takes all lines in /var/log/auth.log that were made N days ago
                if "Successful su for root by root" in line: # this will identify users who used "sudo su" # 2. then takes all lines that say "Successful su..."
                    lines_gen = islice(txt, 2) # 3. and takes the 2 lines below it...
                    tmp.writelines(lines_gen) # 4. then writes them into the tmp.txt file
                if re.match("^.+COMMAND=/bin/bash$", line): # this will identify users who use "sudo bash" and "sudo -i"
                    tmp.writelines(line)
    tmp.close()
    
    subprocess.call("./users.sh") # calls to and executes users.sh
    
    users = [] # a list/array of all known users on the system
    with open("users", "r") as txt: # places all users that are in the users file into the users array
        for u in txt:
            users.append(u)
    
    login = False # at this moment, no one has been detected as a user who has logged in as root
    root_users = []
    # checks the tmp.txt file to see if any known users are named within it
    with open("tmp.txt", "r") as txt:
        for line in txt:
            for word in re.findall(r"\w+", line):
                if word != "root": # this makes sure that if root is in a line, which it will always be, it won't add root to the root_users array
                    if word + "\n" in users:
                        root_users.append(word)
                        login = True # someone has been detected as someone who logged in as root
                        break # this break is placed here to prevent accidental miscount of times a user logged into the root account. it also prevents users who did not log in as root to be falsely tagged.
    
    print("On " + date1 + ":")
    for u in users: # goes through the users array where u = a single known user
        x = 0 # tallies the total amount of times a single users logged into the root account
        t = 0 # keeps track of where variable r is in the root_users array and once it become the length of root_users, it starts back at the top for loop, moving onto the next user in users
        for r in root_users: # goes through the root_users array where r = a single user
            t += 1
            if u == r + "\n":
                x += 1
            if t == len(root_users):
                if x >= 1:
                    print("    " + u + "     became root " + str(x) + " times.")
    
    if login == False:
        print("    No one became root")
    
    os.remove("users")
    os.remove("tmp.txt")

for i in range(7):
    N -= 1 # every time root_users() has gone through its course, one date earlier in auth.log will be scanned (May 7th will be scanned, next May 8th will be scanned, etc.)
    root_users()

