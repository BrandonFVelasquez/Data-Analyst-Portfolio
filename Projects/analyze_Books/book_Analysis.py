import pandas as pd

df = pd.read_csv('bestsellers_with_categories.csv')

# Get the first 5 rows of the DataFrame
print(df.head())

# Get the last 5 rows of the DataFrame
print(df.tail())

# Get the colulmn name
print(df.columns)

# Get a summary of the DataFrame
print(df.describe())

df.drop_duplicates(inplace=True)

df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"},inplace=True)

df["Price"] = df["Price"].astype(float)

author_counts = df["Author"].value_counts()
print(author_counts)

avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()
print(avg_rating_by_genre)

# Export top selling authors to a CSV file
author_counts.head(10).to_csv("top_10_authors.csv", index=True)

# Export average rating by genre to a CSV file
avg_rating_by_genre.to_csv("avg_rating_by_genre.csv", index=True)

