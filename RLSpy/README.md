These two scripts work together in order to find out if a user has logged/used su to become root. (NOTE: There is one feature that needs to be added: looks back at least one week and tells you who and how many times a users logged in as root on each of those days... That way you are informed about the last 7 days and not just the current day.)

Additional Security:
____	- Say a user, let's call him Bob, wants to log into the root account but does not want anyone to know that is was him. If he executed "sudo su <another user>", becoming a different user on the system, then logged in as root, Bob would still be flagged. But if Bob used "sudo -i", the user he had logged into, would be flagged instead.
