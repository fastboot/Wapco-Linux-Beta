import sys
import requests
import time
import hashlib
import random
from datetime import datetime
import os

handle1 = sys.argv[1]
handle2 = sys.argv[2]
#global variables for html-----------------------------------------------------------------------------------------| 
handle1_verdict_ok = 0
handle1_verdict_wa = 0
handle1_verdict_tle = 0
handle1_verdict_mle = 0
handle1_verdict_rte = 0
handle1_verdict_ce = 0
handle1_verdict_oth = 0

handle1_contri = 0
handle1_friends = 0
handle1_max_rating = 0
handle1_min_rating = 1500
handle1_curr_rating = 0
handle1_profile_pic = ""
handle1_avg = 0.0
handle1_accu = 0.0

handle1_implementation = 0
handle1_greedy = 0
handle1_math = 0
handle1_brute_force = 0
handle1_dp = 0
handle1_strings = 0
handle1_sortings = 0
handle1_constructive_algorithms = 0
handle1_dfs_similar = 0
handle1_binary_search = 0
handle1_trees = 0
handle1_two_pointers = 0
handle1_graphs = 0
handle1_number_theory = 0
handle1_data_structures = 0
handle1_games = 0
handle1_combinatorics = 0
handle1_graph_matchings = 0 
handle1_geometry = 0
handle1_bitmasks = 0
handle1_dsu = 0
handle1_shortest_paths = 0
handle1_special = 0
handle1_probabilities = 0
handle1_matrices = 0
handle1_expression_parsing = 0
handle1_hashing = 0
handle1_flows = 0

handle1_GNU_C14 = 0
handle1_GNU_C11 = 0
handle1_GNU_C17 = 0
handle1_Java_8 = 0
handle1_Python_3 = 0
handle1_GNU_C11 = 0
handle1_MS_C = 0
handle1_Python_2 = 0
handle1_PyPy_3 = 0
handle1_PyPy_2 = 0
handle1_Mono_C = 0
handle1_FPC = 0
handle1_PascalABC = 0
handle1_JavaScript = 0
handle1_Perl = 0
handle1_Kotlin = 0
handle1_Clang17_Diagnostics = 0
handle1_Ruby = 0
handle1_Go = 0
handle1_PHP = 0
handle1_Delphi = 0
handle1_Ocaml = 0
handle1_Rust = 0
handle1_Scala = 0
handle1_D = 0


handle2_verdict_ok = 0
handle2_verdict_wa = 0
handle2_verdict_tle = 0
handle2_verdict_mle = 0
handle2_verdict_rte = 0
handle2_verdict_ce = 0
handle2_verdict_oth = 0

handle2_contri = 0
handle2_friends = 0
handle2_max_rating = 0
handle2_min_rating = 1500
handle2_curr_rating = 0
handle2_profile_pic = ""
handle2_avg = 0.0
handle2_accu = 0.0

handle2_implementation = 0
handle2_greedy = 0
handle2_math = 0
handle2_brute_force = 0
handle2_dp = 0
handle2_strings = 0
handle2_sortings = 0
handle2_constructive_algorithms = 0
handle2_dfs_similar = 0
handle2_binary_search = 0
handle2_trees = 0
handle2_two_pointers = 0
handle2_graphs = 0
handle2_number_theory = 0
handle2_data_structures = 0
handle2_games = 0
handle2_combinatorics = 0
handle2_graph_matchings = 0 
handle2_geometry = 0
handle2_bitmasks = 0
handle2_dsu = 0
handle2_shortest_paths = 0
handle2_special = 0
handle2_probabilities = 0
handle2_matrices = 0
handle2_expression_parsing = 0
handle2_hashing = 0
handle2_flows = 0


handle2_GNU_C14 = 0
handle2_GNU_C11 = 0
handle2_GNU_C17 = 0
handle2_Java_8 = 0
handle2_Python_3 = 0
handle2_GNU_C11 = 0
handle2_MS_C = 0
handle2_Python_2 = 0
handle2_PyPy_3 = 0
handle2_PyPy_2 = 0
handle2_Mono_C = 0
handle2_FPC = 0
handle2_PascalABC = 0
handle2_JavaScript = 0
handle2_Perl = 0
handle2_Kotlin = 0
handle2_Clang17_Diagnostics = 0
handle2_Ruby = 0
handle2_Go = 0
handle2_PHP = 0
handle2_Delphi = 0
handle2_Ocaml = 0
handle2_Rust = 0
handle2_Scala = 0
handle2_D = 0


mnth = {}
mnth1 = {}

mnth["01"] = "JAN"
mnth["02"] = "FEB"
mnth["03"] = "MAR"
mnth["04"] = "APR"
mnth["05"] = "MAY"
mnth["06"] = "JUN"
mnth["07"] = "JUL"
mnth["08"] = "AUG"
mnth["09"] = "SEP"
mnth["10"] = "OCT"
mnth["11"] = "NOV"
mnth["12"] = "DEC"

mnth1["JAN"] = 1
mnth1["FEB"] = 2
mnth1["MAR"] = 3
mnth1["APR"] = 4
mnth1["MAY"] = 5
mnth1["JUN"] = 6
mnth1["JUL"] = 7
mnth1["AUG"] = 8
mnth1["SEP"] = 9
mnth1["OCT"] = 10
mnth1["NOV"] = 11
mnth1["DEC"]  = 12



# for all submissions ----------------------------------------------------------------------------------------------|
sol1 = dict()
sol2 = dict()

