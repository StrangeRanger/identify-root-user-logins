This program scans auth.log in order to find out if a user(s) have logged in as root, and identify who they are. This program is disigned to be executed as a cronjob. It is recommended to have this program executed everyday at 11:59 PM. When cronjob executes the program, all data/information collected will be reported to the root_login_log. 

Important Notes:
- When creating the cronjob, create it in root's cronjob by entering `sudo corntab -e`. The recommended cronjob preset/setting is `59 23 * * * python3 /location/of/root_login_search.py`.

Security Features/Notes:
- This program identifies user who have used `sudo bash`, `sudo -i`, `sudo su`, and `su`/`su root`
- If a user on the system created a temporary account in order to log in as root, then deletes the account after he or she is done with it, the temporary account will still show up in the scan results.
- Any and all users who use `sudo su` to change to another user will be marked/identified. This makes it easier to identify a user who tries to blame a different user for logging in as root. (see Program Notes/Faults below)
- Any and all users who attempt to either log into the root account or switch users, and are unsuccessful, will be identified and marked down.

Program Notes/Faults:
- If a user, user1, became a different user on the system via `sudo su {username}`, and logged into the root account, he or she will not be flagged as the user who logged in as root. Instead, the user he or she changed to will take the blame. To make it easier to identify the user who really logged into the root account, the program will print out any and all users who use `sudo su` to change to another user's account.
- Small error: if user inputs their sudo password correctly when executing `sudo su {username}`, but the username does not exist, they will still be marked as `{username} has switched users {X} time(s)`.

Other Notes:
- By default, the auth.log will only be scanned for logs written on the current day. If you wish to change the number of days, change the value of N in the script.

This program only works on Linux based systems.
Current Distros That The Program Works On:
- Ubuntu: Works
- Debian: Works
- CentOS: Unkown
- Mint: Unkown
- Arch: Unkown
- Fedora: unkown
- ...
