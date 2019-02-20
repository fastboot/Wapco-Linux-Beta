import requests
import random
import time
import hashlib
import json
import re
import sys
message = """<!DOCTYPE html>
<html>
<head>
	<title>Analysis</title>
	<link rel="stylesheet" href="../css/design.css">
	<style>
		table {
		    border-collapse: collapse;
		    border-spacing: 0;
		    width: 100%;
		    border: solid #ddd;
		}

		th, td {
		    text-align: center;
		    padding: 14px;
		    min-width:100px;
		}

		tr:nth-child(even){background-color: #f2f2f2}
	</style>
</head>
<body>
<br>
		<div class="w3-container">
			<div class="w3-bar w3-border w3-black">
			  <a href="home.html" style="width:20%" class="w3-bar-item w3-button w3-mobile">Home</a>
			  <a href="analysis.html" style="width:20%" class="w3-bar-item w3-button w3-mobile w3-gray">Analysis</a>
			  <a href="comparator.html" style="width:20%" class="w3-bar-item w3-button w3-mobile">Compare</a>
			  <a href="rankings.html" style="width:20%" class="w3-bar-item w3-button w3-mobile">Rankings</a>
			  <a href="upcoming.html" style="width:20%" class="w3-bar-item w3-button w3-mobile">Upcoming</a>
			</div>
		</div>

	    <div class="w3-container w3-blue w3-margin">
		  <h2>Ranklists</h2>
		</div>
	<div class="w3-container" style="overflow-x:auto;">
		<table>
"""

comp_choice_1= sys.argv[1]
comp_choice_2 = 0
naam=sys.argv[2]

friends_string = ""

if(comp_choice_1=="friends"):
    api_key_1 = sys.argv[3]
    secret_1 = sys.argv[4]
    comp_choice_2 = int(sys.argv[5])

    rand_1 = random.sample(range(100000,999999),1)[0]
    t = int(time.time())
    neo_1 = str(rand_1)+"/user.friends?apiKey="+api_key_1+"&onlyOnline=false&time="+str(t)+"#"+secret_1
    hash_1 = hashlib.sha512(neo_1.encode('utf-8')).hexdigest()
    url_1="http://codeforces.com/api/user.friends?onlyOnline=false&apiKey="+str(api_key_1)+"&time="+str(t)+"&apiSig="+str(rand_1)+str(hash_1)
    
    request_1=requests.get(url = url_1)
    data_1=request_1.json()
    friends_string = naam + ";"
    for x in data_1['result']:
        friends_string += x
        friends_string +=";"

else:
    y_friend = sys.argv[3];
    comp_choice_2 = int(sys.argv[4])
    y_friend = y_friend.replace(":", ";")
    friends_string = naam + ";" + y_friend
    
url_2="http://codeforces.com/api/user.rating?handle="+naam
request_2=requests.get(url=url_2)
data_2=request_2.json()

contest_name = []
list_1 = []

for x in data_2['result']:
	if "Div. 1" in x["contestName"] and "Codeforces" in x["contestName"]:
		st1 = x['contestName']
		f1 = 0
		t1 = ""
		for y in st1:
			if y == ' ' and f1:
				break
			elif y == '#':
				f1 = 1
				t1 += y
			elif f1 == 1:
				t1 += y
		st = "CF Round  <br>" + t1 + " <br> (Div. 1)"
		contest_name.append(st)
		list_1.append(x['contestId'])
	elif "Div. 2" in x["contestName"] and "Educational" not in x["contestName"] and "Codeforces" in x["contestName"]:
		st1 = x['contestName']
		f1 = 0
		t1 = ""
		for y in st1:
			if y == ' ' and f1:
				break
			elif y == '#':
				f1 = 1
				t1 += y
			elif f1 == 1:
				t1 += y
		st = "CF Round <br>" + t1 + " <br>(Div. 2)" 
		
		contest_name.append(st)
		list_1.append(x['contestId'])
	elif "Div. 3" in x["contestName"] and "Codeforces" in x["contestName"]:
		st1 = x['contestName']
		f1 = 0
		t1 = ""
		for y in st1:
			if y == ' ' and f1:
				break
			elif y == '#':
				f1 = 1
				t1 += y
			elif f1 == 1:
				t1 += y
		st = "CF Round <br>" + t1 + " <br>(Div. 3)" 
		contest_name.append(st)
		list_1.append(x['contestId'])
	elif "Educational" in x["contestName"]:
		st1 = x['contestName']
		t1 = ""
		t2 = ""
		f1 = 0
		t1 = st1[st1.index("Round"):]
		for y in t1:
			if(y == ' ' and f1 == 0):
				f1 = 1
			elif(y == ' ' and f1 == 1):
				break
			elif(f1 == 1):
				t2 += y
		t1 = t2
		st = "Educational <br> CF Round <br>" + t1
		contest_name.append(st)
		list_1.append(x['contestId'])

