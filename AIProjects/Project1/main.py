# Basic AI assistant using Langchain and Langgraph

# Langchain is a high level framework that allows us to build AI applications
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI  # OpenAI chat model integration
from langchain.tools import tool  # Tool management in Langchain3
# langgraph is a framework that allows us to build AI agents
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv  # Load environment variables from .env file

# Make a tool next

load_dotenv()


# the entire block below defines a tool. You can create multiple tools in similar ways.
@tool
def cauculator(a: float, b: float) -> str:
    """Useful for performing basic arithmetic calculations with numbers."""
    print('Tool has been called.')
    return f"the sum of {a} and {b} is {a + b}"


def main():
    # higher temperature means more randomness in responses
    model = ChatOpenAI(temperature=0)

    tools = []
    agent_executor = create_react_agent(model, tools)

    print("Welcome! I'm your AI assistant. Type 'quit' to exit.")
    print("You can ask me to perform calculations or chat with me.")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input == 'quit':
            break

        print("\nAssistant: ", end="")
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
        print()  # For newline after the response


if __name__ == "__main__":
    main()
