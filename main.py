from strategy.signal_engine import SmartMoneySignalEngine


print("""
======== SmartMoneyBot ========

1 = OTC
2 = REAL

""")

mode = input("Select Market: ")

market = "REAL"

if mode == "1":
    market = "OTC"

engine = SmartMoneySignalEngine()

result = engine.generate_signal(
    market=market
)

print("\n===== SIGNAL =====")

print("Market:", result["market"])

print("Signal:", result["signal"])

print("BUY SCORE:", result["buy_score"])

print("SELL SCORE:", result["sell_score"])
