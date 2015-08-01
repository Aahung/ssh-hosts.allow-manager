
# SSH hosts.allow Manager

## Intro
Add ip with sshd access for 3 hours to `hosts.allow`

## Usage

### First grand permission
```sh
chmod u=rwx,go=xr,+s main.py
```
### Add IP with Account
```sh
/path/to/here/main.py -a Account -i IP-Address
```
Account does not matter

### Run scan and clean with crontab
```sh
/path/to/here/main.py
```
