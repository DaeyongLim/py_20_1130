#!/usr/bin/env python
# coding: utf-8

# In[1]:


with open('news_naver.html', encoding='cp949') as f:
    news_html = f.read()


# In[2]:


import re

body = re.search('<body.*/body>', news_html, re.I|re.S) # re.S == re.DOTALL
body = body.group()
body = re.sub('<script.*?>.*?</script>', '', body, 0, re.I|re.S)
text = re.sub('<.+?>', '', body, 0, re.I|re.S)
nospace = re.sub('&nbsp;| |\t|\r|\n', '', text)
print (f'news_html = {len(news_html)}, text = {len(text)}, word = {len(text.split())} nospace = {len(nospace)}')


# In[3]:


with open('sports.html', encoding='UTF8') as f:
    sports_html = f.read()


# In[5]:


import re

body = re.search('<body.*/body>', sports_html, re.I|re.S) # re.S == re.DOTALL
body = body.group()
body = re.sub('<script.*?>.*?</script>', '', body, 0, re.I|re.S)
text = re.sub('<.+?>', '', body, 0, re.I|re.S)
nospace = re.sub('&nbsp;| |\t|\r|\n', '', text)
print (f'sports_html = {len(sports_html)}, text = {len(text)}, word = {len(text.split())} nospace = {len(nospace)}')

