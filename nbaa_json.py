import requests 
##json
import json 
g=open("0021700110_full_pbp.json","r")
g1=json.load(g)
g1.keys()

g1["g"]["pd"][0]["pla"][1]["locX"]

def player_scrape():
    print(g1["g"]["pd"][0]

if g1["g"]["pd"][0]["locX"]["locY"][etype=="10"]:
    print(g1["g"]["pd"][0]["pla"])

### player movements 1/10/17
# check if shot or not? (x-coords) etype=1 (made) or etype=2 (missed)
#miami team id: 1610612748
mia_game1=[]
for i in range(len(g1['g']['pd'][3]['pla'])):
    if g1['g']['pd'][3]['pla'][i]['tid']==1610612748:
        if g1['g']['pd'][3]['pla'][i]['etype']==1:
          print(g1['g']['pd'][3]['pla'][i]["locX"],g1["g"]["pd"][3]["pla"][i]["locY"])
        elif g1['g']['pd'][3]['pla'][i]['etype']==2:
          print(g1['g']['pd'][3]['pla'][i]["locX"],g1["g"]["pd"][3]["pla"][i]["locY"])
          mia_game1.append(i)

#miami vice
mia_game1=pd.read_csv("miami_vice.csv")
mia_game1.info()
#viz #miami heat vs. chicago bulls (11/1/17)
import seaborn 
plot=sns.lmplot(x='x',y='y',data=mia_game1,fit_reg=False) 
plot.set(xlabel='x_coord',ylabel='y_coord',title='Miami Shots vs. Chicago') #11/1/17
plt.show() 
##richarson shots? (dirty sprite vs. lean?)
#pid":1626196

#miami vice 2 (den vs. mia?)
g1=open("den vs mia.json")
g1=json.load(g1)
g1.keys()
for i in range(len(g1['g']['pd'][3]['pla'])):
    if g1['g']['pd'][3]['pla'][i]['tid']==1610612748:
        if g1['g']['pd'][3]['pla'][i]['etype']==1:
          print(g1['g']['pd'][3]['pla'][i]["locX"],g1["g"]["pd"][3]["pla"][i]["locY"])
        elif g1['g']['pd'][3]['pla'][i]['etype']==2:
          print(g1['g']['pd'][3]['pla'][i]["locX"],g1["g"]["pd"][3]["pla"][i]["locY"])

#plot shots vs. denver
plot1=sns.lmplot(x='x',y='y',data=mia_game1,fit_reg=False) 
plot1.set(xlabel='x_coord',ylabel='y_coord',title='Miami Shots vs. Denver') #11/3/17 
plt.show() 















