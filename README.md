# Port Scanner

A fast, configurable TCP port scanner written in Python using the `socket` module, threads and `argparse`. It checks a range of ports on a host, reports which ones are open, shows the standard service name, and can optionally read each service's banner.

There are two versions:

- `port_scanner_cli.py`: runs from the command line with arguments and optional flags
- `port_scanner.py`: interactive version that asks questions

## Legal notice

Only scan machines you own or have **written permission** to test. Unauthorized port scanning may be illegal.

## Features

- Choose the host to scan (command-line version: any host; interactive version: press Enter for `127.0.0.1`)
- Scan any port range from 1 to 65535
- Shows the service name for each open port (for example `epmap`, `microsoft-ds`)
- Optional banner grabbing with `--banner`
- Fast scanning with threads (1000 ports in about 10 seconds by default)
- Optional `--timeout` and `--threads` flags with sensible defaults
- Input validation with clear error messages
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
python port_scanner_cli.py 127.0.0.1 1 1000 --threads 500 --timeout 0.5 --banner
```

| Flag | Meaning | Default |
|---|---|---|
| `--threads` | number of worker threads | 100 |
| `--timeout` | seconds to wait per port | 1.0 |
| `--banner` | try to read a banner from each open port | off |

To see the help screen:

```
python port_scanner_cli.py --help
```

For the interactive version, run `python port_scanner.py` and answer the prompts.

## Testing banner grabbing safely

`fake_server.py` starts a harmless fake service on your own computer (port 2222) that sends an SSH-style greeting.

1. In one window: `python fake_server.py`
2. In another window: `python port_scanner_cli.py 127.0.0.1 2200 2500 --banner`

## Example output

```
> python port_scanner_cli.py 127.0.0.1 1 1000
port 135 is open (epmap)
port 445 is open (microsoft-ds)
Open ports found: 2
```

With a banner:

```
> python port_scanner_cli.py 127.0.0.1 2200 2500 --banner
port 2222 is open (unknown) banner: SSH-2.0-FakeServer_1.0
Open ports found: 1
```

Invalid input gives a clean error:

```
> python port_scanner_cli.py 127.0.0.1 1 1000 --threads 0
port_scanner_cli.py: error: timeout must be above 0 and threads at least 1
```

## How it works

1. `argparse` reads the host, the port range and the optional flags
2. The ports are checked by a pool of worker threads at the same time
3. `connect_ex()` tries to connect. A result of `0` means the port is open
4. `socket.getservbyport()` looks up the service name, with `unknown` as a fallback
5. With `--banner`, the scanner connects again and reads up to 1024 bytes with `recv()`
6. The program prints each open port and the total at the end

## Limitations

This is a learning project:

- TCP connect scan only, with no service or version detection
- Banners only appear for services that greet first (
