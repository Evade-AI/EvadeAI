import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from services.solana_service import fetch_balance, fetch_transactions, fetch_sol_price
from services.tax_calculator import generate_tax_data

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/transaction_history", methods=["POST"])
def transaction_history():
    data = request.json
    wallet_address = data.get("wallet_address")

    if not wallet_address:
        return jsonify({"error": "Wallet address is required"}), 400

    try:
        # Fetch SOL balance and price
        balance_in_sol = fetch_balance(wallet_address)
        sol_to_usd = fetch_sol_price()
        balance_in_usd = balance_in_sol * sol_to_usd

        # Fetch transactions
        transactions = fetch_transactions(wallet_address)

        # Generate tax overview
        tax_data = generate_tax_data(balance_in_usd)

        return jsonify({
            "current_balance": f"{balance_in_sol} SOL (${balance_in_usd:.2f})",
            "transactions": transactions,
            "tax_overview": tax_data,
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
