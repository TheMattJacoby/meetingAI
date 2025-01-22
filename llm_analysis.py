import openai

def generate_summary(text):
    """Summarizes text using OpenAI API."""
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "system", "content": "Summarize this meeting professionally."},
                  {"role": "user", "content": text}],
        max_tokens=1024,
        api_key="your-openai-api-key"
    )
    return response["choices"][0]["message"]["content"]