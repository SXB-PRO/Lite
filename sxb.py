import os, platform
try:
    import requests
except:
    os.system('pip install requests')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from Lite import Lite
   Lite_f_a_md__eck()
elif bit == '32bit':
    from Lite32 import Lite
   Lite_f_a_md__eck()
else:
    print('\n YOUR DEVICE IS NOT SUPPORT THIS COMMAND')
    os.system('exit')
