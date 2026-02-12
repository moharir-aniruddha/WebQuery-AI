import streamlit as st
from rag import process_urls, generate_answer

st.set_page_config(page_title="Real Estate RAG", layout="wide")

st.title("WebQuery AI")

# ---------- SESSION STATE FLAGS ----------
if "data_ready" not in st.session_state:
    st.session_state.data_ready = False

if "processing" not in st.session_state:
    st.session_state.processing = False


# ---------------- SIDEBAR ---------------- #
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


# ---------------- MAIN SCREEN LOGIC ---------------- #

# 🟡 STEP 1 — Show processing status
if st.session_state.processing and not st.session_state.data_ready:
    st.subheader("⏳ Processing Articles...")

    status_box = st.empty()

    for status in process_urls(urls):
        status_box.info(status)

    status_box.success("✅ URLs parsed and knowledge base created!")
    st.session_state.data_ready = True
    st.session_state.processing = False


# 🟢 STEP 2 — Show Q&A interface AFTER processing
if st.session_state.data_ready:
    st.subheader("💬 Ask Questions from Articles")

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
