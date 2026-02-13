import streamlit as st
from rag import process_urls, process_pdf, generate_answer


st.set_page_config(page_title="WebQuery AI", layout="wide")

st.title("WebQuery AI")

# ---------- SESSION STATE FLAGS ----------
if "data_ready" not in st.session_state:
    st.session_state.data_ready = False

if "processing" not in st.session_state:
    st.session_state.processing = False

if "mode" not in st.session_state:
    st.session_state.mode = "URL"


# ---------------- SIDEBAR ---------------- #

st.sidebar.header("📂 Choose Input Type")

mode = st.sidebar.radio(
    "Select Data Source",
    ["URL", "PDF"]
)

st.session_state.mode = mode


# ---------------- URL MODE ---------------- #
if mode == "URL":
    st.sidebar.header("🔗 Add Article URLs (Max 3)")

    url1 = st.sidebar.text_input("URL 1")
    url2 = st.sidebar.text_input("URL 2")
    url3 = st.sidebar.text_input("URL 3")

    urls = [u for u in [url1, url2, url3] if u]

    if st.sidebar.button("⚙️ Process URLs"):
        if len(urls) == 0:
            st.sidebar.warning("Please enter at least one URL")
        else:
            st.session_state.processing = True
            st.session_state.data_ready = False
            st.session_state.urls = urls


# ---------------- PDF MODE ---------------- #
if mode == "PDF":
    st.sidebar.header("📄 Upload PDF Document")

    uploaded_files = st.sidebar.file_uploader(
        "Upload one or more PDF files",
        type=["pdf"],
        accept_multiple_files=True
    )

    if st.sidebar.button("⚙️ Process PDF"):
        if not uploaded_files:
            st.sidebar.warning("Please upload at least one PDF file")
        else:
            st.session_state.processing = True
            st.session_state.data_ready = False
            st.session_state.uploaded_files = uploaded_files

# ---------------- MAIN SCREEN LOGIC ---------------- #

# 🟡 STEP 1 — Show processing status
if st.session_state.processing and not st.session_state.data_ready:

    st.subheader("⏳ Processing Knowledge Base...")
    status_box = st.empty()

    # URL Processing
    if st.session_state.mode == "URL":
        for status in process_urls(st.session_state.urls):
            status_box.info(status)

    # PDF Processing
    if st.session_state.mode == "PDF":

        for index, file in enumerate(st.session_state.uploaded_files):
            status_box.info(f"Processing {file.name}...")

            # Reset only for first file
            if index == 0:
                result = process_pdf(file, reset=True)
            else:
                result = process_pdf(file, reset=False)

            if isinstance(result, str):
                status_box.error(result)
                st.session_state.processing = False
                break

        status_box.info("Extracting and indexing all PDF content...")

    status_box.success("✅ Knowledge base created successfully!")
    st.session_state.data_ready = True
    st.session_state.processing = False


# 🟢 STEP 2 — Show Q&A interface AFTER processing
if st.session_state.data_ready:

    st.subheader("💬 Ask Questions")

    query = st.text_input("Enter your question:")

    if st.button("🔍 Get Answer"):
        if not query:
            st.warning("Please enter a question")
        else:
            with st.spinner("Thinking..."):
                answer, sources = generate_answer(query)

            st.subheader("📖 Answer")
            st.write(answer)

            st.subheader("🔎 Sources")
            st.write(sources)
