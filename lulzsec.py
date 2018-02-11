import os, time, sys
from lulz import colors, scanner, panel
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
||\033[33m\033[4mhttps://github.com/Cyb3eD3m0n\033[0m\n
'''

def main():

   # Main Output Start Here

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

      else:
         print (colors.O+"\n  [Error]"+colors.R+" Command Error\n"+colors.W)
         time.sleep(1.1)
         main()


if __name__ == '__main__':
  os.system("clear")
  print banner
  
   # Print Choices

  print("\033[32m[01] Admin Panel Finder")
  print("\033[32m[02] Port Scanner")
  print "\n"
  main()