# for handle1
URL_1 = "https://codeforces.com/api/user.status?handle="+handle1
req_1 = requests.get(url = URL_1)
d_1 = req_1.json()
for r in d_1['result']:
	if r['verdict'] == "OK":
		handle1_verdict_ok += 1
	elif r['verdict'] == "WRONG_ANSWER":
		handle1_verdict_wa += 1
	elif r['verdict'] == "TIME_LIMIT_EXCEEDED":
		handle1_verdict_tle += 1
	elif r['verdict'] == "MEMORY_LIMIT_EXCEEDED":
		handle1_verdict_mle += 1
	elif r['verdict'] == "RUNTIME_ERROR":
		handle1_verdict_rte += 1
	elif r['verdict'] == "COMPILATION_ERROR":
		handle1_verdict_ce += 1
	else:
		handle1_verdict_oth += 1

	if r['programmingLanguage'] == "GNU C++14":
	    handle1_GNU_C14+= 1
	elif r['programmingLanguage'] == "GNU C++11":
	    handle1_GNU_C11+= 1
	elif r['programmingLanguage'] == "GNU C++17":
	    handle1_GNU_C17+= 1
	elif r['programmingLanguage'] == "Java 8":
	    handle1_Java_8+= 1
	elif r['programmingLanguage'] == "Python 3":
	    handle1_Python_3+= 1
	elif r['programmingLanguage'] == "GNU C11":
	    handle1_GNU_C11+= 1
	elif r['programmingLanguage'] == "MS C++":
	    handle1_MS_C+= 1
	elif r['programmingLanguage'] == "Python 2":
	    handle1_Python_2+= 1
	elif r['programmingLanguage'] == "PyPy 3":
	    handle1_PyPy_3+= 1
	elif r['programmingLanguage'] == "PyPy 2":
	    handle1_PyPy_2+= 1
	elif r['programmingLanguage'] == "Mono C#":
	    handle1_Mono_C+= 1
	elif r['programmingLanguage'] == "FPC":
	    handle1_FPC+= 1
	elif r['programmingLanguage'] == "PascalABC.NET":
	    handle1_PascalABC+= 1
	elif r['programmingLanguage'] == "JavaScript":
	    handle1_JavaScript+= 1
	elif r['programmingLanguage'] == "Perl":
	    handle1_Perl+= 1
	elif r['programmingLanguage'] == "Kotlin":
	    handle1_Kotlin+= 1
	elif r['programmingLanguage'] == "Clang++17 Diagnostics":
	    handle1_Clang17_Diagnostics+= 1
	elif r['programmingLanguage'] == "Ruby":
	    handle1_Ruby+= 1
	elif r['programmingLanguage'] == "Go":
	    handle1_Go+= 1
	elif r['programmingLanguage'] == "PHP":
	    handle1_PHP+= 1
	elif r['programmingLanguage'] == "Delphi":
	    handle1_Delphi+= 1
	elif r['programmingLanguage'] == "Ocaml":
	    handle1_Ocaml+= 1
	elif r['programmingLanguage'] == "Rust":
	    handle1_Rust+= 1
	elif r['programmingLanguage'] == "Scala":
	    handle1_Scala+= 1
	else:
	    handle1_D+= 1

	for x in r['problem']['tags']:
		if x == "implementation":
			handle1_implementation += 1
		elif x == "greedy":
			handle1_greedy += 1 
		elif x == "math":
			handle1_math += 1 
		elif x == "brute force":
			handle1_brute_force += 1 
		elif x == "dp":
			handle1_dp += 1 
		elif x == "strings":
			handle1_strings += 1 
		elif x == "sortings":
			handle1_sortings += 1 
		elif x == "constructive algorithms":
			handle1_constructive_algorithms += 1 
		elif x == "dfs and similar":
			handle1_dfs_similar += 1 
		elif x == "binary search":
			handle1_binary_search += 1 
		elif x == "trees":
			handle1_trees += 1 
		elif x == "two pointers":
			handle1_two_pointers += 1 
		elif x == "graphs":
			handle1_graphs += 1 
		elif x == "number theory":
			handle1_number_theory += 1 
		elif x == "data structures":
			handle1_data_structures += 1 
		elif x == "games":
			handle1_games += 1 
		elif x == "combinatorics":
			handle1_combinatorics += 1 
		elif x == "graph matchings":
			handle1_graph_matchings += 1 
		elif x == "geometry":
			handle1_geometry += 1 
		elif x == "bitmasks":
			handle1_bitmasks += 1 
		elif x == "dsu":
			handle1_dsu += 1 
		elif x == "shortest paths":
			handle1_shortest_paths += 1 
		elif x == "*special":
			handle1_special += 1 
		elif x == "probabilities":
			handle1_probabilities += 1 
		elif x == "matrices":
			handle1_matrices += 1 
		elif x == "expression parsing":
			handle1_expression_parsing += 1 
		elif x == "hashing":
			handle1_hashing += 1 
		else:
			handle1_flows += 1 

handle1_accu = handle1_verdict_ok/(handle1_verdict_ok+handle1_verdict_oth+handle1_verdict_wa+handle1_verdict_tle+handle1_verdict_mle+handle1_verdict_rte+handle1_verdict_ce)
handle1_accu *= 100
# for solved problems in each cntst

contst_ac = {}
contst_to = {}
c_id = set()
rating1 = []
for x in d_1['result']:
    if x['author']['participantType'] == "CONTESTANT":
        _id = x['problem']['contestId']
        c_id.add(_id)
        contst_ac[_id] = contst_ac.get(_id, 0) + 0
        if x['verdict'] == "OK":
            contst_ac[_id] = contst_ac.get(_id, 0) + 1
        contst_to[_id] = contst_to.get(_id, 0) + 1

    

