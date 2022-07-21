#!/usr/bin/env python
# coding: utf-8

# In[6]:


import requests
from bs4 import BeautifulSoup
 
page = requests.get('https://www.imdb.com/chart/top/') # mendapatkan link web
soup = BeautifulSoup(page.content, 'html.parser') # Parsing konten menggunakan beautifulsoup
 
links = soup.select("table tbody tr td.titleColumn a") #select semua kontent pada tag ini
year = soup.select("table tbody tr td.titleColumn span.secondaryInfo") #select semua content pada tag ini
linkresult = links #judul film
yearresult = year #tahun film

#mendapatkan judul film
for anchor in linkresult:
    textresult=anchor.text


# In[24]:


#mendapatkan tahun film
tahun=[]
for y in yearresult:
    x=y.text
    tahun.append(x)


# In[20]:


#membuat judul film ke sebuah list
hasil = []
for a in yearresult :
    info = []
    for x in linkresult:
        info.append(x.get_text())
    hasil.append(info)


# In[21]:


import pandas as pd


# In[25]:


#membuat df untuk hasil
film_dict = {'nama':info, 'tahun':tahun}
df = pd.DataFrame(film_dict, columns = ['nama', 'tahun'])
df


# In[26]:


#menyimpan df ke csv
df.to_csv("FilmScrappingResult.csv", sep = ',')


# In[ ]:




