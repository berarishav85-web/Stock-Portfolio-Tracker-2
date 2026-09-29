# Task 2: Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 180
}

print("===== STOCK PORTFOLIO TRACKER =====")

total_investment = 0

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        print("Available stocks:", ", ".join(stock_prices.keys()))
        continue

    quantity = int(input("Enter quantity: "))

    price = stock_prices[stock]
    investment = price * quantity

    print("Stock price:", price)
    print("Investment:", investment)

    total_investment += investment

print("\n===== PORTFOLIO SUMMARY =====")
print("Total Investment = $", total_investment)

# Save result to a text file
with open("portfolio_result.txt", "w") as file:
    file.write("STOCK PORTFOLIO SUMMARY\n")
    file.write("-----------------------\n")
    file.write(f"Total Investment = ${total_investment}\n")

print("Result saved to portfolio_result.txt")