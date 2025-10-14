import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score

# Load and preprocess data
df = pd.read_csv('housing.csv')
X = StandardScaler().fit_transform(df.select_dtypes(include=['float64', 'int64']))

# KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10).fit(X)
k_labels = kmeans.fit_predict(X)
k_score = silhouette_score(X, k_labels)

# EM clustering (Gaussian Mixture)
gmm = GaussianMixture(n_components=3, random_state=42)
g_labels = gmm.fit_predict(X)
g_score = silhouette_score(X, g_labels)

# Print comparison
print(f"Silhouette Score - KMeans: {k_score:.3f}")
print(f"Silhouette Score - EM (GMM): {g_score:.3f}")

if k_score > g_score:
    print("KMeans produced better-defined clusters.")
elif g_score > k_score:
    print("EM (GMM) produced better-defined clusters.")
else:
    print("Both methods produced similar clustering quality.")
