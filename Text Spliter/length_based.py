from langchain_text_splitters import CharacterTextSplitter

text = """Football is one of the most popular sports in the world. It is played between two teams of eleven players, and the main objective is to score goals by kicking the ball into the opponent's net. Football improves physical fitness, teamwork, discipline, and communication skills. Major tournaments like the FIFA World Cup attract millions of fans worldwide. Football is not only a game but also a source of entertainment, passion, and unity among people."""



spliter = CharacterTextSplitter(
    chunk_size=100, 
    chunk_overlap=0, 
    separator=''
)

result = spliter.split_text(text)
print(result)