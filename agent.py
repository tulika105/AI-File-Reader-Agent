from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from file_loader import load_file
from tools import summarize_file, extract_key_points, explain_file
from llm import llm

# -------- Decision Prompt --------
decision_prompt = ChatPromptTemplate.from_template(
    """
You are an AI File Reader Agent.

Based on the user instruction, decide which action to take.
Respond with ONLY ONE word from the following but reason carefully before deciding:
- summarize
- key_points
- explain

User instruction:
{instruction}
"""
)

# -------- Router Logic --------
def route_tool(inputs):
    instruction = inputs["instruction"]
    content = inputs["content"]

    decision = llm.invoke(
        decision_prompt.format(instruction=instruction)
    ).content.lower()

    if "summarize" in decision:
        return summarize_file.invoke(content)
    elif "key" in decision:
        return extract_key_points.invoke(content)
    else:
        return explain_file.invoke(content)

# -------- LCEL Pipeline --------
pipeline = RunnableLambda(route_tool) | StrOutputParser()


def main():
    print("\n📄 AI File Reader Agent (Version 1 – LCEL)\n")

    file_path = input("Enter file path:\n> ")
    instruction = input("What do you want to do with this file?\n> ")

    try:
        content = load_file(file_path)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return

    result = pipeline.invoke({
        "content": content,
        "instruction": instruction
    })

    print("\n✅ Output:\n")
    print(result)


if __name__ == "__main__":
    main()
