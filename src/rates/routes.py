from src.config import Config
from src.rates import bp


@bp.get(f"{Config().API_PREFIX}/rates")
def rates_endpoint():
    return {"data": "test"}
