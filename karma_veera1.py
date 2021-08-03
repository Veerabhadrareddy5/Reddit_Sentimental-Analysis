#!/usr/bin/env python
# coding: utf-8

# In[2]:


import json 
import pandas as pd
import requests
import requests.auth
import datetime as dt
from datetime import datetime
import praw
from praw.models import MoreComments


# In[3]:


client_id='yyQ1y0s1X49FNcWZgFBMjw'
secret_key='Z298-Ooh5Uv3QPTERzq3ZXq2EJqDcQ'

reddit = praw.Reddit(
    client_id="yyQ1y0s1X49FNcWZgFBMjw",
    client_secret="Z298-Ooh5Uv3QPTERzq3ZXq2EJqDcQ",
    user_agent="bxbxb",
    username="veerabhadrareddy",
    password="Veerabhadra@55",
)


# In[3]:


# after creating app in reddit we need to get token access
client_id='NIuT2JF21fmWLw'
secret_key='opN1ncc_gDV44-5J-IVMpVDdtXR42g'

reddit = praw.Reddit(
    client_id="NIuT2JF21fmWLw",
    client_secret="opN1ncc_gDV44-5J-IVMpVDdtXR42g",
    user_agent="ChangeMeClient/0.1 by YourUsername",
    username="veerabhadrareddy",
    password="Veerabhadra@55",
)

#api = PushshiftAPI()
base_url = "https://api.pushshift.io/reddit/search/submission/"


#senstive information dont share password
client_auth = requests.auth.HTTPBasicAuth(client_id, secret_key)
post_data = {"grant_type": "password", "username": "veerabhadrareddy", "password": "Veerabhadra@55"}
headers = {"User-Agent": "ChangeMeClient/0.1 by YourUsername"}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
response.json()

#this is getting authorization i guess
headers = {"Authorization": "bearer " + response.json()['access_token'], "User-Agent": "ChangeMeClient/0.1 by YourUsername"} #use ur access token here
response2 = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
#if you want the info of the user who has been granted the authorization try this command - requests.get(https://oauth.reddit.com/api/v1/me, headers=headers).json()






# In[4]:


api_url = 'https://oauth.reddit.com'
payload = {'before': int(dt.datetime(2021,1,3,23,59).timestamp()), 'after': int(dt.datetime(2021,1,1,0,0).timestamp()), 'subreddit': "COVID19positive", 'limit': None}
request = requests.get(base_url, params=payload)
submissionResponse = request.json()

subredditIds = []
subContent = {}
for k in submissionResponse['data']:
    subredditIds.append('t3_'+k['id'])
    subContent[k['id']] = k['selftext']



# In[6]:


subredditIds


# In[6]:


#userParam = {'id'}
#'user_created_date_time': str(datetime.fromtimestamp(userData['data']['created_utc']))
topicCount = 1
subredditInfo = {}
for submission in reddit.info(subredditIds):
    usernameData = {'username': submission.author}
    userData = requests.get(api_url + '/user/username/about', headers=headers, params=usernameData).json()
    subredditInfo[submission.id] = {'post_id':submission.id, 'name': "t3_"+submission.id, 'topic_or_comment': 'topic'+ str(topicCount), 'parent_id': submission.subreddit_id, 'url': submission.url, 'title': submission.title, 'post_total_awards_received': submission.total_awards_received,
                                    'created_date_time': str(datetime.fromtimestamp(submission.created_utc)), 'post_content': submission.selftext, 'is_video': submission.is_video, 'post_score': submission.score,
                                    'User_name': submission.author, 'user_karma': userData['data']['total_karma'], 'user_awardee_karma(awards received karma)': userData['data']['awardee_karma'],
                                    'user_awarder_karma(awards given karma)': userData['data']['awarder_karma']}
    subredditInfo[submission.id]['post_content'] = subContent[submission.id]
    #subredditInfo = fillUserData(userParam,userData, subredditInfo, submission.id)
    commentCount = 1
    for top_level_comment in submission.comments:
        usernameData1 = {'username': top_level_comment.author}
        userData1 = requests.get(api_url + '/user/username/about', headers=headers, params=usernameData1).json()
        #print(userData1)
        subredditInfo[top_level_comment.id] = {'post_id': top_level_comment.id, 'name': top_level_comment.name, 'topic_or_comment': 'topic' + str(topicCount)+' comment' + str(commentCount), 'parent_id': top_level_comment.parent_id, 'url': top_level_comment.permalink, 'title': '', 'post_total_awards_received': top_level_comment.total_awards_received,
                                               'created_date_time': str(datetime.fromtimestamp(top_level_comment.created_utc)), 'post_content': top_level_comment.body, 'is_video': '', 'post_score': top_level_comment.score,
                                               'User_name': top_level_comment.author, 'user_karma': userData1['data']['total_karma'], 'user_awardee_karma(awards received karma)': userData1['data']['awardee_karma'],
                                               'user_awarder_karma(awards given karma)': userData1['data']['awarder_karma']}
        #subredditInfo = fillUserData(userParam,userData1, subredditInfo, top_level_comment.id)
        subcommentCount = 1
        for second_level_comment in top_level_comment.replies:
            usernameData2 = {'username': second_level_comment.author}
            userData2 = requests.get(api_url + '/user/username/about', headers=headers, params=usernameData2).json()
            subredditInfo[second_level_comment.id] = {'post_id': second_level_comment.id, 'name': second_level_comment.name, 'topic_or_comment': 'topic' + str(topicCount)+ ' comment' + str(commentCount) + ' SubCom' + str(subcommentCount), 'parent_id': second_level_comment.parent_id, 'url': second_level_comment.permalink, 'title': '', 'post_total_awards_received': second_level_comment.total_awards_received,
                                               'created_date_time': str(datetime.fromtimestamp(second_level_comment.created_utc)), 'post_content': second_level_comment.body, 'is_video': '', 'post_score': second_level_comment.score,
               
                                                      'User_name': second_level_comment.author, 'user_karma': userData2['data']['total_karma'], 'user_awardee_karma(awards received karma)': userData2['data']['awardee_karma'],
                                               'user_awarder_karma(awards given karma)': userData2['data']['awarder_karma']}
            #subredditInfo = fillUserData(userParam, userData2, subredditInfo, second_level_comment.id)
            subcommentCount = subcommentCount + 1    
        commentCount = commentCount + 1
    topicCount = topicCount + 1    
    df1 = pd.DataFrame.from_dict(subredditInfo, orient='index')


# In[7]:


len(df1)


# In[8]:


df1


# In[9]:


df1.to_csv('covid_reddit',sep='\t')
df1.to_csv(r'C:\Users\veera\Desktop\sample_covid_21__11-6_.csv')


# 

# In[ ]:




