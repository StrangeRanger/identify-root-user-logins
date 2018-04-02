These two scripts work together in order to find out if a user has logged/used su to become root.

Additional Security Notes:
		- Say a user, let's call him Bob, wants to log into the root account but does not want anyone to know that is was him. If he executed "sudo su <another user>", becoming a different user on the system, then logged in as root, Bob would still be flagged. But if Bob used "sudo -i", the user he had logged into, would be flagged instead.

Program Notes/Falts:	- If this program is to work correctly, the hostname of the computer or server MUST NOT contain the name of any user on the system: if you have a user named bob, the hostname can not be "bob-computer" or anything containing "bob". This will cause the program to falsely flag bob as a user who logged in as root or will double up on the amount of times he logged in as root if he used "sudo su". (NOTE: This will only occure if a user has been flagged as someone who has logged in as root.)		- The auth.log will be scanned up to 1 week.
