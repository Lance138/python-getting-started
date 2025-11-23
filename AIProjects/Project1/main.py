# Basic AI assistant using Langchain and Langgraph
# Using Groq's Llama 3.1 model for demonstration
# Langchain is a high level framework that allows us to build AI applications
import os
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_groq import ChatGroq  # Groq chat model integration
# from langchain_openai import ChatOpenAI  # OpenAI chat model integration
from langchain.tools import tool  # Tool management in Langchain3
# langgraph is a framework that allows us to build AI agents
from langgraph.prebuilt import create_react_agent  # Create agents with tools
from dotenv import load_dotenv  # Load environment variables from .env file
# Make a tool next

load_dotenv()  # Load environment variables from .env file

# the entire block below defines a tool. You can create multiple tools in similar ways.


@tool
def calculator(a: float, b: float, operation: str = "add") -> str:
    """Useful for performing basic arithmetic calculations with numbers."""
    # return f"the sum of {a} and {b} is {a + b}"
    if operation == "add":
        return str(a + b)  # for ReAct agent compatibility
    elif operation == "subtract":
        return str(a - b)
    elif operation == "multiply":
        return str(a * b)
    elif operation == "divide":
        if b != 0:
            return str(a / b)
        else:
            return "Error: Division by zero is not allowed."
    else:
        return f"Unknown operation: {operation}. Please use add, subtract, multiply, or divide."


@tool
def say_hello(name: str) -> str:
    """Greet a person by name. Example usage: 'greet Alice' or 'say hello to <name>'."""
    return f"Hello, {name}!, I hope you are doing good today."


def main():
    # higher temperature means more randomness in responses
    # model = ChatOpenAI(temperature=0)
    model = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=os.getenv("GROQ_API_KEY"),
    )
    tools = [calculator, say_hello]
    system_message = SystemMessage(role='system',
                                   content=("You are a helpful AI assistant. Use tools whenever the user's request matches a tool's function."
                                            "If the user says things like 'greet <name>' or 'say hello to <name>', use the say_hello tool."
                                            "If the user asks math questions, use the calculator tool."
                                            "If a request does not match any tool, answer normally."
                                            )
                                   )
    agent_executor = create_react_agent(
        model=model,
        tools=tools
    )

    print("Welcome! I'm your AI assistant. Type 'quit' to exit.")
    print("You can ask me to perform calculations or chat with me.")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input == 'quit':
            break

        # Detect greeting commands
        if user_input.lower().startswith("greet "):
            name = user_input[6:].strip()
            print(f"\nAssistant: {say_hello(name)}")
            continue

        print("\nAssistant: ", end="")

        input_messages = [
            system_message,
            HumanMessage(content=user_input)
        ]

        for chunk in agent_executor.stream(
            {"messages": input_messages}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
        print()  # For newline after the response


if __name__ == "__main__":
    main()
