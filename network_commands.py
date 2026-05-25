import os

commands = [
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
    print('\n' + '='*60)
    print('Executing:', cmd)
    print('='*60)
    os.system(cmd)
