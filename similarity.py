from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

with open('original', 'r', encoding='utf-8') as file:
	original = file.read()

with open('perfect', 'r', encoding='utf-8') as file:
	perfect = file.read()

with open('bad', 'r', encoding='utf-8') as file:
	bad = file.read()

texts = [original, perfect, bad]
embeddings = model.encode(texts)

# Ähnlichkeitsmatrix
similarity_matrix = cosine_similarity(embeddings)

print(similarity_matrix)