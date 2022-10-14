import platform
bit=platform.architecture()[0]
if bit =='64bit':
    import sxb
    sxb._f_a_md__eck()
else:
    print('Sorry device or system not support this tools')
    exit()
