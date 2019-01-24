# The Way This Script Is Used
This script is disigned to be executed as a cronjob. It is recommended to have this script executed everyday at 11:59 PM. When cronjob executes the script, all data/information collected will be reported to/placed in the root-login-log located in the same directory as the script. 

# Important Notes:
- When creating the cronjob, create it in root's cronjob by executing `sudo corntab -e`. The recommended cronjob preset/setting is `59 23 * * * python3 /location/of/root-login-search-cronjob.py`.

# Other Notes:
- By default, the auth.log will only be scanned for logs written on the current day. If you wish to change the number of days, change the value of N in the script.
