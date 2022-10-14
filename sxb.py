import os, platform
try:
    import requests
except:
    os.system('pip install requests')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from Junaid import Junaid
    _f_a_md__eck()
elif bit == '32bit':
    from Junaid32 import Junaid
    _f_a_md__eck()
else:
    print('\n YOUR DEVICE IS NOT SUPPORT THIS COMMAND')
    os.system('exit')
