# Port Scanner

A simple TCP port scanner in Python using the `socket` module. It checks a range of ports on a host and reports which ones are open.

## Legal notice

Only scan machines you own or have **written permission** to test. Unauthorized scanning may be illegal.

## Features

- Scans any port range from 1 to 65535
- Input validation: rejects letters and invalid ranges, then asks again
- Counts and reports the open ports found
- Uses a timeout so closed ports don't block the scan

## How to run

1. Install Python 3
2. Run `python port_scanner.py`
3. Enter a start port and an end port

The scanner targets `127.0.0.1` (your own computer) by default.

## Example output

```
start port: 130
end port: 140
port 135 is open
Open ports found: 1
```

## Limitations

- Scans one port at a time, so large ranges are slow
- TCP connect scan only, with no service detection
- The host is fixed in the code

## What I learned

Sockets, `connect_ex`, loops, `try/except`, input validation.
