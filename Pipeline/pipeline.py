#!/usr/bin/env python

# попробуем считать данные из db в mongodb
from pymongo import MongoClient
import pprint
import pandas as pd

def print_one_random():
    #печать рандомной записи для проверки подключения к БД
    #print.pprint(collection.find_one())


if __name__ == '__main__':
    db = MongoClient("mongodb://localhost:27017/", uuidRepresentation="standard").arxiv
    collection = db.articles

# подсчёт документов в коллекции для проверки подключения к БД
#collection.count_documents({})

    cats = [
        "astro-ph.IM",
        "astro-ph.CO",
        "astro-ph.EP",
        "astro-ph.GA",
        "astro-ph.HE",
        "astro-ph.SR",
    ]
    cursor = collection.find({"primary_category": {"$in": cats}})

    #считываем записи из каждой категории в dataframe
    m_df = pd.DataFrame(list(cursor))
    m_df.drop(columns=['_id'], inplace=True, errors='ignore')

# подсчёт документов в dataframe
#m_df.count()


    # aggregate count per category
    pipeline = [
        {"$group": {"_id": "$primary_category", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}  # optional: sort descending
    ]

    counts = list(collection.aggregate(pipeline))

    for record in counts:
        print(record["_id"], record["count"])



# choose your category
category = "q-bio.GN"

# find all records in that category
cursor = collection.find({"primary_category": category})

# print first few results nicely
for doc in cursor.limit(5):
    pprint.pprint(doc)


# In[44]:


# target number per category
N = 150

sampled_docs = []
for cat in cats:
    pipeline = [
        {"$match": {"primary_category": cat}},
        {"$sample": {"size": N}}  # random sample of N docs
    ]
    sampled_docs.extend(list(collection.aggregate(pipeline)))

df_test = pd.DataFrame(sampled_docs)
df_test.drop(columns=['_id'], inplace=True, errors='ignore')

print(df_test["primary_category"].value_counts())
print(df_test.shape)


# In[45]:


df_test.head(10)


# In[46]:


df_test_shuffled = df_test.sample(frac=1).reset_index(drop=True)
df_test_shuffled.head(15)


# In[47]:


df_test_shuffled.to_csv("../Data_samples/raw_random_astro_sample150.csv", index=False)


# In[ ]:




