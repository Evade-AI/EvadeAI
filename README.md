# EvadeAI

EvadeAI is a Flask-based API that calculates tax liabilities and retrieves transaction histories for Solana wallet addresses. By analyzing your wallet's balance and recent transactions, it generates a detailed tax overview and presents the last 1,000 transactions associated with your wallet.

---

## Features

### 1. **Tax Overview**
- Calculate estimated tax liabilities based on your wallet's USD balance.
- Simulates tax liability, net capital gains, and potential savings (hypothetical evasion percentage is always "100%").

### 2. **Transaction History**
- Fetches and displays the last 1,000 transactions for a given Solana wallet.
- Includes details such as transaction signature, slot, block time, and transaction type (IN/OUT).

### 3. **Real-Time Data**
- Integrates with Solana RPC API to fetch wallet balances and transaction data.
- Retrieves real-time SOL-to-USD conversion rates using the CoinGecko API.

### 4. **Secure and Cross-Origin Support**
- Includes CORS headers for integration with front-end applications.
- Ensures secure communication with external APIs.

---

## Installation

### Prerequisites
- Python 3.7 or higher
- Pip (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/EvadeAI/EvadeAI.git
   cd EvadeAI
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the application:
   ```bash
   python app.py
   ```

---

## API Endpoints

### **Transaction History**
- **URL**: `/transaction_history`
- **Method**: `POST`
- **Payload**:
   ```json
   {
     "wallet_address": "your_wallet_address_here"
   }
   ```
- **Response**:
   ```json
   {
     "current_balance": "10.5 SOL ($210.00)",
     "transactions": [
       {
         "signature": "abc123...",
         "slot": 12345678,
         "block_time": 1672444800,
         "amount": 0,
         "token": "SOL",
         "flow": "IN"
       }
     ],
     "tax_overview": {
       "total_liability": "$46.20",
       "tax_rate": "22.0%",
       "net_after_tax": "$163.80",
       "net_capital_gains": "$6.30",
       "tax_evadable": "100%"
     }
   }
   ```

---

## Dependencies

The project uses the following libraries:
- **Flask**: A lightweight web framework for building APIs.
- **Flask-CORS**: For enabling Cross-Origin Resource Sharing (CORS).
- **Solana**: For interacting with the Solana blockchain.
- **Solders**: A low-level Solana utility.
- **Requests**: For making HTTP requests.

Install dependencies with:
```bash
pip install -r requirements.txt
```

---

## Example Usage

1. Start the Flask server:
   ```bash
   python app.py
   ```

2. Use an API client like Postman or `curl` to test the `/transaction_history` endpoint:
   ```bash
   curl -X POST http://127.0.0.1:5000/transaction_history \
   -H "Content-Type: application/json" \
   -d '{"wallet_address": "your_wallet_address_here"}'
   ```

3. View the response containing transaction data and a detailed tax overview.

---

## Code Overview

### `app.py`

#### Key Functions:
- **`generate_tax_data(balance_in_usd)`**:
   ```python
   def generate_tax_data(balance_in_usd):
       tax_rate = 22.0  # Example: 22% tax rate
       total_tax_liability = round(balance_in_usd * (tax_rate / 100), 2)
       net_after_tax = round(balance_in_usd - total_tax_liability, 2)
       net_capital_gains = round(balance_in_usd * 0.03, 2)  # Example: Simulated 3% capital gains

       return {
           "total_liability": f"${total_tax_liability}",
           "tax_rate": f"{tax_rate}%",
           "net_after_tax": f"${net_after_tax}",
           "net_capital_gains": f"${net_capital_gains}",
           "tax_evadable": "100%",  # Always 100%
       }
   ```

- **`transaction_history()`**:
   ```python
   @app.route("/transaction_history", methods=["POST"])
   def transaction_history():
       # Fetch balance and transactions, and calculate tax overview
       ...
   ```

- **`add_cors_headers(response)`**:
   ```python
   @app.after_request
   def add_cors_headers(response):
       response.headers["Access-Control-Allow-Origin"] = "*"
       response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
       response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
       return response
   ```

---

## Disclaimer

EvadeAI is a **conceptual project for educational purposes only**. It does not encourage or support illegal activities, including tax evasion. Always consult with a certified tax professional and adhere to local tax laws.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Contact

For questions or feedback, reach out at [support@evadeai.com](mailto:support@evadeai.com).

---

Enjoy analyzing your Solana wallet with EvadeAI! 🚀
