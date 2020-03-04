#!/bin/bash
# Script from https://forum.opsi.org/viewtopic.php?t=9163
PATH=/sbin:/bin/:/usr/sbin/:/usr/bin
OPSICLI="opsi-admin -dS method"
for client in $($OPSICLI getClientIds_list | sort ) ; do
           VALIDATEDMACS=
           HWINFOHASH=$($OPSICLI getHardwareInformation_hash $client)
	   COMPUTERSYSTEM=$(echo "$HWINFOHASH" | grep COMPUTER_SYSTEM | grep -o -P "model': u'.{5,35}" | cut -d, -f1) 
	   #exit
           # get Serial
           HWSERIAL=$(echo "$HWINFOHASH" | grep -i chassis | cut -d':' -f4 | cut -d"'" -f2)
	   #echo "$HWINFOHASH" | grep -i chassis
	   #exit
           # echo $HWSERIAL
           # get MAC Addresses
           NETWORKCONTROLLER=$(echo "$HWINFOHASH" | grep NETWORK_CONTROLLER)
           #;echo $NETWORKCONTROLLER
           IFS='{' read -ra my_array <<< "$NETWORKCONTROLLER"

           #Print the split string
           for i in "${my_array[@]}"
           do
                if grep -q model <<<"$i"; then
                        HWMODEL+=$(echo $(echo "$i" | grep -o -P "model': u'.{0,35}"))";"
                fi
                if grep -q model <<<"$i"; then
                        HWMACS+=$(echo $(echo "$i" | grep -o -P "macAddress': u'.{0,18}"))";"
                fi
           done

           #HWMACS=$(echo ${HWINFOHASH} | grep -o -P "macAddress': u'.{0,17}'" | grep -o '..................$' | rev | grep -o '.................$' | rev)
           # echo $HWMACS
           # check if mac is vaild
           while read -r line; do
             if [ `echo $line | egrep "^([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}$"` ]; then
                     VALIDATEDMACS+=$(echo $line , )
             fi
           done <<< "$HWMACS"
           echo $client "; " $HWSERIAL "; " $COMPUTERSYSTEM "; " $HWMODEL "; " $HWMACS
           HWMODEL=
           HWMACS=

   done

