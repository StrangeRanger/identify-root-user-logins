import pdb
import re
import datetime
from itertools import islice
import subprocess # allows the execution of users.bash from within a python script
import os

# the two lines below changes date to unix/linux format(e.g. March  1 "or" March 20)
date2 = datetime.datetime.now().strftime("%b  %-d")
date1 = datetime.datetime.now().strftime("%b %d")
tmp = open("tmp.txt", "w+") # creates and opens a text file called tmp.txt

with open("/var/log/auth.log", "r") as txt: 
    for line in txt:
        if re.match("^%s.+" % date1, line) or re.match("^%s.+" % date2, line): # takes all lines in /var/log/auth.log that were made on the current day...
            if "Successful su for root by root" in line: # then takes all lines that says <--...
                lines_gen = islice(txt, 2) # and the 2 lines below it...
                tmp.writelines(lines_gen) # then writes them into the tmp.txt file
tmp.close()

subprocess.call("./users.sh") # calls to and executes users.sh

users = [] # a list/array of all known users on the system
with open("users", "r") as txt: # places all users that are in the users file into users
    for u in txt:
        users.append(u)

login = False # at this moment, no one has been detected logging in as root
root_users = []
# checks the tmp.txt file to see if any known users are named within it
with open("tmp.txt", "r") as txt:
    for line in txt:
        for word in re.findall(r"\w+", line):
            if word != "root": # this makes sure that if root is in a line, which it will always be, it won't add root to the root_users array
                if word + "\n" in users:
                    root_users.append(word)
                    login = True # someone has been detected logging in as root

for u in users: # goes through the users array where u = a single user
    #pdb.set_trace()
    x = 0 # tallies the total amount of times a single users logged into the root account
    t = 0
    for r in root_users: # goes through the root_users array where r = a single user
        t += 1
        if u == r + "\n":
            x += 1
        if t == len(root_users):
            if x >= 1:
<<<<<<< HEAD
                print(u + " became root " + str(x) + " times.")
=======
                print(u + " became root " + str(x) + " times.") 
>>>>>>> 3c6ddde1276aa29b505a7cbb3416108666534b9f

if login == False:
    print("No one became root")

os.remove("users") # removes file users
os.remove("tmp.txt") # removes file tmp.txt
