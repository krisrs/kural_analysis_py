
# coding: utf-8

# In[1]:

#import required packages
import numpy as np
import pandas as pd
import nltk
import tamil
import matplotlib.pyplot as plt


# In[2]:

pd_kural = pd.read_csv('F:/analytics/analytics_experiments_personal/kural/kural_dat_utf8.txt',index_col=0,sep=',',header='infer')


# In[3]:

kural_list = list(pd_kural["kural"])


# In[4]:

ng_test = nltk.ngrams(kural_list[0].split(" "),2)
for grams in ng_test : print(grams)


# In[5]:

tri_array = []
for i in range(0,3) : 
    ng = nltk.ngrams(kural_list[i].split(" "),3)
    for grams in ng : 
        tri_array.append(grams)
print(tri_array)


# In[6]:

kural_vocab = []
for i in range(len(kural_list)) :
    k = kural_list[i].split()
    kural_vocab.extend(k)


# In[7]:

wc=[]
for i in range(len(kural_vocab)) :
    c=0
    for j in range(len(kural_list)) :
        c = c + kural_list[j].count(kural_vocab[i])
    wc.append([kural_vocab[i],c])


# In[8]:

len(wc)


# In[9]:

pd_unicount = pd.DataFrame(data=wc)


# In[10]:

pd_unicount.head()
pd_unicount.columns = ["word","count"]
pd_unicount = pd_unicount.drop_duplicates()
pd_unicount.head()


# In[11]:

pd_unicount.describe()


# In[12]:

pd_unicount.query('count==1912')


# In[13]:

pd_unicount = pd_unicount[pd_unicount.word != "ம்"]
pd_unicount.describe()


# In[14]:

pd_unicount.query('count==1717')


# In[15]:

pd_unicount = pd_unicount[pd_unicount.word != "ட"]
pd_unicount.describe()


# In[16]:

pd_unicount.query('count==1314')



# In[17]:

pd_unicount = pd_unicount[pd_unicount.word != "ர்"]
pd_unicount.describe()


# In[18]:

pd_unicount.query('count==736')


# In[19]:

pd_unicount = pd_unicount[pd_unicount.word != "கு"]
pd_unicount.describe()


# In[20]:

pd_unicount.query('count==331')


# In[21]:

pd_unicount = pd_unicount[pd_unicount.word != "க்கு"]
pd_unicount.describe()


# In[22]:

pd_unicount.query('count==233')


# In[23]:

pd_unisort=pd_unicount.sort_values(by='count',ascending=0)
pd_unisort.head()


# In[24]:

test = pd_unisort.query('count>10 and count <=500')


# In[25]:

test_x=list(test["word"])
test_y=list(test["count"])
test_s=list(test["count"])


# In[26]:

import plotly as py
import plotly.graph_objs as go
py.offline.init_notebook_mode()

trace0 = go.Scatter(
    x= test_x,
    y= test_y,
    mode='markers',
    marker=dict(
        size=test_s,
    )
)

data = [trace0]
py.offline.iplot(data, filename='bubblechart-size')


# In[27]:

uyir = ['அ','ஆ','இ','ஈ','உ','ஊ','எ','ஏ','ஐ','ஒ','ஓ','ஔ']
len(uyir)


# In[28]:

mey = ['க்','ங்','ச்','ஞ்','ட்','ண்','த்','ந்','ப்','ம்','ய்','ர்','ல்','வ்','ழ்','ள்','ற்','ன்']
len(mey)


# In[29]:

uyirmey = ['க','கா','கி','கீ','கு','கூ','கெ','கே','கை','கொ','கோ','கௌ','ங','ஙா','ஙி','ஙீ','ஙு','ஙூ','ஙெ','ஙே','ஙை','ஙொ','ஙோ','ஙௌ','ச','சா','சி','சீ','சு','சூ','செ','சே','சை','சொ','சோ','சௌ','ஞ','ஞா','ஞி','ஞீ','ஞு','ஞூ','ஞெ','ஞே','ஞை','ஞொ','ஞோ','ஞௌ','ட','டா','டி','டீ','டு','டூ','டெ','டே','டை','டொ','டோ','டௌ','ண','ணா','ணி','ணீ','ணு','ணூ','ணெ','ணே','ணை','ணொ','ணோ','ணௌ','த','தா','தி','தீ','து','தூ','தெ','தே','தை','தொ','தோ','தௌ','ந','நா','நி','நீ','நு','நூ','நெ','நே','நை','நொ','நோ','நௌ','ப','பா','பி','பீ','பு','பூ','பெ','பே','பை','பொ','போ','பௌ','ம','மா','மி','மீ','மு','மூ','மெ','மே','மை','மொ','மோ','மௌ','ய','யா','யி','யீ','யு','யூ','யெ','யே','யை','யொ','யோ','யௌ','ர','ரா','ரி','ரீ','ரு','ரூ','ரெ','ரே','ரை','ரொ','ரோ','ரௌ','ல','லா','லி','லீ','லு','லூ','லெ','லே','லை','லொ','லோ','லௌ','வ','வா','வி','வீ','வு','வூ','வெ','வே','வை','வொ','வோ','வௌ','ழ','ழா','ழி','ழீ','ழு','ழூ','ழெ','ழே','ழை','ழொ','ழோ','ழௌ','ள','ளா','ளி','ளீ','ளு','ளூ','ளெ','ளே','ளை','ளொ','ளோ','ளௌ','ற','றா','றி','றீ','று','றூ','றெ','றே','றை','றொ','றோ','றௌ','ன','னா','னி','னீ','னு','னூ','னெ','னே','னை','னொ','னோ','னௌ']
len(uyirmey)


