import requests
word = 'Im a developer'
url = "https://sentiment-analytics-api.herokuapp.com/?text={}".format(word) 
response = requests.get(url)
 
data = response.json()
 
print(data)
 
for i in data:
 
    print(i, data[i])

# --- Response Sample
# {"Polarity":0.0,"Sentiment":"Neutral","Sentiment Level":"NEU","Subjectivity":0.0,"Text":"Im a developer"}
"""
output = response.json()

Polarity = output['Polarity']

Sentiment = output['Sentiment']

sentimentLevel = output['Sentiment Level']

Subjectivity = output['Subjectivity']

Text = output['Text']

"""