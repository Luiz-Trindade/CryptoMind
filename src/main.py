import os
from dotenv import load_dotenv
from datetime import datetime
from langchain.schema.output_parser import StrOutputParser
from langchain.prompts import ChatPromptTemplate
#from langchain.chat_models import init_chat_model
from langchain_google_genai import ChatGoogleGenerativeAI
from bot_prompts import *
from bot_tools import *

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY", "")
#print(api_key)

llm = ChatGoogleGenerativeAI(
    model           = "gemini-2.0-flash-thinking-exp-01-21",
    google_api_key  = api_key
)
#llm = init_chat_model(model="",provider="",api_key=api_key)

# Cria um template de prompt
prompt = ChatPromptTemplate.from_template(cripto_bot_prompt)

# Define a Chain usando pipes (|) para encadear os componentes
chain = prompt | llm | StrOutputParser()

actual_datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
#print(actual_datetime)

response = chain.invoke({
    "data_to_analyse" : data_to_analyse(ticker="BTC-USD", periodo="6mo"),
    "actual_datetime" : actual_datetime
})

# Exibe a resposta
print(response)
