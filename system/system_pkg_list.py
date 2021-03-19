import subprocess

def system_pkg_list():

    system_pkg = subprocess.run('pip3 list', shell=True, capture_output=True, text=True).stdout

    return system_pkg