import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime
import json

with open('Timereport2.stats.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    test_json = {}

    for line in csv_reader:
        test_json["LG"] = line[3]
        test_json["SK"] = line[4]
        test_json["CM"] = line[5]
        test_json["LD"] = line[6]

json_data = test_json.copy()

print("json_data")
print(json_data)


for key in test_json:
    total_time = 0

    split_time = test_json[key].split(' ')
    for item in split_time:
        if 'd' in item:
            total_time += int(''.join(filter(lambda i: i.isdigit(), item))) * 8 * 60
        if 'h' in item:
            total_time += int(''.join(filter(lambda i: i.isdigit(), item))) * 60
        if 'm' in item:
            total_time += int(''.join(filter(lambda i: i.isdigit(), item)))

    test_json[key] = total_time


print("total time")
print(test_json)

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Simon Kindhauser: \n' + json_data['SK'], 'Caspar Martens: \n' + json_data['CM'], 'Leonie Däullary: \n' + json_data['LD'], 'Lara Gubler: \n' + json_data['LG']
sizes = [test_json['SK'], test_json['CM'], test_json['LD'], test_json['LG']]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.savefig('time_tracking.png')
plt.show()

