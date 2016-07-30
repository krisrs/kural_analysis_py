
# coding: utf-8

# In[3]:

#import required packages
import numpy as np
import pandas as pd
import nltk
import tamil
import matplotlib.pyplot as plt


# In[4]:

# read the file from my git repo
pd_kural = pd.read_csv('https://raw.githubusercontent.com/krisrs/kural_analysis_py/master/kural_dat_utf8.txt',index_col=0,sep=',',header='infer')


# In[5]:

# creating a list from the pandas dataframe to play around a bit
kural_list = list(pd_kural["kural"])


# In[6]:

# Had earlier created uni/bi/trigrams in R using tm package. Though not the main goal here, 
# just touched a bit using nltk package for python
ng_test = nltk.ngrams(kural_list[0].split(" "),2)
for grams in ng_test : print(grams)


# In[7]:

# Had earlier created uni/bi/trigrams in R using tm package. Though not the main goal here, 
# just touched a bit using nltk package for python
tri_array = []
for i in range(0,3) : 
    ng = nltk.ngrams(kural_list[i].split(" "),3)
    for grams in ng : 
        tri_array.append(grams)
print(tri_array)


# In[8]:

# building a vocabulary of all words in the Thirukkural to get the frequent words
kural_vocab = []
for i in range(len(kural_list)) :
    k = kural_list[i].split()
    kural_vocab.extend(k)


# In[9]:

# just tried creating unigram directly in python without using nltk package
wc=[]
for i in range(len(kural_vocab)) :
    c=0
    for j in range(len(kural_list)) :
        c = c + kural_list[j].count(kural_vocab[i])
    wc.append([kural_vocab[i],c])


# In[10]:

# count of vocab - its common knowledge for Tamil folk that each of the 1330 couplets in Thirukkural is approx 7 words each.
# Just a sniff test to check that consistency.. almost there, though not exact - ok for the high level analysis
len(wc)


# In[11]:

# Had put in the unigram words and counts into a dataframe to weed out some of the stems and split words - 
# In the next few steps, you would see me doing this manually a bit since the stopwords relevant for this is not known as yet
pd_unicount = pd.DataFrame(data=wc)


# In[12]:

pd_unicount.head()
pd_unicount.columns = ["word","count"]
pd_unicount = pd_unicount.drop_duplicates()
pd_unicount.head()


# In[13]:

pd_unicount.describe()


# In[14]:

pd_unicount.query('count==1912')


# In[15]:

pd_unicount = pd_unicount[pd_unicount.word != "ம்"]
pd_unicount.describe()


# In[16]:

pd_unicount.query('count==1717')


# In[17]:

pd_unicount = pd_unicount[pd_unicount.word != "ட"]
pd_unicount.describe()


# In[18]:

pd_unicount.query('count==1314')



# In[19]:

pd_unicount = pd_unicount[pd_unicount.word != "ர்"]
pd_unicount.describe()


# In[20]:

pd_unicount.query('count==736')


# In[21]:

pd_unicount = pd_unicount[pd_unicount.word != "கு"]
pd_unicount.describe()


# In[22]:

pd_unicount.query('count==331')


# In[23]:

pd_unicount = pd_unicount[pd_unicount.word != "க்கு"]
pd_unicount.describe()


# In[24]:

pd_unicount.query('count==233')


# In[25]:

pd_unisort=pd_unicount.sort_values(by='count',ascending=0)
pd_unisort.head()


# In[26]:

# wanted to get a visual feel for a few of the high frequency words 
test = pd_unisort.query('count>10 and count <=500')


# In[27]:

test_x=list(test["word"])
test_y=list(test["count"])
test_s=list(test["count"])


# In[28]:

# Simple 2D Bubble plot in Plotly to get a feel for high frequency words in the above range. 
# That plot look like a Tornado!!

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


# In[29]:

# back to the core - getting the Tamil letter equivalents of vowels & consontants into a list to count their occurrence 
# Vowel equivalent in Tamil is called 'uyir' - which literally means 'life'
uyir = ['அ','ஆ','இ','ஈ','உ','ஊ','எ','ஏ','ஐ','ஒ','ஓ','ஔ']
len(uyir)


# In[30]:

# Consonant equivalent in Tamil is called 'mey' - which literally means 'body'
mey = ['க்','ங்','ச்','ஞ்','ட்','ண்','த்','ந்','ப்','ம்','ய்','ர்','ல்','வ்','ழ்','ள்','ற்','ன்']
len(mey)


