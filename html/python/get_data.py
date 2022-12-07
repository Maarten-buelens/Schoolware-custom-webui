def taken():

    import requests


    from datetime import date


    from datetime import datetime


    import json


    print('<div id="process" class="green" style="display:none;">processing please wait</div>')


    def print_html():

        print('<table id="customers">')

        print('<tr>')

        print('<th>soort</th>')

        print('<th>vak</th>')

        print('<th>titel</th>')

        print('<th>extra</th>')

        print('<th>eind datum</th>')

        print('<th>tijd over</th>')

        print('<th>klaar</th>')

        print('<th>klaar?</th>')

        print('</tr>')


    def get_day(dt):

        day = dt.weekday()

        if (day == 0):

            return "maandag"

        elif (day == 1):

            return "dinsdag"

        elif (day == 2):

            return "woensdag"

        elif (day == 3):

            return "donderdag"

        elif (day == 4):

            return "vrijdag"

        elif (day == 5):

            return "zaterdag"

        elif (day == 6):

            return "zondag"


    #read cookie file

    import os
    print(os.system("echo %cd%"))
    token = "/var/www/cookie"


    cookie = open(token, "r").read().strip()


    cookies = dict(FPWebSession=cookie)


    #construct url with current date


    url_taak = "https://kov.schoolware.be/webleerling/bin/server.fcgi/REST/AgendaPunt/?_dc=1665240724814&Agenda=15868%2C15869&offset=0&limit=40&MaxVan=2023-06-30T00%3A00%3A00&MinVan={}T00%3A00%3A00&IsTaak=true&VervaltOfWees=false&page=1&start=0".format(



        date.today())


    url_toets = "https://kov.schoolware.be/webleerling/bin/server.fcgi/REST/AgendaPunt/?_dc=1665240724814&Agenda=15868%2C15869&offset=0&limit=40&MaxVan=2023-06-30T00%3A00%3A00&MinVan={}T00%3A00%3A00&IsToets=true&VervaltOfWees=false&page=1&start=0".format(



        date.today())


    #make request and check status code


    r = requests.get(url_taak, cookies=cookies)


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


    #make real request for tests


    print_html()


    r_taak = requests.get(url_taak, cookies=cookies).json()


    # print(r_taak)


    #get the data


    data_taak = r_taak["data"]


    #make real request for tasks


    r_toets = requests.get(url_toets, cookies=cookies).json()


    #get the data


    data_toets = r_toets["data"]


    #print(type(data_taak))


    list_taak = []


    for i in data_taak:

        i["taak"] = True

        list_taak.append(i)



    list_all = []


    for i in data_toets:

        list_taak.append(i)


    list_all = list_taak





    list_all.sort(key=lambda x: datetime.strptime(
        x['Van'], '%Y-%m-%d %H:%M:%S'))



    c = 0


    for i in list_all:

        c += 1

        if (c % 2):

            print('<tr>')

        else:

            print('<tr style="background-color: #222125;">')

        try:

            if (i["taak"] == True):

                print('<td><div id="taak" style="text-align:center"> taak </div></td>')

            else:

                print('<td><div id="toets" style="text-align:center"> toets </div></td>')

        except:

            print('<td><div id="toets" style="text-align:center"> toets </div></td>')

        print("<td style='text-align:center'>", i["VakNaam"], "</td>")

        print("<td>", i["Titel"], "</td>")

        print("<td>", i["Commentaar"], "</td>")

        dt = datetime.strptime(i["Van"], '%Y-%m-%d %H:%M:%S')

        print("<td style='text-align:center'>",

            get_day(dt), dt.strftime('%d-%m'), "</td>")

        dif = (dt - datetime.today())
        diff = (dt - datetime.today())

        dif = str(dif).split(".")[0]

        if ("-" in dif):

            print("contains -")
        #print(diff.today())
        try:

            if ("-" not in dif):

                if (i["Completed"] == "nbFalse" and diff.total_seconds() < (24*60*60)):

                    print("<td style='text-align:center'>", dif, "&#x2757</td>")

                else:

                    print("<td style='text-align:center'>", dif, "</td>")

            else:

                print("<td style='text-align:center'>gedaan</td>")

        except:

            if ("-" in dif):

                print("<td style='text-align:center'>gedaan</td>")

            else:

                print("<td style='text-align:center'>", dif, "</td>")

        

        klaar = "none"

        try:

            if (i["taak"] == True):

                if (i["Completed"] == "nbFalse"):

                    print("<td class='red' style='text-align:center'>&#x2716</td>")

                    klaar = False

                else:

                    print("<td class='green' style='text-align:center'>&#x2714;</td>")

                    klaar = True

        except:

            print("<td style='text-align:center'>/</td>")

        try:

            a = i["taak"]

            print("<td>", ('<button class="button" onclick=complete(' +

                        str(c) + ',"' + str(klaar) + '")>done</button>'), "</td>")

        except:

            print("<td>", ('<button class="button" disabled onclick=complete(' +

                        str(c) + ',"' + str(klaar) + '")>done</button>'), "</td>")

        print("<td>", ('<div id="{}" style="display:none;">').format(



            c), i["ID"], '</div>', "</td>")

        print('</tr>')
