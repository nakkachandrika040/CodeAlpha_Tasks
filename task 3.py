# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}
total_investment = 0

print("===== Stock Portfolio Tracker =====")
print("\nAvailable Stocks:")

for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

while True:
    stock_name = input("\nEnter stock symbol (or type 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("❌ Stock not available in the tracker.")
        continue

    try:
        quantity = int(input(f"Enter quantity for {stock_name}: "))

        if quantity <= 0:
            print("❌ Quantity must be greater than zero.")
            continue

        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

    except ValueError:
        print("❌ Please enter a valid number.")

print("\n===== Portfolio Summary =====")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment

    print(
        f"{stock} | Quantity: {quantity} | "
        f"Price: ${price} | Value: ${investment}"
    )

print(f"\n💰 Total Investment Value: ${total_investment}")

# Save results to a text file
with open("portfolio_summary.txt", "w") as file:

    file.write("===== Portfolio Summary =====\n\n")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity

        file.write(
            f"{stock} | Quantity: {quantity} | "
            f"Price: ${price} | Value: ${investment}\n"
        )

    file.write(f"\nTotal Investment Value: ${total_investment}")

print("\n✅ Portfolio summary saved to 'portfolio_summary.txt'")