#!/usr/bin/python

import bluetooth
import time
import os

print "In/Out Board"

while True:
	print "Checking " + time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())

	result = bluetooth.lookup_name('xx:xx:xx:xx:xx:xx', timeout=5)
	if (result != None):
		print "(user): in - all good"
	else:
		print "(user): out - sending alert"

	time.sleep(120)

