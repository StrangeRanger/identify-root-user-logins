import sys
import os.path
import collections
from datetime import datetime, timedelta

class DateError(Exception):
    pass

N = 0 # how many days
path = os.path.split(sys.argv[0])[0] + ("root_login_log" if os.path.isfile("root_login_search.py") else "/root_login_log") # ensures the correct location of root_login_log
log = open(path, "a")

os.chmod(path, 0000) 
log.write("---auth.log scanned on " + str(datetime.now()) + "---\n")

def root_users():
    today = datetime.now().date()
    start_date = today - timedelta(days=N)
    this_year = datetime.now().year
    last_year = this_year - 1
    days = collections.defaultdict(collections.Counter) # A.1. a defaultdict that maps objects (dates) to counters. 

    with open("/var/log/auth.log", "r") as txt: 
        for line in txt:
            fields = line.split() 
            date_str = " ".join(fields[0:2]) + " " 
            # makes sure that the log date is correct; if current date is January 01 2020 and looking a line in log with date Dec 31 that was logged in 2019, the date would = Dec 31 2020. Lines below prevent this.
            try:
                date = datetime.strptime(date_str + str(this_year), "%b %d %Y").date()
                if date > today: raise DateError
            except DateError:
                date = datetime.strptime(date_str + str(last_year), "%b %d %Y").date()
              # will skip any abnormal/non-regular text in /var/log/auth.log that could produce an Error, and then prints out a message telling the user to check out the line in the file.
            except ValueError:
                print("There was an abnormality on a line. Please take a look inside /var/log/auth.log at the line matching this: {}".format(line))
                continue

            if (date < start_date):
                # too old for interest
                continue 
            # "user : TTY=tty/1 ; PWD=/home/user ; USER=root ; COMMAND=/bin/su"
            if fields[4] == "sudo:":
                user = fields[5]
                conditions = (user != "root" and (fields[8] != "incorrect" if len(fields) >= 9 else None) and fields[-4] == "USER=root" and fields[-2] in ("COMMAND=/bin/bash", "COMMAND=/bin/sh", "COMMAND=/bin/su")) 
                # "..."; identifies users who successfully became root using `sudo su`
                if user != "root" and (fields[8] != "incorrect" if len(fields) >= 9 else None) and fields[-3] == "USER=root" and fields[-1] in ("COMMAND=/bin/bash", "COMMAND=/bin/sh", "COMMAND=/bin/su"):
                    days[date]["+" + user] += 1 # A.2. The defaultdict key becomes the date and its value, which is the counter, is the user, which gains a plus 1 in the counter
                # "..."; identifies users who successfully became root using `sudo su root`
                elif conditions and fields[-1] == "root":
                    days[date]["+" + user] += 1 # A.2.
                # "..."; identifies users who unsuccessfully became root using `sudo su`
                elif user != "root" and (fields[8] == "incorrect" if len(fields) >= 9 else None) and fields[-3] == "USER=root" and fields[-1] in ("COMMAND=/bin/bash", "COMMAND=/bin/sh", "COMMAND=/bin/su"):
                    days[date]["*" + user] += 1
                # "..."; identifies users who successfully switched users using `sudo su <username>`
                elif conditions and fields[-1] != "root": 
                    days[date]["-" + user] += 1 # A.2.
                ### code will be placed here that identifies users who unsuccessfully switch users using `sudo su <username>`
                elif user != "root" and (fields[8] == "incorrect" if len(fields) >= 9 else None) and fields[-4] == "USER=root" and fields[-2] in ("COMMAND=/bin/bash", "COMMAND=/bin/sh", "COMMAND=/bin/su"):
                    days[date]["/" + user] += 1 # A.2.

            ## when a way is found, make it so that the severity level is greater with the ones below. "Change your password...<> knows your password"
            # "Successful su for root by user"; identifies users who've successfully became root using `su`
            if fields[4].startswith("su[") and fields[5] == "Successful" and fields[-3] == "root":
                user = fields[-1]                
                if user != "root":
                    days[date]["+" + user] += 1 # A.2.
            # "FAILED su for root by <username>"; identifies users who've unsuccessfully became root using `su`
            elif fields[4].startswith("su[") and fields[5] == "FAILED" and fields[-3] == "root":
                user = fields[-1]
                if user != "root":
                    days[date]["*" + user] += 1 # A.2.
            # "Successful su for <username> by <username>"; identifies users who've successfully switched users using `su <username>`
            elif fields[4].startswith("su[") and fields[5] == "Successful" and fields[-3] != "root":
                user= fields[-1]
                if user != "root":
                    days[date]["-" + user] += 1 # A.2. 
            # "FAILED su for <username> by <username>"; identifies users who've unsuccessfully switched users using `su <username>`
            elif fields[4].startswith("su[") and fields[5] == "FAILED" and fields[-3] != "root":
                user= fields[-1]
                if user != "root":
                    days[date]["/" + user] += 1 # A.2.

    while start_date <= today:
        log.write(start_date.strftime("On %b %d:\n"))
        users = days[start_date]
        if users:
            for user, count in users.items(): # user, count is used because we're reading from a counter; which is a dict that maps username to count of occurrences
                if "+" in user:
                    log.write("    " + user + " became root " + str(count) + (" time\n" if count == 1 else " times\n"))
                elif "-" in user:
                    log.write("    " + user + " switched users " + str(count) + (" time\n" if count == 1 else " times\n"))
                elif "*" in user:
                    log.write("    " + user + " tried to become root " + str(count) + (" time\n" if count == 1 else " times\n"))
                elif "/" in user:
                    log.write("    " + user + " tried to switch users " + str(count) + (" time\n" if count == 1 else " times\n"))
        else:
            log.write("    No one became root\n")
        start_date += timedelta(days=1)

    log.write("*****************************************************+-*/\n" if users else "*****************************************************\n")

root_users()
log.close()























