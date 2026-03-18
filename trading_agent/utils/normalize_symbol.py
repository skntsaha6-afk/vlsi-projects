def normalize_symbol(symbol: str) -> str:
    """
    Normalize a symbol by converting it to uppercase and ensuring it follows the format "NSE:SYMBOL-EQ".
    Args:
        symbol (str): The symbol to normalize.

    Returns:
        str: The normalized symbol.
    """
    normalized_symbol = symbol.strip().upper()
    return normalized_symbol if ":" in normalized_symbol else f"NSE:{normalized_symbol}-EQ"

#print(normalize_symbol("SBIN"))  # Output: "NSE:SBIN-EQ"
