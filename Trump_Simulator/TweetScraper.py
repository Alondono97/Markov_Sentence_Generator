import json
import requests 
import json
from requests_oauthlib import OAuth1

months = {'Jan':1,
          'Feb':2,
          'Mar':3,
          'Apr':4,
          'May':5,
          'Jun':6,
          'Jul':7,
          'Aug':8,
          'Sep':9,
          'Oct':10,
          'Nov':11,
          'Dec':12}

def check_date(date):
  # returns true if date is after 6-16-2015
  # else returns false
  date_elements = date.split()
  # print(date_elements)

  year = int(date_elements[5])
  month = months[date_elements[1]]
  day = int(date_elements[2])
  
  if year < 2015:
    return False
  elif year == 2015:
    if month < 6:
      return False
    elif month == 6:
      if day < 16:
        return False 
  

  return True
    

  
  

GET_TWEET_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

#reads api keys from text file
f = open('twitter_api_keys.txt')  
keys = f.readlines()

#strips new line character from api key
for i in range(4):
  keys[i] = keys[i].strip() 

CONSUMER_KEY = keys[0]
CONSUMER_SECRET = keys[1]
ACCESS_TOKEN = keys[2]
ACCESS_TOKEN_SECRET = keys[3]

oauth = OAuth1(CONSUMER_KEY,
  client_secret=CONSUMER_SECRET,
  resource_owner_key=ACCESS_TOKEN,
  resource_owner_secret=ACCESS_TOKEN_SECRET)


tweet_text_list = []
tweet_list = []


'''
first_tweet_data = {'screen_name':'realDonaldTrump','count':'1','include_rts':'False',
          'tweet_mode':'extended','exclude_replies':'true'}
first_tweet_req = requests.get(GET_TWEET_URL, auth=oauth,params=first_tweet_data)
first_tweet = json.loads(first_tweet_req.text)
curr_date = first_tweet[0]['created_at']
maxid = first_tweet[0]['id'] - 1

tweet_text_list.append(first_tweet[0]['full_text'])
# print('first tweet:')
# print(first_tweet)
# print('\n\n' + curr_date)
# print('\nBegin tweetlist: \n\n')
n =  0
# while(check_date(curr_date)):
'''
maxid = 0
with open('max_id.txt', 'r') as max_id_file:
  maxid = int(max_id_file.readline())


n = 0
while(len(tweet_text_list) < 2518):
  n+=1
  # print(n)
  data = {'screen_name':'realDonaldTrump','count':'200','include_rts':'False',
          'tweet_mode':'extended','exclude_replies':'true','max_id':maxid}
  req = requests.get(GET_TWEET_URL, auth=oauth,params=data)
  # print('req == ', req.text)
  timeline = json.loads(req.text)
  # print(timeline[0])
  if timeline:
    maxid = timeline[0]['id']
    for tl in timeline:
      if tl['id'] < maxid:
        maxid = tl['id']
      tweet_text_list.append(tl['full_text'])
      tweet_list.append(tl)
    curr_date = timeline[len(timeline) - 1]['created_at']  
    # print('curr_date: ' + curr_date)
    # print(tweet_text_list[-1])
    maxid -= 1
  else:
    print(maxid)
    if tweet_text_list:
      print(tweet_text_list[-1])
      print(tweet_list[-1])


print('tweetlist length: ')
print(len(tweet_text_list))
print('\n\ntweet list 1: ')
print(tweet_list[0])
print('\n\ntweetlist 2: ')
print(tweet_list[len(tweet_list) - 1])


'''
with open('tweet_corpus.txt', 'w') as tweetfile:

  for tweet in enumerate(tweet_text_list):
    tweet_text = str(tweet[1])
    if tweet_text[-1] == ' ':
      tweet_text = tweet_text + '.'
    tweetfile.write(tweet_text)


with open('max_id.txt', 'w') as id_file:
  id_file.write(str(maxid))
'''