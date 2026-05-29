# import pandas as pd

# df = pd.read_csv("netflix_titles.csv")

# print(df.head())

import pandas as pd
df =  pd.read_csv("netflix_titles.csv")
print(df.head())

print(df.info())
print(df.isnull().sum())


df["director"]=df["director"].fillna("Unknown")
df["country"]=df["country"].fillna("Unknown")
df["cast"]=df["cast"].fillna("Unknown")

df=df.drop_duplicates()

df['date_added'] = pd.to_datetime(
    df['date_added'].str.strip(),
    format='mixed'
)

print(df.columns)



print(df["type"].value_counts())


import matplotlib.pyplot as plt

df["type"].value_counts().plot(kind='bar')
plt.title ("Movies vs TV Shows")
plt.show()

top_country = df['country'].value_counts().head(10)

print(top_country)

top_country.plot (kind='bar')

plt.title("Top 10 Countries")
plt.show()

print(df['rating'].value_counts())

print(df["listed_in"].value_counts().head(10))


df ["release_year"].value_counts().head(10)

df["release_year"].value_counts().sort_index().plot()

plt.title("Release Year Trend")

plt.show()


df.to_csv("cleaned_netflix.csv", index=False)


import matplotlib.pyplot as plt

top_rating = df['rating'].value_counts().head(5)

top_rating.plot(kind='bar')

plt.title("Top 5 Netflix Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")

plt.show()


