-Version 2.0-

This program scans auth.log in order to find out if a user(s) have logged in as root, and identify who they are.

Security Features/Notes:
- If a user on the system created a temporary account in order to log in as root, then deletes the account after he or she is done with it, the temporary account will still show up in the scan results.
- The auth.log will be scanned up to 7 days worth of logs, unless user manually changes the number of days within the main script.

Program Notes/Faults:
- If a user, user1, became a different user on the system via `sudo su {username}`, and logged into the root account, he or she will not be flagged as the user who logged in as root. Instead, the user he or she changed to will take the blame.
