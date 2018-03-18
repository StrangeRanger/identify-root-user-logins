#!/bin/bash

USERS=`awk -F: '{ print $1 }' < /etc/passwd`

touch users
for u in $USERS; do
	echo $u >> users
done
