from sentence_transformers import SentenceTransformer
import json
import numpy as np

with open("./Data/chunks.json","r") as file:
    chunks = json.load(file)

# print(len(chunks))

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(chunks)

# print(len(embeddings))
# print(embeddings.shape)

np.save("Data/embeddings.npy",embeddings)
