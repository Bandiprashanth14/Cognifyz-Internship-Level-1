#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import packages

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


# Read the data

file_path='C:\\Users\\gouthami\\Downloads\\Cognify Dataset.csv'
df=pd.read_csv(file_path)
df


# In[3]:


# starting 5 rows
df.head()


# In[4]:


# last 5 rows
df.tail()


# **Rows and columns**

# In[5]:


df.size


# In[6]:


df.shape


# **Missing value**

# In[7]:


df.isnull()


# In[8]:


# Missing value in each column
df.isnull().sum()


# In[9]:


# seperate categorical column and  numerical column

cat=df.select_dtypes(include=['object']).columns
num=df.select_dtypes(exclude=['object']).columns
print('cat:',cat)
print('num:',num)


# In[10]:


# fill the missing value with mode because it is categorical column

df['Cuisines']=df['Cuisines'].fillna(df['Cuisines'].mode()[0])


# In[11]:


# again check any missing are available or not

df.isnull().sum()


# **LEVEL :- 1**

# **Task:-1**

# - Determine the top three most common cuisines in Dataset.

# In[12]:


# find value count of cuisines column

a =df['Cuisines'].value_counts()
a


# In[13]:


a.head(10)


# In[14]:


count_cuisines=a


# In[15]:


# find top three most common cuisines in datset with their value count

top_three=count_cuisines.head(3)
top_three


# In[16]:


# top three cuisines

print("The top three Cuisines:")
for i in range(len(top_three.index)):
    print(top_three.index[i])


# In[17]:


# plot bar graph of the top three cuisines

plt.figure(figsize=(5,5))
color=['blue','green','red']
top_three.plot(kind='bar',color=color)
plt.title('Top three most visited Cuisines')
plt.xlabel('Cuisines')
plt.ylabel('Number of Restaurants')
plt.show()


# **Calculate the percentage of restaurants that serve each of the top cuisines**

# In[18]:


# length of the datset
tot_res=len(df)
tot_res


# In[19]:


per= (top_three.values/tot_res)*100


# In[20]:


data=dict(zip(top_three.index,per))
data


# In[21]:


# create the dataframe with their percentage
a=pd.DataFrame(data.items(),columns = ['cuisine','percentage'])
a


# In[22]:


# pie chart plot
plt.title('Percentage of restaurantrants that serve each of the top cuisines.')
plt.pie(a['percentage'],labels=a['cuisine'],autopct='%0.2f%%',explode=[0.05,0.05,0.05],startangle=90)
plt.show()


# **Task :- 2**

# - identify the city with the highest number of restaurants in the dataset.

# In[23]:


df.head()


# In[24]:


# restaurants with their value_counts
df['City'].value_counts()


# In[25]:


# highest number of restaurant in the dataset
city=df['City'].value_counts()
city.index[0]


# - Calculate the average rating for Restaurant in each city.

# In[26]:


mean=df['Aggregate rating'].mean()
mean


# In[27]:


average_ratings = df.groupby(['City','Restaurant Name'])['Aggregate rating'].mean().reset_index()
average_ratings


# In[28]:


average_ratings = df.groupby('City')['Aggregate rating'].mean().reset_index()
average_ratings


# - Determine the city with the highest average rating.

# In[29]:


average_ratings= df.groupby('City')['Aggregate rating'].mean().reset_index()
average_ratings_city=average_ratings.sort_values(by='Aggregate rating',ascending=False)
average_ratings_city


# In[30]:


# city with highest average rating
average_ratings_city.iloc[0,0]


# **Task :- 3**

# - Create a histogram or bar chart to visualize the distribution of price ranges among the restaurants.

# In[31]:


df['Price range'].value_counts(i)


# In[32]:


# plot the bar chart to visualize of price range among the restaurant
price_counts = df['Price range'].value_counts()
plt.bar(['1','2','3','4'], list(price_counts.values), color=['blue', 'orange', 'green','purple'])
plt.xlabel('Price Range')
plt.ylabel('Number of Restaurants')
plt.title('Distribution of Price Ranges Among Restaurants')
plt.show()


# - Calculate the percentage of restaurantsin each price range category.

# In[33]:


total=len(df)
total


# In[35]:


count=df['Price range'].value_counts().values
count


# In[36]:


percentage=round(df['Price range'].value_counts()/total*100,2)
percentage


# In[38]:


df1=pd.DataFrame({'Price range':df['Price range'].value_counts().index,
                 'Count':count,
                 'Percentage':percentage})
df1


# **Task :- 4**

# - Determine the percentage of restaurants that offer online delivery.

# In[39]:


# online delivery yes

df[df['Has Online delivery']=='Yes']['Restaurant Name'].value_counts()


# In[40]:


leng=len(df[df['Has Online delivery']=='Yes'])
leng


# In[42]:


round(df[df['Has Online delivery']=='Yes']['Restaurant Name'].value_counts()/leng*100,2)


# In[43]:


total=len(df)
total


# In[44]:


# percentage of online order taken by the restaurant
percentage=(leng/total)*100
percentage


# - Compare the average ratings of restaurants with and without online delivery.

# In[45]:


online_data=df[df['Has Online delivery']=='Yes']
offline_data=df[df['Has Online delivery']=='No']


# In[46]:


average_ratings= online_data.groupby('Restaurant Name')['Aggregate rating'].mean().reset_index()
average_ratings


# In[47]:


# average rating of restaurant with and without online delivery
df.groupby('Has Online delivery')['Aggregate rating'].mean().round(2).reset_index()


# In[ ]:




