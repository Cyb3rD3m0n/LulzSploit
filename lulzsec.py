import os, time, sys, subprocess
from colored import fg, bg, attr

R = "\033[1;31m"   #  RED
B = "\033[1;34m"   #  BLUE
C = "\033[1;36m"   #  CYAN
G = "\033[1;32m"   #  GREEN
Y = "\033[1;93m"   #  YELLOW
N = "\033[0m"      #  NORMAL
B = "\033[1m"      #  BOLD
P = "\033[35m"     #  PURPLE
U = "\033[4m"      #  UNDERLINE

subprocess.call('clear',shell=True)

try:
  from tools import colors, scanner, panel, cloudflare, DDoS, whs, gbrute, ftpb, Hinst
except ImportError as e:
  time.sleep(1.5)
  print '''\033[1;93m
   _          _      ____
  | |   _   _| |____/ ___|  ___  ___
  | |  | | | | |_  /\___ \ / _ \/ __|
  | |__| |_| | |/ /  ___) |  __/ (__
  |_____\__,_|_/___||____/ \___|\___|\033[1;0m'''

  print ("\n  {}[-]{} Modules Not Found".format(R,N))
  time.sleep(2.5)
  print ("  {}[-]{} Execute install.py to unzip and install all modules\n".format(R,N))
  print ("  {}[-]{} Lulzsec Shutdown!".format(R, N))
  sys.exit()


def main():

      os.system("clear")
  
   # Print Choices

      print ''' {Y}

      _          _      ____
     | |   _   _| |____/ ___|  ___  ___
     | |  | | | | |_  /\___ \ / _ \/ __|
     | |__| |_| | |/ /  ___) |  __/ (__
     |_____\__,_|_/___||____/ \___|\___| {N}

{G}       .;'                   `;,      
{G}     .;'   ,;'            `;,  `;,   {G}[+]{N} created by: cyb3r_d3m0n
{G}    .;'  ,;'  ,;'     `;,  `;,  `;,  {G}[+]{N} version : 1.2
{G}    ::   ::   :   {N}( ){G}   :   ::   ::  {P}[?]{N}{U} https://github.com/Cyb3rD3m0n{N}
{G}    ':.  ':.  ':. {N}/_\{G} ,:'  ,:'  ,:'  
{G}     ':.  ':.    {N}/___\{G}    ,:'  ,:'   {Y}[!]{N} Lulzsec Multi tool 
{G}      ':.       {N}/_____\{G}      ,:'     {Y}[?]{N} Type Main To Exit A Tool
               {N}/       \           

   {G}[+]{N} Laughing At Your Security Since 2011\n
   {R}[-]{N} Dont use bruteforce if hydra is not installed
'''.format(G = G, N = N, P = P, Y = Y, U = U, R = R)

   
      print("\n      \033[4m\033[1;31mTools\033[0m\n")
      print("\033[32m[01]\033[93m Port Scanner\033[0m         \033[32m[06]\033[93m Gmail Bruteforce [Hydra]")
      print("\033[32m[02]\033[93m Admin Panel Finder\033[0m   \033[32m[07]\033[93m FTP Bruteforce   [Hydra]")
      print("\033[32m[03]\033[93m Cloudflare Scanner\033[0m   \033[32m[08]\033[93m Hydra Installer")
      print("\033[32m[04]\033[93m Flood Site\033[0m           ")
      print("\033[32m[05]\033[93m Whois Lookup\033[0m         ")
      print "\n"

   # Command Choice

      lulz = raw_input("  %s%sLulzsec%s > " % (fg('black'), bg(160), attr(0)))

   # Calling Function

      if lulz == '1' or lulz == '01':
          time.sleep(1.1)
          scanner.start()
          main()

      elif lulz == '2' or lulz == '02':
          time.sleep(1.1)
          panel.start()
          main()

      elif lulz == '3' or lulz == '03':
          time.sleep(1.1)
          cloudflare.scan()
          main()

      elif lulz == '4' or lulz == '04':
          time.sleep(1.1)
          DDoS.start()
          main()

      elif lulz == '5' or lulz == '05':
          time.sleep(1.1)
          whs.start()
          main()

      elif lulz == '6' or lulz == '06':
          time.sleep(1.1)
          gbrute.start()
          main()

      elif lulz == '7' or lulz == '07':
          time.sleep(1.1)
          ftpb.start()
          main()

      elif lulz == '8' or lulz == '08':
          time.sleep(1.1)
          Hinst.start()
          main()

      elif lulz == 'exit':
         print ("\n"+G+"[+]"+N+"Lulzsec Tools service is done")
         print (G+"[+]"+N+"Laughing At Your Security Since 2011")
         print (G+"[+]"+N+"All rights reserved!\n")
         sys.exit()

      else:
         print (colors.O+"\n  [Error]"+colors.R+" Command Error\n"+colors.W)
         time.sleep(1.1)
         main()


if __name__ == '__main__':
  main()