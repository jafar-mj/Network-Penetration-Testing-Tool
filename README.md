# Network-Penetration-Testing-Tool

# Port Scanning & Service Enumeration

This Python tool performs network reconnaissance by scanning open ports, identifying services, and extracting banner information. It helps penetration testers understand potential attack surfaces on a target system.

🚀 Features:
✅ Scans open ports (1-1000) using Nmap
✅ Identifies running services on detected ports
✅ Performs banner grabbing for further analysis

🛠 Tools & Libraries: nmap, socket

### HOW TOOL WORK OUTPUT #### 
──(kali㉿kali)-[~/Network-Penetration-Testing-Tool]
└─$ python Script.py 
Enter the target IP: 192.168.217.159
Scanning 192.168.217.159...
[+] Port 21 (ftp) is open.
[+] Port 22 (ssh) is open.
[+] Port 23 (telnet) is open.
[+] Port 25 (smtp) is open.
[+] Port 53 (domain) is open.
[+] Port 80 (http) is open.
[+] Port 111 (rpcbind) is open.
[+] Port 139 (netbios-ssn) is open.
[+] Port 445 (netbios-ssn) is open.
[+] Port 512 (exec) is open.
[+] Port 513 (login) is open.
[+] Port 514 (tcpwrapped) is open.
[+] Banner for 192.168.217.159:21 - 220 (vsFTPd 2.3.4)
[+] Banner for 192.168.217.159:22 - SSH-2.0-OpenSSH_4.7p1 Debian-8ubuntu1
[+] Banner for 192.168.217.159:25 - 220 metasploitable.localdomain ESMTP Postfix (Ubuntu)
[+] Banner for 192.168.217.159:80 - HTTP/1.1 200 OK
Date: Sun, 09 Mar 2025 09:35:32 GMT
Server: Apache/2.2.8 (Ubuntu) DAV/2
X-Powered-By: PHP/5.2.4-2ubuntu5.10
Content-Length: 891
Content-Type: text/html

