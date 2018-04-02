These two scripts work together in order to find out if a user has logged/used su to become root.

Security Features/Notes:
- Say a user, let's call him Bob, wants to log into the root account but does not want anyone to know that is was him. If he executed "sudo su <another user>", becoming a different user on the system, then logged in as root, Bob would still be flagged. But if Bob used "sudo -i", the user he had logged into, would be flagged instead.
- The auth.log will be scanned up to 7 days prior to the current day.

Program Notes/Faults:
- If this program is to work correctly, the hostname of the computer or server MUST NOT contain the name of any user on the system: if you have a user named bob, the hostname can not be "bob-computer" or anything containing "bob". This will cause the program to falsely flag bob as a user who logged in as root or will double up on the amount of times he logged in as root if he used "sudo su". (NOTE: This will only occure if a user has been flagged as someone who has logged in as root.)
- On some flavors of Linux, such as Ubuntu, the necesary information to identify a user who logged in as root will not show up. The specific problem lies in a sentence that contains the username: "session opened for user root by <username>(uid=0)". Sometimes the username will not show up and the sentence will look like this: "session opened for user root by (uid=0)". Therefore the user cannot be identified. This problem has only been identified for times when "sudo su" has been used. This problem does not always occure, but it does more than it does not.
