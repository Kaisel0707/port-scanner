import socket
from concurrent.futures import ThreadPoolExecutor
def check_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((host, port))
    s.close()
    return result == 0
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
ports = list(range(start, end + 1))
with ThreadPoolExecutor(max_workers=100) as ex:
    results = list(ex.map(lambda p: check_port(host, p), ports))
found = 0
for port, is_open in zip(ports, results):
    if is_open:
        try:
            name = socket.getservbyport(port)
        except OSError:
            name = "unknown"
        found += 1
        print(f"port {port} is open ({name})")
print("Open ports found:", found)
