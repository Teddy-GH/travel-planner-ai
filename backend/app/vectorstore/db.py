from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

from app.core.config import settings

def get_embeddings():
    
   # Print api key
    print(f"API key is {settings.OPENAI_API_KEY}")
    
    return OpenAIEmbeddings(
        api_key=settings.OPENAI_API_KEY
    )

def get_vector_store():
    return Chroma(
        collection_name="travel_documents",
        embedding_function=get_embeddings(),
        persist_directory="./chroma_db"
    )    