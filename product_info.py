from langchain_core.tools import tool

from tools.web_search import web_search


@tool
def product_info(product: str) -> str:
    """
    Get information about one product including price,
    specifications, features, ratings, pros and cons.
    """

    query = f"""
    Research the product: {product}

    Find:
    - Current price
    - Specifications
    - Main features
    - Customer rating
    - Pros
    - Cons
    - Important details for a buyer

    Use reliable and current web sources.
    """

    return web_search.invoke(query)