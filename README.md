# bash-teska-inventory
1. copy to opsi server \\backup\opsi_workbench
2. open ssh and go to /home/opsiproducts
3. start with python inventory.py > output.txt
4. look in output.txt for info

If you install hwaudit, macs of wireless adapter will be found too...

Computername;Hardware Type; Serialnumber; found Networkcontroller incl. MACS

output looks like this
```
r27-pc01.paedml-linux.lokal;HP ProDesk 400 G5 Desktop Mini (9LB73ES#ABD);8xxxxxPHK;RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller;38:xx:xx3:c7:95;
lpc-008.paedml-linux.lokal;LIFEBOOK A359 (SK00);EIBxxxx369;Wireless 7265;;RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller;68:84:xx:60:xx:6e;
r27-pclehrer.paedml-linux.lokal;HP ProDesk 400 G5 Desktop Mini (9LB73ES#ABD);8CCxxxxJ;RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller;xx:22:e2:x:xx:23;
lpc-005.paedml-linux.lokal;LIFEBOOK A359 (SK00);Exxxx;Wireless 7265;;RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller;68:84:7e:x0:xx:xx;
lpc-001.paedml-linux.lokal;LIFEBOOK A359 (SK00);EIBDxxxxx8;Wireless 7265;;RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller;68:84:xx:xx:8d:xx;
r27-pc11.paedml-linux.lokal;HP ProDesk 400 G5 Desktop Mini (9LB73ES#ABD);8CCxxxxG;RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller;38:22:e2:xx:xx:xx;
a357-02.paedml-linux.lokal;LIFEBOOK A357;Yxxxx26;RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller;a0:66:10:xx7:xx:xx;Wireless 7265;;
```
