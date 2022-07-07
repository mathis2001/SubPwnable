# SubPwnable

Are your subdomains pwnable? SubPwnable is a simple Python tool designed to help you answer this question by finding your inactive subdomains and looking up their CNAME records. Then you will need to check on https://github.com/EdOverflow/can-i-take-over-xyz if the service used in this record is vulnerable.

## Install:
```bash
$ git clone https://github.com/mathis2001/SubPwnable

$ cd SubPwnable

$ python3 subpwnable.py
```
## Requirements:

- Python3

- Pip3

- dns.resolver

- requests


## Usage:
```bash
usage: ./subpwnable.py [-h] [-d domain] [-l domains list]
```
## options:
```bash
optional arguments:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN   Target a single domain
  -l DOMAIN LIST, --list DOMAIN LIST   Target a list of domains

```

## Screens:
