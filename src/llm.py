def build_llm():
    llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0, openai_api_key=st.secrets["openai_api_key"])
    return llm
