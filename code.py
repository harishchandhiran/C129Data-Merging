import csv
import pandas as pd

data1 = []
data2 = []

with open("stars.csv","r") as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        data1.append(i)

with open("brown_dwarfs.csv","r") as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        data2.append(i)

headers_1 = data1[0]
headers_2 = data2[0]

star_data1 = data1[1:]
star_data2 = data2[1:]

headers = headers_1 + headers_2

star_data = []

for index,data_row in enumerate(star_data1):
    star_data.append(star_data1[index]+star_data2[index])

with open("dataset.csv","a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(star_data)