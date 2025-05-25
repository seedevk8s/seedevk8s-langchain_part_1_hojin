from dotenv import load_dotenv
import os
import meilisearch 

load_dotenv()

client = meilisearch.Client(url=os.getenv("MEILYSEARCH_URL"), api_key=os.getenv("MEILYSEARCH_API_KEY"))

def stock_search(query):
    return client.index('nsdaq').search(query)


