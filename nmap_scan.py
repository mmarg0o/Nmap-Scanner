import nmap
import csv
from colorama import init, Fore
import pyfiglet

init(autoreset=True)

print(pyfiglet.figlet_format("Nmap Scanner", font="big"))

def simple_scan(target, ports="1-1024", filename="report.csv"):
    nm = nmap.PortScanner()
    nm.scan(target, ports)
    rows =[]
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            for port in nm[host][proto].keys():
                state = nm[host][proto][port]['state']
                rows.append([host, proto, port, state])

    if rows:
        for r in rows:
            print(f"{r[0]:15} {r[1]:5} {r[2]:5} {r[3]}")
    else:
        print(Fore.RED + "Nothing found (is host avalible? roots? port range?)")
    
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["host", "proto", "port", "state"])
        writer.writerow(rows)
    print(Fore.LIGHTGREEN_EX + f"Saved to {filename}")

if __name__ == "__main__":
    target = input(Fore.LIGHTBLACK_EX + "IP or domen (for example 192.168.1.1): ").strip()
    ports = input(Fore.LIGHTBLACK_EX + "Ports range (by default 1-1024): ").strip() or "1-1024"
    out = input(Fore.LIGHTBLACK_EX + "CSV name (by default report.csv): ").strip() or "report.csv"
    simple_scan(target, ports, out)