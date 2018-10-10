from __future__ import print_function
import datetime as dt
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from datetime import datetime
import requests
import tzlocal
import json
import pytz
import sys

message = """<html>
<head>
<title>Upcoming</title>
<link rel="stylesheet" href="../css/design.css">
</head>
<body><br>
<div class="w3-container">
			<div class="w3-bar w3-border w3-black">
			  <a href="home.html" style="width:20%" class="w3-bar-item w3-button w3-mobile">Home</a>
			  <a href="analysis.html" style="width:20%" class="w3-bar-item w3-button w3-mobile">Analysis</a>
			  <a href="comparator.html" style="width:20%" class="w3-bar-item w3-button w3-mobile">Compare</a>
			  <a href="rankings.html" style="width:20%" class="w3-bar-item w3-button w3-mobile">Rankings</a>
			  <a href="upcoming.html" style="width:20%" class="w3-bar-item w3-button w3-mobile w3-gray">Upcoming</a>
			</div>
		</div>
		

"""


message += """<div class="w3-container w3-yellow w3-margin">
	  <h2>Update!</h2>
	</div>
	<br>
	<div class="w3-container">
	  <div class="w3-panel w3-pale-yellow w3-leftbar w3-rightbar w3-border-yellow">
	    <p>"""
	    
SCOPES='https://www.googleapis.com/auth/calendar'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('calendar', 'v3', http=creds.authorize(Http()))
now = dt.datetime.utcnow().isoformat() + 'Z'
events_result = service.events().list(calendarId='primary', timeMin=now,maxResults=365, singleEvents=True,orderBy='startTime').execute()
events = events_result.get('items', [])


URL="https://codeforces.com/api/contest.list?gym=false&&locale=en";
req=requests.get(url=URL)
data=req.json()

for x in data['result']:
	if x['phase']=="BEFORE":
		h=0
		for event in events:
			if x['name']==event['summary']:
				h=1
		if h==0:
			stname = x['name']
			fl = 0
			for i in stname:
				if ord(i) < 0 or ord(i) > 128:
					fl =1 
			if fl == 0:
				posix_timestamp_1=x['startTimeSeconds']
				unix_timestamp = float(posix_timestamp_1)
				local_timezone = tzlocal.get_localzone() # get pytz timezone
				local_time = datetime.fromtimestamp(unix_timestamp, local_timezone)
				dt = datetime.fromtimestamp(posix_timestamp_1,local_timezone)
				gog = local_time.strftime('%z')
				gog = gog[:3]+":"+gog[3:]
				en=dt.strftime('%Y-%m-%d'+"T"+'%H:%M:%S'+str(gog))


				posix_timestamp_2=x['startTimeSeconds']+x['durationSeconds']
				unix_timestamp2 = float(posix_timestamp_2)
				local_timezone2 = tzlocal.get_localzone() # get pytz timezone
				local_time2 = datetime.fromtimestamp(unix_timestamp2, local_timezone2)
				dt2 = datetime.fromtimestamp(posix_timestamp_2,local_timezone2)
				gog2 = local_time2.strftime('%z')
				gog2 = gog2[:3]+":"+gog2[3:]
				en2 = dt2.strftime('%Y-%m-%d'+"T"+'%H:%M:%S'+str(gog2))
				
				EVENT = {
				  'summary': x['name'],
				  'location': 'Codeforces',
				  'start': {
				    'dateTime': en
				  },
				  'end': {
				    'dateTime': en2
				  }
				}

				e=service.events().insert(calendarId='primary',sendNotifications='false',body=EVENT).execute()
				st = e['start']['dateTime']
				en = e['end']['dateTime']

				nst = st[:st.index("T")]
				fi = nst.split('-')[2]
				se = nst.split('-')[1]
				th = nst.split('-')[0]

				nst2 = st[st.index("T"):]
				nst2 = nst2[1:nst2.index("+")]

				nst3 = en[:en.index("T")]
				fi3 = nst3.split('-')[2]
				se3 = nst3.split('-')[1]
				th3 = nst3.split('-')[0]

				nst4 = en[en.index("T"):]
				nst4 = nst4[1:nst4.index("+")]
				message +=  e['summary'] + """<br>***Contest added to calendar*** <br>Start: """ + fi+"/"+se+"/"+th + """ at """+nst2+"""<br> """+  """End: """ + fi3+"/"+se3+"/"+th3 + """ at """+nst4+"""<br> """ +"""
				 </p>
			  </div>
			</div>
			<div class="w3-container">
			  <div class="w3-panel w3-pale-yellow w3-leftbar w3-rightbar w3-border-yellow">
			    <p>"""
		else:
			message += """Contest already added! 
			 </p>
	  </div>
	</div>
	<div class="w3-container">
	  <div class="w3-panel w3-pale-yellow w3-leftbar w3-rightbar w3-border-yellow">
	    <p>"""



message += """</p>
		  </div>
		</div><br>
</body>
</html>"""

print(message)
sys.stdout.flush()
