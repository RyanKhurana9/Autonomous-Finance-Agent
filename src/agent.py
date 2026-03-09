from dotenv import load_dotenv
load_dotenv()
from langchain.agents import AgentExecutor, create_react_agent
from langchain_ollama import ChatOllama
from langchain.memory import ConversationBufferMemory
from langchain import hub  # for predefined prompts
from tools import (
    get_stock_price,
    get_stock_news,
    calculate_return,
    get_insider_trading,
    get_stock_chart,
    get_analyst_ratings,
    get_stock_sentiment,
    compare_stocks,
    get_stock_recommendation
)

tools = [
    get_stock_price,
    get_stock_news,
    calculate_return,
    get_insider_trading,
    get_stock_chart,
    get_analyst_ratings,
    get_stock_sentiment,
    compare_stocks,
    get_stock_recommendation
]

model = ChatOllama(model="llama3.1:8b", temperature=0)
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# ✅ Fixed: pull correct prompt, pass to create_react_agent
prompt = hub.pull("hwchase17/react-chat")

# ✅ Fixed: removed memory from here, added prompt
agent = create_react_agent(
    tools=tools,
    llm=model,
    prompt=prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True,
    max_iterations=5,
    memory=memory  # ✅ memory belongs here
)