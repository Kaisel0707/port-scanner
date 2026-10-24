import socket
import argparse
from concurrent.futures import ThreadPoolExecutor
def check_port(host, port, timeout):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    result = s.connect_ex((host, port))
    s.close()
    return result == 0
parser = argparse.ArgumentParser(description="simple threaded TCP port scanner")
parser.add_argument("host", help="host to scan, e.g, 127.0.0.1")
parser.add_argument("start", type=int, help="first port")
parser.add_argument("end", type=int, help="last port")
parser.add_argument("--timeout", type=float, default=1.0, help="seconds to wait per port(default 1.0)")
parser.add_argument("--threads", type=int, default=100, help="number of worker threads (default 100)") 
args = parser.parse_args()
host = args.host
start = args.start
end = args.end
if start < 1 or end > 65535 or start > end:
    parser.error("invalid port range")
ports = list(range(start, end + 1))
if args.timeout <= 0 or args.threads < 1:
    parser.error("timeout must be above 0 and threads at least 1")
with ThreadPoolExecutor(max_workers=args.threads) as ex:
    results = list(ex.map(lambda p: check_port(host, p, args.timeout), ports))
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
