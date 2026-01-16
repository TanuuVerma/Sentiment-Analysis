from textblob import TextBlob

print("AI Sentiment Analyzer")
print("----------------------")

text = input("Enter text: ")

analysis = TextBlob(text)
polarity = analysis.sentiment.polarity

if polarity > 0.05:
    print("Sentiment: Positive 😊")
elif polarity < -0.05:
    print("Sentiment: Negative 😞")
else:
    print("Sentiment: Neutral 😐")
