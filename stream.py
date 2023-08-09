import tweepy
from matplotlib import pyplot as plt
from textblob import TextBlob
import codecs

def percentage(part,whole):
    return 100*float(part)/float(whole)

class project:
    positive = 0
    negative = 0
    neutral = 0
    polarity = 0
    not_analysed = 0
    searchTerm = ''
    noOfSearchTerm = 0
    file=''
    def tweetFeed(self,searchTerm,noOfSearchTerm,consumer_key,consumer_secret_key,access_token,access_secret_token,file='tola'):
        self.searchTerm=searchTerm
        self.noOfSearchTerm=noOfSearchTerm
        auth=tweepy.OAuthHandler(consumer_key,consumer_secret_key)
        auth.set_access_token(access_token,access_secret_token)
        api=tweepy.API(auth)
        #self.searchTerm=input("Enter the term you want to search\n")
        #self.noOfSearchTerm=int(input("Enter the number of tweets you want to feed\n"))
        tweets=tweepy.Cursor(api.search,self.searchTerm).items(self.noOfSearchTerm)

        file=codecs.open(file+'.txt',"wb","utf-8-sig")
        for tweet in tweets:
            data=tweet.text
            file.write(data)
            analysis=TextBlob(tweet.text)
            self.polarity+=analysis.sentiment.polarity
            if analysis.sentiment.polarity==0:
                self.neutral+=1
            if analysis.sentiment.polarity<0.00:
                self.negative+=1
            if analysis.sentiment.polarity>0.00:
                self.positive+=1
        self.not_analysed=self.noOfSearchTerm-(self.positive+self.negative+self.neutral)
        self.not_analysed=percentage(self.not_analysed,self.noOfSearchTerm)
        file.close()
    def graph(self):
        self.positive = format(percentage(self.positive, self.noOfSearchTerm), '.2f')
        self.neutral = format(percentage(self.neutral, self.noOfSearchTerm), '.2f')
        self.negative = format(percentage(self.negative, self.noOfSearchTerm), '.2f')
        label=[f"positive {self.positive} %",f"negative{self.negative}%",f"neutral{self.neutral}",f"no. of tweets not available for analysis{self.not_analysed}%"]
        sizes=[self.positive,self.negative,self.neutral,self.not_analysed]
        color=["yellowgreen","red","gold","black"]

        patches,texts=plt.pie(sizes,colors=color,startangle=90)
        plt.legend(patches,label,loc="lower right")
        plt.title(f"how people are reacting on {self.searchTerm} by analysing {self.noOfSearchTerm} tweets!")
        plt.axis('equal')
        plt.tight_layout()
        plt.show()