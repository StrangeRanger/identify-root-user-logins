This program scans auth.log in order to find out if a user(s) have logged in as root, and identify who they are.

Security Features/Notes:
- This program identifies user who have used `sudo bash`, `sudo -i`, `sudo su`, and `su`/`su root`
- If a user on the system created a temporary account in order to log in as root, then deletes the account after he or she is done with it, the temporary account will still show up in the scan results.
- Any and all users who use `sudo su` to change to another user will be marked/identified. This makes it easier to identify a user who tries to blame a different user for logging in as root. (see Program Notes/Faults below)

Program Notes/Faults:
- If a user, user1, became a different user on the system via `sudo su {username}`, and logged into the root account, he or she will not be flagged as the user who logged in as root. Instead, the user he or she changed to will take the blame. To make it easier to identify the user who really logged into the root account, the program will print out any and all users who use `sudo su` to change to another user's account.
- Small error: if user inputs their sudo password correctly when executing `sudo su <username>`, but the username does not exist, they will still be marked. This will be fixed/made into a feature later in future. The feature will allow you to see users who have tried to log into root account and tried to switch users.

Other Notes:
- By default, the auth.log will be scanned up to 7 days worth of logs. If you wish to change the number of days, change teh value of N in the script.

