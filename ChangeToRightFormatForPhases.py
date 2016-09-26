#Author: Ásgeir Örn Sigurpálsson
#Date: 15th of September
#Puts data in right format - needs to be copied into the model itself for Phase 2



import csv


Dictionary=[{} for i in range (1)]
with open('Split.txt','r',encoding='utf8', newline='') as data:
    #read_data =data.read()
    ReadFile = csv.reader(data, delimiter=",")

    for rows in ReadFile:
        for i in range(1):
            Dictionary[i][rows[0]] = rows[i+1]


with open('Split.dat',"w", newline='') as newdata:

    for course,rlist in Dictionary[0].items():
        s = 'set fixsolution['+course.replace("Slot(", "")+']:= '
        b=rlist.replace(") 1","")
        newdata.write(s)
        newdata.write(b)
        newdata.write(';\n')
