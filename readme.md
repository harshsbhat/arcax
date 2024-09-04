# Arcax - Automated Documentation Generator

Arcax is a Streamlit application designed to generate documentation for websites. It utilizes Firecrawl for scraping or crawling web content and OpenAI's GPT-3.5-turbo model to summarize the content.

## Features

- **URL Input**: Enter the URL of the website you want to document.
- **Action Selection**: Choose between scraping or crawling the website.
- **Documentation Generation**: Generate a summary of the website content.
- **Download Option**: Download the generated summary as a Markdown file

## Installation

### Create a Virtual Environment and Install Dependencies

1. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

2. Activate the virtual environment:
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Configure Environment Variables

1. Create a `.env` file in the root directory of the project.

2. Add your API keys to the `.env` file:
    ```plaintext
    FIRECRAWL_API_KEY=your_firecrawl_api_key
    OPENAI_API_KEY=your_openai_api_key
    ```

## Running the Application

1. Start the Streamlit application with the following command:
    ```bash
    streamlit run app.py
    ```

2. Open your browser and navigate to the URL provided by Streamlit to use the application.

## How It Works

- **URL Input**: Enter the URL of the website you want to document.
- **Action Selection**: Choose between "scrape" or "crawl" to retrieve the website content.
- **Documentation Generation**: The content is processed using OpenAI's GPT-3.5-turbo model to generate a summary.
- **Download Option**: The summary is displayed on the page with an option to download it as a Markdown file.

## Example

1. Enter a URL into the input field.
2. Select an action (either "scrape" or "crawl").
3. Click the "Generate Documentation" button.
4. The application will display a summary of the content, and you can download this summary as a Markdown file.
