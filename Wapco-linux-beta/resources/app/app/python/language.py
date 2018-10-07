import requests
import random
import time
import hashlib
import json
urlneo     = "https://codeforces.com/api/contest.list?gym=false"
reqneo     = requests.get(url = urlneo)
dataneo    = reqneo.json()
contest_id = []

handle   = set()
language = dict()

len1 = 0

for x in dataneo['result']:
    if(len1 == 2):
        break
    if(x['phase'] == 'BEFORE'):
        continue
    if "Educational" in x["name"]:
        contest_id.append(x['id'])
        len1+=1
    else:
        if "Codeforces Round" in x["name"]:
            if "Div. 1" in x["name"] or "Div. 2" in x["name"] or "Div. 3" in x["name"]:
                contest_id.append(x['id'])
                len1+=1       
for y in contest_id:
    url = "https://codeforces.com/api/contest.status?contestId=" + str(y)
    req = requests.get(url = url)
    data = req.json()
    for x in data['result']:
        hndle = x['author']['members'][0]['handle']
        if hndle in handle:
            continue
        else:
            handle.add(hndle)
            lng = x['programmingLanguage']
            language[lng] = language.get(lng, 0) + 1

language = dict(sorted(language.items(), key=lambda x: x[1], reverse = True))
cnt = 1

for x in language:
    if cnt == 1:
        print("""<div class="container">
              <img src="../images/back.jpg" alt="" style="width:100%;height: 600px;float: left;">
              <div class="content">
                <div style = "width:13%;float:left;margin-right:4%;">
                    <img src = "https://assets.billboard.com/assets/1536864895/images/charts/number-one.svg?2ee93f4eb55e153255fa onerror = this.src="../images/default.webp" style="width:35%;height:140px;float:right;">
                </div>
                <div style = "width:80%;float:left;">
                    <strong style = "color:#FFFFFF;font-size:55px;">""" + x + """ </strong> <br>
                    <i style = "color:#E0E0E0;font-size:24px;"> Number of User &nbsp;: &nbsp;"""+ str(language[x]) + """ </i> <br>
                </div>
            </div>
        </div><div class = "row"> </div>""")
    else:
        s1 = str(cnt)
        while len(s1) < 2:
            s1 = "&nbsp;&nbsp;" + s1
        print("""
        <div class="row" style="background-color:#FFFFFF;">
            <div style = "width:15%;float:left;">
            <p class = "xyz"> <font size = "5"> <b>&nbsp;""" + s1 + """.</b>&nbsp;&nbsp;&nbsp;</font></p>
            </div> 
            <div class = ""w3-bar-item" style="width:85%;float:left;">
                <span> <font size = "5"> <strong> """ + str(x) + """ </strong> </font> </span>
                <br><span> <i style="color:grey;font-size: 18px;">  Number of Active User &nbsp;: &nbsp;""" + str(language[x]) + """</i></span>
            </div></div>""")
    cnt += 1
    if(cnt == 51):
        break
