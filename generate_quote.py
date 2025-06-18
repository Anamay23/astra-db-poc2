import os
import openai
from dotenv import load_dotenv
from find_quote import find_quote_and_author
from prompt_instructions import completion_model_name, generation_prompt_template

load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")

def generate_quote(topic, n, author=None, tags=None):

    hits = find_quote_and_author(query_quote=topic, n=n, author=author, tags=tags)
    if hits:
        prompt = generation_prompt_template.format(
            topic=topic,
            examples="\n".join(f"  - {document['quote']}" for document in hits),
        )

        # a little logging:
        print("** quotes found:")
        for document in hits:
            print(f"**    - {document['quote']} ({document['author']})")
        print("** end of logging")

        response = openai.chat.completions.create(
            model=completion_model_name,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=320,
        )
        return response.choices[0].message.content
    
    else:
        print("** no quotes found.")
        return None