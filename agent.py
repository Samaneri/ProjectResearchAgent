import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_core.runnables.history import RunnableWithMessageHistory

from agent.memory import get_session_history
from tools.web_search import web_search
from tools.product_info import product_info
from tools.product_compare import product_compare


load_dotenv()


TOOLS = [
    web_search,
    product_info,
    product_compare
]


SYSTEM_PROMPT = """
You are a Product Research AI Agent.

Your job is to help users research products and make buying decisions.

You have three tools:

1. web_search
   Searches the live web for current information.

2. product_info
   Gets detailed information about one product.

3. product_compare
   Compares multiple products.

Rules:

- For questions about one product, use product_info.
- For comparison questions, use product_compare.
- For general current information, use web_search.
- Do not invent product information.
- Use previous conversation context when answering follow-up questions.
- Give clear answers with price, features, specifications, pros, cons,
  and recommendations when appropriate.
"""


def build_agent():

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY is missing. Check your .env file."
        )

    model = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.3,
        api_key=api_key
    )

    agent = create_agent(
        model=model,
        tools=TOOLS,
        system_prompt=SYSTEM_PROMPT
    )

    return agent