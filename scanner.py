import socket
import argparse
import ipaddress

def net_scan(hosts_to_scan, port, timeout=5):
    """
    Scans a list of hosts for a specified open port.
    """
    active_hosts = []
    print(f"Scanning network for hosts with open port {port}...")
    
    for ip_address in hosts_to_scan:
        try:
            # The 'with' statement automatically handles closing the socket
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(timeout)
                s.connect((str(ip_address), port))
                print(f"✅ {ip_address} is active")
                active_hosts.append(str(ip_address))
        except (socket.error, OverflowError):
            pass  # Pass silently if the host is not active or unreachable
            
    print("\nScan complete.")
    return active_hosts

def main():
    parser = argparse.ArgumentParser(description="Scan a specific network for hosts connected to a port.")
    parser.add_argument("network", help="Network address to scan (e.g., 192.168.1.0)")
    parser.add_argument("mask", help="Subnet mask in CIDR notation (e.g., /24)")
    parser.add_argument("port", type=int, help="Target port to test connections.")
    args = parser.parse_args()

    try:
        network_with_mask = f"{args.network}{args.mask}"
        hosts = ipaddress.ip_network(network_with_mask).hosts()
        
        active_hosts = net_scan(hosts, args.port)

        if active_hosts:
            print(f"\nActive hosts found on {network_with_mask}:")
            for host in active_hosts:
                print(f"- {host}")
        else:
            print(f"\nNo active hosts found on {network_with_mask}.")

    except ValueError:
        print("Invalid network address or mask provided. Please use a format like '192.168.1.0' and '/24'.")
    except IndexError:
        print("Please provide a network address, subnet mask, and port.")

if __name__ == "__main__":
    main()
