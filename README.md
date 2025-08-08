# Network Scanner
A powerful and flexible command-line network scanner built in Python. This tool has been upgraded with multi-threaded performance, making it significantly faster and more efficient at identifying active hosts and open ports on a custom network.
Features
 * Multi-threaded Performance: Scans multiple hosts simultaneously using a configurable number of threads, drastically reducing the total scan time for large networks.
 * Flexible Scanning: Scan any network and subnet by providing the network address and CIDR mask (e.g., 192.168.1.0/24).
 * Port Range Scanning: Scan a single port or a range of ports (e.g., 22-100) to find a variety of services.
 * Service Detection: Attempts to grab a service's banner on open ports to identify what is running.
 * Configurable Threads: Customize the number of threads to control scan speed and resource usage.
 * File Output: Save scan results to a text file for later review.
How to Use
The scanner is a command-line tool that requires three primary arguments: the network address, the subnet mask, and the port or port range to scan.
Prerequisites
You need to have Python 3 installed on your system. All modules used are part of Python's standard library.
Running the Script
Open your terminal or command prompt, navigate to the directory where you saved the script, and run the following command. The optional arguments are shown in brackets [].
python scanner.py [network_address] [subnet_mask] [port_number_or_range] [-t threads] [-o output_file]

Example 1: Basic Scan
To scan the 192.168.1.0/24 network for open port 80:
python scanner.py 192.168.1.0 /24 80

Example 2: Advanced Scan
To scan the 10.0.0.0/8 network for a range of ports from 20 to 25, using 100 threads, and saving the output to a file named results.txt:
python scanner.py 10.0.0.0 /8 20-25 -t 100 -o results.txt

