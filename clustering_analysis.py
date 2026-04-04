import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

df = pd.read_csv("data.csv")

features = [
    "danceability",
    "energy",
    "loudness",
    "tempo",
    "valence",
    "acousticness",
    "speechiness"
]

df = df.dropna(subset=features)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[features])

inertia = []
k_values = range(1, 11)

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(k_values, inertia, marker='o')
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Inertia")
plt.title("Elbow Method for Choosing k")
plt.show()

k = 4

kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
df["cluster"] = kmeans.fit_predict(X_scaled)
df = df[df["artists"].str.contains("Drake", case=False, na=False)]

for cluster_num in sorted(df["cluster"].unique()):
    print(f"\nCluster {cluster_num}")
    print(df[df["cluster"] == cluster_num][["name", "artists"]].head(10))


cluster_summary = df.groupby("cluster")[[
    "danceability",
    "energy",
    "loudness",
    "tempo",
    "valence",
    "acousticness",
    "speechiness"
]].mean()

print(cluster_summary)