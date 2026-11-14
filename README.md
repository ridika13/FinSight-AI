# FinSight – AI-Powered Financial News Intelligence 📈

FinSight is a news research tool I built to make it easier to explore financial news and understand what's happening in the market.

You can add article URLs, process their content, and ask questions about the information in those articles. Instead of going through multiple articles manually, FinSight retrieves relevant information and generates answers with source references.

![FinSight](FinSight.jpg)

## Features

- Add up to three news article URLs through the Streamlit sidebar.
- Extract article content using LangChain's `UnstructuredURLLoader`.
- Split extracted content into smaller chunks for better retrieval.
- Generate text embeddings using Hugging Face Sentence Transformers.
- Store and search relevant information using FAISS vector search.
- Ask questions about processed articles.
- Generate AI-powered answers using Google's Gemini model.
- Display source references alongside generated answers.

## Tech Stack

- **Python** – Core programming language
- **Streamlit** – Web application interface
- **LangChain** – Document processing and retrieval workflow
- **Google Gemini** – Answer generation
- **Hugging Face Sentence Transformers** – Text embeddings
- **FAISS** – Vector storage and similarity search

## How It Works

FinSight follows a Retrieval-Augmented Generation (RAG) workflow:

1. Article URLs are provided by the user.
2. LangChain extracts the article content.
3. The extracted text is split into smaller chunks.
4. Hugging Face generates embeddings for the text.
5. FAISS stores the embeddings and retrieves relevant content based on a question.
6. Gemini uses the retrieved information to generate an answer with source references.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ridika13/FinSight-AI.git
cd FinSight-AI
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure your API key

Create a `.env` file in the project root and add your Google Gemini API key:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

You can obtain an API key from [Google AI Studio](https://aistudio.google.com/apikey).

Keep your `.env` file private. Never upload API keys to GitHub.

### 4. Run the application

```bash
streamlit run main.py
```

The application will open in your browser.

## How to Use

1. Enter up to three financial news article URLs in the sidebar.
2. Click **Process URLs** to extract and process the articles.
3. Wait for the text splitting and embedding process to finish.
4. Enter a question in the question field.
5. View the generated answer and its source references.

## Project Structure

```text
FinSight-AI/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── LICENSE
├── FinSight.jpg
│
└── notebooks/
    ├── retrieval.ipynb
    ├── faiss_tutorial.ipynb
    └── text_loaders_splitters.ipynb
```

## Future Improvements

- Support for uploading documents alongside article URLs.
- Improved handling of websites that restrict automated content extraction.
- Better source organization along with research history.
- Additional financial news analysis features.