# for handle2
URL_2 = "https://codeforces.com/api/user.status?handle="+handle2
req_2 = requests.get(url = URL_2)
d_2 = req_2.json()
for r in d_2['result']:
	if r['verdict'] == "OK":
		handle2_verdict_ok += 1
	elif r['verdict'] == "WRONG_ANSWER":
		handle2_verdict_wa += 1
	elif r['verdict'] == "TIME_LIMIT_EXCEEDED":
		handle2_verdict_tle += 1
	elif r['verdict'] == "MEMORY_LIMIT_EXCEEDED":
		handle2_verdict_mle += 1
	elif r['verdict'] == "RUNTIME_ERROR":
		handle2_verdict_rte += 1
	elif r['verdict'] == "COMPILATION_ERROR":
		handle2_verdict_ce += 1
	else:
		handle2_verdict_oth += 1 

	if r['programmingLanguage'] == "GNU C++14":
	    handle2_GNU_C14+= 1
	elif r['programmingLanguage'] == "GNU C++11":
	    handle2_GNU_C11+= 1
	elif r['programmingLanguage'] == "GNU C++17":
	    handle2_GNU_C17+= 1
	elif r['programmingLanguage'] == "Java 8":
	    handle2_Java_8+= 1
	elif r['programmingLanguage'] == "Python 3":
	    handle2_Python_3+= 1
	elif r['programmingLanguage'] == "GNU C11":
	    handle2_GNU_C11+= 1
	elif r['programmingLanguage'] == "MS C++":
	    handle2_MS_C+= 1
	elif r['programmingLanguage'] == "Python 2":
	    handle2_Python_2+= 1
	elif r['programmingLanguage'] == "PyPy 3":
	    handle2_PyPy_3+= 1
	elif r['programmingLanguage'] == "PyPy 2":
	    handle2_PyPy_2+= 1
	elif r['programmingLanguage'] == "Mono C#":
	    handle2_Mono_C+= 1
	elif r['programmingLanguage'] == "FPC":
	    handle2_FPC+= 1
	elif r['programmingLanguage'] == "PascalABC.NET":
	    handle2_PascalABC+= 1
	elif r['programmingLanguage'] == "JavaScript":
	    handle2_JavaScript+= 1
	elif r['programmingLanguage'] == "Perl":
	    handle2_Perl+= 1
	elif r['programmingLanguage'] == "Kotlin":
	    handle2_Kotlin+= 1
	elif r['programmingLanguage'] == "Clang++17 Diagnostics":
	    handle2_Clang17_Diagnostics+= 1
	elif r['programmingLanguage'] == "Ruby":
	    handle2_Ruby+= 1
	elif r['programmingLanguage'] == "Go":
	    handle2_Go+= 1
	elif r['programmingLanguage'] == "PHP":
	    handle2_PHP+= 1
	elif r['programmingLanguage'] == "Delphi":
	    handle2_Delphi+= 1
	elif r['programmingLanguage'] == "Ocaml":
	    handle2_Ocaml+= 1
	elif r['programmingLanguage'] == "Rust":
	    handle2_Rust+= 1
	elif r['programmingLanguage'] == "Scala":
	    handle2_Scala+= 1
	else:
	    handle2_D+= 1

	for x in r['problem']['tags']:
		if x == "implementation":
			handle2_implementation += 1
		elif x == "greedy":
			handle2_greedy += 1 
		elif x == "math":
			handle2_math += 1 
		elif x == "brute force":
			handle2_brute_force += 1 
		elif x == "dp":
			handle2_dp += 1 
		elif x == "strings":
			handle2_strings += 1 
		elif x == "sortings":
			handle2_sortings += 1 
		elif x == "constructive algorithms":
			handle2_constructive_algorithms += 1 
		elif x == "dfs and similar":
			handle2_dfs_similar += 1 
		elif x == "binary search":
			handle2_binary_search += 1 
		elif x == "trees":
			handle2_trees += 1 
		elif x == "two pointers":
			handle2_two_pointers += 1 
		elif x == "graphs":
			handle2_graphs += 1 
		elif x == "number theory":
			handle2_number_theory += 1 
		elif x == "data structures":
			handle2_data_structures += 1 
		elif x == "games":
			handle2_games += 1 
		elif x == "combinatorics":
			handle2_combinatorics += 1 
		elif x == "graph matchings":
			handle2_graph_matchings += 1 
		elif x == "geometry":
			handle2_geometry += 1 
		elif x == "bitmasks":
			handle2_bitmasks += 1 
		elif x == "dsu":
			handle2_dsu += 1 
		elif x == "shortest paths":
			handle2_shortest_paths += 1 
		elif x == "*special":
			handle2_special += 1 
		elif x == "probabilities":
			handle2_probabilities += 1 
		elif x == "matrices":
			handle2_matrices += 1 
		elif x == "expression parsing":
			handle2_expression_parsing += 1 
		elif x == "hashing":
			handle2_hashing += 1 
		else:
			handle2_flows += 1 

handle2_accu = handle2_verdict_ok/(handle2_verdict_ok+handle2_verdict_oth+handle2_verdict_wa+handle2_verdict_tle+handle2_verdict_mle+handle2_verdict_rte+handle2_verdict_ce)
handle2_accu *= 100
# for solved problems in each cntst

contst_ac2 = {}
contst_to2 = {}
c_id2 = set()

for x2 in d_2['result']:
    if x2['author']['participantType'] == "CONTESTANT":
        _id2 = x2['problem']['contestId']
        c_id2.add(_id2)
        contst_ac2[_id2] = contst_ac2.get(_id2, 0) + 0
        if x2['verdict'] == "OK":
            contst_ac2[_id2] = contst_ac2.get(_id2, 0) + 1
        contst_to2[_id2] = contst_to2.get(_id2, 0) + 1


# for rating graph ---------------------------------------------------------------------------------------------------|

# for handle1
URL_1 = "https://codeforces.com/api/user.rating?handle="+handle1
req_1 = requests.get(url = URL_1)
d_1 = req_1.json()
fd_1 = d_1
rating1 = []
tmptot = 0
tmpac = 0 
for x in d_1['result']:
	if x['contestId'] in contst_ac:
		tmptot += 1
		tmpac += contst_ac[x['contestId']]
		
		date1 = x['ratingUpdateTimeSeconds']
		month = mnth[datetime.utcfromtimestamp(date1).strftime('%m')]
		year = datetime.utcfromtimestamp(date1).strftime('%y')
		day = datetime.utcfromtimestamp(date1).strftime('%d')

		date1 = str(day) + " " + month + " " + "20" + str(year)
		rating1.append([date1, x['newRating']])

