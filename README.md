
# 🤖 RAG Chatbot: PDF Intelligence

A powerful **Retrieval-Augmented Generation (RAG)** application that allows you to "talk" to your PDF documents. This tool uses semantic search to find relevant information within your files and provides accurate, context-aware answers using LLMs.

---

## 🚀 Features
* **PDF Parsing:** Extracts text from multi-page PDF documents effortlessly.
* **Smart Text Chunking:** Breaks long text into manageable 1,000-character bites with a 150-character overlap to preserve context.
* **Vector Search:** Uses **FAISS** to index and retrieve document sections based on meaning, not just keywords.
* **OpenRouter Integration:** Flexible backend support for various LLMs (GPT-3.5, etc.) via OpenRouter.
* **Streamlit UI:** A clean, interactive web interface for uploading files and chatting in real-time.

---

## 🛠️ Tech Stack
* **Framework:** [Streamlit](https://streamlit.io/)
* **LLM Orchestration:** [LangChain](https://www.langchain.com/) & `langchain-classic`
* **Vector Database:** [FAISS](https://github.com/facebookresearch/faiss)
* **PDF Processing:** `pypdf`
* **Environment:** Python 3.13

---

## 📋 Prerequisites
Ensure you have an API key from **OpenRouter** (or OpenAI). Your key should be saved in a `.env` file.

```env
OPENAI_API_KEY=your_sk_or_v1_key_here
```

---

## ⚙️ Installation & Setup

1. **Clone the repository** (or open your project folder):
   ```bash
   cd ragdemo
   ```

2. **Install Dependencies:**
   Run the following command to install all necessary libraries:
   ```bash
   pip install streamlit pypdf langchain-text-splitters langchain-openai langchain-community faiss-cpu langchain-classic python-dotenv
   ```

3. **Run the Application:**
   ```bash
   streamlit run main.py
   ```

---

## 🧠 How It Works
1.  **Extraction:** The app reads your uploaded PDF and converts it into a raw string of text.
2.  **Chunking:** The text is split into **chunks of 1,000 characters**. An **overlap of 150 characters** ensures that sentences aren't cut off in a way that loses meaning.
3.  **Embedding:** Each chunk is converted into a mathematical vector (a list of numbers) that represents its semantic meaning.
4.  **Indexing:** These vectors are stored in a **FAISS** index.
5.  **Retrieval & Generation:** When you ask a question, the app finds the top matching chunks and sends them to the AI as "context." The AI then writes a response based *only* on that context.

---

## ⚠️ Important Notes
* **Scanned PDFs:** This app works best with digital PDFs. If your PDF is a scanned image, the text extraction may return empty results.
* **API Costs:** Every time a document is indexed or a question is asked, API tokens are consumed via your provider.

---

**Happy Chatting!** 🚀
