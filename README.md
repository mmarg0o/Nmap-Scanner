#Nmap Scanner#
A small, easy to use Python wrapper around nmap for quick port scanning practice.
It scans a target and saves results to a CSV file.

##Features##
Simple interactive CLI using input()
Scans a port range (default 1-1024)
Saves scan results to a CSV (host, proto, port, state)

##Requirements##
Python 3.7+
Nmap installed on the system (the nmap executable must be available).

Python packages:
python-nmap (wrapper for Nmap)
pyfiglet (optional, for the ASCII banner)

Install Python packages with:
pip install python-nmap pyfiglet

Install Nmap:
On Debian/Ubuntu: sudo apt install nmap
On macOS (Homebrew): brew install nmap
On Windows: use the official installer from nmap.org