#rating1.reverse()
handle1_avg = tmpac/tmptot

# for handle2
URL_2 = "https://codeforces.com/api/user.rating?handle="+handle2
req_2 = requests.get(url = URL_2)
d_2 = req_2.json()
fd_2 = d_2
rating2 = []
tmptot = 0
tmpac = 0 
for x in d_2['result']:
	if x['contestId'] in contst_ac2:
		tmptot += 1
		tmpac += contst_ac2[x['contestId']]
		date2 = x['ratingUpdateTimeSeconds']
		month2 = mnth[datetime.utcfromtimestamp(date2).strftime('%m')]
		year2 = datetime.utcfromtimestamp(date2).strftime('%y')
		day = datetime.utcfromtimestamp(date2).strftime('%d')

		#date1 = day + " " + month + " " + str(year)
		date2 = str(day) + " " + month2 + " " + "20" + str(year2)
		rating2.append([date2, x['newRating']])

#rating2.reverse()
handle2_avg = tmpac/tmptot


dataset = []
prevr1 = -1
prevr2 = -1
i = 0
j = 0

while i < len(rating1) and j < len(rating2):
	date1 = datetime.strptime(rating1[i][0], '%d %b %Y')
	date2 = datetime.strptime(rating2[j][0], '%d %b %Y')
	if date1 == date2:
		dataset.append([rating1[i][0], rating1[i][1], rating2[j][1]])
		prevr1 = rating1[i][1]
		prevr2 = rating2[j][1]
		i += 1
		j += 1
	else:
		if(date1 > date2):
			dataset.append([rating2[j][0], prevr1, rating2[j][1]])
			prevr2 = rating2[j][1]
			j += 1
		else :
			prevr1 = rating1[i][1]
			dataset.append([rating1[i][0], rating1[i][1], prevr2])
			i += 1
if i < len(rating1):
	dataset.append([rating1[i][0], rating1[i][1], prevr2])
	i += 1
if j < len(rating2):
	dataset.append([rating2[j][0], prevr1, rating2[j][1]])
	j += 1

# for contribution and friends ---------------------------------------------------------------------------------------|

# for handle1
URL_1 = "http://codeforces.com/api/user.info?handles="+handle1
req_1 = requests.get(url = URL_1)
d_1 = req_1.json()
handle1_max_rating = d_1['result'][0]['maxRating']
handle1_curr_rating = d_1['result'][0]['rating']
handle1_contri = d_1['result'][0]['contribution']*3
handle1_friends = d_1['result'][0]['friendOfCount']
handle1_profile_pic = str(d_1['result'][0]['titlePhoto']) 
if handle1_contri < 0:
	handle1_contri = 0

# for handle2
URL_2 = "http://codeforces.com/api/user.info?handles="+handle2
req_2 = requests.get(url = URL_2)
d_2 = req_2.json()
handle2_max_rating = d_2['result'][0]['maxRating']
handle2_curr_rating = d_2['result'][0]['rating']
handle2_contri = d_2['result'][0]['contribution']*3
handle2_friends = d_2['result'][0]['friendOfCount']
handle2_profile_pic = str(d_2['result'][0]['titlePhoto'])

if handle2_contri < 0:
	handle2_contri = 0

# for table -----------------------------------------------------------------------------------------------------| 

# for handle1
lstf_rnks = []
lstf_rnks2 = []

lstf_rat_chg = []
lstf_rat_chg2 = []

lstf_sol = []
lstf_sol2 = []

d = 1500
d2 = 1500 
for x in fd_1['result']:
	if handle1_min_rating > x['newRating']:
		handle1_min_rating = x['newRating']
	if handle1_min_rating > x['oldRating']:
		handle1_min_rating = x['oldRating']
	if x['contestId'] in contst_ac:
		lstf_rnks.append(x['rank'])
		lstf_rat_chg.append(x['newRating']-x['oldRating'])
		lstf_sol.append(contst_ac[x['contestId']])

lstf_rnks.reverse()
lstf_sol.reverse()
lstf_rat_chg.reverse()

while len(lstf_rnks) < 5:
	lstf_rnks.append('X')

while len(lstf_sol) < 5:
	lstf_sol.append('X')

while len(lstf_rat_chg) < 5:
	lstf_rat_chg.append('X')


# for handle2
for x in fd_2['result']:
	if handle2_min_rating > x['newRating']:
		handle2_min_rating = x['newRating']
	if handle2_min_rating > x['oldRating']:
		handle2_min_rating = x['oldRating']
	if x['contestId'] in contst_ac2:
		lstf_rnks2.append(x['rank'])
		lstf_rat_chg2.append(x['newRating']-x['oldRating'])
		lstf_sol2.append(contst_ac2[x['contestId']])

lstf_rnks2.reverse()
lstf_sol2.reverse()
lstf_rat_chg2.reverse()

while len(lstf_rnks2) < 5:
	lstf_rnks2.append('X')

while len(lstf_sol2) < 5:
	lstf_sol2.append('X')

while len(lstf_rat_chg2) < 5:
	lstf_rat_chg2.append('X')


