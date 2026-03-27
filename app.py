import streamlit as st
from rag_chain import rag_answer

st.set_page_config(page_title="Enterprise SOP Assistant", layout="centered")

st.title("🏢 Enterprise RAG-Based SOP Assistant")
st.write("Ask questions related to company SOP documents.")

query = st.text_input("🔍 Enter your SOP question:")

if st.button("Get Answer"):
    if query.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Searching SOPs..."):
            answer = rag_answer(query)
            st.success("Answer Found")
            st.write(answer)
