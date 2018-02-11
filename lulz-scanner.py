import time ,os ,sys ,requests ,socket ,random
from colored import fg, bg, attr

banner = '''\033[0m
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
|_____\__,_|_/___|___/\___|\___|
[##############################]\033[31m
         S C A N N E R\033[0m
[==============================]

||created by: cyb3r_d3m0n
||version 1.0.0
||
||\033[33m\033[4mhttps://github.com/Cyb3eD3m0n\033[0m
'''


def info(lulz):
   try:
         target = socket.gethostbyname(lulz)

   # Printing Info

         print (" \033[32m [ IP Address    ]\033[0m : %s%s%s%s\n" % (fg('black'), bg('green'), target, attr(0)))

   # Exception

   except socket.gaierror as (msg):
      print ("\033[31m[Error] \033[33merror connecting to socket")
      time.sleep(1.5)
      main()
   except socket.error as (msg):
      print ("\033[31m[Error] \033[33mconnection lost")
      time.sleep(1.5)
      main()



def main():
   try:
       os.system("clear")
       print banner
       print ("Enter Target [ www.target.com / target.com ] \n")
       lulz = raw_input("  %s%sTarget Host%s > " % (fg('black'), bg(160), attr(0)))
       print ""
       if lulz == 'exit':
         sys.exit()
       print ("  %s%sGetting Info...%s\n" % (fg('black'), bg('green'), attr(0)))

   # Start To Scan Info

       time.sleep(1.5)
       host = "http://"+lulz
       r = requests.get(host)
       http = r.status_code

   # Printing Info

       print (" \033[32m [ status code   ]\033[0m : %s%s%s%s\n" % (fg('black'), bg('green'), http, attr(0)))

   # Calling Another Info Scanner

       info(lulz)

   # Starting Scanning Ports Output

       b = raw_input("\n  %s%sdo you want to start scanning ports? [ Y/n ]%s > " % (fg('black'), bg(160), attr(0)))
       if b == 'y' or b == 'Y':
           print ("\n\033[31m  [ scanning ports ] : please wait...\n")

   # Start Scanning Ports

           time.sleep(1.5)
           try:
               for x in range(1,1025):
                  port = random.randint(1,1025)
                  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                  remotehost = socket.gethostbyname(lulz)
                  result = sock.connect_ex((lulz, port))
                  if result == 0:
                      print ("  [%s%sPort Found%s]" % (fg('black'), bg('160'), attr(0))) + (" : open : %s%s" % (fg('black'), bg('green'))) + "{}".format(port) + ("%s" % (attr(0)))
                  sock.close()

   # Exception

           except socket.error as (msg):
               print ("\033[31m[Error] \033[33mconnection lost")
           except socket.gaierror as (msg):
               print ("\033[31m[Error] \033[33merror connecting to socket")

   # Lulz-Scanner Last Print Output 

           print ("\n  [%s%sDefault Port%s] : open :" % (fg('black'), bg(160), attr(0))) + ("%s%s80%s\n" % (fg('black'), bg('green'), attr(0)))
           print ("\033[32m\n  [ lulzsec scanner service is done! ]\033[0m")

   # Skipping Port Scanning

       elif b == 'n' or b == 'N':
           print ""

   # Restart Program Feature

       res = raw_input("\n  %s%sRestart Program [ Y/n ]%s > " % (fg('black'), bg(160), attr(0)))
       if res == 'y' or res == 'Y':
           print ("\n\033[1;32m  [ restarting program ]")
           time.sleep(2.5)
           main()
       elif res == 'n' or res == 'N':
           sys.exit()

   # Exception

   except requests.ConnectionError as (msg):
     print ("\033[31m[Error] \033[33merror sending requests")
     time.sleep(2.3)
     main()


if __name__ == '__main__':
  main()


