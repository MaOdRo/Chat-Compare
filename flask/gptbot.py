from llama_index import StorageContext, load_index_from_storage
import os
import openai
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY", None)
openai.api_key = api_key

def answerMeProductB(question):
    storage_context = StorageContext.from_defaults(persist_dir = 'Stores/ProductB/')
    index = load_index_from_storage(storage_context)
    query_engine = index.as_query_engine()
    response = query_engine.query(question)
    return response