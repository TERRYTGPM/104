import csv

with open("e.csv", newline='') as f:
    reader = csv.reader(f)
    data = list(reader)



data.pop(0)
totalw = 0
totale = 0

for e in data:
    totalw = totalw + float(e[2])
    totale = totale + 1

medain = float(totalw / totale)

print(medain)