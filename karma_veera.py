#!/usr/bin/env python
# coding: utf-8

# In[70]:


import json 
import pandas as pd
import requests
import requests.auth
import datetime as dt
from datetime import datetime

import praw
from praw.models import MoreComments

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


# In[71]:


api_url = 'https://oauth.reddit.com'
payload = {'before': int(dt.datetime(2021,7,6,23,59).timestamp()), 'after': int(dt.datetime(2021,7,1,0,0).timestamp()), 'subreddit': "COVID19positive", 'limit': None}
request = requests.get(base_url, params=payload)
submissionResponse = request.json()


# In[72]:


import pandas as pd
import numpy as np
temp=pd.read_csv(r'C:\Users\veera\Desktop\covid_reddit_final\july\covid_21_july6_1_.csv')
subredditIds1=[]
score=list(temp["post_id"])
subredditIds = list(temp['name'])

len(subredditIds)


# In[ ]:





# In[73]:


user_score=[]
for i in score:
    try:
        sc1=reddit.comment(i)
        user_score.append(sc1.score)
        
    except:
        user_score.append(0)


# In[74]:


down_votes=[]
up=[]
up_vote_ratio=[]


# In[75]:


for i in user_score:
    Ratio=0.75
    down = (i * (Ratio - 1))/(1 - (2 * Ratio))
    upvotes = i + down
    down_votes.append(down)
    up.append(upvotes)
    up_vote_ratio.append(upvotes*down)
    
    
    


# In[76]:


created_date=[]
for i in score:
    try:
        sc1=reddit.comment(i)
        created_date.append(sc1.created_utc )
        
    except:
        created_date.append(0)


# In[77]:


dfv=pd.DataFrame()
has={}
count=0


# In[78]:


for submission in reddit.info(subredditIds): 
    usernameData = {'username': submission.author}
    userData = requests.get(api_url + '/user/username/about', headers=headers, params=usernameData).json()
    has[count]=userData['data']
    count+=1
   


# In[79]:


len(has)


# In[80]:


is_employee=[]
for i in range(len(has)):
    try:
        is_employee.append(has[i]['is_employee'])
        
    except:
        is_employee.append('False')
len(is_employee)


# In[81]:


is_friend=[]
for i in range(len(has)):
    try:
        is_friend.append(has[i]['is_friend'])
        
    except:
        is_friend.append('False')
len(is_friend)


# In[82]:


default_set=[]
for i in range(len(has)):
    try:
        default_set.append(has[i]['subreddit']['default_set'])
        
    except:
        default_set.append('False')
len(default_set)


# In[83]:


user_is_contributor=[]
for i in range(len(has)):
    try:
        user_is_contributor.append(has[i]['subreddit']['user_is_contributor'])
        
    except:
        user_is_contributor.append('False')
len(user_is_contributor)


# In[84]:


banner_img=[]
for i in range(len(has)):
    try:
        banner_img.append(has[i]['subreddit']['banner_img'])
        
    except:
        banner_img.append(' ')
len(banner_img)


# In[85]:


user_is_banned=[]
for i in range(len(has)):
    try:
        user_is_banned.append(has[i]['subreddit']['user_is_banned'])
        
    except:
        user_is_banned.append('False')
len(user_is_banned)


# In[86]:


restrict_posting=[]
for i in range(len(has)):
    try:
        restrict_posting.append(has[i]['subreddit']['restrict_posting'])
        
    except:
        restrict_posting.append('False')
len(restrict_posting)


# In[87]:


free_form_reports=[]
for i in range(len(has)):
    try:
        free_form_reports.append(has[i]['subreddit']['free_form_reports'])
        
    except:
        free_form_reports.append('False')
len(free_form_reports)


# In[88]:


community_icon=[]
for i in range(len(has)):
    try:
        community_icon.append(has[i]['subreddit']['community_icon'])
        
    except:
        community_icon.append('None')
len(community_icon)


# In[89]:


show_media=[]
for i in range(len(has)):
    try:
        show_media.append(has[i]['subreddit']['show_media'])
        
    except:
        show_media.append('False')
len(show_media)


# In[90]:


icon_color=[]
for i in range(len(has)):
    try:
        icon_color.append(has[i]['subreddit']['icon_color'])
        
    except:
        icon_color.append(' ')
len(icon_color)


# In[91]:


user_is_muted=[]
for i in range(len(has)):
    try:
        user_is_muted.append(has[i]['subreddit']['user_is_muted'])
        
    except:
        user_is_muted.append('False ')