message = """<!DOCTYPE html>
<html>
<head> 
<title>Compare</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="../css/design.css">
	<style>
	table {
	    
	    border-spacing: 0;
	    width: 100%;
	    border: 3px solid #ddd;
	}

	th, td {
	    text-align: center;
	    padding: 14px;
	    min-width:15%;
	}

	tr:nth-child(even){background-color: #f2f2f2}
	div.sticky {
		    position: -webkit-sticky;
		    position: sticky;
		    top: 0;
		    background-color: yellow;
		    padding: 50px;
		    font-size: 20px;
		}
	.wrapper {
	  width:100%;
	  clear:both;
	}
	.first {
	  width:50%;
	  float:left;
	}
	.second {
	  width:50%;
	  float:right;
	}
	.one{
		width:100%;
		float:left;
	}
	.box{
		display: block;
	    padding: 10px;
	    margin-bottom: 100px;
	    margin-top: 100px;
	    text-align: justify;

	}
    </style>
	<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {

        var data = google.visualization.arrayToDataTable([
          ['Verdict', 'Number'],
          ['AC',     """+str(handle1_verdict_ok)+"""],
          ['WA',      """+str(handle1_verdict_wa)+"""],
          ['TLE',  """+str(handle1_verdict_tle)+"""],
          ['MLE', """+str(handle1_verdict_mle)+"""],
          ['RTE', """+str(handle1_verdict_rte)+"""],
          ['CE',    """+str(handle1_verdict_ce)+"""],
          ['OTHER', """+str(handle1_verdict_oth)+"""]
        ]);

        var options = {
          title: 'Verdicts',
          colors: ['greenyellow', 'red', 'gold', 'blue', 'blueviolet', 'cyan', 'grey']
        };

        var chart = new google.visualization.PieChart(document.getElementById('piechart'));

        chart.draw(data, options);
      }
    </script>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {

        var data = google.visualization.arrayToDataTable([
          ['Verdict', 'Number'],
          ['AC',     """+str(handle2_verdict_ok)+"""],
          ['WA',      """+str(handle2_verdict_wa)+"""],
          ['TLE',  """+str(handle2_verdict_tle)+"""],
          ['MLE', """+str(handle2_verdict_mle)+"""],
          ['RTE', """+str(handle2_verdict_rte)+"""],
          ['CE',    """+str(handle2_verdict_ce)+"""],
          ['OTHER', """+str(handle2_verdict_oth)+"""]
        ]);

        var options = {
          title: 'Verdicts',
          colors: ['greenyellow', 'red', 'gold', 'blue', 'blueviolet', 'cyan', 'grey']
        };

        var chart = new google.visualization.PieChart(document.getElementById('piechart1'));

        chart.draw(data, options);
      }
    </script>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load("current", {packages:["corechart"]});
      google.charts.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['Language', 'No of Submissions'],
          ['GNU C++14',              """+str(handle1_GNU_C14)+"""],
          ['GNU C++11',              """+str(handle1_GNU_C11)+"""],
          ['GNU C++17',              """+str(handle1_GNU_C17)+"""],
          ['Java 8',                 """+str(handle1_Java_8)+"""],
          ['Python 3',               """+str(handle1_Python_3)+"""],
          ['GNU C11',                """+str(handle1_GNU_C11)+"""],
          ['MS C++',                 """+str(handle1_MS_C)+"""],
          ['Python 2',               """+str(handle1_Python_2)+"""],
          ['PyPy 3',                 """+str(handle1_PyPy_3)+"""],
          ['PyPy 2',                 """+str(handle1_PyPy_2)+"""],
          ['Mono C#',                """+str(handle1_Mono_C)+"""],
          ['FPC',                    """+str(handle1_FPC)+"""],
          ['PascalABC.NET',          """+str(handle1_PascalABC)+"""],
          ['JavaScript',             """+str(handle1_JavaScript)+"""],
          ['Perl',                   """+str(handle1_Perl)+"""],
          ['Kotlin',                 """+str(handle1_Kotlin)+"""],
          ['Clang++17 Diagnostics',  """+str(handle1_Clang17_Diagnostics)+"""],
          ['Ruby',                   """+str(handle1_Ruby)+"""],
          ['Go',                     """+str(handle1_Go)+"""],
          ['PHP',                    """+str(handle1_PHP)+"""],
          ['Delphi',                 """+str(handle1_Delphi)+"""],
          ['Ocaml',                  """+str(handle1_Ocaml)+"""],
          ['Rust',                   """+str(handle1_Rust)+"""],
          ['Scala',                  """+str(handle1_Scala)+"""],
          ['D',                      """+str(handle1_D)+"""]
        ]);

        var options = {
          title: 'Languages Used',
          pieHole: 0.4,
          is3D:true
        };

        var chart = new google.visualization.PieChart(document.getElementById('donutchart11'));
        chart.draw(data, options);
      }
    </script>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load("current", {packages:["corechart"]});
      google.charts.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['Language', 'No of Submissions'],   
		  ['GNU C++14',              """+str(handle2_GNU_C14)+"""],
		  ['GNU C++11',              """+str(handle2_GNU_C11)+"""],
		  ['GNU C++17',              """+str(handle2_GNU_C17)+"""],
		  ['Java 8',                 """+str(handle2_Java_8)+"""],
		  ['Python 3',               """+str(handle2_Python_3)+"""],
		  ['GNU C11',                """+str(handle2_GNU_C11)+"""],
		  ['MS C++',                 """+str(handle2_MS_C)+"""],
		  ['Python 2',               """+str(handle2_Python_2)+"""],
		  ['PyPy 3',                 """+str(handle2_PyPy_3)+"""],
		  ['PyPy 2',                 """+str(handle2_PyPy_2)+"""],
		  ['Mono C#',                """+str(handle2_Mono_C)+"""],
		  ['FPC',                    """+str(handle2_FPC)+"""],
		  ['PascalABC.NET',          """+str(handle2_PascalABC)+"""],
		  ['JavaScript',             """+str(handle2_JavaScript)+"""],
		  ['Perl',                   """+str(handle2_Perl)+"""],
		  ['Kotlin',                 """+str(handle2_Kotlin)+"""],
		  ['Clang++17 Diagnostics',  """+str(handle2_Clang17_Diagnostics)+"""],
		  ['Ruby',                   """+str(handle2_Ruby)+"""],
		  ['Go',                     """+str(handle2_Go)+"""],
		  ['PHP',                    """+str(handle2_PHP)+"""],
		  ['Delphi',                 """+str(handle2_Delphi)+"""],
		  ['Ocaml',                  """+str(handle2_Ocaml)+"""],
		  ['Rust',                   """+str(handle2_Rust)+"""],
		  ['Scala',                  """+str(handle2_Scala)+"""],
		  ['D',                      """+str(handle2_D)+"""]
        ]);

        var options = {
          title: 'Languages Used',
          pieHole: 0.4,
          is3D:true
        };

        var chart = new google.visualization.PieChart(document.getElementById('donutchart12'));
        chart.draw(data, options);
      }
    </script>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['line']});
      google.charts.setOnLoadCallback(drawChart);

    function drawChart() {

      var data = new google.visualization.DataTable();
      data.addColumn('string', 'Day');
      data.addColumn('number', '"""+handle1+"""');
      data.addColumn('number', '"""+handle2+"""');
      
      data.addRows(["""
