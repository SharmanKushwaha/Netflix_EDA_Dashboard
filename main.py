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
print("\n--- First 5 rows ---")
print(df.head())
print("\n--- Column Info ---")
print(df.info())
print("\n--- Missing Values ---")
print(df.isnull().sum())
print("\n--- Column Names ---")
print(df.columns.tolist())