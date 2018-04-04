These two scripts work together in order to find out if a user has logged in as root.

Important Notes:
- If this program is to work correctly, the hostname of the computer or server MUST NOT contain the name of any user on the system: if you have a user named bob, the hostname can not be "bob-computer" or anything containing "bob". This will cause the program to falsely flag bob as a user who logged in as root or will double up on the amount of times he had logged in as root if he used `sudo su`. (NOTE: This will only occure if a user has been flagged as someone who has logged in as root.)


Security Features/Notes:
- If a user, user1, executed "sudo su *{username}*", becoming a different user on the system, then logged in as root, he or she would still be flagged. But if user1 used `sudo -i`, the user he or she had logged into, would be flagged instead.
- The auth.log will be scanned up to 7 days worth of logs, unless user manually changes the number of days within the main script.

Program Notes/Faults:
- On some flavors of Linux, if not all, the necesary information to identify a user who logged in as root will not show up. The specific problem lies in a sentence that contains the username: "session opened for user root by *{username}*(uid=0)". Sometimes the username will not show up and the sentence will look like this: "session opened for user root by (uid=0)". Therefore the user cannot be identified. This problem only occures at times when `sudo su` is used in combination with a gui terminal. If one of the two is not used, this problem does not occure. In this instance, a gui terminal does not include times when remotely connecting to a server via ssh, or when using a headless/non-gui system: tty1.
