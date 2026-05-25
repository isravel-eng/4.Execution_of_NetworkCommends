# 4. Execution of Network Commands

## AIM
Use of network commands in real-time environment.

## SOFTWARE REQUIRED
- Command Prompt
- Network Protocol Analyzer
- Python

---

## PROCEDURE

This experiment demonstrates commonly used networking commands.

Commands covered:

- netstat
- ipconfig
- ping
- tracert
- nslookup
- getmac
- hostname
- nbtstat
- arp
- systeminfo

---

## COMMAND DESCRIPTION

| Command | Purpose |
|---|---|
| netstat | Shows active connections |
| ipconfig | Displays IP configuration |
| ping | Tests connectivity |
| tracert | Displays route packets take |
| nslookup | DNS lookup |
| getmac | Shows MAC address |
| hostname | Shows device name |
| nbtstat | Displays NetBIOS statistics |
| arp | Displays ARP table |
| systeminfo | Shows system configuration |

---
##  OUTPUTS - MANUALLY USING COMMAND PROMPT
### ``netstat``

<img width="1378" height="626" alt="image" src="https://github.com/user-attachments/assets/3f9222ab-98bc-49a7-8031-26f9ca73ecc3" />

### ``ipconfig``

<img width="977" height="677" alt="image" src="https://github.com/user-attachments/assets/ae157856-b6e0-4dcb-b62a-642f16d2e3fc" />

### ``ping``

<img width="955" height="301" alt="image" src="https://github.com/user-attachments/assets/5c332317-bb4c-418d-983b-41239378c067" />

### ``tracert``

<img width="835" height="287" alt="image" src="https://github.com/user-attachments/assets/19898b52-88f2-4a59-b031-43dbe696f526" />

### ``nslookup``

<img width="783" height="809" alt="image" src="https://github.com/user-attachments/assets/fbe84e95-d3d6-4a7f-a4dc-def20b1c34ef" />

### ``getmac``

<img width="1013" height="167" alt="image" src="https://github.com/user-attachments/assets/7c0d91bf-97b9-41f7-9304-d2192a959812" />

### ``hostname``

<img width="468" height="68" alt="image" src="https://github.com/user-attachments/assets/d4cdd3f5-0cb8-497b-873b-c5ce83d7c582" />

### ``nbtstat``

<img width="1128" height="626" alt="image" src="https://github.com/user-attachments/assets/cc024499-c2cc-44b7-b328-eba285679da3" />

### ``arp``

<img width="1119" height="790" alt="image" src="https://github.com/user-attachments/assets/8e0e7889-3721-4c26-9706-dd5dcb0bd5c6" />

### ``systeminfo``

<img width="823" height="1033" alt="image" src="https://github.com/user-attachments/assets/bd25e002-ce3c-4b81-a9af-ebbff63f97cb" />

---

## PROGRAM

```python
import os

commands=[
'ipconfig',
'netstat',
'ping google.com',
'tracert google.com',
'nslookup google.com',
'getmac',
'hostname',
'nbtstat',
'arp -a',
'systeminfo'
]

for cmd in commands:
 print('\n'+'='*50)
 print('Executing:',cmd)
 print('='*50)
 os.system(cmd)
```

---


## EXECUTION

```bash
python network_commands.py
```

---

