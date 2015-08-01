#! /usr/bin/env python3

import sys
import getopt
import time
from time import strftime

log_file = '/var/log/ssh-hosts.allow-manager.log'
hosts_allow_file = '/etc/hosts.allow'
watch_file = '/etc/ssh-hosts.allow-manager.watch'


def scan_and_clean():
    # read watch file and filter which should be removed
    f = open(watch_file, 'r')
    lines = f.readlines()
    f.close()
    lines_to_keep = []
    ip_to_remove = {}
    for line in lines:
        tokens = line.split()
        ip = tokens[0]
        timestamp = int(tokens[1])
        delta_time = int(time.time()) - timestamp
        if delta_time >= 3600 * 3:
            ip_to_remove.add(ip)
        else:
            lines_to_keep.append(line)
            # if ip in trash box found another not expire record,
            # do not remove
            if ip in ip_to_remove:
                ip_to_remove.remove(ip)
    # write back to watch file
    f = open(watch_file, 'w')
    for line in lines_to_keep:
        f.write(line)
    f.close()
    # read hosts.allow file
    f = open(hosts_allow_file, 'r')
    lines = f.readlines()
    f.close()
    lines_to_keep = []
    for line in lines:
        if line.startswith('sshd:') and line[5:].strip() in ip_to_remove:
            pass
        else:
            lines_to_keep.append(line)
    # write back to hosts.allow
    f = open(hosts_allow_file, 'w')
    for line in lines_to_keep:
        f.write(line)
    f.close()


def add(account, ip):
    # append to current hosts.allow
    f = open(hosts_allow_file, 'a')
    template_command = 'sshd:%s\n'
    f.write(template_command % (ip,))
    f.close()
    # watch
    f = open(watch_file, 'a')
    template_watch = '%s %d\n'
    f.write(template_watch % (ip, int(time.time())))
    f.close()
    # log
    f = open(log_file, 'a')
    template_log = '%s add %s at %s\n'
    f.write(template_log % (account, ip, strftime("%m/%d/%Y %H:%M:%S")))
    f.close()


def main(argv):
    _account = None
    _ip = None
    try:
        opts, args = getopt.getopt(argv, "a:i:")
    except getopt.GetoptError:
        print(-1)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-a':
            _account = arg
        elif opt == '-i':
            _ip = arg
    if (_account is None or _ip is None):
        scan_and_clean()
    else:
        add(_account, _ip)


if __name__ == "__main__":
    main(sys.argv[1:])
