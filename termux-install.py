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

def output_true(msg,input)

   i = "{} [status] : {}processing{}".format(G,Y,N)

   stdout.write(msg + " %s" % i)
   stdout.flush()

   if subprocess.call(input+' >/dev/null 2/&1', shell=True)==0:
     i = "{} [status] : {}done!{}".format(G,Y,N)

   else:
     i = "{} [status] : {}warning!{}".format(G,R,N)

   stdout.write("\r " + msg + i)


script ="cp -r /data/data/com.termux/files/home/LulzSploit/tools/lsfconsole /data/data/com.termux/files/usr/bin"
folder ="cp -r /data/data/com.termux/files/home/LulzSploit /data/data/com.termux/files/usr/share"
home ="cd /data/data/com.termux/files/home"
clean ="rm -rf /data/data/com.termux/files/home/LulzSploit"




print '''
{G}    .;'                      `;,    {G}[+]{N} Laughing At Your Security Since 2011
{G}  .;'  ,;'               `;,  `;,    {Y}_          _      ____        _       _ _{G}
{G} .;'  ,;'  ,;'   {Y}_{G}   `;,  `;,  `;,  {Y}| |   _   _| |____/ ___| _ __ | | ___ (_) |_{G}
{G} ::   ::   :    {Y}(_){G}    :   ::   ::  {Y}| |  | | | | |_  /\___ \| '_ \| |/ _ \| | __|{G}
{G} ':.  ':.  ':.  {Y}/_\{G}  ,;'  ,:'  ,:'  {Y}| |__| |_| | |/ /  ___) | |_) | | (_) | | |_{G}
{G}  ':.  ':.     {Y}/___\{G}     ,:'  ,:'   {Y}|_____\__,_|_/___||____/| .__/|_|\___/|_|\__|{G}
{G}    ':.       {Y}/_____\{G}        ,:'                            {Y}|_|
             {Y}/       \{N}


{G}[+]{Y} LulzSploit Installer For Termux{N}

{G}[?]{Y} Make sure that you execute first the module-setup.py to prevent errors{N}
{G}[+]{Y} LulzSploit v.3.5{N}


'''.format(Y = Y, G = G, N = N)
print "\033[1;31m[warning] \033[1;93mthis is important\033[0m"
print "\033[1;93m[?] if module-setup.py is not executed you need to execute it now!")
choice = raw_input("do you want to execute the module-setup.py [y/n]  : ")
if choice == 'y' or choice == 'Y':
  print "=" * 47
  os.system("unzip tools.zip")
  print "=" * 47
elif choice == 'n' or choice == 'N':
  print "\033[1;31m[warning] \033[1;93mif you get an error you need to re-install or wait for updates\033[0m"
print Y
print "=" * 47
print G + "\n[+] Installing\n" + N
print "=" * 47
print ""
print output_true(G +"[+] preparing to homedir   :",home)
print output_true(G +"[+] installing shortcuts   :",script)
print output_true(G +"[+] moving folder          :",folder)
print output_true(G +"[+] cleaning               :",clean)
print ""
print "=" * 47
print G + "\n[+] Installing Done!" + N
print Y + "\n[?] Type lsfconsole to start the program" + N






