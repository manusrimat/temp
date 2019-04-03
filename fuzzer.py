
#!/usr/bin/python
import subprocess
import os
import base64
import sys
import random,string


from subprocess import Popen, PIPE
while True:
    s = ""
    for i in range(100):
        s+= random.choice(string.printable);
    child = subprocess.Popen("./jsonParser", stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    _, stdErrOut = child.communicate(input = s)
    if child.returncode == -11:
        print "BROKEN FAILURE (%d): %s" % (child.returncode, s)
        print "|%s|" % stdErrOut
        print base64.b64encode(s)
        sys.exit(0);
print("none found")
