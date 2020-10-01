
import json
from collections import Counter

temp = []
with open('message_1.json') as json_file:
    data = json.load(json_file)
    
    for i, message in enumerate(data['messages']):
        if message["sender_name"] == "Benjamin De Worsop":
            if "content" in message.keys():
                temp = temp + message["content"].split(' ')

# print(temp)

count = Counter(temp)
temp2 = count.most_common(100)

for word in temp2:
    if len(word[0]) > 3:
        print(word)