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

## EXECUTION

```bash
python network_commands.py
```

---

## SAMPLE OUTPUT

Executing: ipconfig

Executing: netstat

Executing: ping google.com

Executing: tracert google.com

Executing: nslookup google.com

Executing: getmac

Executing: hostname

Executing: nbtstat

Executing: arp -a

Executing: systeminfo

---

## RESULT
Thus execution of network commands was performed successfully.
