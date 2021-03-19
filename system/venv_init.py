import subprocess
import os
import sys
from .system_py_version import system_py_version

def venv_init():
    
    if system_py_version() == True:
        subprocess.run('python3 -m venv venv',shell=True)
        return True
    else:
        sys.exit('VenvError! Not able to initialize virtual environment!')

    