# In[31]:

# unlike in English where vowels and consonants make up the full character set for the language, Tamil has 
# uyir-mey a 12 x 18 matrix combination of uyir and mey that lend a rich 'body full of life' character set for the language
# There's also a singleton letter in the Tamil language - we'll leave him alone (pun!) for now
# so, in all uyir (12), mey (18), and uyirmey(216) and the singleton (aydham - 1) form the native Tamil character set. 
# Later day works have a few more due to the influence of sanskrit - none of that is in this core Tamil work. We'll ignore those 
uyirmey = ['க','கா','கி','கீ','கு','கூ','கெ','கே','கை','கொ','கோ','கௌ','ங','ஙா','ஙி','ஙீ','ஙு','ஙூ','ஙெ','ஙே','ஙை','ஙொ','ஙோ','ஙௌ','ச','சா','சி','சீ','சு','சூ','செ','சே','சை','சொ','சோ','சௌ','ஞ','ஞா','ஞி','ஞீ','ஞு','ஞூ','ஞெ','ஞே','ஞை','ஞொ','ஞோ','ஞௌ','ட','டா','டி','டீ','டு','டூ','டெ','டே','டை','டொ','டோ','டௌ','ண','ணா','ணி','ணீ','ணு','ணூ','ணெ','ணே','ணை','ணொ','ணோ','ணௌ','த','தா','தி','தீ','து','தூ','தெ','தே','தை','தொ','தோ','தௌ','ந','நா','நி','நீ','நு','நூ','நெ','நே','நை','நொ','நோ','நௌ','ப','பா','பி','பீ','பு','பூ','பெ','பே','பை','பொ','போ','பௌ','ம','மா','மி','மீ','மு','மூ','மெ','மே','மை','மொ','மோ','மௌ','ய','யா','யி','யீ','யு','யூ','யெ','யே','யை','யொ','யோ','யௌ','ர','ரா','ரி','ரீ','ரு','ரூ','ரெ','ரே','ரை','ரொ','ரோ','ரௌ','ல','லா','லி','லீ','லு','லூ','லெ','லே','லை','லொ','லோ','லௌ','வ','வா','வி','வீ','வு','வூ','வெ','வே','வை','வொ','வோ','வௌ','ழ','ழா','ழி','ழீ','ழு','ழூ','ழெ','ழே','ழை','ழொ','ழோ','ழௌ','ள','ளா','ளி','ளீ','ளு','ளூ','ளெ','ளே','ளை','ளொ','ளோ','ளௌ','ற','றா','றி','றீ','று','றூ','றெ','றே','றை','றொ','றோ','றௌ','ன','னா','னி','னீ','னு','னூ','னெ','னே','னை','னொ','னோ','னௌ']
len(uyirmey)


# In[32]:

aydham = ['ஃ']


# In[33]:

# printed out the first couplet in the list to start counting the letters
kural_list[0]


# In[34]:

# counting characters in the first kural - quick visual check shows simple counts uyirmey characters twice,
# once for their uyir form and again for the mey form
len(kural_list[0])


# In[35]:

# this is worked around by using the open-tamil package which has get_letters function that gets the exact letters
len(tamil.utf8.get_letters(kural_list[0]))


# In[36]:

tamil.utf8.get_letters(kural_list[0][1])[0] == mey[0]


# In[37]:

# counting the frequency of occurrence of uyir letters in all 1330 couplets in Thirukkural. 
# Interesting to note the last vowel 'ஔ' is not used at all
uyir_count = []
for u in range(len(uyir)) :
    count = 0
    for k in range(len(kural_list)) :
        for l in range(len(kural_list[k])) :
            if tamil.utf8.get_letters(kural_list[k][l])[0] == uyir[u] :
                count = count + 1
    uyir_count.append([uyir[u],count])
print(uyir_count)


# In[38]:

# counting the frequency of occurrence of mey letters in all 1330 couplets in Thirukkural.
mey_count = []
for m in range(len(mey)):
    all_count = 0
    for k in range(len(kural_list)):
        this_count = kural_list[k].count(mey[m],0,len(kural_list[k])-1)
        all_count = all_count + this_count
    mey_count.append([mey[m],all_count])
print(mey_count)


# In[54]:

