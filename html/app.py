from flask import Flask, request
import time
import os
app = Flask(__name__)



def make_request(full_id,klaar):
    import requests


    token = "/var/www/cookie"
    cookie = open(token,"r").read().strip()
    print("cookie = " + str(cookie))
    cookies = dict(FPWebSession = cookie)
    print("klaar = " + str(klaar))
    #construct url with current date
    if(klaar == "False"):
        url_taak = ("https://kov.schoolware.be/webleerling/bin/server.fcgi/leerling/completeagendatask?AgendapuntID={}&Completed=true").format(full_id)
        r = requests.post(url_taak, cookies=cookies)
        print(r.status_code)
    elif(klaar == "True"):
        url_taak = ("https://kov.schoolware.be/webleerling/bin/server.fcgi/leerling/completeagendatask?AgendapuntID={}&Completed=false").format(full_id)
        r = requests.post(url_taak, cookies=cookies)
        print(r.status_code)
    else:
        print("klaar = " + str(klaar) + " not valid")
    








@app.route('/done', methods=['POST'])
def done():
    print("a request")
    print(request.form) # should display 'bar'
    
    full_id = request.form['id'].strip()
    klaar = request.form['klaar'].strip()
    make_request(full_id,klaar)
    #response.headers.add('Access-Control-Allow-Origin', '*')
    

@app.route('/cookie', methods=['GET'])
def cookie():
    
    f=open("cookie","w")
    cookie = os.popen("python3 /var/www/get_cookie.py").read()
    f.write(cookie)
    f.close()
    return cookie


if __name__=='__main__':
    app.run(port=8081,host='0.0.0.0')
