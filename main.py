import os
import streamlit as st
import pickle
import time
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env (especially openai api key)

st.set_page_config(
    page_title="FinSight | Financial News",
    page_icon="📈",
    layout="wide"
)

st.title("FinSight – AI-Powered Financial News Intelligence 📈")
st.markdown("Research financial news, explore market trends, and get AI-powered insights.")
st.sidebar.title("FinSight | Article Sources")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")
file_path = "faiss_store_openai.pkl"

main_placeholder = st.empty()
llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash", temperature=0.3, max_output_tokens=500)

if process_url_clicked:
    # load data
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("Data Loading...Started...✅✅✅")
    data = loader.load()
    # split data
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=1000
    )
    main_placeholder.text("Text Splitter...Started...✅✅✅")
    docs = text_splitter.split_documents(data)
    # create embeddings and save it to FAISS index
    embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    vectorstore_openai = FAISS.from_documents(docs, embeddings)
    main_placeholder.success("Article embeddings generated successfully! ✅")
    time.sleep(2)

    # Save the FAISS index to a pickle file
    with open(file_path, "wb") as f:
        pickle.dump(vectorstore_openai, f)

query = main_placeholder.text_input("Ask FinSight about the articles:")

if query:
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            vectorstore = pickle.load(f)

        docs = vectorstore.similarity_search(query, k=4)

        if not docs:
            st.warning("No relevant article content found.")
        else:
            context = "\n\n".join(doc.page_content for doc in docs)

            prompt = f"""
You are FinSight, a financial news research assistant.

Answer the question using ONLY the article content below.
If the information is not available, say so.
Keep the answer clear, factual, and concise.

Article content:
{context}

Question:
{query}
"""

            try:
                response = llm.invoke(prompt)

                st.header("FinSight Insights 📊")
                st.write(response.content)

                sources = list(dict.fromkeys(
                    doc.metadata.get("source", "")
                    for doc in docs
                    if doc.metadata.get("source")
                ))

                if sources:
                    st.subheader("Sources:")
                    for source in sources:
                        st.write(source)

            except Exception as e:
                st.error(f"Unable to generate answer: {e}")
    else:
        st.warning("Please process article URLs first.")




