"""
**1.Reading Data From CSV**
"""

import csv

fcsv=open('Datas.csv','r')
frow=csv.reader(fcsv)
for i in frow:
  print('Name of the person is {} , Experience is {} and Withdrawing the Amount in PKR.{}'.format(i[0],i[1],i[2]))
fcsv.close()

"""# ** 2. Writing in CSV File using Writerow()**"""

fcs=open('Datas.csv','w')
fwrt=csv.writer(fcs)
fwrt.writerow(['Name','Experience','Salary'])
fcs.close()

"""**3. Writing in CSV File using Writerows()**"""

rows=[['Ahmed','2','15000'],['Akram','3','18000'],['Zahid','4','20000']]

fcs=open('Datas.csv','a', newline='')
fwr=csv.writer(fcs)
fwr.writerows(rows)
fcs.close()

"""**4. Read CSV File using Dictionary Method**"""

import csv as c
f = open('Datas.csv', "r")
row = c.DictReader(f)
for i in row:
  print(i)

"""5. Write CSV File For Dictionary"""

mulValues=[{'Name': 'Ahmed','Progress':2,'Year':2022},{'Name': 'Kashif','Progress':5,'Year':2022}]

with open('Details.csv','w', newline='') as file_name:
  fields=['Name','Progress','Year']
  fs=csv.DictWriter(file_name,fieldnames=fields)
  fs.writeheader()
  fs.writerows(rowdicts=mulValues)