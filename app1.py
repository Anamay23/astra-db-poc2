import streamlit as st
from find_quote import find_quote_and_author
from generate_quote import generate_quote

st.set_page_config(page_title="Philosophical Quote Tool", layout="centered")

st.title("Search or Generate Philosophical Quotes")

tab_search, tab_generate = st.tabs(["Search Quotes", "Generate Quote"])

with tab_search:
    st.header("Search Quotes")

    query = st.text_input("Enter a philosophical quote or idea:")
    top_k = st.slider("Number of results", 1, 10, 2)
    author = st.text_input("Filter by author (optional):")
    tag_input = st.text_input("Filter by tags (comma-separated, optional):")
    tags = [tag.strip() for tag in tag_input.split(",")] if tag_input else None

    similarity_threshold = 0.4
    similarity_threshold = st.slider("Minimum similarity score (optional)", 0.0, 1.0, step=0.05)

    if st.button("Search"):
        if not query:
            st.warning("Please enter a quote to search.")
        else:
            with st.spinner("Searching..."):
                try:
                    results = find_quote_and_author(query, top_k, author if author else None, tags, similarity_threshold)

                    if results:
                        st.success(f"Found {len(results)} result(s):")
                        for idx, res in enumerate(results, 1):
                            st.markdown(f"**{idx}.** [similarity={res['$similarity']:.3f}] \"{res['quote']}\" — *{res['author']}*")
                    else:
                        st.info("No matching quotes found.")
                except Exception as e:
                    st.error(f"An error occurred: {e}")

with tab_generate:
    st.header("Generate a New Philosophical Quote")

    topic = st.text_input("Enter a topic or theme for the quote:")
    n_examples = st.slider("Number of example quotes to use", 1, 5, 2)
    author_gen = st.text_input("Filter examples by author (optional):")
    tags_input_gen = st.text_input("Filter examples by tags (optional, comma-separated):")
    tags_gen = [tag.strip() for tag in tags_input_gen.split(",")] if tags_input_gen else None

    if st.button("Generate Quote"):
        if not topic:
            st.warning("Please enter a topic.")
        else:
            try:
                generated_quote = generate_quote(topic, n=n_examples, author=author_gen if author_gen else None, tags=tags_gen)
                if generated_quote:
                    st.success("Generated Quote:")
                    st.markdown(f"> {generated_quote}")
                else:
                    st.info("No quotes found to base generation on.")
            except Exception as e:
                st.error(f"An error occurred: {e}")
