import csv,json
from collections import Counter
f=open('subscriptions.csv','r')
c=csv.reader(f)
f=open('watch-history.json','r',encoding='utf-8')
jfile=json.load(f)

def getsubs():
    subs=[i for i in c]
    subs.pop(0)
    subs.pop(len(subs)-1)
    ids=[i[0] for i in subs]
    cid=[i[1] for i in subs]
    names=[i[2] for i in subs]
    return ids,cid,names

def getwatchedchannels():
    
    watchedchannels,watchedsubs,ch=[],[],0
    results=[]
    for i in range(len(jfile)):
        while 1:
            try:
                watchedchannels.append(jfile[i]['subtitles'][0]['name'])
            except:
                watchedchannels.append('AD')
                ch+=1
            break
    for i in range(ch):
        watchedchannels.remove('AD')
    return watchedchannels

#!removes empty lists   
def removeempty(watched):
    emptied=[i for i in watched if i[0]!=0]
    emptied.sort(key = lambda x: x[0])
    emptied.reverse()
    return [x for i,x in enumerate(emptied) if i<=10]
    
    
def watchedsubs():
    watchedsubs=[]
    watchedsubssorted=[]
    for i in watchedchannels:
        if i in names:
            watchedsubs.append(i)
    result = [item for items, c in Counter(watchedsubs).most_common() for item in [items] * c]
    for i in names:
        watchedsubssorted.append([result.count(i),i])
    return removeempty(watchedsubssorted)

ids,cid,names=getsubs()
watchedchannels=getwatchedchannels()

def getdate(year,jfile=jfile):
    mns,freq=[],[]
    ch=0
    date=[i['time'][:10] for i in jfile]
    month=[i[5::] for i in date if i[:4]==str(year)]
    for i in range(1,13):
        ch=0
        for t in month:
            if int(t[:2])==i:
                ch+=1
    
        freq.append(ch)
    return freq
    
def gettime(jfile=jfile):
    data=[]
    hour=[i['time'][11:19] for i in jfile]
    #print(hour[2][:2])
    for i in range(6,24):
        freq=0
        for j in hour:
            #print(j[:2])
            if j[:2]==str(i):
                freq+=1
        data.append(freq)   
    return(data)

watsubs=watchedsubs()
import matplotlib.pyplot as plt

def dis1():
    plt.bar([i[1] for i in watsubs],[i[0] for i in watsubs],color=['#0096FF','#6495ED','#1434A4','#191970','#4169E1','green','black'])
    plt.xlabel('Channels')
    plt.ylabel('Number of videos watched')
    plt.title('Most Watched Subcribers')
    plt.show()
x1=['January','February','March','April','May','June','July','August','September','October','November','December']
def dis2():
    plt.plot(x1,getdate(int(input("enter year:"))))
    plt.xlim(0,11)
    plt.ylim(ymin=0.0)
    plt.ylabel('Number of videos watched')
    plt.title('Number of Videos Watched Per Month')
    plt.show()
x=["7AM","8AM","9AM","10AM","11AM","12PM","1PM","2PM","3PM","4PM","5PM","6PM","7PM","8PM","9PM","10PM","11PM","12PM"]
def dis3():
    plt.bar(x,gettime())
    plt.ylabel('Number of videos watched')
    plt.title('Number of Videos Watched Per Hour')
    plt.show()

print("YouTube Demographics Analyer")
while 1:
    ch=int(input("1.Most Viewed Subscribed Channels\n2.Most Active Months\n3.Most Active Hours\n->"))
    if ch==1:
        dis1()
    elif ch==2:
        dis2() 
    elif ch==3:
        dis3()
    elif ch==4:
        break
    else:print("wrong message")
