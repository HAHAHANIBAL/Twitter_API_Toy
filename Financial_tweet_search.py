#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc


from twython import Twython, TwythonError

#Requires Authentication as of Twitter API v1.1
#Input custom API
twitter = Twython('APIKEY', 'APISECRET', 'TOKEN', 'TOKENSECRET')
try:
#GET search/tweets documentation
#search options can be found here, date, count, language, etc.
    search_results = twitter.search(q='love'.encode('utf-8'), count=50,lang='en',result_type='popular',geocode='37.781157,-122.398720,10mi')
except TwythonError as e:
    print e

count=0
for tweet in search_results['statuses']:
    count+=1
    #search single date tweet, looking for pre-defined parameters..
    print tweet['text'], '\n'
    if "Feb 25" in tweet['created_at']:
        print 'Tweet from @%s Date: %s' % (tweet['user']['screen_name'], tweet['created_at'])
        print tweet['text'], '\n'

print count
