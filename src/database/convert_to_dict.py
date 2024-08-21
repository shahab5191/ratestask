from typing import Dict, List, Tuple


def convert_to_dict(
    colnames: Tuple[str],
    rows: Tuple[str] | None
) -> List[Dict[str, str]]:
    if rows is None:
        return []

    data = [dict(zip(colnames, row)) for row in rows]
    return data
