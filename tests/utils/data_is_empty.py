from typing import Any, Dict, List


def is_empty(rates: List[Dict[str, Any]]) -> bool:
    for rate in rates:
        if rate.get("average_price") is not None:
            return False

    return True
