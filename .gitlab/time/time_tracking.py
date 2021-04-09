import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime
import json

with open('Timereport.stats.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    test_json = {}

    for line in csv_reader:
        test_json["estimate"] = line[0]
        test_json["spend"] = line[1]
        test_json["LG"] = line[3]
        test_json["SK"] = line[6]
        test_json["CM"] = line[4]
        test_json["LD"] = line[5]

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

# Pie chart, time per team member
labels = 'Simon Kindhauser: \n' + json_data['SK'], 'Caspar Martens: \n' + json_data['CM'], 'Leonie Däullary: \n' + json_data['LD'], 'Lara Gubler: \n' + json_data['LG']
sizes = [test_json['SK'], test_json['CM'], test_json['LD'], test_json['LG']]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')

plt.savefig('time_tracking.png')
plt.show()

# Bar chart, time estimate/spend
labels = ['estimate/spend']
estimate_means = test_json['estimate']
spend_means = test_json['spend']

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width / 2, estimate_means, width, label='estimate')
rects2 = ax.bar(x + width / 2, spend_means, width, label='spend')

ax.set_ylabel('Time in minutes')
ax.set_title('Comparison time estimate and spend')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.savefig('time_tracking_estimate_spend.png')
plt.show()



