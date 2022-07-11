from asyncio.proactor_events import _ProactorBasePipeTransport
from flask import Flask, render_template,request
import os
import requests, json
import time
import sys
import subprocess

app = Flask(__name__)

try:
    if os.name =='posix':
        os.system('mkdir rageapps')
        
        if not os.path.exists(os.path.join('rageapps/cfg')):
            os.system('echo pune > rageapps/cfg')
            print('First Time !!!')
        else:
            pass
    else:
        os.mkdir('.rage-apps')
        

except:
    print('data persistence not available !!')



# URL
api_key = "729d99bd52f8edc51126144a21673993"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
with open('rageapps/cfg','r') as c1:
    city_name = c1.read()
complete_url = base_url + "appid=" + api_key + "&q=" + city_name


print(complete_url)
response = requests.get(complete_url)
x = response.json()


#Icons
def iconn(ids):
    id1 = ids
    if 200<= id1 <=232:
        ico = 'cloud-lightning'
    elif 300<= id1 <=321:
        ico = 'cloud-drizzle'
    elif 500<= id1 <=531:
        ico = 'cloud-rain'
    elif 600<= id1  <=622:
        ico = 'cloud-snow'
    elif 700<= id1 <=781:
        ico = 'wind'
    elif 801<= id1 <=804:
        ico = 'cloud'
    elif 'n' in x['weather'][0]['icon']:
        ico = 'moon'
    else:
        ico = 'sun'
    return ico

@app.route('/')
def index():
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    with open('rageapps/cfg','r') as c1:
        city_name = c1.read()
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name


  
    response = requests.get(complete_url)
    x = response.json()

    return render_template('sideleft.html',day=time.strftime('%A',time.localtime(x['dt'])),
    date=time.strftime('%d %b %Y',time.localtime(x['dt'])),
    city = x['name']+', '+x['sys']['country'],
    tempr = round(int(x['main']['temp'])-273.15),
    main = x['weather'][0]['main'],
    icon = iconn(x['weather'][0]['id'])
    )

@app.route('/side')
def index1():
    
    base_url = "http://api.openweathermap.org/data/2.5/forecast?"
   
    complete_url = base_url + 'appid=' + api_key + '&q=' + city_name + '&count=5'
    with open('rageapps/cfg','r') as c1:
        city_name2 = c1.read()
 
    response = requests.get(complete_url)

    x1 = response.json()
    we = []
    dy = []
    ic = []
    for i in range(0,len(x1['list'])):
        if i%8==0:
            q = round(x1['list'][i]['main']['temp']-273.15)
            e = time.strftime('%A',time.localtime(x1['list'][i]['dt']))
            r = x1['list'][i]['weather'][0]['id']
        
            we.append(q)
            dy.append(e)
            ic.append(r)

    
            


    return render_template('sideright.html',#desc=x['weather'][0]['description'].capitalize(),
    
    desc = x['weather'][0]['description'].title(),
    humid =x['main']['humidity'],
    wind=round(x['wind']['speed']*3.6),
    
    
    d1 = dy[1][0:3],
    d2 = dy[2][0:3],
    d3 = dy[3][0:3],
    d4 = dy[4][0:3],

    w1 = we[1],
    w2 = we[2],
    w3 = we[3],
    w4 = we[4],

    i1=iconn(ic[1]),
    i2=iconn(ic[2]),
    i3=iconn(ic[3]),
    i4=iconn(ic[4]),
    cpn = city_name2
    )
   

@app.route('/', methods=['GET', 'POST'])
def city():

    if request.method == 'POST':
        cname = request.form.get('city')
        base_url = "http://api.openweathermap.org/data/2.5/forecast?"
   
        complete_url = base_url + 'appid=' + api_key + '&q=' + cname
        response = requests.get(complete_url)
        x = response.json()
        
        if x['cod'] == '404':
            subprocess.Popen(["python3","error.py"])
        else:
            try:
                with open('rageapps/cfg','w') as f:
                    f.write(str(cname))
                    f.close 
                    subprocess.Popen(["python3","update.py"])
                    print('Updated !! ')
            except:
                print('error')

        return index1() 
    
    
   

    
if __name__ == '__main__':

    app.run(debug=True,port=8000)
    
    
