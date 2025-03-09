import socket
import nmap

def scan_ports(target):
    try:
        scanner = nmap.PortScanner()
    except nmap.PortScannerError:
        print("[-] Nmap is not installed or not found. Please install it first.")
        return

    try:
        scanner.scan(hosts=target, arguments='-p 1-1000 -sV')  # More reliable scan
        if not scanner.all_hosts():
            print("[-] No hosts found. Ensure the target is online.")
            return

        for host in scanner.all_hosts():
            print(f"Scanning {host}...")
            for proto in scanner[host].all_protocols():
                ports = scanner[host][proto].keys()
                for port in ports:
                    service = scanner[host][proto][port].get('name', 'unknown')
                    print(f"[+] Port {port} ({service}) is open.")
    except Exception as e:
        print(f"[-] Error scanning target: {e}")

def banner_grabbing(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)  # Prevents hanging
        s.connect((ip, port))

        # Different ports require different initial requests
        if port == 80 or port == 443:  # HTTP/HTTPS
            s.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
        else:
            s.send(b'Hello\r\n')

        banner = s.recv(1024).decode(errors='ignore').strip()
        print(f"[+] Banner for {ip}:{port} - {banner}")
        s.close()
    except Exception as e:
        print(f"[-] Could not grab banner for {ip}:{port} - {e}")

if __name__ == "__main__":
    target_ip = input("Enter the target IP: ")

    # Validate IP
    try:
        socket.inet_aton(target_ip)
    except socket.error:
        print("[-] Invalid IP address.")
        exit()

    scan_ports(target_ip)

    common_ports = [21, 22, 25, 80, 110, 443]  # Try common ports
    for port in common_ports:
        banner_grabbing(target_ip, port)
