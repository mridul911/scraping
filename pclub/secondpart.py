import csv
import json
import re
import pandas as pd
def white(s):  #calculating if it has single or multiple words
    count=0
    for a in s:
        if(a.isspace())== True:
            count+=1
    return count
string_check= re.compile('[@_!#$%^&*()<>?/\|}{~:]') #check if it has any special character or not
with open('GSOC 2019.csv', 'r',encoding="utf8") as f:#opening file and reading it
    d_reader = csv.DictReader(f)
    headers = d_reader.fieldnames
    wname=[]
    rname=[]
    for line in d_reader:
        #print(white(line['name']))
        if (string_check.search(line['name'])== None and white(line['name'])>=1 and line['name'].islower()== False ):
            rname.append(line['name'])
        else:
            wname.append(line['name'])
print(wname)
#pd.read_json('students.json').to_csv('students.csv') converting json to csv type
with open('students.csv','r',encoding="utf8") as f1:
    d_reader1 = csv.DictReader(f1)
    headers1= d_reader1.fieldnames
    answer=[]
    for line1 in d_reader1:
        #print(line1['n'])
        if line1['n'] in rname:
            answer.append(line1['n'])
            answer.append(line1['i'])
            answer.append(line1['p'])
with open('GSOC 2019.csv', 'r',encoding="utf8") as f:
    d_reader = csv.DictReader(f)
    headers = d_reader.fieldnames
    for line in d_reader:
        if (answer[0]==line['name']):
            answer.append(line['orgname'])
            answer.append(line['proname'])
print(answer)
