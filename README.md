# pyCrclient

A Cyberoam VPN client written in python3.7 that allows establishing secure connections (using username and password) over the Internet between a remote user and the Corporate Intranet.

## Requirements
- Install `python3` and `python3-venv` on host

## How to use
- Clone this repo
```shell
git clone https://github.com/j4w3d/pyCrclient.git
```
- Create a new virtual environment 
```shell
cd pyCrclient

# create venv
python3 -m venv venv

```

- Install requirements
```shell
venv/bin/pip install -r requirements.txt
```

- Run auto_login.py
```shell
venv/bin/python auto_login.py
```

## TODO:
- Daemonize the auto_login
