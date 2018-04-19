This program scans auth.log in order to find out if a user(s) have logged in as root, and identify who they are.

Security Features/Notes:
- This program identifies user who have used `sudo bash`, `sudo -i`, `sudo su`, and `su`/`su root`
- If a user on the system created a temporary account in order to log in as root, then deletes the account after he or she is done with it, the temporary account will still show up in the scan results.

Program Notes/Faults:
- If a user, user1, became a different user on the system via `sudo su {username}`, and logged into the root account, he or she will not be flagged as the user who logged in as root. Instead, the user he or she changed to will take the blame. To counter act this, it is recommended to use `last` or `lastlog` with the date of your choosing, to identify all users who logged onto the system. Use the information you gain from last/lastlog with the information from this program to pinpoint the exact user.

Other Notes:
- By default, the auth.log will be scanned up to 7 days worth of logs. If you wish to change the number of days, change teh value of N in the script.

