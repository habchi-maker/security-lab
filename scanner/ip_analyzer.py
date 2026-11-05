import ipaddress

def analyze_ip(ip):
    try:
        address = ipaddress.ip_address(ip)

        print("IP address:", address)
        print("IP version:", address.version)
        print("Private IP:", address.is_private)
        print("Loopback:", address.is_loopback)

    except ValueError:
        print("Invalid IP address!")


if __name__ == "__main__":
    analyze_ip("192.168.1.10")