for i in range(len(dataset)):
	x = dataset[i]
	message += "["
	for j in range(len(x)):
		if j < len(x) - 1:
			if(j == 0):
				if(x[j] == -1):
					message += "'" + "null" + "'" + ',' 
				else:
					message += "'" + str(x[j]) + "'" + ','
			else:	
				if(x[j] == -1):
					message += "null" + ',' 
				else:
					message += str(x[j]) + ','
		else:
			if(x[j] == -1):
				message += "null" 
			else:
				message += str(x[j])
	message += "]"
	if(i < len(dataset) - 1):
		message += ","

message +=	"""]);

      var options = {
        chart: {
          title: 'Rating graph',
          subtitle: ''
        },
        vAxis: {format: ''},
        width: 950,
        height: 550,
        axes: {
          x: {
            0: {side: 'bottom'}
          }
        }
      };

      var chart = new google.charts.Line(document.getElementById('line_top_x'));

      chart.draw(data, google.charts.Line.convertOptions(options));
    }
  </script>
  <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['bar']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['', '"""+handle1+"""', '"""+handle2+"""'],
          ['Current Rating', """+str(handle1_curr_rating)+""", """+str(handle2_curr_rating)+"""],
          ['Max Rating', """+str(handle1_max_rating)+""", """+str(handle2_max_rating)+"""],
          ['Min Rating', """+str(handle1_min_rating)+""", """+str(handle2_min_rating)+"""]
        ]);

        var options = {
          chart: {
            title: 'Rating',
            subtitle: '',
          },
          bars: 'vertical',
          vAxis: {format: ''},
          height: 550,
          width: 950,
          colors: ['yellow', 'blue']
        };

        var chart = new google.charts.Bar(document.getElementById('columnchart_material'));

        chart.draw(data, google.charts.Bar.convertOptions(options));
      }
    </script>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load("current", {packages:["corechart"]});
      google.charts.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['Popularity', 'Numbers'],
          ['Friends of """+str(handle2)+"""',     """+str(handle2_friends)+"""],
          ['Contribution of """+str(handle2)+"""',      """+str(handle2_contri)+"""],
          ['Contribution of """+str(handle1)+"""',      """+str(handle1_contri)+"""],
          ['Friends of """+str(handle1)+"""',     """+str(handle1_friends)+"""]
        ]);

        var options = {
          title: 'Popularity',
          colors: ['mediumseagreen', 'mediumspringgreen', 'skyblue', 'steelblue'],
          pieHole: 0.4
        };

        var chart = new google.visualization.PieChart(document.getElementById('donutchart'));
        chart.draw(data, options);
      }
    </script>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['bar']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['', '"""+handle1+"""', '"""+handle2+"""'],
          ['Average', """+str(handle1_avg)+""", """+str(handle2_avg)+"""],
          
        ]);

        var options = {
          chart: {
            title: 'Average Problems Solved Per Contest',
            subtitle: '',
          },
            vAxis: {format: ''},
            height: 200,
         	 width: 600,
          bars: 'horizontal' // Required for Material Bar Charts.
        };

        var chart = new google.charts.Bar(document.getElementById('barchart_material1'));
        chart.draw(data, google.charts.Bar.convertOptions(options));
      }
    </script>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['bar']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['', '"""+handle1+"""', '"""+handle2+"""'],
          ['Accuracy', """+str(handle1_accu)+""", """+str(handle2_accu)+"""]
          
        ]);

        var options = {
          chart: {
            title: 'Accuracy',
            subtitle: '',
          },
            vAxis: {format: ''},
            height: 200,
            width: 600,
          bars: 'horizontal' // Required for Material Bar Charts.
        };

        var chart = new google.charts.Bar(document.getElementById('barchart_material2'));
        chart.draw(data, google.charts.Bar.convertOptions(options));
      }
    </script>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load("current", {packages:["corechart"]});
      google.charts.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['Tags', 'No of problems solved'],
          ['implementation',     		"""+str(handle1_implementation)+"""],
          ['greedy',     		 		"""+str(handle1_greedy)+"""],
          ['math',     			 		"""+str(handle1_math)+"""],
          ['brute force',     	 		"""+str(handle1_brute_force)+"""],
          ['dp', 		    	 		"""+str(handle1_dp)+"""],
          ['strings',     	 			"""+str(handle1_strings)+"""],
          ['sortings',     	 			"""+str(handle1_sortings)+"""],
          ['constructive algorithms',   """+str(handle1_constructive_algorithms)+"""],
          ['dfs and similar',     	    """+str(handle1_dfs_similar)+"""],
          ['binary search',     	 	"""+str(handle1_binary_search)+"""],
          ['trees',     	 			"""+str(handle1_trees)+"""],
          ['two pointers',     	 		"""+str(handle1_two_pointers)+"""],
          ['graphs',     	 			"""+str(handle1_graphs)+"""],
          ['number theory',     	 	"""+str(handle1_number_theory)+"""],
          ['data structures',     	 	"""+str(handle1_data_structures)+"""],
          ['games',     	 			"""+str(handle1_games)+"""],
          ['combinatorics',     	 	"""+str(handle1_combinatorics)+"""],
          ['graph matchings',     	 	"""+str(handle1_graph_matchings)+"""],
          ['geometry',     	 			"""+str(handle1_geometry)+"""],
          ['bitmasks',     	 			"""+str(handle1_bitmasks)+"""],
          ['dsu',     	 				"""+str(handle1_dsu)+"""],
          ['shortest paths',     	 	"""+str(handle1_shortest_paths)+"""],
          ['*special',     	 			"""+str(handle1_special)+"""],
          ['probabilities',     	 	"""+str(handle1_probabilities)+"""],
          ['matrices',     	 			"""+str(handle1_matrices)+"""],
          ['expression parsing',     	"""+str(handle1_expression_parsing)+"""],
          ['hashing',     	 			"""+str(handle1_hashing)+"""],
          ['flows',     	 			"""+str(handle1_flows)+"""]
        ]);

        var options = {
          title: 'Tags',
          pieHole: 0.4
        };

        var chart = new google.visualization.PieChart(document.getElementById('donutchart1'));
        chart.draw(data, options);
      }
    </script>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load("current", {packages:["corechart"]});
      google.charts.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['Tags', 'No of problems solved'],
          ['implementation',     		"""+str(handle2_implementation)+"""],
          ['greedy',     		 		"""+str(handle2_greedy)+"""],
          ['math',     			 		"""+str(handle2_math)+"""],
          ['brute force',     	 		"""+str(handle2_brute_force)+"""],
          ['dp', 		    	 		"""+str(handle2_dp)+"""],
          ['strings',     	 			"""+str(handle2_strings)+"""],
          ['sortings',     	 			"""+str(handle2_sortings)+"""],
          ['constructive algorithms',   """+str(handle2_constructive_algorithms)+"""],
          ['dfs and similar',     	    """+str(handle2_dfs_similar)+"""],
          ['binary search',     	 	"""+str(handle2_binary_search)+"""],
          ['trees',     	 			"""+str(handle2_trees)+"""],
          ['two pointers',     	 		"""+str(handle2_two_pointers)+"""],
          ['graphs',     	 			"""+str(handle2_graphs)+"""],
          ['number theory',     	 	"""+str(handle2_number_theory)+"""],
          ['data structures',     	 	"""+str(handle2_data_structures)+"""],
          ['games',     	 			"""+str(handle2_games)+"""],
          ['combinatorics',     	 	"""+str(handle2_combinatorics)+"""],
          ['graph matchings',     	 	"""+str(handle2_graph_matchings)+"""],
          ['geometry',     	 			"""+str(handle2_geometry)+"""],
          ['bitmasks',     	 			"""+str(handle2_bitmasks)+"""],
          ['dsu',     	 				"""+str(handle2_dsu)+"""],
          ['shortest paths',     	 	"""+str(handle2_shortest_paths)+"""],
          ['*special',     	 			"""+str(handle2_special)+"""],
          ['probabilities',     	 	"""+str(handle2_probabilities)+"""],
          ['matrices',     	 			"""+str(handle2_matrices)+"""],
          ['expression parsing',     	"""+str(handle2_expression_parsing)+"""],
          ['hashing',     	 			"""+str(handle2_hashing)+"""],
          ['flows',     	 			"""+str(handle2_flows)+"""]
        ]);

        var options = {
          title: 'Tags',
          pieHole: 0.4
        };

        var chart = new google.visualization.PieChart(document.getElementById('donutchart2'));
        chart.draw(data, options);
      }
    </script>
</head>
<body>
  <br>
  <div class="w3-container">
      <div class="w3-bar w3-border w3-black">
        <a href="home.html" style="width:20%" class="w3-bar-item w3-button w3-mobile">Home</a>
        <a href="analysis.html" style="width:20%" class="w3-bar-item w3-button w3-mobile">Analysis</a>
        <a href="comparator.html" style="width:20%" class="w3-bar-item w3-button w3-mobile w3-gray">Compare</a>
        <a href="rankings.html" style="width:20%" class="w3-bar-item w3-button w3-mobile">Rankings</a>
        <a href="upcoming.html" style="width:20%" class="w3-bar-item w3-button w3-mobile">Upcoming</a>
      </div>
    </div>
    <div class="w3-container w3-red w3-margin">
		  <h2>Compare</h2>
		</div>
    <br><br>

    <div class="w3-half">
		    <center>
		  <div class="w3-card-4" style="width:50%;">
		    <img src="https:"""+handle1_profile_pic+"""" alt="" class="w3-bar-item w3-rectangle w3-hide-medium" style="width:100%;height:350px;">
		    <div class="w3-container w3-center">
		      <p><h2>"""+handle1+"""</h2></p>
		    </div>
		  </div>
   		</center>
    </div>


    <div class="w3-half">
		    <center>
		  <div class="w3-card-4" style="width:50%;">
		    <img src="https:"""+handle2_profile_pic+"""" alt="" class="w3-bar-item w3-rectangle w3-hide-medium" style="width:100%;height:350px;">
		    <div class="w3-container w3-center">
		      <p><h2>"""+handle2+"""</h2></p>
		    </div>
		  </div>
    </center>
    </div>

    <br><br>

    <div class="w3-container"> 
		  <div class="w3-panel w3-white w3-leftbar w3-rightbar w3-border-red">
		    <p>
		    <h3><strong><font color="red">Verdicts:</font></strong></h3> 
		    </p>
		  </div>
		</div>

	<div class="w3-half">
		    <center>

    <div class="w3-container w3-margin-left w3-margin-bottom w3-margin-top">
        	<div class="w3-card" id="piechart" style="width: 600px; height: 600px;"></div>
      	</div>
		  
    </center>
    </div>

    <div class="w3-half">
		    <center>
		    
    <div class="w3-container w3-margin-left w3-margin-bottom w3-margin-top">
        <div class="w3-card" id="piechart1" style="width: 600px; height: 600px;"></div>
      </div>
		  
    </center>
    </div>

    

    <div class="w3-container">
		  <div class="w3-panel w3-white w3-leftbar w3-rightbar w3-border-red">
		    <p>
		    <h3><strong><font color="red">Languages:</font></strong></h3> 
		    </p>
		  </div>
		</div>


    <div class="w3-half">
      <div class="w3-container w3-margin-bottom w3-margin-right w3-margin-left">
        <div class="w3-card" id="donutchart11" style="width: 600px; height: 600px;"></div>
      </div>
    </div>

    <div class="w3-half">
      <div class="w3-container w3-margin-bottom w3-margin-right w3-margin-left">
        <div class="w3-card" id="donutchart12" style="width: 600px; height: 600px;"></div>
      </div>
    </div>

    <div class="w3-container">
		  <div class="w3-panel w3-white w3-leftbar w3-rightbar w3-border-red">
		    <p>
		    <h3><strong><font color="red">Problems Solved:</font></strong></h3> 
		    </p>
		  </div>
		</div>

    <div class="w3-half">
      <div class="w3-container w3-margin-bottom w3-margin-right w3-margin-left">
        <div class="w3-card" id="donutchart1" style="width: 600px; height: 600px;"></div>
      </div>
    </div>

    <div class="w3-half">
      <div class="w3-container w3-margin-bottom w3-margin-right w3-margin-left">
        <div class="w3-card" id="donutchart2" style="width: 600px; height: 600px;"></div>
      </div>
    </div>

    <div class="w3-container">
		  <div class="w3-panel w3-white w3-leftbar w3-rightbar w3-border-red">
		    <p>
		    <h3><strong><font color="red">Rating Graph:</font></strong></h3> 
		    </p>
		  </div>
		</div>

    <div class="w3-container w3-margin">
      <center><div class="w3-card w3-margin" id="line_top_x" style="width: 1000px; height: 600px"></div></center>
    </div>


    <div class="w3-container">
		  <div class="w3-panel w3-white w3-leftbar w3-rightbar w3-border-red">
		    <p>
		    <h3><strong><font color="red">Max & Min Rating:</font></strong></h3> 
		    </p>
		  </div>
		</div>

    <div class="w3-container w3-margin">
    	<center><div class="w3-card w3-margin" id="columnchart_material" style="width: 1000px; height: 600px"></div></center>
    </div>


    <div class="w3-container">
		  <div class="w3-panel w3-white w3-leftbar w3-rightbar w3-border-red">
		    <p>
		    <h3><strong><font color="red">Popularity:</font></strong></h3> 
		    </p>
		  </div>
		</div>

    <div class="w3-container w3-margin">
    	<center><div class="w3-card w3-margin" id="donutchart" style="width: 1000px; height: 600px"></div></center>
    </div>


    <div class="w3-container">
		  <div class="w3-panel w3-white w3-leftbar w3-rightbar w3-border-red">
		    <p>
		    <h3><strong><font color="red">Average & Accuracy:</font></strong></h3> 
		    </p>
		  </div>
		</div>
    <div class="w3-half">
      <div class="w3-container w3-card w3-margin">
        <div class="w3-margin-top" id="barchart_material1" style="width: 600px; height: 300px;"></div>
      </div>
    </div>

    <div class="w3-half">
      <div class="w3-container w3-card w3-margin">
        <div class="w3-margin-top" id="barchart_material2" style="width: 600px; height: 300px;"></div>
      </div>
    </div>
    

    <div class="w3-container">
		  <div class="w3-panel w3-white w3-leftbar w3-rightbar w3-border-red">
		    <p>
		    <h3><strong><font color="red">Last Five Contests:</font></strong></h3> 
		    </p>
		  </div>
		</div>
	<br>
   	<div class="w3-container">
		<table> """

