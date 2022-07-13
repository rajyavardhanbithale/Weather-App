import requests 
import os
import subprocess
while True:
    try:
        requests.get('https://www.google.com/').status_code
        ncon = 'online'
        break
    except:
        ncon = 'offline'
        break

if ncon == 'online':
   os.system('python3 main.py')

else:
    subprocess.Popen(['python3','-m','http.server'])
    os.system('python3 main_error.py')

