import numpy as np
from scipy.spatial import distance

# Define the vectors
v1 = np.array([40, 120, 60])
v2 = np.array([60, 50, 90])

print(f"Vector 1: {v1}")
print(f"Vector 2: {v2}\n")

# 1. Euclidean Distance
# Formula: sqrt(sum((v1[i] - v2[i])^2))
euclidean_dist = np.linalg.norm(v1 - v2)
# Or using scipy:
# euclidean_dist_scipy = distance.euclidean(v1, v2)
print(f"Euclidean Distance: {euclidean_dist:.4f}")

# 2. Manhattan Distance (L1 Distance)
# Formula: sum(abs(v1[i] - v2[i]))
manhattan_dist = np.sum(np.abs(v1 - v2))
# Or using scipy:
# manhattan_dist_scipy = distance.cityblock(v1, v2) # cityblock is another name for Manhattan
print(f"Manhattan Distance: {manhattan_dist:.4f}")

# 3. Dot Product
# Formula: sum(v1[i] * v2[i])
dot_product = np.dot(v1, v2)
print(f"Dot Product: {dot_product:.4f}")

# 4. Cosine Similarity and Cosine Distance
# Cosine Similarity: (v1 . v2) / (||v1|| * ||v2||)
# Cosine Distance: 1 - Cosine Similarity

cosine_similarity = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
cosine_dist = 1 - cosine_similarity
# Or using scipy for cosine distance directly:
# cosine_dist_scipy = distance.cosine(v1, v2)
print(f"Cosine Similarity: {cosine_similarity:.4f}")
print(f"Cosine Distance: {cosine_dist:.4f}")