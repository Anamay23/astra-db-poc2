# Calls OpenAI Embeddings API to generate vector embeddings for quotes
# Embed quotes in batches for efficiency

import os
from dotenv import load_dotenv
import openai
from typing import List

# Load environment variables
load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Embedding model and batch size
EMBEDDING_MODEL = "text-embedding-3-small"
OPENAI_BATCH_SIZE = 80

def get_embeddings_batch(texts: List[str]) -> List[List[float]]:
    """
    Takes a list of texts and returns a list of corresponding embeddings.
    Args:
        texts (List[str]): List of input strings to embed.
    Returns:
        List[List[float]]: List of embedding vectors.
    """
    embeddings = []

    # Ensure batching --> 450 + 80 - 1 = 529 // 80 = 6 batches
    num_batches = (len(texts) + OPENAI_BATCH_SIZE - 1) // OPENAI_BATCH_SIZE

    for i in range(num_batches):
        start = i * OPENAI_BATCH_SIZE
        end = start + OPENAI_BATCH_SIZE
        batch = texts[start:end]

        response = openai.embeddings.create(
            input=batch,
            model=EMBEDDING_MODEL
        )

        batch_embeddings = [item.embedding for item in response.data]
        embeddings.extend(batch_embeddings)

    return embeddings

#print("Trying to generate a test embedding...")
#text = "Hello, world!"
#test_embedding = get_openai_embedding(text, model="text-embedding-3-small")
#print("Test embedding generated. Length:", len(test_embedding))