# getting the count of the singleton 'ஃ'
ay_count = 0
for k in range(len(kural_list)):
    count = kural_list[k].count(aydham[0],0,len(kural_list[k])-1)
    ay_count = ay_count + count
ay_count


# In[55]:

# converting the list of uyirmey letters into a 18 x 12 array 
umey = np.reshape(np.array(uyirmey),(18,-1))


# In[41]:

umey


# In[42]:

len(umey) 


# In[43]:

np.shape(umey)


# In[44]:

# while the get_letters function of the open tamil function worked for the mey and uyir separately, it didnt work for uyirmey. 
# It was treating all 12 combinations of a mey letter with uyir as the same, and hence count of all 
# for e.g. the 12 combinations க,கா,கி,கீ,கு,கூ,கெ,கே,கை,கொ,கோ,கௌ as well as the mey form 'க்' 
# were all treated as க (the first in each of 18 rows) and all their counts were shown against க and those individual letters had a count of 0
# after a bit of working around, found the basic count method on the string variable avoided this problem with some adjustments

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


# In[45]:

# got the counts for all 216 uyirmey letters - did some sample validations to ensure the double counting problem went away
len(umey_count_all)


# In[46]:

umey_count_all[0:5]


# In[47]:

# got them into a pandas df to use for plotting
pd_umey_count_all = pd.DataFrame(umey_count_all)


# In[48]:

pd_umey_count_all.columns = ['u_num','m_num','uyir','mey','uyirmey','count']
pd_umey_count_all.head()


# In[49]:

y = np.array(uyir_count)[:,1].astype(np.float)/10
y


# In[50]:

# 2d bubble plot of occurrence of the 12 uyir letters bubbles sized & colored by the count of occurrences. 
# see notes below the plot for some key observations

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
layout = dict(       title = "Bubble chart of frequency of occurrence of Tamil letters of type uyir(vowel equivalent) in ancient work Thirukkural"
)
data = [trace0]
fig = dict(data=data,layout=layout)
py.offline.iplot(fig, filename='bubblechart-size')


# In[ ]:

# observations on above plot
# shows a nice pattern the 'a' (and 'e') sounding forms of uyir letters occur more than the 'aa' (and 'ee') forms 
# declining pattern as we go from the first to the last of the uyir letters (after the point above is factored in)
# the last of the uyir letters ஔ is not used at all (surprising as the singleton 'ஃ' is used quite a bit)


# In[51]:

# 2d bubble plot of occurrence of the 18 uyir letters bubbles sized & colored by the count of occurrences.
# see notes below the plot for some key observations
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
        color = list(np.array(mey_count)[:,1]),
         )
)
layout = dict(       title = "Bubble chart of frequency of occurrence of Tamil letters of type 'mey'(consonant equivalent) in ancient work Thirukkural"
)
data = [trace0]
fig = dict(data=data,layout=layout)
py.offline.iplot(fig, filename='bubblechart-size')


# In[ ]:

# Observations on the above plot
# specific mey letters have a really high frequency of occurrence 
# going by knowledge of the work, this is largely due to these letters usually occurring as last letter of many words


# In[52]:

# 3d Bubble plot of occurrence of the 12 x 18 uyirmey letters (combination of uyir & mey) 
# bubbles sized & colored by the count of occurrences on a specific color scale for visual appeal. 
# see notes below the plot for some key observations

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
layout=dict(height=800, width=800, title="3D Bubble plot of count of Tamil letters of type </br>             'uyirmey' (combination of uyir & mey) in the ancient tamil work Thirukkural")
fig=dict(data=data, layout=layout)
py.offline.iplot(fig, filename='3DBubble')


# In[ ]:

# flip the plot on all 3 axes to get a better feel..
# this shows a pattern different from the 2D mey plot 
# General pattern is in keeping with what was observed in uyir letters
# the 'a' (or 'e' or 'u') sounding combinations of meys with the uyirs are more frequent than 'aa' or 'ee' or 'oo' sounding counterparts
# While the 'ai' sounding uyir ஐ was low frequency, combinations of this uyir letter with some specific meys - i.e.
# combinations such as கை, மை and a few others occur frequently - again due to being usual word ending letters.
# as I had suspected, all 12 combinations of meys such as 'ங்' and 'ஞ்' were zeros
# the combination of uyir ஔ with all 18 mey letters were 0 - again something surprising

