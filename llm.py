from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

# llm is imported for both agent.py and tools.py
# in agent.py, it is used for decision making to choose the appropriate tool based on user instruction
# in tools.py, it is used for generating tool outputs