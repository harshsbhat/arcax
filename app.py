import streamlit as st
import openai
from firecrawl import FirecrawlApp
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize FirecrawlApp with the API key
firecrawl_api_key = os.getenv('FIRECRAWL_API_KEY')
firecrawl_app = FirecrawlApp(api_key=firecrawl_api_key)

# OpenAI API Key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Streamlit Interface
st.title("Automated Documentation Generator")
url = st.text_input("Enter the URL of the website:")
action = st.selectbox("Choose Action", ["scrape", "crawl"])

if st.button("Generate Documentation"):
    if not url:
        st.error("Please enter a URL.")
    else:
        try:
            # Scrape or crawl based on user input
            if action == "scrape":
                scrape_result = firecrawl_app.scrape_url(url, params={'formats': ['markdown']})
                content = scrape_result.get('markdown', '')
            else:
                crawl_status = firecrawl_app.crawl_url(
                    url, 
                    params={'limit': 100, 'scrapeOptions': {'formats': ['markdown']}}
                )
                content = crawl_status.get('markdown', '')

            if content:
                # Process the content with OpenAI models
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": f"Summarize the following content:\n\n{content}"}
                    ]
                )
                summary = response.choices[0].message['content'].strip()

                # Display the generated documentation
                st.subheader("Summary")
                st.write(summary)

                # Option to download the documentation
                st.download_button("Download as Markdown", content, file_name="documentation.md")

            else:
                st.error("No content found in the scrape/crawl result.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
