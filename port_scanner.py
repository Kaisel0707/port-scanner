import socket
host = input("Host to scan (Enter for 127.0.0.1): ")
if host == "":
    host = "127.0.0.1"
while True:
    try:
        start = int(input("start port: "))
        end = int(input("end port: "))
        if start < 1 or end > 65535 or start > end:
            print("invalid port range")
        else:
            break
    except ValueError:
        print("please enter a number")
found = 0
for port in range(start, end + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((host, port))
    if result == 0:
        try:
            name = socket.getservbyport(port)
        except OSError:
            name = "unknown"
        found += 1
        print(f"port {port} is open ({name})")
    s.close()
print("Open ports found:", found)
