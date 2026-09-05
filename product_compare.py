from langchain_core.tools import tool

from tools.product_info import product_info


@tool
def product_compare(products: str) -> str:
    """
    Compare two or more products.
    """

    product_list = [p.strip() for p in products.split(",")]

    results = []

    for product in product_list:
        info = product_info.invoke(product)
        results.append(
            f"\n\n===== {product} =====\n{info}"
        )

    return "\n".join(results)