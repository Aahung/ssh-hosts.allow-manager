
# SSH hosts.allow Manager

## Intro
Add ip with sshd access for 3 hours to `hosts.allow`

## Usage

### First install
```sh
./build.py
```
### Add IP with Account
```sh
/path/to/here/ssh-hosts.allow-manager -a Account -i IP-Address
```
Account does not matter

### Run scan and clean with crontab
```sh
/path/to/here/ssh-hosts.allow-manager
```
