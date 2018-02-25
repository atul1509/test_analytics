import json
import numpy as np

###read data
json_data1 = open('/home/atul/practice/ml/Untitled Folder 4/2017-11-01.json','r')
data1 = json.load(json_data1)

json_data2 = open('/home/atul/practice/ml/Untitled Folder 4/2017-11-02.json','r')
data2 = json.load(json_data2)

json_data3 = open('/home/atul/practice/ml/Untitled Folder 4/2017-11-03.json','r')
data3 = json.load(json_data3)

m1 = len(data1)
m2 = len(data2)
m3 = len(data3)


#print(data1[m1-1])
arr = []

for i in range(0,m1):

    arr .append( np.array([data1[i][key] for key in ('user_id', 'screen_name', 'text', 'time', 'id')]))

#

for i in range(0,m2):
    arr.append(np.array([data2[i][key] for key in ('user_id', 'screen_name', 'text', 'time', 'id')]))


for i in range(0, m3):
    arr.append(np.array([data3[i][key] for key in ('user_id', 'screen_name', 'text', 'time', 'id')]))


#print (arr[0])


#######
#print (arr[110][2].capitalize())
#print (arr[9203][2].lower())
num_donald =0
pos_tweet = 0
u_id = {}

####tweets for donald trump
for i in range(0, len(arr)):
    text = arr[i][2].lower()
    #name = arr[i][1].lower()

    if('donald' in text or 'president' in text or 'trump' in text):
        num_donald += 1
        if('good' in text or 'nice' in text):
            pos_tweet += 1
            if(arr[i][1] not in u_id):
                u_id[arr[i][0]] = 1
            else:
                u_id[arr[i][0]] += 1

####positive tweets more than 50%
num_pos = {}
for id in u_id.keys():
    num_pos[id] = 0
for i in range(0,len(arr)):
    for id in u_id:
        if(id == arr[i][0]):
            num_pos[id] += 1


num_pos_tweet = 0
for id in u_id.keys():
    dif = num_pos[id] - u_id[id]
    if(float(dif)/num_pos[id] <= 0.5):
        num_pos_tweet += 1


print('% of accounts tweeting about Donald Trump ',(float(num_donald)/len(arr))*100)
print('% of Donald Trump tweets which are positive in nature:',(float(len(u_id))/len(arr))*100)
print('% of accounts with more than 50% positive tweets about Donald Trump: ',(float(num_pos_tweet)/len(u_id))*100)




