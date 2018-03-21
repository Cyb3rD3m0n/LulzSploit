import os, time, sys, subprocess, platform
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
platformS = str(platform.system())
platformR = str(platform.release())

if str(platform.system()) != "Linux":
  print '''\033[1;93m
   _          _      ____        _       _ _
  | |   _   _| |____/ ___| _ __ | | ___ (_) |_
  | |  | | | | |_  /\___ \| '_ \| |/ _ \| | __|
  | |__| |_| | |/ /  ___) | |_) | | (_) | | |_
  |_____\__,_|_/___||____/| .__/|_|\___/|_|\__|
                          |_| \033[0m'''

  print ("\n  {}[-]{} you are not using Linux System{}".format(R,Y,N))
  time.sleep(1.5)
  print ("{}[-]{} Lulzsploit is running on : {PS} : version {PR}".format(R,N))
  time.sleep(1.5)
  print ("{}[-]{} Invaid Platform".format(R,N))
  print ("  {}[-]{} please run this script on Linux System{}",format(R,Y,N))
  time.sleep(1.1)
  print ("  {}[-]{} LulzSploit Shutdown!{}".format(R,Y,N))


subprocess.call('clear',shell=True)

try:
  from tools import scanner, panel, cloudflare, DDoS, whs, gbrute, ftpb, Hinst, payloads, tortool
except ImportError as e:
  time.sleep(1.5)
  print '''\033[1;93m
   _          _      ____        _       _ _
  | |   _   _| |____/ ___| _ __ | | ___ (_) |_
  | |  | | | | |_  /\___ \| '_ \| |/ _ \| | __|
  | |__| |_| | |/ /  ___) | |_) | | (_) | | |_
  |_____\__,_|_/___||____/| .__/|_|\___/|_|\__|
                          |_| \033[0m'''

  print ("\n  {}[-]{} Modules Not Found{}".format(R,Y,N))
  time.sleep(2.5)
  print ("  {}[-]{} Execute setup.py to unzip and install all modules{}\n".format(R,Y,N))
  print ("  {}[-]{} LulzSploit Shutdown!{}".format(R,Y,N))
  sys.exit()


def main():
   try:

      os.system("clear")
  
   # Print Choices

      print '''
{G}      .;'                      `;,    {G}[+]{N} Laughing At Your Security Since 2011
{G}    .;'  ,;'               `;,  `;,    {Y}_          _      ____        _       _ _{G}
{G}   .;'  ,;'  ,;'   {Y}_{G}   `;,  `;,  `;,  {Y}| |   _   _| |____/ ___| _ __ | | ___ (_) |_{G}
{G}   ::   ::   :    {Y}(_){G}    :   ::   ::  {Y}| |  | | | | |_  /\___ \| '_ \| |/ _ \| | __|{G}
{G}   ':.  ':.  ':.  {Y}/_\{G}  ,;'  ,:'  ,:'  {Y}| |__| |_| | |/ /  ___) | |_) | | (_) | | |_{G}
{G}    ':.  ':.     {Y}/___\{G}     ,:'  ,:'   {Y}|_____\__,_|_/___||____/| .__/|_|\___/|_|\__|{G}
{G}      ':.       {Y}/_____\{G}        ,:'                            {Y}|_|
               {Y}/       \{N}

   {G}[+]{N} Lulzsploit is running on : {PS} : version {PR}
   {G}[+]{N} created by: cyb3r_d3m0n
   {G}[+]{N} lulzsploit v3.5
   {Y}[?]{N} Type Main To Exit A Tool
   {P}[?]{N} {U}https://github.com/Cyb3rD3m0n{N}

   {R}Warnings{N}
   ========
   {R}[-]{N} Dont use bruteforce if hydra is not installed
   {R}[-]{N} Dont use payload creator if metasploit is not installed\n
'''.format(G = G, N = N, P = P, Y = Y, U = U, R = R, PS = platformS, PR = platformR)

      print("   \033[32m[01]\033[93m Port Scanner\033[0m         \033[32m[06]\033[93m Gmail Bruteforce [Hydra]")
      print("   \033[32m[02]\033[93m Admin Panel Finder\033[0m   \033[32m[07]\033[93m FTP Bruteforce   [Hydra]")
      print("   \033[32m[03]\033[93m Cloudflare Scanner\033[0m   \033[32m[08]\033[93m Hydra Installer")
      print("   \033[32m[04]\033[93m Flood Site\033[0m           \033[32m[09]\033[93m payload creator  [msfvenom]")
      print("   \033[32m[05]\033[93m Whois Lookup\033[0m         \033[32m[10]\033[93m Connect Tor")
      print "\n"

   # Command Choice

      lulz = raw_input("  %s%sLulzSploit%s > " % (fg('black'), bg(160), attr(0)))

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

      elif lulz == '9' or lulz == '09':
          time.sleep(1.1)
          payloads.start()
          main()

      elif lulz == '10':
          time.sleep(1.1)
          tortool.start()
          main()

      elif lulz == 'exit':
         os.system("clear")
         print ("\n"+G+"[+]"+N+"LulzSploit process is done\n")
         sys.exit()

      else:
         print (colors.O+"\n  [Error]"+colors.R+" Command Error\n"+colors.W)
         time.sleep(1.1)
         main()

   except KeyboardInterrupt:
      try:
        print ("\n   \033[1;93m[-] \033[1;0mStop keyboard interrupting")
        time.sleep(1.5)
        main()
      except KeyboardInterrupt:
        os.system("clear")
        os.system("figlet 'STOP'")
        time.sleep(1.5)
        main()

if __name__ == '__main__':
  main()
