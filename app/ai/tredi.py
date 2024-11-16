from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import pandas as pd
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

openai_api_key = ""

model = None
tokenizer = None

# def embedding():
#     # 임베딩
    
#     return retriever


def run(query: str):
    # langchain 실행
    df = pd.read_csv("resources/df_final.csv")
    if df is None:
        raise ValueError("No data found")
    else:
        print("Data loaded")

    embedding = OpenAIEmbeddings(
        model="text-embedding-3-large", openai_api_key=openai_api_key
    )

    database = Chroma.from_texts(
        texts=df["summary"].tolist(), embedding=embedding, persist_directory="./chroma"
    )

    retriever = database.as_retriever()

    llm = ChatOpenAI(model="gpt-4", openai_api_key=openai_api_key)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    qa_chain.run(query)
    # "css 알려줘" "java 알려줘" "python 알려줘"
    search_results = retriever.get_relevant_documents(query)
    top_result = search_results[0]  # 가장 유사한 summary 가져오기

    if df is None:
        raise ValueError("No data found")

    # 해당 row에 해당하는 title, link, summary 출력
    most_similar_row = df.iloc[df["summary"].tolist().index(top_result.page_content)]

    title = most_similar_row["title"]
    link = most_similar_row["link"]
    summary = most_similar_row["summary"]

    return {
        "title": title,
        "link": link,
        "summary": summary,
    }
