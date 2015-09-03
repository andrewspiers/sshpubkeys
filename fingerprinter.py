#!/usr/bin/env python

import sshpubkeys

import fileinput

for line in fileinput.input():
    key = sshpubkeys.SSHKey(line)
    if len(line.split(None,3)) >= 3:
        print (line.split(None,3)[-1] + " :")
    print (key.hash())
