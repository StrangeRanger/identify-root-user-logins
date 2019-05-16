# The Way This Script Is Used
This version of the script is created with the intent of being executed manually. Execution command: `sudo python3 root-login-search.py`

# Other Notes
## Script Notes
By default, the auth.log will be scanned up to 8 days worth of logs. The reason for this is due to that fact that logrotate generally rotates every 7 days. Though it does not always rotate at the beginning of a new day, meaning it can ratate at 13:54:21, etc. By scanning the logs of the past 8 days, it is possible to make sure that that script will scan the previous/archived log, just to make sure nothing was missed.
If you wish to change the number of days, change the value of N in the script.
