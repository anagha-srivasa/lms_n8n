import streamlit as st
import requests

st.title("IntelliLearn - n8n Direct Frontend")

st.markdown("This dashboard sends data directly to your n8n Webhook, bypassing the FastAPI backend.")

webhook_url = st.text_input(
    "n8n Webhook URL", 
    value="http://localhost:5678/webhook-test/evaluate-performance",
    help="Use /webhook-test/ for testing or /webhook/ for production."
)

st.subheader("Student Context")
col1, col2 = st.columns(2)
with col1:
    subject = st.text_input("Subject", value="Math")
    task_type = st.selectbox("Task Type", ["doubt_solving", "assessment", "content_generation"])
with col2:
    learning_rate = st.slider("Learning Rate", min_value=1, max_value=100, value=75)

summary = st.text_area("ILM Chat Summary", value="Student is learning basic calculus.")
rag_context = st.text_area("RAG Textbook Context", value="A derivative represents the rate of change.")
user_input = st.text_area("User Input / Doubt", value="What is a derivative?")

if st.button("Send Request to n8n"):
    payload = {
        "task_type": task_type,
        "subject": subject,
        "learning_rate": learning_rate,
        "summary": summary,
        "doubt": user_input, 
        "rag_context": rag_context
    }
    
    try:
        with st.spinner("Waiting for LM Studio via n8n..."):
            response = requests.post(webhook_url, json=payload)
            response.raise_for_status()
            
            result = response.json()
            
            st.subheader("AI Response")
            st.success(result.get("response", "Success, but no 'response' key found in the returned JSON."))
            
    except requests.exceptions.ConnectionError:
        st.error("Connection Error: Could not connect to n8n. Make sure n8n is running and the Webhook URL is correct.")
    except requests.exceptions.HTTPError as err:
        st.error(f"HTTP Error: {err}")
        st.json(response.json())
    except Exception as e:
        st.error(f"An error occurred: {e}")
