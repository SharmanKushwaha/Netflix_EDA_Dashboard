# 🎬 Netflix EDA & Dashboard

## 📖 Overview
Exploratory Data Analysis and Interactive Dashboard on Netflix's content library. This project cleans, analyzes, and visualizes Netflix's movie and TV show catalog to uncover key trends.

## 📊 Dataset
- 8,770 titles (after cleaning)
- 11 columns
- Source: Kaggle

## 📈 Key Insights
1. **Movies vs TV Shows:** Movies dominate the platform (~70%).
2. **Top Country:** United States produces the most content.
3. **Top Genre:** Documentaries are the most common genre.
4. **Content Growth:** Netflix added the most content in 2020.
5. **Most Common Rating:** TV-MA (Mature audiences) is the most frequent rating.
6. **Average Duration:** Movies average ~90 minutes; TV Shows average ~2 seasons.
7. **Top Director:** Raúl Campos has the most titles.
8. **Peak Year:** 2020 had the most content added.

## 📊 Visualizations
- **Static Charts (Matplotlib / Seaborn):**
  - Content Growth Over Years (Line Chart)
  - Top 10 Genres (Bar Chart)
  - Most Common Ratings (Countplot)
  - Heatmap of Content Added by Year and Type
- **Interactive Charts (Plotly):**
  - Top 10 Countries (Bar Chart)
  - Movies vs TV Shows (Pie Chart)
  - Content Growth Over Years (Line Chart)

> All charts are saved in the `Visualization/` folder. Open the `.html` files in your browser to explore interactive plots.

## 🛠️ Tech Stack
- Python 3.8+
- Pandas
- Matplotlib / Seaborn
- Plotly

## 🚀 How to Run
```bash
git clone https://github.com/SharmanKushwaha/Netflix_EDA_Dashboard.git
cd Netflix_EDA_Dashboard
pip install -r requirements.txt
python main.py