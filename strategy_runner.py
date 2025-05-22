import yfinance as yf
import backtrader as bt

class TestStrategy(bt.Strategy):
    def __init__(self):
        self.sma10 = bt.indicators.SMA(period=10)
        self.sma30 = bt.indicators.SMA(period=30)
        self.rsi = bt.indicators.RSI()

    def next(self):
        if not self.position:
            if self.rsi[0] > 60 and self.sma10[0] > self.sma30[0]:
                self.buy()
        else:
            if self.rsi[0] < 50 or self.sma10[0] < self.sma30[0]:
                self.sell()

def run_backtest(params):
    ticker = params.get("ticker", "AAPL")
    df = yf.download(ticker, start="2022-01-01", end="2023-01-01")

    data = bt.feeds.PandasData(dataname=df)
    cerebro = bt.Cerebro()
    cerebro.addstrategy(TestStrategy)
    cerebro.adddata(data)
    cerebro.broker.set_cash(100000)
    result = cerebro.run()
    return {"final_value": cerebro.broker.getvalue()}