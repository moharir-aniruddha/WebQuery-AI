from uuid import uuid4
from dotenv import load_dotenv
from pathlib import Path

from langchain_classic.chains.qa_with_sources.retrieval import RetrievalQAWithSourcesChain
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_community.document_loaders import WebBaseLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings


load_dotenv()
chunk_size = 500
embedding_model = "sentence-transformers/all-MiniLM-L6-v2"
vectorStore_dir = Path(__file__).parent/"resources/vectorstore"
collection_name = "real_estate"

llm = None
vector_store = None
def initialize_components():
    global llm , vector_store
    if llm is None:
        llm = ChatGroq(model="llama-3.3-70b-versatile" , temperature=0.9 , max_tokens=500)

    if vector_store is None:
        ef = HuggingFaceEmbeddings(
            model_name = embedding_model
        )

        vector_store = Chroma(
            collection_name=collection_name,
            embedding_function=ef,
            persist_directory=str(vectorStore_dir)
        )

def process_urls(url):
    yield "Initializing Components"
    initialize_components()
    vector_store.reset_collection()

    yield "Loading data"
    loader = WebBaseLoader(url)
    data = loader.load()

    yield "Splitting Data"
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ".", " "],
        chunk_size=500,
        chunk_overlap=100
    )

    docs = text_splitter.split_documents(data)

    yield "Saving data to Vector DB"
    uuids = [str(uuid4()) for _ in range(len(docs))]
    vector_store.add_documents(documents=docs, ids=uuids)

def generate_answer(query):
    if not vector_store:
        raise RuntimeError("No vector store")

    chain = RetrievalQAWithSourcesChain.from_llm(llm=llm , retriever=vector_store.as_retriever())
    result = chain.invoke({"question" : query} , return_only_outputs=True)
    sources = result.get("sources" , "")
    return result['answer'],sources


if __name__ == "__main__":
    urls = [
        "https://www.jpmorgan.com/insights/global-research/real-estate/us-housing-market-outlook",
        "https://finance.yahoo.com/news/americas-top-10-real-estate-150000749.html",
        "https://www.usbank.com/investing/financial-perspectives/investing-insights/interest-rates-impact-on-housing-market.html"

    ]

    process_urls(urls)
    answer , sources = generate_answer("Give me a broader overview of the financial perspectives in the US bank")
    print(f"Answer: {answer}")
    print(f"Sources: {sources}")
