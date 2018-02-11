import time ,os ,sys ,requests ,socket ,random
from colored import fg, bg, attr


def info(lulz):
   try:
         target = socket.gethostbyname(lulz)

   # Printing Info

         print (" \033[32m [ IP Address    ]\033[0m : %s%s%s%s\n" % (fg('black'), bg('green'), target, attr(0)))

   # Exception

   except socket.gaierror as (msg):
      print ("\033[31m[Error] \033[33merror connecting to socket")
      time.sleep(1.5)
      start()
   except socket.error as (msg):
      print ("\033[31m[Error] \033[33mconnection lost")
      time.sleep(1.5)
      start()



def start():
   try:
       print ("\nEnter Target [ www.target.com / target.com ] \n")
       lulz = raw_input("  %s%sTarget Host%s > " % (fg('black'), bg(160), attr(0)))
       print ""
       if lulz == 'exit':
         print ""
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
               start()
           except socket.gaierror as (msg):
               print ("\033[31m[Error] \033[33merror connecting to socket")
               start()

   # Lulz-Scanner Last Print Output 

           print ("\n  [%s%sDefault Port%s] : open :" % (fg('black'), bg(160), attr(0))) + ("%s%s80%s\n" % (fg('black'), bg('green'), attr(0)))
           print ("\033[32m\n  [ lulzsec scanner service is done! ]\033[0m")

   # Exit

           ex = raw_input("\n  %s%sdo you want to exit [ Y/n ]%s > " % (fg('black'), bg(160), attr(0)))

   # New Or End Function

           if ex == 'n' or ex == 'N':
               start()

           elif ex == 'y' or ex == 'Y':
               print ""

   # Skipping Port Scanning

       elif b == 'n' or b == 'N':
           print ""

   # Exception

   except requests.ConnectionError as (msg):
     print ("\033[31m[Error] \033[33merror sending requests")
     time.sleep(2.3)
     start()