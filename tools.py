from langchain_groq import ChatGroq
from langchain_core.tools import tool
from llm import llm


@tool # decorartor to register as a tool
def summarize_file(text: str) -> str:
    """Summarize the file content in 3-4 concise lines."""
    prompt = f"Summarize the following text concisely:\n\n{text}"
    return llm.invoke(prompt).content


@tool
def extract_key_points(text: str) -> str:
    """Extract the most important key points as bullet points."""
    prompt = f"Extract the key points from the following text:\n\n{text}"
    return llm.invoke(prompt).content


@tool
def explain_file(text: str) -> str:
    """Explain the file content in simple terms for a beginner."""
    prompt = f"Explain the following text in simple terms:\n\n{text}"
    return llm.invoke(prompt).content
