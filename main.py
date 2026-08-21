import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly.express as px
import os
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
# print("\n1. Movies and TV show counts.")
# print(df["type"].value_counts())
# # Q2: Which country has the most content?
# # print(df["country"])
# print("\n2. Country with the most content.")
# print(df["country"].value_counts().head(1))
# # Q3: Top 10 genre?
# print("\n3. Top 10 genre.")
# print(df['genre'].explode().value_counts().head(10))
# # Q4: How has content grown over the years?
# print("\n4. Content growth over years.")
# print(df["year_added"].value_counts().sort_index(ascending=True))
# # Q5: What are the most common ratings?
# print("\n5. Most common rating.")
# print(df["rating"].value_counts().head(10))
# # Q6: What is the avg duration of movies vs TV shows?
# print("\n6. Avg duration by type.")
# print(df.groupby("type")["duration_int"].mean())
# # Q7: Who are the top 10 directors?
# print("\n7. Top 10 directors.")
# print(df[df['director'] != 'Unkown']['director'].value_counts().head(10))
# # Q8: Which year had the most content added?
# print("\n8. Year with the most content.")
# print(df['year_added'].value_counts().head(1))
# Visualization 
print("\n--- Visualizations ---")
# Line plot of Content growth over time.
os.makedirs('Visualization', exist_ok=True)
plt.figure(figsize=(10, 6))
content_growth = df["year_added"].value_counts().sort_index()
content_growth.plot(kind='line', marker='o', color='#E50914', linewidth=2, markersize=6)
plt.title('Netflix Content Growth Over Years', fontsize=16, fontweight='bold')
plt.xlabel('Year Added', fontsize=12)
plt.ylabel('Number of Titles Added', fontsize=12)
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('visualization/content_growth.png', dpi=300, bbox_inches='tight')
plt.show()
plt.figure(figsize=(10, 6))
top_genres = df['genre'].explode().value_counts().head(10)
top_genres.plot(kind='bar', color='#E50914', edgecolor='black', linewidth=1)
plt.title('Top 10 Genres on Netflix', fontsize=16, fontweight='bold')
plt.xlabel('Genre', fontsize=12)
plt.ylabel('Number of Titles', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('visualization/top_genres.png', dpi=300, bbox_inches='tight')
plt.show()
print("\n--- Seaborn Visualizations ---")
year_type_counts = df.groupby(['year_added', 'type']).size().unstack(fill_value=0)
plt.figure(figsize=(14, 8))
sns.heatmap(
    year_type_counts,
    annot=True,
    fmt='d',
    cmap='YlOrRd',
    linewidths=0.5,
    cbar_kws={'label': 'Number of Titles'}
)
plt.title('Netflix Content Added by Year and Type', fontsize=16, fontweight='bold')
plt.xlabel('Type', fontsize=12)
plt.ylabel('Year Added', fontsize=12)
plt.tight_layout()
plt.savefig('Visualization/heatmap_year_type.png', dpi=300, bbox_inches='tight')
plt.show()
plt.figure(figsize=(10, 6))
sns.countplot(data=df,
    x='rating',
    order=df['rating'].value_counts().index[:10],
    palette='coolwarm',
    hue='rating',
    legend=False)
plt.title('Top 10 Most Common Ratings on Netflix', fontsize=16, fontweight='bold')
plt.xlabel('Rating', fontsize=12)
plt.ylabel('Number of Titles', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('Visualization/countplot_ratings.png', dpi=300, bbox_inches='tight')
plt.show()