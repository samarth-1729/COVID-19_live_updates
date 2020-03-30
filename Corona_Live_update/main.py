# Importing all the required libraries

import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import os
import numpy as np 
import matplotlib.pyplot as plt

# Extracting the data

extract_content = lambda row: [x.text.replace('\n','') for x in row]

URL = 'https://www.mohfw.gov.in/'

SHORT_HEADERS = ['SNo','State','Indian-Confirmed','Foreign-Confirmed','Cured','Death']

response = requests.get(URL).content

soup = BeautifulSoup(response, 'html.parser')

header = extract_content(soup.tr.find_all('th'))

stats = []

all_rows = soup.find_all('tr')

for row in all_rows:
    stat = extract_content(row.find_all('td'))
    # print(stat)
    if stat:
        if len(stat) == 5:
            # print(stat)
            # last row 
            stat = ['', *stat]
            # print(stat)
            stats.append(stat)

        elif len(stat) == 6:
            stats.append(stat)

stats[-1][1] = "Total Cases"
# print(stats[-1][1])
stats.remove(stats[-1])

# Table Information

objects = []

for row in stats:
    objects.append(row[1])
# print(objects)
y_pos = np.arange(len(objects))
# print(y_pos)
performance = []

for row in stats:
    # print(row[2], row[3])
    performance.append(int(row[2]) + int(row[3]))
# print(performance)
table = tabulate(stats, headers=SHORT_HEADERS)

print(table)

# Plot the graph

plt.barh(y_pos, performance, align='center', alpha = 0.5,
                color = (234/256.0, 128/256.0, 252/256.0),
                edgecolor = (106/256.0, 27/256.0, 154/256.0))

plt.yticks(y_pos, objects)
plt.xlim(1, 200)
plt.xlabel('Number of Cases')
plt.title('Corona Virus Cases')
plt.show()
