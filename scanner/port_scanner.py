import socket

def scan_port(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((target, port))

            if result == 0:
                print(f"Port {port}: OPEN")
            else:
                print(f"Port {port}: CLOSED")

    except OSError as error:
        print("Error:", error)


if __name__ == "__main__":
    target = "127.0.0.1"

    for port in [22, 80, 443, 3306]:
        scan_port(target, port)
