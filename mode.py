import statistics
import csv
import pandas


df = pandas.read_csv("e.csv")
filedata = df["Height"].tolist()

mode = statistics.mode(filedata)
print(mode)