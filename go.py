# To check who has submitted cs300 assignment xD

from urllib.request import urlopen
import csv

file = 'https://www.cse.iitk.ac.in/users/cs300/attendance.csv'
students=[]
with urlopen(file) as f:
    # print(f)
    s=f.read().decode('utf-8')
    rows=(csv.reader(s.splitlines(),delimiter=','))
    for row in rows:
        if(row[1]!=""):
            students.append(row[1])

file=input("File to see : ")
pre="http://home.iitk.ac.in/~"
post="/cs300/"+file
for student in students:
    try:
        r = urlopen(pre+student+post)
    except Exception as e:
        continue
    else:
        print(student)

