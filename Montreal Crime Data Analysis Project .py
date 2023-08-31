#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[13]:


data = pd.read_csv(r"C:\Users\Admin\Desktop\Alex\mtl-crime-data.csv")


# In[16]:


data.head()


# In[17]:


data.info()


# In[18]:


data.columns


# In[19]:


#Removing unwanted columns
data = data.drop('Unnamed: 0', axis=1)


# In[20]:


data.columns


# In[21]:


data.info()


# In[22]:


# Converting datatypes to required format
data['date'] = pd.to_datetime(data['date'])


# In[23]:


pd.DataFrame(data.dtypes, columns=['Datatype']).rename_axis('Columns')


# In[24]:


pd.DataFrame(data.isnull().sum(), columns=['Missing Values']).rename_axis('Feature')


# In[25]:


#Data Analysis,Visualization-neighbourhoods have the highest number of reported crimes
top_neighbourhood = pd.DataFrame(data['neighbourhood'].value_counts()).rename({"neighbourhood":"Case Reported"}, axis = 1).rename_axis("Neighbourhood").head(10)

top_neighbourhood.style.bar()


# In[26]:


top_neighbourhood = top_neighbourhood.sort_values(by='Case Reported', ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(data=top_neighbourhood, x=top_neighbourhood.index, y='Case Reported', palette='viridis')

plt.xlabel('Neighbourhood')
plt.ylabel('Cases Reported')
plt.title('Top 10 Neighbourhoods where most crimes are reported')

# Rotating x-axis labels for better visibility
plt.xticks(rotation=45, ha='right')

# Display the plot
plt.tight_layout()
plt.show()


# In[27]:


#What are the most frequent crimes by neighbourhood
top_neighbourhoods = data['neighbourhood'].value_counts().head(10).index

# Filter the data to include only the top 10 neighbourhoods
data_top_neighbourhoods = data[data['neighbourhood'].isin(top_neighbourhoods)]

# Get the order of neighborhoods by crime count in descending order
neighbourhood_order = data_top_neighbourhoods.groupby('neighbourhood')['category'].count().sort_values(ascending=False).index

# Create a count plot using Seaborn
plt.figure(figsize=(10, 6))
sns.countplot(data=data_top_neighbourhoods, x='neighbourhood', hue='category', palette='viridis', order=neighbourhood_order)

# Adding labels and title
plt.xlabel('Neighbourhood')
plt.ylabel('Count')
plt.title('Distribution of Crime for Top 10 Neighbourhoods')

# Slightly rotate the x-axis labels for readability
plt.xticks(rotation=45, ha='right')

# Display the plot
plt.tight_layout()
plt.show()


# In[28]:


#Number of reported crimes committed annualy in Montreal
pd.DataFrame(data['year'].value_counts()).rename({"year":"Case Reported"}, axis = 1).rename_axis("Year")


# In[29]:


#What are the trends in the categories of reported crimes?
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='year', hue='category', palette='viridis')

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Count')
plt.title('Distribution of Crime over Years')

# Display the plot
plt.tight_layout()
plt.show()


# In[30]:


#Did crime rates increase or decrease
year_wise_trend = data.groupby('year').sum(numeric_only=True).drop(['longitude', 'latitude'], axis=1).rename({'count': 'Case Reported'}, axis=1)

# Create a line plot using Seaborn
plt.figure(figsize=(10, 6))
sns.lineplot(data=year_wise_trend, x=year_wise_trend.index, y='Case Reported')

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Cases Reported')
plt.title('Trend of Crime from 2015 to 2021')

# Display the plot
plt.tight_layout()
plt.show()


# In[31]:


data['Month'] = data['date'].apply(lambda time: time.month)
data['Day of Week'] = data['date'].apply(lambda time: time.dayofweek)


# In[32]:


dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
data['Day of Week'] = data['Day of Week'].map(dmap)


# In[33]:


sns.countplot(x='Day of Week',data=data,hue='category',palette='viridis')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


# In[34]:


sns.countplot(x='Month', data=data, hue='category', palette='viridis')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


# In[35]:


data.head()


# In[36]:


#correlation between days/months

dayMonth = data.groupby(by=['Day of Week', 'Month']).count()['category'].unstack()
dayMonth.head()


# In[37]:


plt.figure(figsize=(12,6))
sns.heatmap(dayMonth,cmap='coolwarm')


# In[38]:


#Neighbourhoods with highest number of reported crimes:
#Plateau
#Centre-Sud
#Downtown
#Mondays have the highest number of reported crimes, followed by Tuesday and Wednesday
#August is the month with most number of reported crimes, followed by July and June
#Home invasions are the most reported crime, followed by theft in/from a motor vehicle and mischief
#2015 had the highest crime rate (24,222 cases), and 2021 the lowest (10,547 cases.
#Overall, crime reports decreased every year from 2015 to 2021


# In[ ]:




