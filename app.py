from flask import Flask, request, jsonify
from strategy_runner import run_backtest
from order_executor import execute_order
from config import ALPACA_API_KEY, ALPACA_SECRET_KEY

app = Flask(__name__)

@app.route("/run_backtest", methods=["POST"])
def backtest():
    data = request.json
    result = run_backtest(data)
    return jsonify(result)

@app.route("/execute_trade", methods=["POST"])
def trade():
    data = request.json
    result = execute_order(data)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)