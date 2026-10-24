# Port Scanner

A fast, configurable TCP port scanner written in Python using the `socket` module, threads and `argparse`. It checks a range of ports on a host and reports which ones are open, along with the standard service name.

There are two versions:

- `port_scanner_cli.py`: runs from the command line with arguments and optional flags
- `port_scanner.py`: interactive version that asks questions

## Legal notice

Only scan machines you own or have **written permission** to test. Unauthorized port scanning may be illegal.

## Features

- Choose the host to scan (command-line version: any host; interactive version: press Enter for `127.0.0.1`)
- Scan any port range from 1 to 65535
- Shows the service name for each open port (for example `epmap`, `microsoft-ds`)
- Input validation with clear error messages
- Counts and reports the open ports found
- Fast scanning with threads (1000 ports in about 10 seconds by default)
- Optional `--timeout` and `--threads` flags with sensible defaults
- Built-in `--help` screen (command-line version)

## How to run

1. Install Python 3
2. Download `port_scanner_cli.py`
3. Run it from Command Prompt or a terminal:

```
python port_scanner_cli.py 127.0.0.1 1 1000
```

The arguments are: host, first port, last port.

Optional flags:

```
python port_scanner_cli.py 127.0.0.1 1 1000 --threads 500 --timeout 0.5
```

| Flag | Meaning | Default |
|---|---|---|
| `--threads` | number of worker threads | 100 |
| `--timeout` | seconds to wait per port | 1.0 |

To see the help screen:

```
python port_scanner_cli.py --help
```

For the interactive version, run `python port_scanner.py` and answer the prompts.

## Example output

```
> python port_scanner_cli.py 127.0.0.1 1 1000
port 135 is open (epmap)
port 445 is open (microsoft-ds)
Open ports found: 2
```

Invalid input gives a clean error:

```
> python port_scanner_cli.py 127.0.0.1 1 1000 --threads 0
usage: port_scanner_cli.py [-h] [--timeout TIMEOUT] [--threads THREADS] host start end
port_scanner_cli.py: error: timeout must be above 0 and threads at least 1
```

## How it works

1. `argparse` reads the host, the port range and the optional flags
2. The ports are checked by a pool of worker threads at the same time
3. `connect_ex()` tries to connect. A result of `0` means the port is open
4. `socket.getservbyport()` looks up the service name, with `unknown` as a fallback
5. The program prints each open port and the total at the end

## Limitations

This is a learning project:

- TCP connect scan only, with no banner grabbing or service detection
- Service names come from the standard port list, not from what is really running
- Results are printed only, not saved

## Planned improvements

- Save results to a file (JSON or CSV)
- Banner grabbing

## What I learned

Sockets, `connect_ex`, loops, `try/except`, input validation, threads with `ThreadPoolExecutor`, command-line arguments with `argparse`, optional flags with defaults, and responsible scanning.
