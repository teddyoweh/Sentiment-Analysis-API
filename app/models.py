
from textblob import TextBlob
class analyzeSentiment:
    
    def result(text):

        pol = TextBlob(text).sentiment.polarity
        sub = TextBlob(text).sentiment.subjectivity
        
        if pol >= 0.8:
            senmt = 'P++'
        elif pol >=0.5:
            senmt = 'P+'
        elif pol >=0.3:
            senmt = 'P'
        elif pol >=0.0:
            senmt = 'NEU'
        elif pol >=-0.1:
            senmt = 'N'
        elif pol >=-0.4:
            senmt = 'N+'
        elif pol >=-0.8:
            senmt = 'N++'
        if senmt.startswith('NEU'):
            sentiment = 'Neutral'
        elif senmt.startswith('N'):
            sentiment = 'Negative'
        elif senmt.startswith('P'):
            sentiment = 'Positive'
        
        box = [text,sentiment,senmt,pol,sub]
        return box
    