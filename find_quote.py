import pandas as pd
import os
import openai
from dotenv import load_dotenv
from connect import connect_to_database

load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")
EMBEDDING_MODEL = "text-embedding-3-small"

def find_quote_and_author(query_quote, n, author=None, tags=None, metric_threshold=0.4):

    collection_name = "philosophy_quotes"
    db = connect_to_database()
    collection = db.get_collection(collection_name)

    query_vector = openai.embeddings.create(
        input=[query_quote],
        model=EMBEDDING_MODEL,
    ).data[0].embedding

    filter_clause = {}
    if author:
        filter_clause["author"] = author
    if tags:
        filter_clause["tags"] = {}
        for tag in tags:
            filter_clause["tags"][tag] = True

    results_full = collection.find(
        filter=filter_clause,
        sort={"$vector": query_vector},
        limit=n,
        projection={"quote": 1, "author": 1, "_id": 0},
        include_similarity=True,
    )

    print("Retrieved results")

    results = [res for res in results_full if res["$similarity"] >= metric_threshold]
    return results