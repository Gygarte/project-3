import subprocess
def pkg_install(pkg):
    
    return subprocess.run('pip3 install ' + pkg, shell=True).returncode
