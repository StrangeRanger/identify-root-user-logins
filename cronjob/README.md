# General Info
## The Way This Script Is Used
This script is designed to be executed as a cronjob. When cronjob executes the script, all data/information collected will be reported to/placed in the root-login-log located in the same directory as the script. 

## Setting Up Cronjob:
When creating the cronjob, create it in root's cronjob by executing `sudo corntab -e`. The cronjob will want to look something like this `58 23 * * * python3 /location/of/root-login-search-cronjob.py`. Currently, it is recommended to create two cronjobs: `58 23 * * * python3 /location/of/root-login-search-cronjob.py` and on a separate line `58 11 * * * python3 /location/of/root-login-search-cronjob.py`. It is not necessary to use both but it is recommended, because of a current flaw in the script. Check the main README.md to read the different flaws that have been found in the script

## Maintaining root-login-search.log
Currently, the only to maintain the logs is by manually going in and deleting all the logs if you feel that there are too many. Later in the future, an update may be added that will create a [logrotate](https://linux.die.net/man/8/logrotate) specifically for maintaining the log file.

# Using SMTP To Send Scan Report Via Email (Optional)
If you want to use SMTP and Mail to send yourself the results of the scan by email you will want to do a few things to the script.
- Inside the script, uncomment all commented out `print` lines that have "B.1." at the end of them. This will print all the same info that is written to the log.
- Instead of entering the cronjob setting listed in the "Important Notes", use this: `58 23 * * * python3 /location/of/root-login-search-cronjob.py | mail -s "root-login-search-cronjob results" {email of recipient}`.

## Email/SMTP Troubleshooting
Depending on flavor of linux, the above cronjob may not work, the email does not send, or the email does get sent but it contains nothing. There are a few things that you can do/try, to fix a problem:
- Remove email from the cronjob and create a variable above it that says `MAILTO={email of recipient}`. This is what it would look like (just don't forget to add your own email to the MAILTO variable):
  ```sh
  MAILTO={email of recipient}
  58 23 * * * python3 /location/of/root-login-search-cronjob.py | mail -s "root-login-search-cronjob results" $MAILTO
  ```
- Instead of executing the script from a directory that does not contain the script, first move to that directory and then execute script. This is what is would look like:
  ```sh
  58 23 * * * cd /directory/containing/root-login-search-cronjob.py && python3 root-login-search-cronjob.py | mail -s "root-login-search-cronjob results" {email of recipient}
  ```
- If those don't work you can try combining both of them.
- Check your SMTP configuration, which are locate here: `/etc/ssmtp/ssmtp.conf`.
- If all else fails and it does not work, then please report the issue here, stating the Linux distro, version number, what you have done to try to solve the problem, and if possible, an image or two of your ssmtp.config file (make sure to sensor out the AuthUser and AuthPass; I don't think I need to explain why you should do that)

## SMTP Links
Here are a few links to help you get started in setting up with SMTP 
- Debian Wiki: [sSMTP](https://wiki.debian.org/sSMTP)
- Arch Wiki: [SSMTP](https://wiki.archlinux.org/index.php/SSMTP)
- Gist: [SSMTP setup on Debian](https://gist.github.com/StrangeRanger/d8e83e4683ac98510171f716453ba4db)

# Other Notes
## Script Notes
By default, the auth.log will only be scanned for logs written on the current day and the day before. If the time that the cronjob is executed is based off of when they. If you wish to change the number of days, change the value of N in the script.

## Non-Script Notes
Anywhere, inside of this README.md, that you see `{}` with text inside, are things that you substitute with whatever is described between the curly brackets: `{username}` will be replaced with the your username such as `StrangeRanger`.