colname = ['Problems Solved By ' + handle1, 'Problems Solved By ' + handle2, 'Rank of ' + handle1, 'Rank of ' + handle2, 'Rating Change of ' + handle1, 'Rating Change of ' + handle2]
message += "\n<tr>\n"
message += """<th style="width:10%";>S.No</th>\n"""

for x in colname:
    message += "<th>" + x + "</th>\n"
message += "</tr>\n"

for i in range(0, 5):
	message += "<tr>\n"
	
	message += """<td style = "width:10%;">\n""" + str(i + 1) 
	message += "</td>\n"
    
	message += "<td>\n" + str(lstf_sol[i])
	message += "</td>\n"

	message += "<td>\n" + str(lstf_sol2[i])
	message += "</td>\n"

	message += "<td>\n" + str(lstf_rnks[i])
	message += "</td>\n"

	message += "<td>\n" + str(lstf_rnks2[i])
	message += "</td>\n"

	if lstf_rat_chg[i] > 0:
		message += """<td><font color="green">\n""" + "+" + str(lstf_rat_chg[i])
		message += "</font></td>\n"
	else:
		message += """<td><font color="red">\n"""  + str(lstf_rat_chg[i])
		message += "</font></td>\n"

	if lstf_rat_chg2[i] > 0: 
		message += """<td><font color="green">\n""" + "+" + str(lstf_rat_chg2[i])
		message += "</font></td>\n"
	else:
		message += """<td><font color="red">\n""" + str(lstf_rat_chg2[i])
		message += "</font></td>\n"
	message += "</tr>\n"


message += """  </table> </div>
        <hr> 
		</body>
		</html>"""

print(message)
sys.stdout.flush()







