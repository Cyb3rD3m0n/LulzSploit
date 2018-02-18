import os, time, subprocess
from sys import stdout

R = "\033[1;31m"   #  RED
B = "\033[1;34m"   #  BLUE
C = "\033[1;36m"   #  CYAN
G = "\033[1;32m"   #  GREEN
Y = "\033[1;93m"   #  YELLOW
W = "\033[0m"      #  NORMAL
B = "\033[1m"      #  BOLD
P = "\033[35m"     #  PURPLE
U = "\033[4m"      #  UNDERLINE
O = "\033[36m"      #  ORANGE

def Command_exe(msg,cmd):
	i = "\033[1mSTATUS :[Processing]"
	stdout.write(" " + msg + " %s" % i)
	stdout.flush()
	if subprocess.call(cmd+' >/dev/null 2>&1', shell=True)==0:
		i = "[\033[1mOK"+W+"]"
	else:
		i = "[\033[1mERROR"+W+"] :["+O+"WARNING"+W+"]"
		
	stdout.write("\r " + msg +" STATUS:%s" % i)

Shortcuts ="cp -r /data/data/com.termux/files/home/LulzSploit/tools/lsfconsole /data/data/com.termux/files/usr/bin/lsfconsole "
Files     ="cp -r * /data/data/com.termux/files/home/LulzSploit /data/data/com.termux/files/usrp/local/share/LulzSploit "
Homedir   ="cd /data/data/com.termux/files/home"

print '''
{G}    .;'                      `;,    {G}[+]{W} Laughing At Your Security Since 2011
{G}  .;'  ,;'               `;,  `;,    {Y}_          _      ____        _       _ _{G}
{G} .;'  ,;'  ,;'   {Y}_{G}   `;,  `;,  `;,  {Y}| |   _   _| |____/ ___| _ __ | | ___ (_) |_{G}
{G} ::   ::   :    {Y}(_){G}    :   ::   ::  {Y}| |  | | | | |_  /\___ \| '_ \| |/ _ \| | __|{G}
{G} ':.  ':.  ':.  {Y}/_\{G}  ,;'  ,:'  ,:'  {Y}| |__| |_| | |/ /  ___) | |_) | | (_) | | |_{G}
{G}  ':.  ':.     {Y}/___\{G}     ,:'  ,:'   {Y}|_____\__,_|_/___||____/| .__/|_|\___/|_|\__|{G}
{G}    ':.       {Y}/_____\{G}        ,:'                            {Y}|_|
             {Y}/       \{W}'''.format(Y = Y, G = G, W = W)
print R + ("_________________________________________________")
print ("_________________________________________________|")
print R + "  __________________________________________|" + W
print R + " |  [+]" + G + " INSTALLING" + W
print Command_exe(R + "|  [+]" + G + " Extracting Modules",'unzip tools.zip')
print Command_exe(R + "|  [+]" + G + " Creating Files\033[0m",'mkdir -p /data/data/com.termux/files/usr/share/LulzSploit')
print Command_exe(R + "|  [+]" + G + " Copying Files\033[0m",'cp -r * /data/data/com.termux/files/usr/share/LulzSploit')
print Command_exe(R + "|  [+]" + G + " Creating Shortcuts\033[0m",Shortcuts)
print Command_exe(R + "|  [+]" + G + " Extracting Files\033[0m",Files)
print Command_exe(R + "|  [+]" + G + " Giving Root Access\033[0m",'chmod -R -c 750 /usr/share/LulzSploit/')
print R + "=" * 47 + W
print R + " |  [+]" + O + " Done Installing!" + W
print Command_exe(R + "|  [+]" + G + " Going back to home directory\033[0m",Homedir)
print R + "[+]" + O + ": To run the program just type" + G + " lsfconsole" + W
print("\n")
