import socket
import requests
import nmap
from colorama import Fore, Style
from urllib.parse import urlparse

scorpion_art = '''
             __/ \\
            /   O   \\
           /     O    \\
          /            \\
         /    (    )    \\
        /    /      \\    \\
       /    |        |    \\
      /     |        |     \\
     /     /|        |\\     \\
     \\____/ |________| \\_____/
           /          \\
          /            \\
         /              \\
'''

print(Fore.GREEN + scorpion_art, Style.RESET_ALL)
print(Fore.RED + "              Created by KhalidAch!", Style.RESET_ALL)




print()
print()
print()

def main():
    url_input = input("Enter target URL: ")
    print()
    print("________________________________________________")
    print()
    parsed_url = urlparse(url_input)

    if not parsed_url.scheme or not parsed_url.netloc:
        print("Invalid URL format. Please provide a valid URL with scheme (e.g., http://) and hostname.")
        return

    hostname = parsed_url.netloc
    scheme = parsed_url.scheme
    complete_url = f"{scheme}://{hostname}"

    try:
        response = requests.get(complete_url)
        server = socket.gethostbyname(hostname)
        print(Fore.GREEN + "[+]", Style.RESET_ALL,  "Response status code:", response.status_code, response.reason)
        print(Fore.GREEN + "[+]", Style.RESET_ALL,  "Server IP:", server)
        
        np = nmap.PortScanner()
        np.scan(server, arguments="-sV -T5")
        
        # Print scan results
        for host in np.all_hosts():
            for proto in np[host].all_protocols():
                print()
                print("________________________________________________")
                print()
                print(f"{Fore.GREEN}[+] {Style.RESET_ALL} Open ports:")
                print()
                ports = np[host][proto].items()
                for port, port_info in ports:
                    state = port_info.get('state', 'Unknown')
                    service = port_info.get('name', 'Unknown')
                    method = port_info.get('method', 'Unknown')
                    print(f"{Fore.BLUE}[*] {Style.RESET_ALL}Port: {port}\tState: {state}\tService: {service}\tMethod: {method}")
                    # Reset color
                    print(Style.RESET_ALL)

    except socket.gaierror as gai_err:
        print("Invalid hostname:", gai_err)
    except requests.exceptions.RequestException:
        print("Request error occurred:")

main()

