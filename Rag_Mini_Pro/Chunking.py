from langchain_text_splitters import RecursiveCharacterTextSplitter
import json

with open("./Data/knowledge.txt","r") as file:
    text = file.read()

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap=50
)

chunks = splitter.split_text(text)

with open("./Data/chunks.json","w") as file:
    json.dump(chunks,file,indent=4,ensure_ascii=False)

# for i,chunk in enumerate(chunks):
#     print(f"\n--- Chunk {i + 1} ---")
#     print(chunk)

# print(len(chunks))

