# INST-414-Module-4-Assignment
# Music Clustering Analysis (Drake-Based)

This project uses K-Means clustering to group songs based on audio features and identify different listening patterns within Drake-related music.

## Overview
Instead of grouping songs by artist or genre, this project analyzes audio characteristics such as energy, danceability, tempo, and speechiness to uncover distinct music styles.

## Key Insight
The model successfully identified different types of Drake songs, including:
- High-energy rap tracks
- Melodic / R&B songs
- Mainstream hits
- Outlier or mixed-style tracks

This demonstrates how clustering can be used in recommendation systems to group songs by “vibe” rather than just artist.

## Methods Used
- Data preprocessing with pandas  
- Feature scaling using StandardScaler  
- Elbow method to determine optimal number of clusters (k = 4)  
- K-Means clustering using scikit-learn  

## Dataset
A filtered dataset of Drake-related songs is included (`data_sample.csv`) due to file size limitations.

## Files
- `clustering_analysis.py` → main analysis code  
- `data_sample.csv` → dataset used for clustering  

## Why This Matters
This type of analysis is commonly used in music recommendation systems (like Spotify or Apple Music) to improve personalization and user experience.
