import alpaca_trade_api as tradeapi
from config import ALPACA_API_KEY, ALPACA_SECRET_KEY

def execute_order(params):
    symbol = params.get("symbol", "AAPL")
    qty = int(params.get("qty", 1))
    side = params.get("side", "buy")  # 新增這行，讀取是 buy 還是 sell

    api = tradeapi.REST(
        ALPACA_API_KEY,
        ALPACA_SECRET_KEY,
        base_url='https://paper-api.alpaca.markets'  # 實盤可改為 'https://api.alpaca.markets'
    )

    order = api.submit_order(
        symbol=symbol,
        qty=qty,
        side=side,  # 使用參數指定的方向
        type='market',
        time_in_force='gtc'
    )

    return {"order_id": order.id}
