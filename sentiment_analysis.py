from textblob import TextBlob
import sys

# # Requirements
# Install TextBlob
# `pip install TextBlob` 
# # How to run 
# `python sentiment_analysis.py <DATASETFILE>`
# or to save the output to a file
# `python sentiment_analysis.py <DATASETFILE> > <DATASETFILE>_analysis_result.csv`


def find_ngrams(n, input_sequence):
    # Split sentence into tokens.
    tokens = input_sequence.split()
    ngrams = []
    for i in range(len(tokens) - n + 1):
        # Take n consecutive tokens in array.
        ngram = tokens[i:i+n]
        # Concatenate array items into string.
        ngram = ' '.join(ngram)
        ngrams.append(ngram)

    return ngrams

def analysis_tweet(tweet):
    ngrams = find_ngrams(3, tweet)
    analysis = {}
    avg = 0
    for ngram in ngrams:
        blob = TextBlob(ngram)
        avg += blob.sentiment.polarity
    if len(ngrams) > 0:
        avg = avg/len(ngrams)
    sentiment = 'neutral'
    if avg > 0:
        sentiment = 'positive'
    elif avg < 0:
        sentiment = 'negative'
    return sentiment

if __name__ == '__main__':
    #open file from argv param
    dataset = open(sys.argv[1], 'r')
    #read from the file all the tweets
    tweets = dataset.readlines()    

    #loop over tweets with a sentiment analysis function
    for tweet in tweets:
        # remove line breaks
        tweet = tweet.replace('\n', '') 
        print("Sentiment:%s , Tweet:'%s'" % (analysis_tweet(tweet), tweet))
