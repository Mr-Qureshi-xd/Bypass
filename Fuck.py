import os, platform, time
time.sleep(2)
os.system('https://facebook.com/groups/447671328737321/')
time.sleep(2)
print('\n\x1b[1;37m Checking Update...');time.sleep(0.5)
os.system('git pull')
try:
    import gtts
except IOError:
    os.system('pip install gtts')
def Update():
    exit('\033[1;31m(×) Commands On Update Please Wait For Update ❤ ')
def Run():
        bit = platform.architecture()[0]
        if bit == '64bit':
            print("\x1b[1;92m Congratulations ! Your Device Support this Tool")

            import KAUSAR_64
            KAUSAR_64.Main()
           
        elif bit =='32bit':
            print('\x1b[1;92m Congratulations! Your Device Support This Tool')
            import KAUSAR_32
            KAUSAR_32.Main()
        else:
            exit('\033[1;31m[×] Device Not Support 32bit')
Run()
