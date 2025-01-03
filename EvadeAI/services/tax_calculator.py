def generate_tax_data(balance_in_usd):
    tax_rate = 22.0  # 22% tax rate
    total_tax_liability = round(balance_in_usd * (tax_rate / 100), 2)
    net_after_tax = round(balance_in_usd - total_tax_liability, 2)
    net_capital_gains = round(balance_in_usd * 0.03, 2)  # Simulated 3% capital gains

    return {
        "total_liability": f"${total_tax_liability}",
        "tax_rate": f"{tax_rate}%",
        "net_after_tax": f"${net_after_tax}",
        "net_capital_gains": f"${net_capital_gains}",
        "tax_evadable": "100%",
    }
