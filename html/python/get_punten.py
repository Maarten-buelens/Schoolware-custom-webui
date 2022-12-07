def punten():

    import requests
    from datetime import datetime
    import math


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


    def print_html():

        print('<table id="customers">')

        print('<tr>')

        print('<th style="text-align:center">soort</th>')

        print('<th style="text-align:center">vak</th>')

        print('<th style="text-align:center">commentaar</th>')

        print('<th style="text-align:center">datum</th>')

        print('<th style="text-align:center">publicatie datum</th>')

        print('<th style="text-align:center">punt</th>')

        print('<th style="text-align:center">%</th>')

        print('</tr>')

    token = "/var/www/cookie"
    cookie = open(token, "r").read().strip()
    cookies = dict(FPWebSession=cookie)

    #construct url with current date

    #url_taak = "https://kov.schoolware.be/webleerling/bin/server.fcgi/REST/PuntenbladGrid?BeoordelingMomentVan=2022-09-01+00:00:00&Leerling=15201"
    url_taak = "https://kov.schoolware.be/webleerling/bin/server.fcgi/REST/PuntenbladGridLeerling?BeoordelingMomentVan=2022-09-01+00:00:00&BeoordelingMomentTot=2022-12-25+22:32:05"#&Leerling=15201"


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


    #make request and json data
    r = requests.get(url_taak, cookies=cookies).json()

    #take only data
    data = r["data"]
    #print(data)
    print_html()
    c = 0


    evalu = []
    #get points
    for i in data:
        i = i["Beoordelingen"]
        evalu.append(i)
    all_eval = []

    #make new list
    for i in evalu:
        for x in i:
            all_eval.append(x)

    #sort list by time
    all_eval.sort(key=lambda x: datetime.strptime(
        x['BeoordelingMomentDatum'], '%Y-%m-%d %H:%M:%S'), reverse=True)
    #print(all_eval)
    prev = 0
    #for every point
    for i in all_eval:

        #print("prev = " , str(prev))
        #print("code = ",str(i["DagelijksWerkCode"]))
        #print(i)

        if (i["BeoordelingMomentType_"] == "bmtToets"):
            print("<td class='red' style='width:5%'>toets</td>")
        else:
            print("<td class='orange' style='width:5%;color: orange;'>taak</td>")

        #name
        print("<td style='width:20%'>",
            i["IngerichtVakNaamgebruiker"], "</td>")
        #titel point
        print("<td style='width:20%'>",
            i["BeoordelingMomentOmschrijving"], "</td>")
        #date of point
        dt = datetime.strptime(
            i["BeoordelingMomentDatum"], '%Y-%m-%d %H:%M:%S')
        print("<td style='width:10%'>", get_day(
            dt), dt.strftime('%d-%m'), "</td>")
        #date of publication
        dt = datetime.strptime(
            i["BeoordelingMomentPublicatieDatum"], '%Y-%m-%d %H:%M:%S')
        if (dt.strftime('%H:%M') != "00:00"):
            print("<td style='width:10%'>", get_day(dt),
                dt.strftime('%d-%m %H:%M'), "</td>")
        else:
            print("<td style='width:10%'>", get_day(
                dt), dt.strftime('%d-%m'), "</td>")
            #get only numbers of point
        try:
            punt = i["BeoordelingWaarde"]
            cijfer = round(float(punt["NumeriekAsString"]) * int(i["BeoordelingMomentNoemer"]),2)
            tot = int(i["BeoordelingMomentNoemer"])
            pro = float(punt["NumeriekAsString"]) * 100

            if (cijfer >= (tot/2)):
                goed = "good"
            else:
                goed = "bad"
            print("<td>", ('<div data-v-4bbde73e="" class="progress"><div data-v-4bbde73e="" role="progressbar" aria-valuenow="40" aria-valuemin="0" aria-valuemax="100" class="progress-bar-{} progress-bar-success" style="width: {}%;"><span style="margin-left:50%;" data-v-4bbde73e="">{} / {}</span></div></div>').format(goed, pro, cijfer, tot), "</td>")
            c += 1
            print("<td style='width:5%'>", str(
                round(((cijfer/tot)*100), 2)), "%</td>")
        except:
            print("<td>n/a or see other</td>")
        print("</tr>")
        if (i["DagelijksWerkCode"] == "DW 1" and prev == 1):
            prev = 0
            print("<tr>")
            print("<td style='text-align: center;background-color: #5a5a5a;font-family: Helvetica;'>DW1</td>")
            print("<td style='text-align: center;background-color: #5a5a5a;font-family: Helvetica;'>DW1</td>")
            print("<td style='text-align: center;background-color: #5a5a5a;font-family: Helvetica;'>DW1</td>")
            print("<td style='text-align: center;background-color: #5a5a5a;font-family: Helvetica;'>DW1</td>")
            print("<td style='text-align: center;background-color: #5a5a5a;font-family: Helvetica;'>DW1</td>")
            print("<td style='text-align: center;background-color: #5a5a5a;font-family: Helvetica;'>DW1</td>")
            print("<td style='text-align: center;background-color: #5a5a5a;font-family: Helvetica;'>DW1</td>")
            print("</tr>")

        if (i["DagelijksWerkCode"] == "DW 2"):
            prev = 1
