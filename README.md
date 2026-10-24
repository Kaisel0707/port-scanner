# Port Scanner

A fast TCP port scanner written in Python using the `socket` module and threads. It checks a range of ports on a host and reports which ones are open, along with the standard service name.

## Legal notice

Only scan machines you own or have **written permission** to test. Unauthorized port scanning may be illegal.

## Features

- Choose the host to scan (press Enter to scan your own computer, `127.0.0.1`)
- Scan any port range from 1 to 65535
- Shows the service name for each open port (for example `epmap`, `microsoft-ds`)
- Input validation: rejects letters and invalid ranges, then asks again
- Counts and reports the open ports found
- Uses a timeout so closed ports don't block the scan
- Fast scanning with 100 threads (1000 ports in about 10 seconds)

## How to run

1. Install Python 3
2. Download `port_scanner.py`
3. Run it: `python port_scanner.py`
4. Enter a host (or press Enter), then a start port and an end port

## Example output

```
Host to scan (Enter for 127.0.0.1):
start port: 1
end port: 1000
port 135 is open (epmap)
port 445 is open (microsoft-ds)
Open ports found: 2
```

## How it works

1. The ports are checked by a pool of 100 worker threads at the same time
2. `connect_ex()` tries to connect. A result of `0` means the port is open
3. `socket.getservbyport()` looks up the service name, with `unknown` as a fallback
4. The program prints each open port and the total at the end

## Limitations

This is a learning project:

- TCP connect scan only, with no banner grabbing or service detection
- Service names come from the standard port list, not from what is really running
- Always uses 100 threads and a 1-second timeout, with no option to change them

## Planned improvements

- Command-line arguments with `argparse`
- Save results to a file
- Banner grabbing

## What I learned

Sockets, `connect_ex`, loops, `try/except`, input validation, threads with `ThreadPoolExecutor`, and responsible scanning.