len(user_is_muted)


# In[92]:


display_name=[]
for i in range(len(has)):
    try:
        display_name.append(has[i]['subreddit']['display_name'])
        
    except:
        display_name.append(' ')
len(display_name)


# In[93]:


header_img=[]
for i in range(len(has)):
    try:
        header_img.append(has[i]['subreddit']['header_img'])
        
    except:
        header_img.append('None')
len(header_img)


# In[94]:


title=[]
for i in range(len(has)):
    try:
        title.append(has[i]['subreddit']['title'])
        
    except:
        title.append(' ')
len(title)


# In[95]:


previous_names=[]
for i in range(len(has)):
    try:
        previous_names.append(has[i]['subreddit']['previous_names'])
        
    except:
        previous_names.append(' ')
len(previous_names)


# In[96]:


over_18=[]
for i in range(len(has)):
    try:
        over_18.append(has[i]['subreddit']['over_18'])
        
    except:
        over_18.append('False ')
len(over_18)


# In[97]:


icon_size=[]
for i in range(len(has)):
    try:
        icon_size.append(has[i]['subreddit']['icon_size'])
        
    except:
        icon_size.append([256, 256])
len(icon_size)


# In[98]:


primary_color=[]
for i in range(len(has)):
    try:
        primary_color.append(has[i]['subreddit']['primary_color'])
        
    except:
        primary_color.append(" ")
len(primary_color)



# In[99]:


icon_img=[]
for i in range(len(has)):
    try:
        icon_img.append(has[i]['subreddit']['icon_img'])
        
    except:
        icon_img.append(" ")
len(icon_img)


# In[100]:


description=[]
for i in range(len(has)):
    try:
        description.append(has[i]['subreddit']['description'])
        
    except:
        description.append(" ")
len(description)


# In[101]:


submit_link_label=[]
for i in range(len(has)):
    try:
        submit_link_label.append(has[i]['subreddit']['submit_link_label'])
        
    except:
        submit_link_label.append(" ")
len(submit_link_label)


# In[102]:


header_size=[]
for i in range(len(has)):
    try:
        header_size.append(has[i]['subreddit']['header_size'])
        
    except:
        header_size.append("None")
len(header_size)


# In[103]:


restrict_commenting=[]
for i in range(len(has)):
    try:
        restrict_commenting.append(has[i]['subreddit']['restrict_commenting'])
        
    except:
        restrict_commenting.append("False")
len(restrict_commenting)


# In[104]:


subscribers=[]
for i in range(len(has)):
    try:
        subscribers.append(has[i]['subreddit']['subscribers'])
        
    except:
        subscribers.append(0)
len(subscribers)


# In[105]:


submit_text_label=[]
for i in range(len(has)):
    try:
        submit_text_label.append(has[i]['subreddit']['submit_text_label'])
        
    except:
        submit_text_label.append(" ")
len(submit_text_label)


# In[106]:


is_default_icon=[]
for i in range(len(has)):
    try:
        is_default_icon.append(has[i]['subreddit']['is_default_icon'])
        
    except:
        is_default_icon.append("False")
len(is_default_icon)


# In[107]:


link_flair_position=[]
for i in range(len(has)):
    try:
        link_flair_position.append(has[i]['subreddit']['link_flair_position'])
        
    except:
        link_flair_position.append(" ")
len(link_flair_position)


# In[108]:


display_name_prefixed=[]
for i in range(len(has)):
    try:
        display_name_prefixed.append(has[i]['subreddit']['display_name_prefixed'])
        
    except:
        display_name_prefixed.append(" ")
len(display_name_prefixed)


# In[109]:


key_color=[]
for i in range(len(has)):
    try:
        key_color.append(has[i]['subreddit']['key_color'])
        
    except:
        key_color.append(" ")
len(subscribers)


# In[110]:


name=[]
for i in range(len(has)):
    try:
        name.append(has[i]['subreddit']['name'])
        
    except:
        name.append(" ")
len(name)


# In[111]:


is_default_banner=[]
for i in range(len(has)):
    try:
        is_default_banner.append(has[i]['subreddit']['is_default_banner'])
        
    except:
        is_default_banner.append("False ")
len(name)


# In[112]:


url=[]
for i in range(len(has)):
    try:
        url.append(has[i]['subreddit']['url'])
        
    except:
        url.append(" ")
len(url)


# In[113]:


quarantine=[]
for i in range(len(has)):
    try:
        quarantine.append(has[i]['subreddit']['quarantine'])
        
    except:
        quarantine.append("False")
len(quarantine)


# In[114]:


banner_size=[]
for i in range(len(has)):
    try:
        banner_size.append(has[i]['subreddit']['banner_size'])
        
    except:
        banner_size.append("None")
len(banner_size)


# In[115]:


user_is_moderator=[]
for i in range(len(has)):
    try:
        user_is_moderator.append(has[i]['subreddit']['user_is_moderator'])
        
    except:
        user_is_moderator.append("False")
len(user_is_moderator)


# In[116]:


public_description=[]
for i in range(len(has)):
    try:
        public_description.append(has[i]['subreddit']['public_description'])
        
    except:
        public_description.append(" ")
len(public_description)


# In[117]:


link_flair_enabled=[]
for i in range(len(has)):
    try:
        link_flair_enabled.append(has[i]['subreddit']['link_flair_enabled'])
        
    except:
        link_flair_enabled.append("False")
len(link_flair_enabled)


# In[118]:


disable_contributor_requests=[]
for i in range(len(has)):
    try:
        disable_contributor_requests.append(has[i]['subreddit']['disable_contributor_requests'])
        
    except:
        disable_contributor_requests.append("False")
len(disable_contributor_requests)


# In[119]:


subreddit_type=[]
for i in range(len(has)):
    try:
        subreddit_type.append(has[i]['subreddit']['subreddit_type'])
        
    except:
        subreddit_type.append(" ")
len(subreddit_type)


# In[120]:


user_is_subscriber=[]
for i in range(len(has)):
    try:
        user_is_subscriber.append(has[i]['subreddit']['user_is_subscriber'])
        
    except:
        user_is_subscriber.append("False")
len(user_is_subscriber)


# In[121]:


snoovatar_size=[]
for i in range(len(has)):
    try:
        snoovatar_size.append(has[i]['snoovatar_size'])
        
    except:
        snoovatar_size.append("None")
len(snoovatar_size)


# In[122]:


awarder_karma=[]
for i in range(len(has)):
    try:
        awarder_karma.append(has[i]['awarder_karma'])
        
    except:
        awarder_karma.append(0)
len(awarder_karma)


# In[123]:


id=[]
for i in range(len(has)):
    try:
        id.append(has[i]['id'])
        
    except:
        id.append(0)
len(id)


# In[124]:


verified=[]
for i in range(len(has)):
    try:
        verified.append(has[i]['verified'])
        
    except:
        verified.append("False")
len(verified)


# In[125]:


is_gold=[]
for i in range(len(has)):
    try:
        is_gold.append(has[i]['is_gold'])
        
    except:
        is_gold.append("False")
len(is_gold)


# In[126]:


is_mod=[]
for i in range(len(has)):
    try:
        is_mod.append(has[i]['is_mod'])
        
    except:
        is_mod.append("False")
len(is_mod)


# In[127]:


awardee_karma=[]
for i in range(len(has)):
    try:
        awardee_karma.append(has[i]['awardee_karma'])
        
    except:
        awardee_karma.append(0)
        
len(awardee_karma)


# In[128]:


verified_mail=[]
for i in range(len(has)):
    try:
        verified_mail.append(has[i]['subreddit']['has_verified_email'])
        
    except:
        verified_mail.append('False')
len(verified_mail)


# In[129]:


icon_img=[]
for i in range(len(has)):
    try:
        icon_img.append(has[i]['subreddit']['icon_img'])
        
    except:
        icon_img.append('False')
len(icon_img)


# In[130]:


hide_from_robots=[]
for i in range(len(has)):
    try:
        hide_from_robots.append(has[i]['subreddit']['hide_from_robots'])
        
    except:
        hide_from_robots.append('False')
len(hide_from_robots)


# In[131]:


link_karma=[]
for i in range(len(has)):
    try:
        link_karma.append(has[i]['link_karma'])
        
    except:
        link_karma.append(0)
len(link_karma)


# In[132]:


comment_karma=[]
for i in range(len(has)):
    try:
        comment_karma.append(has[i]['comment_karma'])
        
    except:
        comment_karma.append(0)
len(comment_karma)


# In[133]:


total_karma=[]

for i in range(len(has)):
    try:
        total_karma.append(has[i]['total_karma'])
        
    except:
        total_karma.append(0)
len(total_karma)


