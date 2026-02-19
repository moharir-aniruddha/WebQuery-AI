# 🌐 WebQuery AI – Ask Questions from Any Webpage

WebQuery AI is a Retrieval-Augmented Generation (RAG) based web application that allows users to provide static webpage URLs and ask questions based on the content of those pages.

---

## 📸 Application UI

![WebQuery AI UI](assets/UI.png)

### 📄 PDF Upload & Query Interface
![PDF Feature UI](assets/pdf-ui.png)

---

## 🚀 Features

- Accepts static webpage URLs  
- Upload and process PDF documents  
- Extracts and processes content from multiple sources  
- Splits text into chunks for better retrieval  
- Stores embeddings using Chroma vector database  
- Generates context-aware answers using LLM  
- Interactive Streamlit UI  
- Progress status display during parsing   

---

## 🏗️ Tech Stack

- **Python**
- **Streamlit** – Web interface  
- **LangChain** – RAG pipeline  
- **ChromaDB** – Vector database  
- **Sentence Transformers** – Embeddings  
- **Groq / LLM API** – Answer generation  
- **Unstructured Loader** – Webpage parsing  
- **PyPDF Loader** – PDF document processing  

---

## 🧠 How It Works

### 🔹 Webpage Flow

1. User enters one or more static webpage URLs.  
2. The system loads and extracts text from the URLs.  
3. Text is split into smaller chunks.  
4. Embeddings are generated for each chunk.  
5. ChromaDB stores these embeddings.  
6. When a question is asked:
   - Relevant chunks are retrieved.
   - The LLM generates an answer using retrieved context.

### 🔹 PDF Flow

1. User uploads one or more PDF documents.  
2. The system extracts text from PDFs.  
3. Text is split into chunks.  
4. Embeddings are created and stored in ChromaDB.  
5. User asks questions based on uploaded documents.  
6. The system retrieves relevant sections and generates answers.

---

## 🏛️ RAG Architecture Diagram

![RAG Architecture](assets/Rag_architecture.png)

---

## 📂 Project Structure

```
WebQuery-AI/
│
├── assets/
│   ├── ui-screenshot.png
│   └── rag-architecture.png
│
├── main.py
├── rag.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```
git clone https://github.com/moharir-aniruddha/WebQuery-AI.git
cd WebQuery-AI
```

### 2️⃣ Create Virtual Environment

```
python -m venv .venv
```

Activate:

**Windows**
```
.venv\Scripts\activate
```

**Mac/Linux**
```
source .venv/bin/activate
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root folder and add:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```
streamlit run main.py
```

---

## 📌 Usage

### 🌍 Using Webpage URLs

1. Open the sidebar.  
2. Enter one or more static webpage URLs.  
3. Click **Parse URLs**.  
4. Wait until parsing completes.  
5. Ask questions related to webpage content.  

### 📄 Using PDF Documents

1. Upload one or more PDF files.  
2. Wait until document processing completes.  
3. Ask questions based on PDF content. 

---

## ⚠️ Limitations

- Works best with static webpages (e.g., news articles).  
- Dynamic websites may not load properly.  
- Large PDFs may increase processing time.  
- Performance depends on system resources. 

---

## 🔮 Future Improvements

- React Frontend UI  
- Async Web Loader  
- Caching for Faster Reloads  
- Improved Retrieval Strategy  
- Deployment on Streamlit Cloud 

---

## 👨‍💻 Author

**Aniruddha**  
Final Year Engineering Student  
Focused on Generative AI  

---

## 📄 License

This project is developed for educational and learning purposes.
