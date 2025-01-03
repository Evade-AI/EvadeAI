class Transaction:
    def __init__(self, signature, slot, block_time, amount, token, flow):
        self.signature = signature
        self.slot = slot
        self.block_time = block_time
        self.amount = amount
        self.token = token
        self.flow = flow

    def to_dict(self):
        return {
            "signature": self.signature,
            "slot": self.slot,
            "block_time": self.block_time,
            "amount": self.amount,
            "token": self.token,
            "flow": self.flow,
        }
