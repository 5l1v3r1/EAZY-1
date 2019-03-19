import sys 
import urllib2
import os 
import time 
import re
import httplib


def banner() :
   print '''           
                        8EA          888888888       888  888
888888888            888    888            8P        888  888      
888                D8P       D8P          8P         Y88  Y88
888888888         D8P         D8P        8P           8bd8P
888               D8P888888888D8P       8P             88P
888               D8P         D8P      8P               44
888888888         D8P         D8P     888888888         YT 

Coded By r0ckin ; 
Home : m4l4b.blogspot.com &sec4ever.com & v4-team.com 
Contact : xj3@live.fr  ; 
Follow : http://twitter.com/r0ckiin
# '''

if os.name == 'nt':
     os.system('cls')
     os.system('color f')
else:
    os.system('clear')
banner()
print "\n"
print "EAZY Finder ; Reverse IP Lookup & Find Files ... "

ask= raw_input(" Get websites first [yes/no]?  $#")
f=open('rezult.html','w')

	
if ask=="yes" : 
  file=open('dom.txt','w')
  ip=raw_input('ip :')
  con = urllib2.urlopen('http://viewdns.info/reverseip/?host='+ip)
  urlread = con.read()
  find = re.findall('(<tr><td>)(.*?)(</td><td)',urlread)
  number = len(find)
  for sites in range(number) : 
        if sites == 0 :
		  continue
        thefin = find[sites][1]
        file.write(thefin + '\n')	
  con = urllib2.urlopen('http://sameip.org/ip/'+ip)
  urlread = con.read()
  find = re.findall('(<a href="http://)(.*?)(" rel=)',urlread)
  number = len(find)
  for sites in range(number) : 
		thefin = find[sites][1]
		file.write(thefin + '\n')
		os.system('exit')
		
 
else : 
 
 print "You need to add  websites  in dom.txt"

getshell = raw_input(" Scan For Uploaded Shells[yes/no] ? $# ")
getpanels = raw_input(" Scan For  Admin Panels  [yes/no]?  $# ")
getdir = raw_input(" Scan For Sensitive Direcorys [/backup etc ...][yes/no]  ?  $# ")
getzip = raw_input(" Scan For .ZIP Files [Contain database Informations or Backup ]  ?  $# ")
getuploads = raw_input(" Scan For  Uploads [yes/no] ?  $# ")
getinstalls = raw_input(" scan For the Install Folders [yes/no]?  $# ")
f=open("rezult.html","w")
try:
  adminlist = open("admin.txt", "r")
except(IOError):
  print "admin.txt Not Found!"
  exit()
  
try:
  ziplist = open("zip.txt", "r")
except(IOError):
  print "zip.txt Not Found!"
  exit()
  
try:
  dirlist = open("dir.txt", "r")
except(IOError):
  print "dir.txt Not Found!"
  exit()
  
try:
  installlist = open("install.txt", "r")
except(IOError):
  print "install.txt Not Found!"
  exit()
  
try:
  shelllist = open("shell.txt", "r")
except(IOError):
  print "shell.txt Not Found!"
  exit()
  
try:
  uplist = open("upload.txt", "r")
except(IOError):
  print "upload.txt Not Found!"
  exit()  
admins = adminlist.read().split()
shells = shelllist.read().split()
zips = ziplist.read().split()
ups = uplist.read().split()
installs= installlist.read().split()
sensdirs=dirlist.read().split()
sriw=open('dom.txt','r')
sit=sriw.read().split()
def sdirectory() : 
  for dir  in sensdirs:
   for site in sit:
      try:
        conn = httplib.HTTPConnection(site)
        conn.request("HEAD",dir)
        res = conn.getresponse()
        if res.status == 301 or res.status == 302  :
		    f.write("<hr><b>Sinsitive Direcotry  FOund<b> </hr><br>"+site+dir+"<br>")
      except IOError:
		print " Not FounD ... ~#"

def shell() : 
  for shell in shells:
   for site in sit:
      try:
        conn = httplib.HTTPConnection(site)
        conn.request("HEAD",shell)
        res = conn.getresponse()
        if res.status == 200  :
		    f.write("<hr><b>Shell FOund<b> </hr><br>"+site+shell+"<br>")
      except IOError:
		print " Not FounD ... ~#"

	                                           		
def adminss() :
  for admin in admins:
   for site in sit:
      try:
           conn = httplib.HTTPConnection(site)
           conn.request("HEAD",admin)
           res = conn.getresponse()
           if res.status == 200 or res.status == 301 or res.status == 302 :
		    f.write("<hr><b>Admin Panel FOund <b></hr><br>"+site+admin+"<br>")
      except IOError:
		print " Not FounD ... ~#"
			
def zipss() :
  for zip in zips:
   for site in sit:
      try:
           conn = httplib.HTTPConnection(site)
           conn.request("HEAD",zip)
           res = conn.getresponse()
           if res.status == 200 :
		    f.write("<hr><b>.zip  <b></hr><br>"+site+zip+"<br>")
      except IOError:
		print " Not FounD ... ~#"
			
def upss() :
  for up in ups:
   for site in sit:
      try:
           conn = httplib.HTTPConnection(site)
           conn.request("HEAD",up)
           res = conn.getresponse()
           if res.status == 200 :
		    f.write("<hr><b>upload <b></hr><br>"+site+up+"<br>")
      except IOError:
		print "  Not FounD ... ~#"
		
def installss() :
  for install in installs:
   for site in sit:
      try:
           conn = httplib.HTTPConnection(site)
           conn.request("HEAD",install)
           res = conn.getresponse()
           if res.status == 200 or res.status == 301 or res.status == 302 :
		    f.write("<hr><b>Installation  FOund <b></hr><br>"+site+install+"<br>")
      except IOError:
		print "Install  Not FounD ... ~#" 
if getshell=="yes":
 shell()
if getpanels=="yes":
 adminss()
if getzip=="yes":
 zipss()
if getuploads=="yes":
 upss()
if getinstalls=="yes":
 installss()
if getdir=="yes":
 sdirectory()
 
else : 
 print "No Options Selected :D [Ta Khtar Chi haja /D ] "

