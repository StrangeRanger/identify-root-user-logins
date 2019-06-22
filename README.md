# Purpose/What It Does
The script was created for the purpose of identifying users, on a linux based system, who have have successfully and unsuccessfully logged into/switch to the root user account as well as those who have successfully and unsuccessfully switched to a different user on the system. It does this by looking for a hard coded pattern/string/set of lines that are written to `/var/log/auth.log`. These patterns can be looked at in `identifying-patterns.odt`.

## Specifics
- There are two versions of the script. One is designed for manual execution. The other is designed to be executed as a CronJob.
- When executing either versions of the script, you **must** use `sudo` or else an error will be produced telling you that you do not have permission to read the log. 

## Security Features/Notes:
- This script identifies user who have used `sudo bash`, `sudo -i`, `sudo su`, and `su`/`su root`
- If a user on the system created a temporary account in order to log in as root, then deletes the account after he or she is done with it, the temporary account will still show up in the scan results.
- Any and all users who use `sudo su` to change to another user will be marked/identified. This makes it easier to identify a user who tries to blame a different user for logging in as root. (see Script Notes/Faults below)
- Any and all users who attempt to either log into the root account or switch users, and are unsuccessful, will be identified and marked down.
- Users who are not in the sudoers file and try to execute a command with root privilege, will be identified.

## Script Faults/Limitations
- If a user with sudo power, call him Mal, switches to another user who may or may not have sudo power, call him Vic, then uses `sudo` or `su`, will cause Vic to be blamed for executing the commands instead of Mal. Though, Mal must know Vic's password in order successfully use sudo. The best way to verify who actually did it is 
  - Semi-built in helper: Because the script will identify users who use `su` and `sudo su`, Mal will be identified as an individual who switched users.
  - Method of weeding out true culprit: Look through the auth.log at the logs taken on the given day that the incident took place... To know what to look for, please refer to "identifying-patterns.odt"; it contains all auth.log logs that are created in relation to the given commands and there relative success or failure...

## Flaws (that will be fixed, hopefully, in the future)
- If a user inputs their sudo password correctly when executing `sudo su <username>`, but the username does not exist, they will not be marked at all. 
- If a user executes `su <username>`, where username is that of a user that is not on the system, it will not be logged/identified as a user who tried to be switched to.
- The linux system uses something called [logrotate](https://linux.die.net/man/8/logrotate) which causes the auth.log to be "rotated"/changed, usually weekly, at some point in the day. This means that if an individual tried logging into root, or any of the other possibilities, and the log was rotated before the script was executed, the individual would not be identified. A fix/work around is being looked into. This currently only applies to the cronjob version of the script.

# Other Notes
- When an individual logs into the root accounts, whether it be via `sudo su` or `su`, then as root use `sudo su` or `su`, that user will be identified twice. Even though the user changed to the root user, the script will still identify them as a user who logged into the root account.

# What It Doesn't Do
- The script will not identify the root user itself for anything, even if it does/meets the requirements/identifiers that are mentioned above. This means that if for some reason root changes to another user, the script will not identify root doing this.

# Stystem Related Information
## Requirements
- Python 3.x

## Linux Distros That The Script Works On:
- Ubuntu
  - Bionic Beaver: DOES NOT WORK; version of script that works on [Bionic Beaver](https://github.com/StrangeRanger/identify-root-user-logins)
  - Xenial Xerus: DOES NOT WORK; version of script that works on [Xenial Xerus](https://github.com/StrangeRanger/identify-root-user-logins) 
  - Trusty Tahr and before: N/A
- Debian
  - Buster: Works 
  - Stretch: DOES NOT WORK; version of script that works on [Stretch](https://github.com/StrangeRanger/identify-root-user-logins)
  - Jessie and before: N/A
- Kali
  - 2019.2: Works
  - 2019.1 and before: N/A
- Redhat
  - DOES NOT WORK
- "More will be tested in the future"
