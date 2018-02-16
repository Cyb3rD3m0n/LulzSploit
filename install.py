import os, sys, time


banner = '''\033[37m
 _          _      ____        _       _ _
| |   _   _| |____/ ___| _ __ | | ___ (_) |_
| |  | | | | |_  /\___ \| '_ \| |/ _ \| | __|
| |__| |_| | |/ /  ___) | |_) | | (_) | | |_
|_____\__,_|_/___||____/| .__/|_|\___/|_|\__|
                        |_|

||LulzSploit Tools Installer
||created by: cyb3r_d3m0n
||created in: Philippines
||\033[33m\033[4mhttps://github.com/Cyb3eD3m0n\033[0m\n
'''

print banner
print ("\033[32m[ Installing... ]\n\033[0m")
time.sleep(2.5)
print ("\033[32m\n[ Unzipping Lulz Modules ]\033[0m\n")
time.sleep(1.5)
print "=" * 47
print ""
os.system("unzip tools.zip")
print ""
print "#" * 47
time.sleep(2.5)
print ("\033[32m\n[ Installing Lulz Requirements ]\n\033[0m")
time.sleep(1.1)
print "=" * 47
print ""
os.system("pip2 install -r lulz-requirements.txt")
print ""
print "#" * 47
time.sleep(2.5)
print ("\033[32m\n[ cleaning... ]\n\033[0m")
time.sleep(1.1)
os.system("chmod +x lulzsec.py")
os.system("rm -rf tools.zip")
os.system("rm -rf lulz-requirements.txt")
time.sleep(2.5)
print ("\033[32m\n[ Done Installing ] : LulzSploit is ready to use\033[0m")
print "\n"
sys.exit()