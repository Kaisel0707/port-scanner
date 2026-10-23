# Port Scanner

A simple TCP port scanner written in Python using the `socket` module. It checks a range of ports on a host and reports which ones are open, along with the standard service name.

## Legal notice

Only scan machines you own or have **written permission** to test. Unauthorized port scanning may be illegal.

## Features

- Choose the host to scan (press Enter to scan your own computer, `127.0.0.1`)
- Scan any port range from 1 to 65535
- Shows the service name for each open port (for example `epmap`, `microsoft-ds`)
- Input validation: rejects letters and invalid ranges, then asks again
- Counts and reports the open ports found
- Uses a timeout so closed ports don't block the scan

## How to run

1. Install Python 3
2. Download `port_scanner.py`
3. Run it: `python port_scanner.py`
4. Enter a host (or press Enter), then a start port and an end port

## Example output

```
Host to scan (Enter for 127.0.0.1):
start port: 130
end port: 140
port 135 is open (epmap)
Open ports found: 1
```

## How it works

1. For each port in the range, the program creates a TCP socket with a 1-second timeout
2. `connect_ex()` tries to connect. A result of `0` means the
