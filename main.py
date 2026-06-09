from strategy.signal_engine import SmartMoneySignalEngine

engine = SmartMoneySignalEngine()

result = engine.generate_signal()

print("===== SIGNAL =====")
print(result)
