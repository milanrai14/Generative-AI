from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

documents = [
    "Lionel Messi is an Argentine footballer known for his exceptional dribbling, playmaking, goalscoring, and long career at Barcelona. He later played for Paris Saint-Germain and Inter Miami and won the FIFA World Cup with Argentina in 2022.",

    "Cristiano Ronaldo is a Portuguese footballer known for his powerful shooting, athleticism, goalscoring, and aerial ability. He played for Manchester United, Real Madrid and Juventus before moving to Al-Nassr in Saudi Arabia.",

    "Neymar is a Brazilian footballer known for his dribbling, creativity, flair, and attacking ability. He became famous at Santos and later played for Barcelona, Paris Saint-Germain, and other clubs.",

    "Luis Suárez is a Uruguayan striker known for his goalscoring, finishing, movement, and competitive style. He played for Ajax, Liverpool, Barcelona, Atlético Madrid, and other clubs.",

    "Andrés Iniesta is a Spanish midfielder famous for his passing, ball control, vision, and ability to control the tempo of matches. He spent most of his career at Barcelona and scored Spain's winning goal in the 2010 FIFA World Cup final.",

    "Lamine Yamal is a Spanish footballer who developed at Barcelona's La Masia academy. He is known for his dribbling, creativity, passing, and attacking ability and has emerged as one of the prominent young players in world football."
]
query = 'tell me about Lionel Messi'

doc_embeddings = embedding.embed_documents(documents)
query_embeddings = embedding.embed_query(query)

scores = cosine_similarity([query_embeddings], doc_embeddings)[0]

index, score = sorted(list(enumerate(scores)), key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("Similarity score is: ", score)