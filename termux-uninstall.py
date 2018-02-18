import os, time, subprocess
from sys import stdout

R = "\033[1;31m"   #  RED
B = "\033[1;34m"   #  BLUE
C = "\033[1;36m"   #  CYAN
G = "\033[1;32m"   #  GREEN
Y = "\033[1;93m"   #  YELLOW
N = "\033[0m"      #  NORMAL
B = "\033[1m"      #  BOLD
P = "\033[35m"     #  PURPLE
U = "\033[4m"      #  UNDERLINE
O = "\033[36m"     #  ORANGE

def output_true(msg,input):

   i = "{} [status] : {}processing{}".format(G,Y,N)

   stdout.write(msg + " %s" % i)
   stdout.flush()

   if subprocess.call(input+' >/dev/null 2/&1', shell=True)==0:
     i = "{} [status] : {}done!{}".format(G,Y,N)

   else:
     i = "{} [status] : {}warning!{}".format(G,R,N)

   stdout.write("\r " + msg + i)


script ="rm -rf /data/data/com.termux/files/usr/bin/lsfconsole"
folder ="rm -rf /data/data/com.termux/files/usr/share/LulzSploit"
home ="cd /data/data/com.termux/files/home"

choice = raw_input("\033[1;32m[-]\033[1;93m are you sure do you want to uninstall LulzSploit? [y/N]\n\n  > ")
if choice == 'n' or choice == 'N':
  sys.exit()
elif choice == 'y' or choice == 'Y':
  print output_true("preparing to home folder",home)
  print output_true("\033[1;31m[-]\033[0m uninstalling tool",folder)
  print output_true("\033[1;31m[-]\033[0m deleting shortcut",script)
  print "\n\033[1;32m[+]\033[0m you need to re-install the tool by git cloning it again"
  sys.exit()
else:
  sys.exit()



