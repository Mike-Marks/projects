import nmap

# PS: you've got many other ways to scam a network using nmap, use the real nmap for more scanning options :)
def scan_target(target, ports='1-1024'):
    scanner = nmap.PortScanner()
    print(f"Scanning {target} for ports {ports}...\n")

    try:
        scanner.scan(hosts=target, ports=ports, arguments='-sV')  # -sV for service detection

        for host in scanner.all_hosts():
            print(f"Host: {host} ({scanner[host].hostname()})")
            print(f"State: {scanner[host].state()}")

            for proto in scanner[host].all_protocols():
                print(f"\nProtocol: {proto}")
                ports = scanner[host][proto].keys()
                for port in sorted(ports):
                    state = scanner[host][proto][port]['state']
                    name = scanner[host][proto][port].get('name', '')
                    product = scanner[host][proto][port].get('product', '')
                    version = scanner[host][proto][port].get('version', '')
                    print(f"Port: {port}\tState: {state}\tService: {name} {product} {version}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    target_ip = input("Enter target IP or hostname: ")
    port_range = input("Enter port range (e.g., 22,80,443 or 1-1024): ")
    scan_target(target_ip, port_range)

# Usage Example
# $ python3 nmap_scanner.py
# Enter target IP or hostname: scanme.nmap.org
# Enter port range (e.g., 22,80,443 or 1-1024): 22,80,443