# In[30]:

len(kural_list[0])


# In[31]:

tamil.utf8.get_letters(kural_list[0])


# In[32]:

tamil.utf8.get_letters(kural_list[0][1])[0] == mey[0]


# In[33]:

uyir_count = []
for u in range(len(uyir)) :
    count = 0
    for k in range(len(kural_list)) :
        for l in range(len(kural_list[k])) :
            if tamil.utf8.get_letters(kural_list[k][l])[0] == uyir[u] :
                count = count + 1
    uyir_count.append([uyir[u],count])
print(uyir_count)


# In[34]:

mey_count = []
for m in range(len(mey)):
    all_count = 0
    for k in range(len(kural_list)):
        this_count = kural_list[k].count(mey[m],0,len(kural_list[k])-1)
        all_count = all_count + this_count
    mey_count.append([mey[m],all_count])
print(mey_count)


# In[35]:

umey = np.reshape(np.array(uyirmey),(18,-1))


# In[36]:

umey


# In[37]:

len(umey) 


# In[38]:

np.shape(umey)


# In[39]:

umey_count = []
umey_count_all = []
for m in range(0,18):
    for n in range(0,12):
        all_count=0
        for k in range(0,1330):
            this_count = kural_list[k].count(umey[m][n],0,len(kural_list[k])-1)
            if n == 0:
                x_count = 0
                for x in range(1,12):
                    count = kural_list[k].count(umey[m][x],0,len(kural_list[k])-1)
                    x_count = x_count + count
                this_count = this_count - x_count
                y_count = kural_list[k].count(mey[m],0,len(kural_list[k])-1)
                this_count = this_count - y_count
            umey_count.append([n+1,m+1,uyir[n],mey[m],umey[m][n],this_count])
            all_count = all_count + this_count
        umey_count_all.append([n+1,m+1,uyir[n],mey[m],umey[m][n],all_count])


# In[40]:

len(umey_count_all)


# In[41]:

umey_count_all[0:5]


# In[42]:

pd_umey_count_all = pd.DataFrame(umey_count_all)


# In[43]:

pd_umey_count_all.columns = ['u_num','m_num','uyir','mey','uyirmey','count']
pd_umey_count_all.head()


# In[44]:

y = np.array(uyir_count)[:,1].astype(np.float)/10
y


# In[45]:

import plotly as py
import plotly.graph_objs as go
py.offline.init_notebook_mode()

trace0 = go.Scatter(
    x= list(np.array(uyir_count)[:,0]),
    y= list(np.array(uyir_count)[:,1]),
    text = list(np.array(uyir_count)[:,0]),
    mode='markers',
    marker=dict(
        size= list(np.array(uyir_count)[:,1].astype(np.float)/10),
        color = list(np.array(uyir_count)[:,1])
    )
)

data = [trace0]
py.offline.iplot(data, filename='bubblechart-size')


# In[46]:

import plotly as py
import plotly.graph_objs as go
py.offline.init_notebook_mode()

trace0 = go.Scatter(
    x= list(np.array(mey_count)[:,0]),
    y= list(np.array(mey_count)[:,1]),
    text = list(np.array(mey_count)[:,0]),
    mode='markers',
    marker=dict(
        size= list(np.array(mey_count)[:,1].astype(np.float)/10),
        color = list(np.array(mey_count)[:,1])
        )
)

data = [trace0]
py.offline.iplot(data, filename='bubblechart-size')


# In[47]:

import plotly as py
from plotly.graph_objs import *
py.offline.init_notebook_mode()

import pandas as pd

# Get Data: this ex will only use part of it (i.e. rows 750-1500)


trace1 = Scatter3d(
    x= pd_umey_count_all['uyir'],
    y= pd_umey_count_all['mey'],
    z= pd_umey_count_all['count'],
    
    text=pd_umey_count_all['uyirmey'],
    mode='markers',
    marker=dict(
        sizemode='diameter',
        sizeref=7,
        size=pd_umey_count_all['count'],
        color = pd_umey_count_all['count'],
        colorscale = 'Viridis',
        colorbar = dict(title = 'Uyirmey Count <br> by Kural'),
        opacity = 0.5   
    )
)

data=[trace1]
layout=dict(height=800, width=800, title="Scatter plot of 'uyirmey' character count by each Thirukkural")
fig=dict(data=data, layout=layout)
py.offline.iplot(fig, filename='3DBubble')


# In[ ]:



