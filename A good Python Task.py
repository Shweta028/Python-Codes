#!/usr/bin/python2

from datetime import datetime
import platform, os, subprocess, re
from googlesearch import search
import webbrowser
import commands

# Creating function to access date and time
def dateandTime():
	return datetime.now()

# Creating function to extract processor information for different OS
def cpuInfo():
	#  this is platform checking library 
    if platform.system() == "Windows":
        return platform.processor()

	#  for Mac or OS X library 

    elif platform.system() == "Darwin":
        os.environ['PATH'] = os.environ['PATH'] + os.pathsep + '/usr/sbin'
        command ="sysctl -n machdep.cpu.brand_string"
        return subprocess.check_output(command).strip()
	
	# this is for any linux kernel oriented OS 

    elif platform.system() == "Linux":
        command = "lscpu  |  grep -i 'Model name'"
        all_info = subprocess.check_output(command, shell=True)
	cpu_info=all_info.split(":")[1].lstrip().strip()
	return cpu_info
	
        
# Creating function to extract RAM information
def ramInfo():
	y=commands.getoutput('free -m | grep -i mem')
	ram_output=y.split(":")[1].lstrip().split()[0]
	return ram_output+" MB"

# Creating function to call search function from googlesearch module
def searchGoogle():

	query =raw_input("Enter your query : ")
	print  "Searching..."
	for j in search(query, tld="com", num=10, stop=1, pause=2):
		print(j)

# Creating function to call open fucntion of webbrowser module
def openUrl():
	new=2	
	#url="http://www.google.com"
	site=raw_input("Enter the url : ")
	url="http://"+site
	# Open URL in new browser window
	webbrowser.open(url,new=new) # opens in default browser

# Creating function for various Shutdown options
def shutOptions():
	while(1):
		opt=raw_input("Type s/l/h/p for shutdown/logout/hibernate/suspend respectively : ")
		if opt=='s':os.system('shutdown -h now')
		elif opt=='l':
			os.system('gnome-session-quit')
			break
		elif opt=='h':os.system('sudo pm-hibernate')
		elif opt=='p':os.system('sudo pm-suspend')
		else: print("invalid option")	
	
# Creating function to execute command from root access
def rebootSys():
	os.system('sudo reboot')

# Creating function to run python file
def runPyFile():
	loc=raw_input("Enter name of python file with location : ")
	#1st way to run file 
	execfile(loc)
	#2nd way to run file
	os.system('python '+loc)

# Displaying options
while(1):
	print"\nMENU:"
	print"1.DATE and TIME"
	print"2.RAM and CPU"
	print"3.Google Search"
	print"4.Open Website"
	print"5.Shutdown options"
	print"6.Reboot"
	print"7.Run Python File"
	print"8.Exit"
	print"9.Open source code"
	ch=input("\nEnter your choice: ")
	print("\n")
	if ch==1: 
		print"Current DATE and TIME is:",dateandTime()
	elif ch==2:
		print"Your CPU details are: ",cpuInfo()
		print"Your system RAM is: ",ramInfo()
	elif ch==3:
		searchGoogle()
	elif ch==4:
		openUrl()
	elif ch==5:
		shutOpt()
	elif ch==6:
		rebootSys()
	elif ch==7:
		runPyFile()
	elif ch==8:
		exit()
	elif ch==9:
		os.system('gedit Desktop/task.py') # returns to the source code
		exit()
	else:
		print"Please Enter a valid Choice"

	
