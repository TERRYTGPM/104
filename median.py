import csv

with open("e.csv", newline='') as f:
    reader = csv.reader(f)
    data = list(reader)



data.pop(0)
totalw = 0
totale = 0
sortdata = []

for e in data:
    totalw = totalw + float(e[2])
    totale = totale + 1


sortdata.push(totalw)
sortdata.sort()


if totale%2 == 0:
    m1 = float(totale//2)
    m2 = float(totale//2 -1)

    median = (m1+m2)/2
    print(median)

else:
    median = totale//2
    print(median)