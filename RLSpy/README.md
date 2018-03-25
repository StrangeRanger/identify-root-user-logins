These two scripts work together in order to find out if a user has logged/used su to become root. (NOTE: There is one feature that needs to be added: looks back at least one week and tells you who and how many times a users logged in as root on each of those days... That way you are informed about the last 7 days and not just the current day.)

Additional Security Notes:
	- Say a user, let's call him Bob, wants to log into the root account but does not want anyone to know that is was him. If he executed "sudo su <another user>", becoming a different user on the system, then logged in as root, Bob would still be flagged. But if Bob used "sudo -i", the user he had logged into, would be flagged insteadi.

Program Notes/Falts:
	- If this program is to work correctly, the hostname of the computer or server MUST NOT contain the name of any user on the system: if you have a user named bob, the hostname can not be "bob-computer" or anything containing "bob". This will cause the program to falsely flag bob as a user who logged in as root or will double up on the amount of times he logged in as root if he used "sudo su". (NOTE: This will only occure if a user has been flagged as someone who has logged in as root.)
