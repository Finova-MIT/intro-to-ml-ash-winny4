wrld_cup_winner={           #data from DAV LMS (Wikipedia)
"1975": "West Indies", 
"1979": "West Indies", 
"1983": "India", 
"1987": "Australia", 
"1992": "Pakistan", 
"1996": "Sri Lanka", 
"1999" : "Australia", 
"2003" : "Australia", 
"2007" : "Australia" 
} 
ccount = [] 
for i in wrld_cup_winner: 
    if i in ccount: 
        continue 
    else: 
        cntry = wrld_cup_winner[i] 
        ccount.append(cntry) 
print(ccount) #only one instance of each winner
