def agenda():


    import requests
    from datetime import date
    from datetime import datetime


    def print_html():
        print('<table id="customers">')
        print('<tr>')
        print('<th>vak</th>')
        print('<th>onderwerp</th>')
        print('<th>lokaal</th>')
        print('</tr>')




    token = "/var/www/cookie"
    cookie = open(token, "r").read().strip()

    cookies = dict(FPWebSession=cookie)



    #construct url with current date




    day = datetime.today().day
    day = int(day) + 1

    week = str(datetime.today().year) + "-" + str(datetime.today().month) + "-" + str(day)
    #print(week)
    url_toets = ("https://kov.schoolware.be/webleerling/bin/server.fcgi/REST/AgendaPunt/?_dc=1665930432452&MaxVan={}T00%3A00%3A00&MinTot={}T00%3A00%3A00&Agenda=6819%2C6820%2C15868%2C15869%2C16968&NietMappen=6819%2C16968&MapAgendasOp=6820&page=1&start=0&limit=0").format(week,date.today())
    #url_toets = "https://kov.schoolware.be/webleerling/bin/server.fcgi/REST/AgendaPunt/"





    #make request and check status code
    r = requests.get(url_toets, cookies=cookies)
    #check status code if 401 get new token
    if (r.status_code == 401):



        print('<div class="green">')

        print("needed new token<br>")

        print("thank you for waiting")

        print('</div>')



        cookie = requests.get("http://localhost:8081/cookie", cookies=cookies)



        try:

            open(token, "x").close()



        except:

            a = 1



        #write new cookie to file

        open(token, "w").write(str(cookie.text))





    #read cookie file again



    cookie = open(token, "r").read().strip()



    cookies = dict(FPWebSession=cookie)



    if (cookie == ""):



        raise Exception("error cookie is empty")


    r_toets = requests.get(url_toets, cookies=cookies).json()


    data = r_toets["data"]
    #print(data)

    #    dt = datetime.strptime(i["UniekAgendaPuntTot"], '%Y-%m-%d %H:%M:%S')

    today = datetime.today()
    #today = datetime.strptime("2022-10-17 9:12:50", '%Y-%m-%d %H:%M:%S')
    #    print("<td style='text-align:center'>", get_day(dt), dt.strftime('%d-%m'), "</td>")
    this_day = []
    for i in data:
        dt = datetime.strptime(i["Van"], '%Y-%m-%d %H:%M:%S')
        if(dt.year == today.year and dt.month == today.month and dt.day == today.day):
            this_day.append(i)

    a=True
    b=True
    c=True
    d=True
    e=True
    f=True
    g=True
    h=True

    a_vak=""
    b_vak=""
    c_vak=""
    d_vak=""
    e_vak=""
    f_vak=""
    g_vak=""
    h_vak=""


    for i in this_day:
        
            dt = datetime.strptime(i["Van"], '%Y-%m-%d %H:%M:%S')
            #print("dt.today() = ",dt)
            now = dt
            if(now.hour == 8 and now.minute == 25):
                a_vak=i["VakNaam"]
            elif(now.hour == 9 and now.minute == 15):
                b_vak=i["VakNaam"]
            elif(now.hour == 10 and now.minute == 20):
                c_vak=i["VakNaam"]
            elif(now.hour == 11 and now.minute == 10):
                d_vak=i["VakNaam"]
            elif(now.hour == 12 and now.minute == 55):
                e_vak=i["VakNaam"]
            elif(now.hour == 13 and now.minute == 45):
                f_vak=i["VakNaam"]
            elif(now.hour == 14 and now.minute == 50):
                g_vak=i["VakNaam"]
            elif(now.hour == 15 and now.minute == 40):
                h_vak=i["VakNaam"]


    for i in this_day:
        if(i["TypePunt"] == 2):
            dt = datetime.strptime(i["Van"], '%Y-%m-%d %H:%M:%S')
            #print("dt.today() = ",dt)
            now = dt
            dt = datetime.today()
            if(now.hour == 8 and now.minute == 25):
                a=False
            elif(now.hour == 9 and now.minute == 15):
                b=False
            elif(now.hour == 10 and now.minute == 20):
                c=False
            elif(now.hour == 11 and now.minute == 10):
                d=False
            elif(now.hour == 12 and now.minute == 55):
                e=False
            elif(now.hour == 13 and now.minute == 45):
                f=False
            elif(now.hour == 14 and now.minute == 50):
                g=False
            elif(now.hour == 15 and now.minute == 40):
                h=False


    # print("a="+str(a))
    # print("b="+str(b))
    # print("c="+str(c))
    # print("d="+str(d))
    # print("e="+str(e))
    # print("f="+str(f))
    # print("g="+str(g))
    # print("h="+str(h))


    print_html()





    for i in this_day:
        dt = datetime.strptime(i["Van"], '%Y-%m-%d %H:%M:%S')
        if(dt.year == today.year and dt.month == today.month and dt.day == today.day and i["TypePunt"] == 2):
            print("<td>",i["VakNaam"], "</td>")
            print("<td>",i["Titel"], "</td>")
            print("<td>",i["LokaalCode"], "</td>")  
            print('</tr>')

        elif(dt.year == today.year and dt.month == today.month and dt.day == today.day and i["TypePunt"] == 1):
            if(a==True and i["VakNaam"] == a_vak):
                a=0

                print("<td>",i["VakNaam"], "</td>")
                print("<td>","/", "</td>")
                print("<td>",i["LokaalCode"], "</td>")
                print('</tr>') 
            elif(b==True and i["VakNaam"] == b_vak):
                b=0

                print("<td>",i["VakNaam"], "</td>")
                print("<td>","/", "</td>")
                print("<td>",i["LokaalCode"], "</td>")
                print('</tr>')      
            elif(c==True and i["VakNaam"] == c_vak):

                c=0

                print("<td>",i["VakNaam"], "</td>")
                print("<td>","/", "</td>")
                print("<td>",i["LokaalCode"], "</td>")
                print('</tr>')               
            elif(d==True and i["VakNaam"] == d_vak):
                d=0

                print("<td>",i["VakNaam"], "</td>")
                print("<td>","/", "</td>")
                print("<td>",i["LokaalCode"], "</td>")
                print('</tr>') 
            elif(e==True and i["VakNaam"] == e_vak):
                e=0

                print("<td>",i["VakNaam"], "</td>")
                print("<td>","/", "</td>")
                print("<td>",i["LokaalCode"], "</td>")
                print('</tr>')      
            elif(f==True and i["VakNaam"] == f_vak):
                f=0
    
                print("<td>",i["VakNaam"], "</td>")
                print("<td>","/", "</td>")
                print("<td>",i["LokaalCode"], "</td>")
                print('</tr>') 
            elif(g==True and i["VakNaam"] == g_vak):
                g=0
            
                print("<td>",i["VakNaam"], "</td>")
                print("<td>","/", "</td>")
                print("<td>",i["LokaalCode"], "</td>")
                print('</tr>') 
            elif(h==True and i["VakNaam"] == h_vak):
                h=0
            
                print("<td>",i["VakNaam"], "</td>")
                print("<td>","/", "</td>")
                print("<td>",i["LokaalCode"], "</td>")
                print('</tr>') 

