import sys
import os.path
import collections
from datetime import datetime, timedelta

N = 0 # how many days
path = os.path.split(sys.argv[0])[0] + "/root_login_log" # ensures the correct location of root_login_log
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
            # makes sure that the log date is correct; current date is January 01 2020 and looking a line in log with date Dec 29 that was logged in 2019. Makes sure date added to days is not Dec 29 2020.
            try:
                date = datetime.strptime(date_str + str(this_year), "%b %d %Y").date()
                if date > today: raise ValueError
            except ValueError:
                date = datetime.strptime(date_str + str(last_year), "%b %d %Y").date()

            if (date < start_date):
                # too old for interest
                continue 
            # "user : TTY=tty/1 ; PWD=/home/user ; USER=root ; COMMAND=/bin/su"
            if fields[4] == "sudo:":
                user = fields[5]
                if user != "root" and fields[-3] == "USER=root" and fields[-1] in ("COMMAND=/bin/bash", "COMMAND=/bin/sh", "COMMAND=/bin/su"): 
                    days[date][user] += 1 # A.2. The defaultdict key becomes the date and its value, which is the counter, is the user, which gains a plus 1 in the counter
            # "Successful su for root by user"; identifies users who use su without sudo
            if fields[4].startswith("su[") and fields[5] == "Successful" and fields[-3] == "root":
                user = fields[-1]
                if user != "root":
                    days[date][user] += 1 # A.2.

    while start_date <= today:
        log.write(start_date.strftime("On %b %d:\n"))
        users = days[start_date]
        if users:
            for user,count in users.items(): # user,count is used because we're reading from a counter; which is a dict that maps username to count of occurrences
                log.write("    " + str(user) + " became root " + str(count) + (" time\n" if count == 1 else " times\n"))
        else:
            log.write("    No one became root\n")
        start_date += timedelta(days=1)

root_users()
log.write("*****************************************************\n")
log.close()