# In[134]:


pref_show_snoovatar=[]

for i in range(len(has)):
    try:
        pref_show_snoovatar.append(has[i]['pref_show_snoovatar'])
        
    except:
        pref_show_snoovatar.append("False")
len(pref_show_snoovatar)


# In[135]:


accept_chats=[]

for i in range(len(has)):
    try:
        accept_chats.append(has[i]['accept_chats'])
        
    except:
        accept_chats.append("False")
len(accept_chats)


# In[136]:


name=[]
for i in range(len(has)):
    try:
        name.append(has[i]['name'])
        
    except:
        name.append('False')
len(name)


# In[137]:


cake_day=[]
for i in range(len(has)):
    try:
        cake_day.append(has[i]['created_utc'])
        
    except:
        cake_day.append(0)
len(cake_day)


# In[138]:


created=[]
for i in range(len(has)):
    try:
        created.append(has[i]['created'])
        
    except:
        created.append(0)
len(created)


# In[139]:


snoovatar_img=[]
for i in range(len(has)):
    try:
        snoovatar_img.append(has[i]['snoovatar_img'])
        
    except:
        snoovatar_img.append(" ")
len(snoovatar_img)


# In[140]:


accept_followers=[]

for i in range(len(has)):
    try:
        accept_followers.append(has[i]['accept_followers'])
        
    except:
        accept_followers.append("False")
len(accept_followers)


# In[141]:


has_subscribed=[]

for i in range(len(has)):
    try:
        has_subscribed.append(has[i]['has_subscribed'])
        
    except:
        has_subscribed.append("False")
len(has_subscribed)


# In[142]:


accept_pms=[]

for i in range(len(has)):
    try:
        accept_pms.append(has[i]['accept_pms'])
        
    except:
        accept_pms.append("False")
len(accept_pms)


# In[147]:


dic1={}


# In[161]:


dic={"user_score":user_score,"up":up}


# In[169]:


dic1={"user_score":user_score,"down_votes":down_votes,"up":up,"up_vote_ratio":up_vote_ratio,
     "created_date":created_date,"is_employee":is_employee,"is_friend":is_friend,"default_set":default_set,
     "user_is_contributor":user_is_contributor,"banner_img":banner_img
     ,"user_is_banned":user_is_banned,"restrict_posting":restrict_posting,
     "free_form_reports":free_form_reports,"community_icon":community_icon,
     "show_media":show_media,"icon_color":icon_color,"user_is_muted":user_is_muted,
     "display_name":display_name,"header_img":header_img,"title":title,
     "previous_names":previous_names,"over_18":over_18,
     "icon_size":icon_size,"primary_color":primary_color,"icon_img":icon_img,"description":description,"submit_link_label":submit_link_label,
"header_size":header_size, "restrict_commenting":restrict_commenting,"subscribers":subscribers,
     "submit_text_label":submit_text_label,"is_default_icon":is_default_icon,"link_flair_position":link_flair_position,
     "display_name_prefixed":display_name_prefixed,"key_color":key_color,"name":name,"is_default_banner":is_default_banner,
     "url":url,"quarantine":quarantine,"banner_size":banner_size,"user_is_moderator":user_is_moderator,
     "public_description":public_description,"link_flair_enabled":link_flair_enabled,
     "disable_contributor_requests":disable_contributor_requests,"subreddit_type":subreddit_type,
     "user_is_subscriber":user_is_subscriber,"snoovatar_size":snoovatar_size,"awarder_karma":awarder_karma,
     "id":id,"verified":verified,"is_gold":is_gold,"is_mod":is_mod,"awardee_karma":awardee_karma,"verified_mail":verified_mail,
     "icon_img":icon_img,"hide_from_robots":hide_from_robots,"link_karma":link_karma,"comment_karma":comment_karma,
     "total_karma":total_karma,"pref_show_snoovatar":pref_show_snoovatar,"accept_chats":accept_chats,
     "name":name,"cake_day":cake_day,"created":created,"snoovatar_img":snoovatar_img,"accept_followers":accept_followers,
     "has_subscribed":has_subscribed,"accept_pms":accept_pms
     
      }


# In[172]:


dfk=pd.DataFrame(dic1)


# In[173]:


dfk


# In[174]:


dfk.to_csv('covid_reddit',sep='\t')
dfk.to_csv(r'C:\Users\veera\Desktop\covid_reddit_final\july\covid_21_july6_111_karma.csv')


# In[ ]:




