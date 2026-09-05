import os

from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import tool

load_dotenv()


@tool
def web_search(query: str) -> str:
    """
    Search the web for current product information.
    """

    search = TavilySearchResults(
        max_results=5,
        tavily_api_key=os.getenv("TAVILY_API_KEY")
    )

    results = search.invoke(query)

    return str(results)