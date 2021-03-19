import sys

def system_py_version():
    
    if sys.version_info[0] == 3:
        return True
    else:
        sys.exit('VersionError! Upgrade to python 3!')

