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
	  <h2>Upcoming!</h2>
	</div>
	<br>
	<div class="w3-container">
	  <div class="w3-panel w3-pale-yellow w3-leftbar w3-rightbar w3-border-yellow">
	    <p>"""
SCOPES='https://www.googleapis.com/auth/calendar.readonly'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('calendar', 'v3', http=creds.authorize(Http()))
now = dt.datetime.utcnow().isoformat() + 'Z'
events_result = service.events().list(calendarId='primary', timeMin=now,maxResults=365, singleEvents=True,orderBy='startTime').execute()
events = events_result.get('items', [])

if not events:
    message += """No upcoming events found.</p>
	  </div>
	</div>
    """
for event in events:
	if event['location'] == "Codeforces":
	    st = event['start']['dateTime']
	    en =  event['end']['dateTime']

	    nst = st[:st.index("T")]
	    fi = nst.split('-')[2]
	    se = nst.split('-')[1]
	    th = nst.split('-')[0]

	    nst2 = st[st.index("T"):]
	    nst2 = nst2[1:nst2.index("+")]
	    #fi2 = nst.split(':')[2]
	    #se2 = nst.split(':')[1]
	    #th2 = nst.split(':')[0] 

	    nst3 = en[:en.index("T")]
	    fi3 = nst3.split('-')[2]
	    se3 = nst3.split('-')[1]
	    th3 = nst3.split('-')[0]

	    nst4 = en[en.index("T"):]
	    nkst4 = nst4[1:nst4.index("+")]

	    message += event['summary'] + """<br> Start: """ + fi+"/"+se+"/"+th + """ at """+nst2+"""<br> """+  """End: """ + fi3+"/"+se3+"/"+th3 + """ at """+nst4+"""<br> """ +""" </p>
		  </div>
		</div><div class="w3-container">
		  <div class="w3-panel w3-pale-yellow w3-leftbar w3-rightbar w3-border-yellow">
		    <p> """
message += """</p>
		  </div>
		</div><br>
</body>
</html>"""

print(message)
sys.stdout.flush()
