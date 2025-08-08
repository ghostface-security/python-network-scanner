# Network Scanner
A simple, fast, and flexible command-line tool for scanning a network for active hosts on a specific port. This script is built using Python's standard socket and ipaddress libraries, making it lightweight and easy to use.
Features
 * Flexible Scanning: Scan any network and subnet by providing the network address and CIDR mask (e.g., 192.168.1.0/24).
 * Targeted Port Scan: Check for a specific open port on all hosts within the defined network.
 * Clear Output: Provides real-time feedback on active hosts found and a final summary.
 * Built-in Error Handling: Gracefully handles invalid network addresses or subnet masks.
How to Use
The scanner is a command-line tool that requires three arguments: the network address, the subnet mask, and the port to scan.
Prerequisites
You need to have Python 3 installed on your system. No other external libraries are required as this tool uses built-in Python modules.
Running the Script
Open your terminal or command prompt, navigate to the directory where you saved the script, and run the following command, replacing the placeholders with your desired values:
python scanner.py [network_address] [subnet_mask] [port_number]

Example
To scan the 192.168.1.0/24 network for open port 80 (the standard HTTP port), you would run:
python scanner.py 192.168.1.0 /24 80

The script will then iterate through all IP addresses in that range and report which ones are active on that port.
