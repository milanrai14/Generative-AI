from sklearn.metrics.pairwise import cosine_similarity

# Two example vectors
vector_a = [[1, 2, 3]]
vector_b = [[2, 4, 6]]

similarity = cosine_similarity(vector_a, vector_b)

print("Cosine similarity:", similarity[0][0])


vector_a = [[1, 0]]
vector_b = [[0, 1]]

print(cosine_similarity(vector_a, vector_b)[0][0])