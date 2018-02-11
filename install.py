import os, sys, time


banner = '''\033[37m
 _          _
| |   _   _| |_______  ___  ___
| |  | | | | |_  / __|/ _ \/ __|
| |__| |_| | |/ /\__ \  __/ (__
|_____\__,_|_/___|___/\___|\___|\033[0m
[##############################]\033[31m
           T O O L S\033[0m
[==============================]

||Lulzsec Tools Installer
||created by: cyb3r_d3m0n
||\033[33m\033[4mhttps://github.com/Cyb3eD3m0n\033[0m\n
'''

print banner
print ("\033[32m[ Installing... ]\n\033[0m")
time.sleep(2.5)
print ("\033[32m\n[ Unzipping Lulz Modules ]\033[0m\n")
time.sleep(1.5)
os.system("unzip lulz.zip")
time.sleep(2.5)
print ("\033[32m\n[ Installing Lulz Requirements ]\n\033[0m")
time.sleep(1.1)
os.system("pip2 install -r lulz-requirements.txt")
time.sleep(2.5)
print ("\033[32m\n[ preparing... ]\n\033[0m")
time.sleep(1.1)
os.system("chmod +x lulzsec.py")
time.sleep(2.5)
print ("\033[32m\n[ Done Installing ] : Lulzsec Tools is ready to use\033[0m")
print "\n"
sys.exit()