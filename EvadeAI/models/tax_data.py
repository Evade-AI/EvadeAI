class TaxData:
    def __init__(self, total_liability, tax_rate, net_after_tax, net_capital_gains, tax_evadable):
        self.total_liability = total_liability
        self.tax_rate = tax_rate
        self.net_after_tax = net_after_tax
        self.net_capital_gains = net_capital_gains
        self.tax_evadable = tax_evadable

    def to_dict(self):
        return {
            "total_liability": self.total_liability,
            "tax_rate": self.tax_rate,
            "net_after_tax": self.net_after_tax,
            "net_capital_gains": self.net_capital_gains,
            "tax_evadable": self.tax_evadable,
        }
