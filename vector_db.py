# Defines how to create or load the vector-enabled collection in Astra DB, and insert documents with embeddings

"""New Behavior: Insert documents in bulk, with quote, author, tags, and embedding (stored in "$vector" field).
Action: Build a document structure: {"quote": ..., "author": ..., "tags": ..., "$vector": ...}
Use insert_many() for batch inserts."""

# vector_db.py
import pandas as pd
from connect import connect_to_database
from embedder import get_embeddings_batch

EMBEDDING_MODEL = "text-embedding-3-small"
OPENAI_BATCH_SIZE = 80

def insert_quotes_to_astra(csv_path: str, collection_name: str) -> None:

    df = pd.read_csv(csv_path)
    print(f"Loaded {len(df)} quotes")

    # Step 2: Prepare text to embed (only quote)
    texts = df["quote"].tolist()

    # Step 3: Generate embeddings in batches
    embeddings = get_embeddings_batch(texts)
    print(f"Generated {len(embeddings)} embeddings.")

    # Step 4: Connect to Astra DB
    db = connect_to_database()
    collection = db.get_collection(collection_name)

    # Step 5: Format documents for insertion
    documents = []
    for i, row in df.iterrows():
        tags_raw = row.get("tags", "")
        if pd.isna(tags_raw) or not tags_raw.strip():
            tags = {}
        else:
            tag_list = [tag.strip() for tag in tags_raw.split(";") if tag.strip()]
            tags = {tag: True for tag in tag_list}

        doc = {
            "quote": row["quote"],
            "author": row["author"],
            "$vector": embeddings[i],
            "tags": tags
        }
        documents.append(doc)

    # Step 6: Insert all documents
    print(f"Inserting {len(documents)} documents into Astra DB collection '{collection_name}' ...")
    result = collection.insert_many(documents)
    print(f"Successfully inserted {len(result.inserted_ids)} documents.")

if __name__ == "__main__":
    file = "philosopher_quotes.csv"
    collection_name = "philosophy_quotes"
    insert_quotes_to_astra(file, collection_name)