Clustering Analysis – Music Recommendation System

This project uses K-Means clustering to group songs based on audio features and identify different listening patterns within Drake-related music.

Overview

Instead of grouping songs by artist or genre, this project analyzes audio characteristics such as energy, danceability, tempo, valence, acousticness, and speechiness to uncover distinct music styles.

Key Insight

The model identified four main clusters of Drake-related songs:

High-energy rap tracks (higher energy and speechiness)
Melodic / R&B songs (higher acousticness, lower energy)
Mainstream balanced tracks (moderate values across features)
Outlier or mixed-style songs (less consistent feature patterns)

This demonstrates how clustering can be used in recommendation systems to group songs by vibe rather than just artist.

Methods Used

Data preprocessing with pandas
Feature scaling using StandardScaler
Elbow method to evaluate cluster sizes (k = 1–10)
Final model selection: k = 4 (based on interpretability and elbow trend)
K-Means clustering using scikit-learn

Dataset

A filtered dataset of Drake-related songs is included (data_sample.csv) due to file size limitations. The dataset contains audio features used for clustering.

Files

clustering_analysis.py → main analysis code
data_sample.csv → dataset used for clustering

Why This Matters

This type of analysis is commonly used in music recommendation systems (e.g., Spotify, Apple Music) to improve personalization by grouping content based on listening patterns rather than metadata alone.
