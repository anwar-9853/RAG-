import os
import streamlit as st 
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_classic.chains.question_answering import load_qa_chain


# Load environment variables

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

st.header("RAG Chatbot")

with st.sidebar:
    st.title("Your Document")
    file = st.file_uploader("Upload PDF file", type="pdf")

if file is not None:
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted

    if not text.strip():
        st.error("Could not extract text from this PDF.")
    else:
        # 1. Split Text
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=150,
            length_function=len
        )
        chunks = text_splitter.split_text(text)
        
        if not chunks:
            st.error("Text splitter failed to create any chunks.")
        else:
            # 2. Setup Embeddings and Vector Store
            # Note: OpenRouter works best if you specify an embedding model 
            # if your key/plan supports it, otherwise standard OpenAI key is needed.
            embeddings = OpenAIEmbeddings(
                openai_api_key=OPENAI_API_KEY, 
                openai_api_base="https://openrouter.ai/api/v1"
            )
            
            vector_store = FAISS.from_texts(chunks, embeddings)
            st.success(f"Successfully indexed {len(chunks)} chunks!")
            
            # 3. Setup LLM
            llm = ChatOpenAI(
                openai_api_key=OPENAI_API_KEY,
                openai_api_base="https://openrouter.ai/api/v1",
                temperature=0,
                max_tokens=1000,
                model_name='openai/gpt-3.5-turbo' 
            )
            
            # 4. User Interaction
            user_question = st.text_input("Type your question here:")
            
            if user_question:
                # Search for similar chunks
                match = vector_store.similarity_search(user_question)
                
                # Setup and run the QA chain
                chain = load_qa_chain(llm, chain_type="stuff")
                response = chain.run(input_documents=match, question=user_question)
                
                st.write("### Answer:")
                st.write(response)