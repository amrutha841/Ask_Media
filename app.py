#!flask/bin/python
from flask import Flask
from flask import request
from urllib.request import urlopen
import requests
import json
import json
import operator
app = Flask(__name__)

@app.route('/api/v1/default/',methods=['POST'])
def defTask():
    repoName = request.form['repository_name']
    userName = request.form['user_name']
    days_of_week = {0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
    interRes = json.load(urlopen('https://api.github.com/repos/'+userName+'/'+repoName+'/stats/commit_activity'))
    maxi = -1
    Indexmax = -1
    week = 0

    for obj in interRes:
        if 'days' in obj:
            for i,val in enumerate(obj['days']):
                if val > maxi:
                    week = obj['week']       
                    maxi = val
                    Indexmax = i
    summi = 0
    n = 0
    for obj in interRes:
        if 'days' in obj:
            for i,val in enumerate(obj['days']):
                if (i == Indexmax):
                    summi += val
                    n +=1   

    aggo = float(summi)/n
    finRes= {"Day-of-week-most-commits":days_of_week[Indexmax],"Average":aggo}
    print(finRes)
    return str(finRes)


@app.route('/api/v1/bonusTask1/',methods=['POST'])
def task1():
    repoName = request.form['repository_name']
    userName = request.form['user_name']
    try:
        requestRange = request.form['request_range']
    except:
        requestRange = 52
    days_of_week = {0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
    #url = 'https://api.github.com/repos/'+userName+'/'+repoName+'/stats/commit_activity'
    #interRes = requests.get(url)
    #interRes.json()
    interRes = json.load(urlopen('https://api.github.com/repos/'+userName+'/'+repoName+'/stats/commit_activity'))
    #interRes = json.loads(interRes)
    maxi = -1
    Indexmax = -1
    week = 0
    weekCount =0
    for obj in interRes:
        weekCount+=1
        print(obj)
        if (int(weekCount) > int(requestRange)):
            break
        else:    
            if 'days' in obj:
                for i,val in enumerate(obj['days']):
                    if val > maxi:
                        week = obj['week']       
                        maxi = val
                        Indexmax = i
    summi = 0
    n = 0
    aggo=0
    weekCount = 0
    for obj in interRes:
        weekCount+=1
        if (int(weekCount) > int(requestRange)):
            break
        else:
            if 'days' in obj:
                for i,val in enumerate(obj['days']):
                    if (i == Indexmax):
                        summi += val
                        n +=1   
    if summi == 0:
        aggo = 0
    else:
        print(summi)
        print(n)
        aggo = float(summi)/n
    finRes= {"Day-of-week-most-commits":days_of_week[Indexmax],"Average":aggo}
    return str(finRes)


@app.route('/api/v1/bonusTask2/',methods=['POST'])
def Task2():
    repoName = request.form['repository_name']
    userName = request.form['user_name']
    try:
        sortOrder = request.form['sort_order']
    except:
        sortOrder = "1"
    days_of_week = {0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',4:'Thursday',5:'Friday',6:'Saturday'}
    
    interRes = json.load(urlopen('https://api.github.com/repos/'+userName+'/'+repoName+'/stats/commit_activity'))
   

    week = 0
    tempMap = {}
    final ={}
    for obj in interRes:
        print(obj)
        if 'days' in obj:
            for i,val in enumerate(obj['days']):
                if i in tempMap:
                    tempList = tempMap[i] 
                    count = tempList[0]
                    count = count + val
                    n= tempList[1]
                    n +=1
                    tempList[0] =count
                    tempList[1] = n
                    tempMap[i] = tempList
                else:
                    tempList = []
                    tempList.append(val)
                    tempList.append(1)
                    tempMap[i] = tempList
    for key,value in tempMap.items():
        if key in days_of_week:
            d = tempMap[key]
            avg = float(d[0])/d[1]
            final[days_of_week[key]] = avg 
    if sortOrder == "1":
        sorted_x = sorted(final.items(), key=operator.itemgetter(1),reverse=True)
    else:
        sorted_x = sorted(final.items(), key=operator.itemgetter(1))
    print(sorted_x)
    return str(sorted_x)


if __name__ == '__main__':
    app.run(debug=True)