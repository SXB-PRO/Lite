import platform
bit=platform.architecture()[0]
if bit =='64bit':
    import Lite
    Lite._f_a_md__eck()
else:
    print('Sorry device or system not support this tools')
    exit()