contest_name = contest_name[::-1]
list_1 = list_1[::-1]
medal_tally = []
medal_df = []
max_len = 0

for x in range(0, min(comp_choice_2, len(list_1))):
    url_3 = "http://codeforces.com/api/contest.standings?contestId="+str(list_1[x])+"&handles="+friends_string
    request_3 = requests.get(url=url_3)
    data_3=request_3.json()
    sz=len(data_3['result']['rows'])

    friend = []
    for in_1 in range(0,sz):
        friend.append(data_3['result']['rows'][in_1]['party']['members'][0]['handle'])
    medal_tally.append(friend)

    max_len = max(max_len, int(len(friend)))
    
for i in range(0, max_len):
    some = []
    for j in range(0, len(medal_tally)):
        if(i < len(medal_tally[j])):
            some.append(medal_tally[j][i])
        else:
            some.append("-")
    medal_df.append(some)


message += "\n<tr>\n"
message += """<th style="width:50px";>S.No</th>\n"""

for i in range(min(int(comp_choice_2), len(list_1))):
    message += "<th>" + contest_name[i] + "</th>\n"

message += "</tr>\n"
row = len(medal_df)
col = len(medal_df[0])

for i in range(row - 1):
	message += """<tr>\n"""
	message += "<td>" + str(i + 1) + "." + "</td>\n"
	for j in range(col):
		if i == 0:
			if medal_df[i][j] == "-":
				message += "<td>" + medal_df[i][j] + "</td>\n"
			else:
				message += """<td class="w3-amber">""" + medal_df[i][j] + "</td>\n"
		elif i == 1:
			if medal_df[i][j] == "-":
				message += "<td>" + medal_df[i][j] + "</td>\n"
			else:
				message += """<td class="w3-gray">""" + medal_df[i][j] + "</td>\n"
		elif i == 2:
			if medal_df[i][j] == "-":
				message += "<td>" + medal_df[i][j] + "</td>\n"
			else:
				message += """<td class="w3-orange">""" + medal_df[i][j] + "</td>\n"
		elif medal_df[i][j] != "-":
			if medal_df[i + 1][j] != "-":
				message += "<td>" + medal_df[i][j] + "</td>\n"
			else:
				message += """<td class="w3-brown">""" + medal_df[i][j] + "</td>\n"
		else:
			message += "<td>" + medal_df[i][j] + "</td>\n"
	message += "</tr>\n"

message += "<tr>\n"
message += "<td>" + str(row) + "." + "</td>\n"
for x in medal_df[row - 1]:
	if x == "-":
		message += "<td>" + x + "</td>\n"
	else:
		if row == 3:
			message += """<td class="w3-orange">""" + x + "</td>\n"
		elif row == 2:
			message += """<td class="w3-gray">""" + x + "</td>\n"
		else:
			message += """<td class="w3-brown">""" + x + "</td>\n"
message += """  </tr>
				</table> 
			</div>
		</body>
		</html>
	"""
print(message)

sys.stdout.flush()
