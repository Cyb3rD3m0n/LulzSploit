import os, sys, time

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

print '''
{G}    .;'                      `;,    {G}[+]{N} Laughing At Your Security Since 2011
{G}  .;'  ,;'               `;,  `;,    {Y}_          _      ____        _       _ _{G}
{G} .;'  ,;'  ,;'   {Y}_{G}   `;,  `;,  `;,  {Y}| |   _   _| |____/ ___| _ __ | | ___ (_) |_{G}
{G} ::   ::   :    {Y}(_){G}    :   ::   ::  {Y}| |  | | | | |_  /\___ \| '_ \| |/ _ \| | __|{G}
{G} ':.  ':.  ':.  {Y}/_\{G}  ,;'  ,:'  ,:'  {Y}| |__| |_| | |/ /  ___) | |_) | | (_) | | |_{G}
{G}  ':.  ':.     {Y}/___\{G}     ,:'  ,:'   {Y}|_____\__,_|_/___||____/| .__/|_|\___/|_|\__|{G}
{G}    ':.       {Y}/_____\{G}        ,:'                            {Y}|_|
             {Y}/       \{N}

{G}[+]{Y} LulzSploit Setup{N}
{G}[+]{Y} LulzSploit v.3.5{N}


'''.format(Y = Y, G = G, N = N)
print "=" * 47
print ("\n\033[1;32m[+] \033[0mmodule-setup.py is running...\n")
os.system("unzip tools.zip")
print "=" * 47
os.system("pip2 install -r lulz-requirements.txt")
os.system("chmod +x lulzsploit.py")
os.system("rm -rf tools.zip")
os.systen("rm -rf lulz-requirements.txt")
print "=" * 47
print ("\n\033[1;32m[+] \033[0mmodule-setup.py is done!\n")
sys.exit()
