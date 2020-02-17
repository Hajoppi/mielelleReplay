# -*- coding: utf-8 -*-
import json
import matplotlib.pyplot as plt
import numpy as np


import pandas as pd
import re
from wordcloud import WordCloud
from pathlib import Path



with open('donations.json') as f:
    data = json.load(f)

date_values = {}
messages = []
for value in data:
    date = value["TransactionDate"]
    messages.append(value["Message"])
    if (date in date_values):
        date_values[date] += 1
    else:
        date_values[date] = 1
words = []
for message in messages:
    message_words = message.split(" ")
    for w in message_words:
        if (len(w) > 2 and w != "että"):
            words.append(w.lower().replace("!",""))

wordMap = {}

for w in words:
    if (w in wordMap):
        wordMap[w] += 1
    else:
        wordMap[w] = 1


#words = WordCloud(width=512, height=512).generate_from_frequencies(wordMap)
#plt.figure(figsize=(10, 8), facecolor='k')
#plt.imshow(words)
#plt.axis('off')
#plt.tight_layout(pad=0)
#plt.show()

date_numbers = np.array(list(map(lambda x: date_values[x["TransactionDate"]], data)))

amounts = np.array(list(map(lambda x: x["Amount"], data)))
dates = list(map(lambda x: x["TransactionDate"][:-4], data))
print(amounts)
plt.bar(dates[::-1], amounts)
plt.show()