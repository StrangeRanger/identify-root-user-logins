This program scans auth.log in order to find out if a user(s) have logged in as root, and identify who they are. This program is disigned to be executed as a cronjob. It is recommended to have this program executed everyday at 11:59 PM. When cronjob executes the program, all data/information collected will be reported to the root_login_log. 

Important Notes:
- When creating the cronjob, create it in root's cronjob by entering `sudo corntab -e`. The recommended cronjob preset/setting is `59 23 * * * python3 /location/of/root_login_search.py`.

Security Features/Notes:
- This program identifies user who have used `sudo bash`, `sudo -i`, `sudo su`, and `su`/`su root`
- If a user on the system created a temporary account in order to log in as root, then deletes the account after he or she is done with it, the temporary account will still show up in the scan results.

Program Notes/Faults:
- If a user, user1, became a different user on the system via `sudo su {username}`, and logged into the root account, he or she will not be flagged as the user who logged in as root. Instead, the user user1 changed to will take the blame. To counter act this, it is recommended to use `last` or `lastlog` with the date of your choosing, to identify all users who logged onto the system. Use the information you gain from last/lastlog with the information from this program to pinpoint the exact user.

Other Notes:
- By default, the auth.log will only be scanned for logs written on the current day. If you wish to change the number of days, change the value of N in the script.
