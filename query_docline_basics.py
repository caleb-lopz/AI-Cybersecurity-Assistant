
from google import genai
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
import chromadb 
import os

load_dotenv()

client_model = chromadb.PersistentClient(path="./chroma_db")
collection = client_model.get_collection(name = "cybersec")
embedder = SentenceTransformer("all-MiniLM-L6-v2")
client = genai.Client(api_key=os.getenv("API_KEY"))

print("Hello, I'm a cybersecurity assistant chatbot. You can ask me anything about cybersecurity. Type 'exit' to end our conversation.")
chat_history = []
while True:
    question = input("yo: ")
    if question.lower() == "exit":
        break
    question_embedding = embedder.encode([question]).tolist()
    
    rel_chunks = collection.query(query_embeddings=question_embedding, n_results=5)
    context = "\n\n".join(rel_chunks["documents"][0])
    prompt_system = f"you are an expert cybersecurity assistant, use words that anyone can understand, keep your answers concise, stay focused on the original intent, based on: {context} answer: {question}"

    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents= prompt_system)
    chat_history.append({"role": "user", "content": question})
    chat_history.append({"role": "model", "content": response})
    print(response.text) 