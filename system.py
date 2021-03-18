import subprocess
import sys

def system():

    #Default state is False

    system_pkg = subprocess.run('pip3 list', shell=True, capture_output=True, text=True).stdout

    for pkg in ['numpy','pandas', 'matplotlib','seaborn','tensorflow','keras-tuner','scikit-learn','xlrd']:
        if pkg in system_pkg:
            print(pkg + ' '+'installed!')
        else:
            print('Do you want to install '+ pkg +'? [y/n]')
            response = input()
            if response =='y':
                if subprocess.run('pip3 install ' + pkg, shell=True).returncode == 0:
                    print(f'Succesfully intalled {pkg}')
                    continue
                else:
                    print(f'Installation error! Do you want to continue without {pkg}? The program might not work properly! [y/n]')
                    response = input()
                    if response == 'y':
                        continue
                    else:
                        sys.exit('Execution interrupted by user choice!')
            else:
                print('Execution might not work properly!')
                print('Do you want to continue? [y/n]')
                response = input()
                if response == 'y':
                    continue
                else:
                    sys.exit('Execution interrupted by user choice!')
                    
    #Permission requested for further execution
    # Until further development

    print('System set up!')
    print('Do you want to continue? [y/n]')
    response = input()
    if response =='y':
        return True #Change the system state; used in main.py
    else:
        sys.exit('Execution interupted by user choice!')



