import requests
from config.config import SOLANA_RPC_URL, COIN_GECKO_API_URL

def fetch_balance(wallet_address):
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getBalance",
        "params": [wallet_address],
    }
    response = requests.post(SOLANA_RPC_URL, json=payload)
    response_data = response.json()

    if "error" in response_data:
        raise Exception("Unable to fetch balance")
    
    lamports = response_data.get("result", {}).get("value", 0)
    return lamports / 1e9  # Convert lamports to SOL


def fetch_transactions(wallet_address):
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getSignaturesForAddress",
        "params": [wallet_address, {"limit": 1000}],
    }
    response = requests.post(SOLANA_RPC_URL, json=payload)
    response_data = response.json()

    if "error" in response_data:
        raise Exception("Unable to fetch transactions")

    transactions = []
    for tx in response_data.get("result", []):
        transactions.append({
            "signature": tx["signature"],
            "slot": tx["slot"],
            "block_time": tx.get("blockTime"),
            "amount": 0,  # Placeholder
            "token": "SOL",
            "flow": "IN" if tx.get("err") is None else "OUT",
        })
    return transactions


def fetch_sol_price():
    response = requests.get(COIN_GECKO_API_URL)
    response_data = response.json()

    sol_price = response_data.get("solana", {}).get("usd")
    if not sol_price:
        raise Exception("Unable to fetch SOL price")
    return sol_price
