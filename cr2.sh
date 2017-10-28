#!/bin/bash

DATE=`date | awk '{ print $2 " " $3 }'`
USERS=`awk -F: '{ print $1 }' < /etc/passwd`

touch tmp
chmod 000 tmp
grep -a "$DATE" /var/log/auth.log | grep "Successful su for root by root" -n -2 | grep "session opened for user root by" > tmp
for u in $USERS; do
	if [ "$u" == "root" ]; then
		continue
	fi
	while read i; do
		grep "$u" <<< "$i" >/dev/null
		if [ "$?" == "0" ]; then
			echo "$u" became root
			break
		fi
	done < tmp
done
rm tmp
