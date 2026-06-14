from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    
    if analysis.sentiment.polarity > 0:
        return "Positive 😊"
    elif analysis.sentiment.polarity < 0:
        return "Negative 😞"
    else:
        return "Neutral 😐"

texts = [
    "I love this product!",
    "This is the worst experience ever.",
    "It is okay, nothing special."
]

for t in texts:
    print("Text:", t)
    print("Sentiment:", analyze_sentiment(t))
    print()