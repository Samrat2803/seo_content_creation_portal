import gradio as gr
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_community.tools import DuckDuckGoSearchResults
import requests
from bs4 import BeautifulSoup
import re
import os

try:
    server_port = int(os.environ.get('SERVER_PORT', ''))
except ValueError:
    server_port = 7860

root_path = os.environ.get('ROOT_PATH', '')

# Define the function to fetch top-ranked articles
def fetch_top_ranked_articles(keywords):
    search = DuckDuckGoSearchResults()
    article_texts = []
    article_links = []
    link_regex = re.compile(r'link: (https?://[^\s]+)')

    for keyword in keywords.split(','):
        try:
            results_str = search.run(keyword.strip())
            print(f"Results for {keyword.strip()}: {results_str}")

            # Extract links using regex
            links = link_regex.findall(results_str)
            
            for link in links[:2]:
                article_links.append(link)
                try:
                    response = requests.get(link)
                    soup = BeautifulSoup(response.text, 'html.parser')
                    paragraphs = soup.find_all('p')
                    article_text = ' '.join([para.get_text() for para in paragraphs])
                    article_texts.append(article_text)
                except Exception as e:
                    print(f"Failed to fetch article from {link}: {e}")
                    continue
        except Exception as e:
            print(f"Error fetching search results for {keyword.strip()}: {e}")
            continue

    return article_texts, article_links

# Define the function to generate SEO content
def seo_content_writer(model, api_key, topic, keywords, length, language, tone, audience):
    try:
        # Initialize the OpenAI model
        model = ChatOpenAI(model=model, api_key=api_key)

        # Fetch top-ranked articles
        top_ranked_articles, article_links = fetch_top_ranked_articles(topic +", "+keywords)

        # Combine articles for context
        context = ' '.join(top_ranked_articles)

        # Create the prompt with the given parameters
        prompt = f"You are an expert SEO content writer. Write a detailed and SEO-optimized article about {topic}. Use the following keywords: {keywords}. The article should be around {length} words long, in {language} language, with a {tone} tone, aimed at {audience}. Divide the text into small paragraphs, separated by <p></p> tags. Refer to these top-ranked articles for inspiration: {context}."

        # Invoke the model with the formatted prompt
        response = model.invoke([HumanMessage(content=prompt)])

        # Extract and print the generated text
        generated_text = response.content.strip()
        
        # Construct the HTML content
        content_html = f"""
        <html>
        <head>
            <title>{topic}</title>
            <meta name="keywords" content="{keywords}">
            <meta name="description" content="{generated_text[:100]}"> <!-- Truncated description for SEO purposes -->
        </head>
        <body>
            <h1>{topic}</h1>
            <p>{generated_text}</p>
        </body>
        </html>
        """
    except Exception as e:
        error_message = f"Error generating SEO content: {e}"
        content_html = f"<html><body><h1>Error</h1><p>{error_message}</p></body></html>"
        article_links = []

    return content_html, article_links

# Create the Gradio interface
demo = gr.Interface(
    fn=seo_content_writer,
    inputs=[
        gr.Dropdown(label="OpenAI Model", choices=["gpt-3.5-turbo", "gpt-4"], value="gpt-3.5-turbo"),
        gr.Textbox(label="OpenAI API Key", type="password"),
        gr.Textbox(label="Topic", value="5 funny facts about Rahul Gandhi"),
        gr.Textbox(label="Keywords", value="Rahul Gandhi funny, Rahul Gandhi facts, Rahul Gandhi humor"),
        gr.Number(label="Length (in words)", value=100),
        gr.Textbox(label="Language", value="English"),
        gr.Textbox(label="Tone", value="exciting"),
        gr.Textbox(label="Audience", value="general")
    ],
    outputs=[
        gr.HTML(label="Generated SEO Content"),
        gr.JSON(label="References")
    ],
    title="SEO Content Generator",
    description="Generate SEO-optimized articles by providing the topic, keywords, desired length, language, tone, and target audience. This tool fetches top-ranked articles for context and generates a detailed article.",
    article="<p>This application utilizes OpenAI's language models to generate high-quality SEO content. It also fetches top-ranked articles from the web for contextual relevance.</p>"
)
# Launch the Gradio app on the specified port
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0",
                server_port=server_port,
                root_path=root_path)