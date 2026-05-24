import processor

print("--- Welome to the Terminal Shop ---")
order_total = processor.process("prod_01", 2)
print(f"Your final total with tax is: ${order_total}")
