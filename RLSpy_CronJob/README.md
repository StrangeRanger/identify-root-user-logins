-Version 2.0-

This program scans auth.log in order to find out if a user(s) have logged in as root, and identify who they are. This program is disigned to be executed as a cronjob. It is recommended to have this program executed every Saturday at 11:59 PM. When cronjob executes the program, all data/information collected will be reported to the root_login_log. 

Important Notes:
- When creating the cronjob, create it in root's cronjob by entering `sudo corntab -e`. The recommended crontab preset/setting is `59 23 * * 6 cd {location of RLSpy_CronJob} && python3 root_login_search.py`. It is important that you include `cd {location of RLSpy_CronJob}` or else the cronjob will not work.

Security Features/Notes:
- The auth.log will be scanned up to 7 days worth of logs, unless users manually changes the number of days within the main script.

Program Notes/Faults:
- If a user, user1, became a different user on the system via `sudo su {username}`, and logged into the root account, he or she will not be flagged as the user who logged in as root. Instead, the user user1 changed to will take the blame.
