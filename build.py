#! /usr/bin/env python3

import subprocess

source_file = open('ssh-hosts.allow-manager.cpp', 'r')
source = source_file.read()
source_file.close()
pwd = subprocess.check_output(['pwd']).strip().decode('utf-8')
source = source % (pwd,)

tem_file = open('.source.cpp', 'w')
tem_file.write(source)
tem_file.close()

subprocess.check_output(['g++', '.source.cpp', '-o', 'ssh-hosts.allow-manager'])
subprocess.check_output(['rm', '.source.cpp'])
subprocess.check_output(['chmod', 'u=rwx,go=xr,+s', 'ssh-hosts.allow-manager'])
