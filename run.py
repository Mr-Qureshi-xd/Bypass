from os import system
from platform import machine
print('Checking For Update...')
system('git pull')
print('Subcrib My Channel First...')
os.system('xdg-open https://youtube.com/c/MrQureshiTech')
time.sleep(2)
prinnt('Join Our Facebook Group For More Update bruh...')
os.system('xdg-open https://facebook.com/groups/447671328737321/')
if machine()=='aarch64':
    os.system('chmod 777 nox.so')
    import nox.so
    nox.main
else:
    os.system('chmod 777 nox32.so')
    import nox32.so
    nox.main