## OUTPUT USING PYTHON PROGRAM THAT ACCESS CMD THROUGH OS MODULE
```
PS C:\CN\4.Execution_of_NetworkCommends> py network_commands.py

============================================================
Executing: ipconfig
============================================================

Windows IP Configuration


Unknown adapter McAfee VPN:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . : 

Wireless LAN adapter Local Area Connection* 3:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . : 

Wireless LAN adapter Local Area Connection* 4:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . : 

Wireless LAN adapter Wi-Fi:

   Connection-specific DNS Suffix  . : saveetha.in
   IPv6 Address. . . . . . . . . . . : 2403:8600:c090:42:0:400:f9:1df6
   Link-local IPv6 Address . . . . . : fe80::4a05:e47d:c9e3:ffc1%11
   Autoconfiguration IPv4 Address. . : 169.254.225.208
   Subnet Mask . . . . . . . . . . . : 255.255.0.0
   Default Gateway . . . . . . . . . : fe80::eedd:24ff:fe3d:ced5%11

============================================================
Executing: netstat
============================================================

Active Connections

  Proto  Local Address          Foreign Address        State
  TCP    127.0.0.1:50208        ISRAVEL:55414          TIME_WAIT
  TCP    127.0.0.1:50208        ISRAVEL:59397          TIME_WAIT
  TCP    127.0.0.1:50208        ISRAVEL:63447          TIME_WAIT
  TCP    127.0.0.1:50208        ISRAVEL:64007          TIME_WAIT
  TCP    127.0.0.1:52081        ISRAVEL:52082          ESTABLISHED
  TCP    127.0.0.1:52082        ISRAVEL:52081          ESTABLISHED
  TCP    127.0.0.1:55413        ISRAVEL:50208          TIME_WAIT
  TCP    127.0.0.1:59396        ISRAVEL:50208          TIME_WAIT
  TCP    127.0.0.1:63446        ISRAVEL:50208          TIME_WAIT
  TCP    127.0.0.1:63988        ISRAVEL:63989          ESTABLISHED
  TCP    127.0.0.1:63989        ISRAVEL:63988          ESTABLISHED
  TCP    127.0.0.1:64006        ISRAVEL:50208          TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:49394  [64:ff9b::acbc:9b19]:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:49671  [2603:1061:10:1::11]:http  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:49706  g2600-140f-0006-0000-0000-0000-17c7-458a:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:49722  [64:ff9b::14cf:4955]:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:50023  [2606:50c0:8001::215]:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:50513  g2600-140f-0006-0000-0000-0000-17c7-4591:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:51255  [64:ff9b::4f7:bce0]:https  TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:51256  [2603:1020:5:12::502]:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:51506  [64:ff9b::14be:91a0]:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:51507  [2603:1020:206:e::6c6]:https  TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:51514  [2603:1061:14:155::1]:https  CLOSE_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:51708  g2600-140f-0006-0000-0000-0000-17c7-4578:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:51791  [2603:1061:10::13]:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:51970  g2600-140f-0006-0000-0000-0000-17c7-4591:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:52043  [64:ff9b::34b6:8fd0]:https  TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:52071  [2600:1901:0:5e8a::]:https  TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:52554  [2620:1ec:33:1::10]:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:53152  [64:ff9b::14bd:ad1a]:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:53154  [2603:1061:14:150::1]:https  TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:53158  [64:ff9b::4f7:bce0]:https  TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:53160  [64:ff9b::4f7:bce0]:https  TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:53163  [2603:1030:210:21::564]:https  TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:53298  [64:ff9b::34b6:8fd0]:https  TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:53516  [2603:1061:14:150::1]:https  TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:53596  [64:ff9b::d6b:55d]:https  TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:53597  [64:ff9b::d6b:55d]:https  TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:53705  cdn-185-199-111-133:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:53766  lb-140-82-112-25-iad:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:53863  [2603:1040:a06:6::1]:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:54547  [2620:1ec:33::12]:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:54833  [2a04:4e42:8e::684]:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:55412  [2603:1046:2000:90::80]:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:55634  [64:ff9b::14bd:ad0a]:https  TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:55685  [64:ff9b::34b6:8fd0]:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:55696  [64:ff9b::3374:f668]:https  CLOSE_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:55710  [64:ff9b::acd7:bce8]:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:55713  [64:ff9b::3374:f668]:https  CLOSE_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:55717  [64:ff9b::3374:f668]:https  CLOSE_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:55718  [64:ff9b::3374:f668]:https  CLOSE_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:55719  [64:ff9b::3374:f668]:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:55720  [64:ff9b::3374:f668]:https  CLOSE_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:55721  [64:ff9b::3374:f668]:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:55722  [64:ff9b::3374:f668]:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:55723  [64:ff9b::3374:f668]:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:55724  [64:ff9b::3374:f668]:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:55725  [64:ff9b::3374:f668]:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:55726  [64:ff9b::3374:f668]:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:55727  [64:ff9b::3374:f668]:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:55728  [64:ff9b::3374:f668]:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:55729  [64:ff9b::3374:f668]:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:55730  [64:ff9b::3374:f668]:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:55731  [64:ff9b::3374:f668]:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:55732  ec2-52-70-120-218:https  TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:55733  ec2-34-206-202-34:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:55734  [64:ff9b::3374:f668]:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:55805  [2603:1061:14:150::1]:https  TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:56693  [2603:1061:10:1::16]:https  TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:57237  g2600-140f-5e00-0014-0000-0000-17d3-3c24:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:57260  [64:ff9b::14bd:ad0a]:https  TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:58259  [2603:1061:14:150::1]:https  TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:58728  [2603:1061:14:150::1]:https  TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:59208  [2620:1ec:33::11]:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:59352  [2606:50c0:8001::154]:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:59558  ec2-34-206-202-34:https  TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:59570  [64:ff9b::14bd:ad0a]:https  TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:59773  [64:ff9b::34b6:8fd0]:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:59846  server-18-161-216-37:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:59919  whatsapp-cdn6-shv-03-maa3:https  TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:59926  [2603:1040:a06:6::1]:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:61445  [64:ff9b::14bd:ad0a]:https  TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:61560  [64:ff9b::14bd:ad0a]:https  TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:62162  [2603:1061:14:150::1]:https  TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:62771  g2600-140f-5e00-0014-0000-0000-17d3-3c29:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:63109  [64:ff9b::d6b:55d]:https  TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:63888  [2603:1061:14:150::1]:https  TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:63889  [64:ff9b::4f7:bce0]:https  TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:63977  [2a06:98c1:310b::ac40:9bd1]:https  TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:63978  [2a06:98c1:310b::ac40:9bd1]:https  TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:63979  [2a06:98c1:310b::ac40:9bd1]:https  TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:63980  [2a06:98c1:310b::ac40:9bd1]:https  TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:63981  [2a06:98c1:310b::ac40:9bd1]:https  TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:63982  [2a06:98c1:310b::ac40:9bd1]:https  TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:63984  [64:ff9b::d6b:55d]:https  TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:63991  ec2-3-111-241-224:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:63996  [2606:4700:4408::ac40:9517]:http  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:63999  [2606:4700:4402::6812:25e4]:https  TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:64001  ec2-52-70-120-218:https  TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:64005  ec2-34-206-202-34:https  TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:64008  [2606:4700:4408::ac40:9517]:http  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:64010  [64:ff9b::d6b:55d]:https  TIME_WAIT
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:64013  [2606:4700:4408::ac40:9517]:http  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:65195  lb-140-82-112-21-iad:https  ESTABLISHED
  TCP    [2403:8600:c090:42:0:400:f9:1df6]:65429  ec2-34-206-202-34:https  TIME_WAIT

============================================================
Executing: ping google.com
============================================================

Pinging google.com [2404:6800:4007:83b::200e] with 32 bytes of data:
Reply from 2404:6800:4007:83b::200e: time=55ms 
Reply from 2404:6800:4007:83b::200e: time=17ms 
Reply from 2404:6800:4007:83b::200e: time=59ms 
Reply from 2404:6800:4007:83b::200e: time=11ms 

Ping statistics for 2404:6800:4007:83b::200e:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 11ms, Maximum = 59ms, Average = 35ms

============================================================
Executing: tracert google.com
============================================================

Tracing route to google.com [2404:6800:4007:83b::200e]
over a maximum of 30 hops:

  1    32 ms    12 ms    11 ms  2403:8600:c090:42::1 
  2     *        *        *     Request timed out.
  3     *        *        *     Request timed out.
  4    81 ms    10 ms    10 ms  lcmaaa-an-in-x0e.1e100.net [2404:6800:4007:83b::200e] 

Trace complete.

============================================================
Executing: nslookup google.com
============================================================
Server:  UnKnown
Address:  2403:8600:c090:42:a000::200

Non-authoritative answer:
Name:    google.com
Addresses:  2404:6800:4007:83b::200e
          172.217.24.14


============================================================
Executing: getmac
============================================================

Physical Address    Transport Name                                            
=================== ==========================================================
DC-56-7B-61-44-43   \Device\Tcpip_{90C6B9AD-4BD0-4F67-86D6-9F93B0B3D730}      
00-FF-E5-6C-31-A2   Media disconnected                                        

============================================================
Executing: hostname
============================================================
ISRAVEL

============================================================
Executing: nbtstat
============================================================

Displays protocol statistics and current TCP/IP connections using NBT
(NetBIOS over TCP/IP).

NBTSTAT [ [-a RemoteName] [-A IP address] [-c] [-n]
        [-r] [-R] [-RR] [-s] [-S] [interval] ]

  -a   (adapter status) Lists the remote machine's name table given its name
  -A   (Adapter status) Lists the remote machine's name table given its
                        IP address.
  -c   (cache)          Lists NBT's cache of remote [machine] names and their IP addresses
  -n   (names)          Lists local NetBIOS names.
  -r   (resolved)       Lists names resolved by broadcast and via WINS
  -R   (Reload)         Purges and reloads the remote cache name table
  -S   (Sessions)       Lists sessions table with the destination IP addresses
  -s   (sessions)       Lists sessions table converting destination IP
                        addresses to computer NETBIOS names.
  -RR  (ReleaseRefresh) Sends Name Release packets to WINS and then, starts Refresh

  RemoteName   Remote host machine name.
  IP address   Dotted decimal representation of the IP address.
  interval     Redisplays selected statistics, pausing interval seconds
               between each display. Press Ctrl+C to stop redisplaying
               statistics.


============================================================
Executing: arp -a
============================================================

Interface: 169.254.225.208 --- 0xb
  Internet Address      Physical Address      Type
  169.254.112.209       e0-2e-0b-7a-bc-e6     dynamic   
  169.254.255.255       ff-ff-ff-ff-ff-ff     static    
  224.0.0.22            01-00-5e-00-00-16     static    
  224.0.0.251           01-00-5e-00-00-fb     static    
  224.0.0.252           01-00-5e-00-00-fc     static    
  224.0.1.60            01-00-5e-00-01-3c     static    
  224.77.77.77          01-00-5e-4d-4d-4d     static    
  239.192.152.143       01-00-5e-40-98-8f     static    
  239.255.102.18        01-00-5e-7f-66-12     static    
  239.255.255.250       01-00-5e-7f-ff-fa     static    
  255.255.255.255       ff-ff-ff-ff-ff-ff     static    

============================================================
Executing: systeminfo
============================================================
                                                                              
Host Name:                     ISRAVEL
OS Name:                       Microsoft Windows 11 Home Single Language
OS Version:                    10.0.26200 N/A Build 26200
OS Manufacturer:               Microsoft Corporation
OS Configuration:              Standalone Workstation
OS Build Type:                 Multiprocessor Free
Registered Owner:              N/A
Registered Organization:       N/A
Product ID:                    00356-24816-88583-AAOEM
Original Install Date:         05-05-2026, 10:34:34 PM
System Boot Time:              17-05-2026, 06:09:33 PM
System Manufacturer:           Dell Inc.
System Model:                  Inspiron 15 3530
System Type:                   x64-based PC
Processor(s):                  1 Processor(s) Installed.
                               [01]: Intel64 Family 6 Model 186 Stepping 3 GenuineIntel ~1600 Mhz
BIOS Version:                  Dell Inc. 1.30.0, 23-03-2026
Windows Directory:             C:\WINDOWS
System Directory:              C:\WINDOWS\system32
Boot Device:                   \Device\HarddiskVolume1
System Locale:                 en-us;English (United States)
Input Locale:                  00004009
Time Zone:                     (UTC+05:30) Chennai, Kolkata, Mumbai, New Delhi
Total Physical Memory:         7,877 MB
Available Physical Memory:     1,149 MB
Virtual Memory: Max Size:      18,629 MB
Virtual Memory: Available:     4,187 MB
Virtual Memory: In Use:        14,442 MB
Page File Location(s):         C:\pagefile.sys
Domain:                        WORKGROUP
Logon Server:                  \\ISRAVEL
Hotfix(s):                     6 Hotfix(s) Installed.
                               [01]: KB5087051
                               [02]: KB5050575
                               [03]: KB5054156
                               [04]: KB5059093
                               [05]: KB5089549
                               [06]: KB5092762
Network Card(s):               2 NIC(s) Installed.
                               [01]: Realtek RTL8852BE WiFi 6 802.11ax PCIe Adapter
                                     Connection Name: Wi-Fi
                                     DHCP Enabled:    Yes
                                     DHCP Server:     255.255.255.255
                                     IP address(es)
                                     [01]: 169.254.225.208
                                     [02]: fe80::4a05:e47d:c9e3:ffc1
                                     [03]: 2403:8600:c090:42:0:400:f9:1df6
                               [02]: TAP-Windows Adapter V9
                                     Connection Name: McAfee VPN
                                     Status:          Media disconnected
Virtualization-based security: Status: Running
                               Required Security Properties:
                                     Base Virtualization Support
                               Available Security Properties:
                                     Base Virtualization Support
                                     Secure Boot
                                     DMA Protection
                                     UEFI Code Readonly
                                     SMM Security Mitigations 1.0
                                     Mode Based Execution Control
                                     APIC Virtualization
                               Services Configured:
                                     Hypervisor enforced Code Integrity
                               Services Running:
                                     Hypervisor enforced Code Integrity
                               App Control for Business policy: Enforced
                               App Control for Business user mode policy: Off
                               Security Features Enabled:
Hyper-V Requirements:          A hypervisor has been detected. Features required for Hyper-V will not be displayed.
PS C:\CN\4.Execution_of_NetworkCommends> 
```
---

## RESULT
Thus execution of network commands was performed successfully.
