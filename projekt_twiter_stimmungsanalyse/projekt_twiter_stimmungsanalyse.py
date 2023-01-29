import json
from textblob import TextBlob

# obama = []
with open("data.json", "r") as file:
    data_js = json.load(file)
    # for entry in data_js:
        # if "obama" in entry["topic"]:
        #     obama.append(entry)
obama = [x for x in data_js if x["topic"] == "obama"]
for topic in obama:
    tweet = topic["tweet"]
    twobama = TextBlob(tweet)
    polar = twobama.sentiment.polarity
    if polar < -0.2:
        topic["sentiment"] = "negative"
    elif polar > 0.2:
        topic["sentiment"] = "positive"
    else:
        topic["sentiment"] = "neutral"

with open("obama.json", "w") as file:
    json.dump(obama, file)
    
import seaborn as sns
sns.set_theme()
sen_obama = [tweet["sentiment"]for tweet in obama]
sns_plot = sns.histplot(x = sen_obama)
sns_plot.figure.savefig("sentiment_obama.png")