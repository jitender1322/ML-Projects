import json
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

with open("./Data/chunks.json","r") as file:
    chunks = json.load(file)

embeddings = np.load("./Data/embeddings.npy")

embeddings = embeddings.astype("float32")

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

# print("Total chunks:", len(chunks))
# print("Vectors indexed:", index.ntotal)
# print("Vector dimensions:", dimension)

model = SentenceTransformer("all-MiniLM-L6-v2")

query = input("Enter your query : ")

query_embedding = model.encode([query])
query_embedding = query_embedding.astype("float32")

distances,indices = index.search(query_embedding,k=3)

for i in range(3):
    idx = indices[0][i]
    print(f"Rank {i+1}: {chunks[idx]}")
    print(f"Distance: {distances[0][i]}")