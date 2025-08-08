# 🧠 Philosophy Quote Tool — Quote Search & Generation

This project demonstrates advanced **vector search** and **generative AI** capabilities on a curated dataset of philosophical quotes. It showcases how to build a semantic search and quote generation system powered by **OpenAI embeddings** and **Astra DB vector search**.

## ✨ Features

- **🧭 Semantic Quote Search**  
  Search philosophical quotes by *meaning*, not just keywords — powered by OpenAI vector embeddings. Supports optional filters for **author** and **tags**.

- **📝 Philosophical Quote Generation**  
  Generate new, AI-crafted quotes inspired by existing ones. The model is guided using retrieved quotes to stay thematically and stylistically consistent.

- **🚀 Efficient Vector Storage & Querying**  
  Uses **Astra DB's vector search** for scalable, fast similarity lookups over dense embedding vectors.

- **⚡ Batch Embedding Computation**  
  Embeds the dataset in batches to reduce API calls and speed up processing using OpenAI’s `text-embedding-3-small` model.


## 🛠️ About the Project

The app integrates two powerful capabilities:

- **Vector Search**: Quotes and queries are both transformed into dense vector representations using OpenAI embeddings. This allows the system to return semantically similar results even when the query uses different words than the quote.

- **Context-Aware Quote Generation**: Once the user provides a topic, the app retrieves similar quotes from the dataset and uses them as examples in a custom prompt to OpenAI’s GPT model, generating a new quote that fits both the style and the theme.

This showcases how **retrieval-augmented generation (RAG)** can be combined with vector databases to produce meaningful, creative outputs. It’s a great PoC for semantic search systems, personalized generation tools, and educational or creative writing aids using a vector db like Astra.

---

## 🗂️ Files in this Repo

| File                     | Purpose                                                                  |
|--------------------------|--------------------------------------------------------------------------|
| `app1.py`                | Streamlit UI application integrating search and generation features     |
| `connect.py`             | Handles connection setup to Astra DB and OpenAI                         |
| `embedder.py`            | Batch embedding generation utility using OpenAI Embeddings API          |
| `find_quote.py`          | Logic to embed queries and find relevant quotes from Astra DB           |
| `generate_quote.py`      | Uses the search results to prompt OpenAI for quote generation           |
| `prompt_instructions.py` | Contains prompt templates and model config                              |
| `vector_db.py`           | Functions for batch inserting and managing quotes & embeddings in Astra DB |
| `requirements.txt`       | Required Python packages                                                 |
