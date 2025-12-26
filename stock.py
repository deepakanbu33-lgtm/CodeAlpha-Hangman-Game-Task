# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

total_value = 0
portfolio = {}

print("📈 Stock Portfolio Tracker")

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()
    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        continue

    quantity = int(input("Enter quantity: "))
    portfolio[stock] = quantity
    total_value += stock_prices[stock] * quantity

print("\n📊 Portfolio Summary")
for stock, qty in portfolio.items():
    print(f"{stock} - {qty} shares @ ₹{stock_prices[stock]}")

print("💰 Total Investment Value: ₹", total_value)

# Save to file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    for stock, qty in portfolio.items():
        file.write(f"{stock} - {qty} shares\n")
    file.write(f"Total Investment: ₹{total_value}")

print("\n✅ Portfolio saved to portfolio.txt")
