#!/usr/bin/python

# Import os library
import os
from time import sleep
hostname1 = "10.7.0.77" #Vision Clever III
hostname2 = "10.7.0.17" #PS4
application = "uTorrent" #example
var = 7
#curl  http://ipdeny.com/ipblocks/data/countries/fr.zone > FR_blocked_zone
while var == 7 :

	response1 = os.system("ping -c 1 " + hostname1)
	response2 = os.system("ping -c 1 " + hostname2)
        isappruning = os.system("pgrep uTorrent")
	#and then check the response...
	if response1 == 0 or response2 == 0:
  		print hostname1, hostname2, 'is up!'
  		print 'killing ', application
  		#os.system("killall -9 uTorrent");
  		os.system("osascript -e 'quit app \"uTorrent\"'");
  		#os.system("pfctl -d");
		print 'sleep 300 sec'
		sleep(300)
		continue
	elif response1 != 0 and response2 != 0:
		if isappruning  == 0:
  			print 'And application already running'
			print 'sleep 10 sec'
			sleep(300)
		else :
  			print "Starting uTorrent"
  			#os.system("/Applications/uTorrent.app/Contents/MacOS/uTorrent & ");
  		        #os.system("pfctl -e");
  			os.system("open -a uTorrent");
			print 'sleep 10 sec'
			sleep(300)
