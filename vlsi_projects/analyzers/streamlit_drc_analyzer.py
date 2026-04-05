import streamlit as st 
import tempfile

from python_practice.vlsi_projects.analyzers.langchain_drc_agent import run_agent

st.set_page_config(page_title="EDA DRC Analyzer", layout="wide")

st.title("🧩 EDA DRC Analyzer (Agentic AI)")

# -------------------------------
# Upload File
# -------------------------------
uploaded_file = st.file_uploader("Upload DRC Report", type=["txt"])

if uploaded_file:
    # Save file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as tmp:
        tmp.write(uploaded_file.read())
        temp_path = tmp.name

    st.success("File uploaded successfully!")

    # Save path in session
    st.session_state["file_path"] = temp_path

# -------------------------------
# Tabs UI
# -------------------------------
tab1, tab2 = st.tabs(["📄 Raw Report", "🤖 AI Analysis"])

# -------------------------------
# TAB 1 → Show File
# -------------------------------
with tab1:
    if "file_path" in st.session_state:
        with open(st.session_state["file_path"], "r") as f:
            content = f.read()

        st.text_area("DRC Report", content, height=400)
    else:
        st.warning("Upload a file first")

# -------------------------------
# TAB 2 → Run Agent
# -------------------------------
with tab2:
    if "file_path" in st.session_state:

        if st.button("🚀 Run Analysis"):
            with st.spinner("Agent analyzing..."):
                result = run_agent(st.session_state["file_path"])
                
                # Store result
                st.session_state["result"] = result

        if "result" in st.session_state:
            st.subheader("📊 Analysis Result")
            st.markdown(st.session_state["result"])

    else:
        st.warning("Upload file first")
