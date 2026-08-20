import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly.express as px
print("=" * 60)
print("NETFLIX DATA ANALYSIS")
print("=" * 60)
url = "https://raw.githubusercontent.com/aniketanraje/assignment-dataset/main/netflix_titles.csv"
df = pd.read_csv(url)
print(f"\nDataset loaded successfully!")
print(f"   Rows: {df.shape[0]}")
print(f"   Columns: {df.shape[1]}")
# print("\n--- First 5 rows ---")
# print(df.head())
# print("\n--- Column Info ---")
# print(df.info())
# print("\n--- Missing Values ---")
# print(df.isnull().sum())
# print("\n--- Column Names ---")
# print(df.columns.tolist())
# print(df['director'].isnull().sum())
df["director"] = df["director"].fillna('Unkown')
df[["cast", "country"]] = df[["cast", "country"]].fillna('Unkown')
#print(df["cast"].head())
# print(df["rating"].head(10))
df["rating"] = df['rating'].fillna('Not Rated')
df = df.dropna(subset=['date_added'])
# print(f"   Rows: {df.shape[0]}")
# print(f"   Columns: {df.shape[1]}")
# print(df["date_added"].tail(10))
# print(df["release_year"].head())
df["date_added"] = df["date_added"].str.strip()
df["date_added"] = pd.to_datetime(df["date_added"])
df["year_added"] = df["date_added"].dt.year
# print(df[["date_added", "year_added"]].head())
# print(df.info())
# print(df["duration"].unique().tolist())
df["duration_int"] = df["duration"].str.extract(r'(\d+)').astype(float)
df["duration_unit"]  = df["duration"].str.extract(r'([A-Za-z]+)').astype(str)
# print(df[["duration", "duration_int", "duration_unit"]])
# print(df["listed_in"])
df["genre"] = df["listed_in"].str.split(', ')
# print(df["genre"])
df["show_id"].duplicated().sum()
# print(df.info())
# Dataset fully cleaned!!!
# Q1: How many movies vs TV shows?
print("\n1. Movies and TV show counts.")
print(df["type"].value_counts())
# Q2: Which country has the most content?
# print(df["country"])
print("\n2. Country with the most content.")
print(df["country"].value_counts().head(1))
# Q3: Top 10 genre?
print("\n3. Top 10 genre.")
print(df['genre'].explode().value_counts().head(10))
# Q4: How has content grown over the years?
print("\n4. Content growth over years.")
print(df["year_added"].value_counts().sort_index(ascending=True))
# Q5: What are the most common ratings?
print("\n5. Most common rating.")
print(df["rating"].value_counts().head(10))
# Q6: What is the avg duration of movies vs TV shows?
print("\n6. Avg duration by type.")
print(df.groupby("type")["duration_int"].mean())
# Q7: Who are the top 10 directors?
print("\n7. Top 10 directors.")
print(df[df['director'] != 'Unkown']['director'].value_counts().head(10))
# Q8: Which year had the most content added?
print("\n8. Year with the most content.")
print(df['year_added'].value_counts().head(1))