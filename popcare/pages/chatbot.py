import os


openai_api_key =  st.secrets["OPENAI_API_KEY"]  # insert your Open AI API key here, this required for the chatbot to work
=======
load_dotenv("key.env")
openai_api_key = st.secrets["OPENAI_API_KEY"]  # insert your Open AI API key here, this required for the chatbot to work


# Streamlit
import streamlit as st
from streamlit import session_state as state

# Langchain
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory



# Establish client connection
model = "gpt-4o-mini"
client = ChatOpenAI(
    api_key= openai_api_key, temperature=0.5, model=model
)

# Store Chat History
if "chat_history" not in state:
    state.chat_history = InMemoryChatMessageHistory()

def get_openai_response(input):
    system_prompt = (
        "You are a helpful assistant. If you know the user's name, use it in your response."

    )


    qa_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            MessagesPlaceholder("chat_history"),
            ("user", "{input}")
        ]
    )

    chain = qa_prompt | client
    chain_with_history = RunnableWithMessageHistory(
        chain,
        lambda session_id: state.chat_history,
        input_messages_key="input",
        history_messages_key="chat_history",
    )
    return chain_with_history.invoke({"input": input}, {'configurable': {'session_id': '1234'}})  # Remove the extra argument here

# Display Chat History
for msg in state.chat_history.messages:
    st.chat_message(msg.type).write(msg.content)

user_input = st.chat_input("Ask your question here...")
if user_input:
    st.chat_message("user").write(user_input)
    response = get_openai_response(user_input)
    st.chat_message("ai").write(response.content)
