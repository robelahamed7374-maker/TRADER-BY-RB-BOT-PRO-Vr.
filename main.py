class SmartMoneySignalEngine:

    def generate_signal(self, market="REAL"):

        if market == "OTC":

            return {
                "market": "OTC",
                "signal": "WAIT",
                "buy_score": 50,
                "sell_score": 50
            }

        return {
            "market": "REAL",
            "signal": "WAIT",
            "buy_score": 50,
            "sell_score": 50
        }
