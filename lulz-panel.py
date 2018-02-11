import socket ,requests ,os ,time ,sys ,random
from colored import fg, bg ,attr

   # Main Banner

lulzbanner = '''\033[32m
   ____  _
  |  _ \(_)_ __   ___  _   _
  | |_) | | '_ \ / _ \| | | |
  |  __/| | | | | (_) | |_| |
  |_|   |_|_| |_|\___/ \__, |
                       |___/
 _          _
| |   _   _| |_______  ___  ___
| |  | | | | |_  / __|/ _ \/ __|
| |__| |_| | |/ /\__ \  __/ (__
|_____\__,_|_/___|___/\___|\___|\033[0m
[##############################]\033[31m
     Admin   Panel   Finder\033[0m
[==============================]

||created by: cyb3r_d3m0n
||version 1.0.0
||
||\033[33m\033[4mhttps://github.com/Cyb3eD3m0n\033[0m
'''

   # Starting Programs Output

def lulz():
   try:

   # Opening Sub-Link For Scanning Admin Panels

       f = open("lulz.txt","r");

   # Getting Target

       print lulzbanner
       target = raw_input("  %s%sTarget Host%s > " % (fg('black'), bg(160), attr(0)))
       if target == 'exit':
         sys.exit()

   # Start To Scan Info

       print ("\n  %s%sGetting Info...%s\n" % (fg('black'), bg('green'), attr(0)))
       time.sleep(2.5)
       url = socket.gethostbyname(target)
       host = "http://"+url
       r = requests.get(host)
       http = r.status_code

   # Printing The Info

       print (" \033[32m [ IP Address    ]\033[0m : %s%s%s%s" % (fg('black'), bg('green'), url, attr(0)))
       print (" \033[32m [ status code   ]\033[0m : %s%s%s%s" % (fg('black'), bg('green'), http, attr(0)))

   # Scanning For Admin Panels

       print "\n"
       time.sleep(1.5)
       print "\033[32m[+] Finding Admin Panel...\033[0m\n"
       print ("\033[32m      Status           :            link        \033[0m\n")
       for x in range (1, 482):
         try:
           sub_link = f.readline()
           plurl = "http://"+target+sub_link
           C = requests.get(plurl)
           statcode = C.status_code
           if statcode == 200:
              print ("\033[32m[+] Admin panel found! : %s%s%s%s\033[0m\033[0m\033[0m\033[0m" % (fg('black'), bg('green'), plurl, attr(0)))
           else:
              print ("\033[31m[-] Error Panel        : %s" % (plurl))

   # Exception

         except requests.ConnectionError as (msg):
            print ""

   # Exception

   except socket.error as (msg):
     print ("\033[31m[Error] \033[33mconnection lost") + "\033[0m"
     time.sleep(1.5)
     main()
   except socket.gaierror as (msg):
     print ("\033[31m[Error] \033[33merror connecting to socket") + "\033[0m"
     time.sleep(1.5)
     main()


def main():

   # Starting The Program

       os.system("clear")
       lulz()


if __name__=='__main__':
  main()