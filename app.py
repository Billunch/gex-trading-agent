from flask import Flask, request, jsonify
from order_executor import execute_order

app = Flask(__name__)

# 首頁路由
@app.route("/")
def home():
    return "✅ GEX Trading Agent is live!"

# 策略執行入口，可連接 TradingView Webhook
@app.route("/run-strategy", methods=["POST"])
def run_strategy():
    try:
        data = request.get_json()
        # 你可以根據傳入資料做處理
        result = execute_order(data)  # 例如 data={'symbol': 'AAPL', 'side': 'buy'}
        return jsonify({"status": "success", "result": result})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# 本地開發或 Render 部署都適用
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
