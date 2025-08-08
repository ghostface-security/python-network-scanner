import socket
import argparse
import ipaddress
from concurrent.futures import ThreadPoolExecutor

def scan_host(host, ports, timeout):
    """
    Scans a single host for a list of open ports and grabs service banners.
    Returns a dictionary of open ports and banners.
    """
    open_ports = {}
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(timeout)
                s.connect((host, port))
                
                # Grab banner (what service is running?)
                s.sendall(b'GET / HTTP/1.1\r\n\r\n')
                banner = s.recv(1024).decode(errors='ignore').strip().split('\n')[0]
                
                open_ports[port] = banner if banner else "Unknown"
        except (socket.error, OverflowError):
            continue
    return {host: open_ports}

def net_scan(hosts_to_scan, ports, threads, timeout):
    """
    Orchestrates the network scan using a ThreadPoolExecutor for performance.
    """
    print(f"Scanning network for hosts with open ports {ports}...")
    
    scan_results = {}
    
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {executor.submit(scan_host, host, ports, timeout): host for host in hosts_to_scan}
        
        for future in futures:
            result = future.result()
            scan_results.update(result)
            
    print("\nScan complete.")
    return scan_results

def main():
    parser = argparse.ArgumentParser(description="A multi-threaded network scanner.")
    parser.add_argument("network", help="Network address to scan (e.g., 192.168.1.0)")
    parser.add_argument("mask", help="Subnet mask in CIDR notation (e.g., /24)")
    parser.add_argument("ports", help="Port or port range to scan (e.g., 80 or 80-100)")
    parser.add_argument("-t", "--threads", type=int, default=50, help="Number of threads to use for scanning (default: 50)")
    parser.add_argument("-o", "--output", help="Save results to a file (e.g., results.txt)")
    args = parser.parse_args()
    
    # Parse the port argument
    if '-' in args.ports:
        start_port, end_port = map(int, args.ports.split('-'))
        ports_to_scan = range(start_port, end_port + 1)
    else:
        ports_to_scan = [int(args.ports)]

    try:
        network_with_mask = f"{args.network}{args.mask}"
        hosts = list(ipaddress.ip_network(network_with_mask).hosts())
        
        scan_results = net_scan(hosts, ports_to_scan, args.threads, 2)

        # Print to console
        print(f"\nScan results for {network_with_mask}:")
        for host, ports in scan_results.items():
            if ports:
                print(f"Host: {host}")
                for port, banner in ports.items():
                    print(f"  - Port {port} is open ({banner})")
        
        # Save to file if specified
        if args.output:
            with open(args.output, 'w') as f:
                for host, ports in scan_results.items():
                    if ports:
                        f.write(f"Host: {host}\n")
                        for port, banner in ports.items():
                            f.write(f"  - Port {port} is open ({banner})\n")
            print(f"\nResults saved to {args.output}")

    except ValueError:
        print("Invalid network address or mask provided. Please use a format like '192.168.1.0' and '/24'.")
    except IndexError:
        print("Please provide a network address, subnet mask, and port.")

if __name__ == "__main__":
    main()
