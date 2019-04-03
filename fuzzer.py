
#!/usr/bin/python
import subprocess
import os
import base64
import sys
import random,string


from subprocess import Popen, PIPE
while True:
    tester = ""
    temp = ""
    for x in range(12):
        temp = random.choice(string.printable)
        tester = tester + temp
    child = subprocess.Popen("./jsonParser", stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    _, stdErrOut = child.communicate(input = tester)
    segFault = -11
    if child.returncode == segFault:
        print "BROKEN FAILURE (%d): %s" % (child.returncode, tester)
        print "Base 64 Encoded segfault string:"
        print base64.b64encode(tester)
        sys.exit(0);
print("none found")
