import os, time, sys
from tools import colors, scanner, panel, cloudflare, DDoS, whs
from colored import fg, bg, attr


banner = '''\033[37m
 _          _
| |   _   _| |_______  ___  ___
| |  | | | | |_  / __|/ _ \/ __|
| |__| |_| | |/ /\__ \  __/ (__
|_____\__,_|_/___|___/\___|\___|\033[0m
[##############################]\033[31m
           T O O L S\033[0m
[==============================]

||created by: cyb3r_d3m0n
||version 1.0
||created in:  Philippines
||\033[33m\033[4mhttps://github.com/Cyb3rD3m0n\033[0m\n

\033[32m[?]\033[0m To exit a tool you need to type "main"
\033[32m[+]\033[0m Wait on updates!
'''

def main():

      os.system("clear")
      print banner
  
   # Print Choices

      print("      \033[4m\033[1;31mTools\033[0m\n")
      print("\033[32m[01] Port Scanner")
      print("\033[32m[02] Admin Panel Finder")
      print("\033[32m[03] Cloudflare Scanner")
      print("\033[32m[04] Flood Site")
      print("\033[32m[05] Whois Lookup")
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

      elif lulz == 'exit':
         sys.exit()

      else:
         print (colors.O+"\n  [Error]"+colors.R+" Command Error\n"+colors.W)
         time.sleep(1.1)
         main()


if __name__ == '__main__':
  main()