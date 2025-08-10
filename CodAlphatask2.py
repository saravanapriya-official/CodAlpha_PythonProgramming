# Hardcoded stock prices (simulating real prices)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "AMZN": 140,
    "MSFT": 320
}

portfolio = {}
total_value = 0

print("📈 Welcome to the Stock Portfolio Tracker!")
print("Enter your stock holdings. Type 'done' when finished.\n")

# Get user input for stocks and quantities
while True:
    stock = input("Enter stock symbol (e.g., AAPL): ").upper()
    
    if stock == "DONE":
        break
    
    if stock not in stock_prices:
        print("❌ Stock not found in our price list. Try again.\n")
        continue
    
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = quantity
    except ValueError:
        print("❌ Please enter a valid number.\n")

# Calculate and display results
print("\n📊 Portfolio Summary:")
for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    print(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${value}")
    total_value += value

print(f"\n💰 Total Investment Value: ${total_value}")

# Optional: Save to file
save = input("\nDo you want to save the result to a file? (yes/no): ").lower()
if save == "yes":
    filename = "portfolio_summary.txt"
    with open(filename, "w") as file:
        file.write("Stock Portfolio Summary:\n")
        for stock, quantity in portfolio.items():
            value = stock_prices[stock] * quantity
            file.write(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${value}\n")
        file.write(f"\nTotal Investment Value: ${total_value}\n")
    print(f"✅ Portfolio saved to '{filename}'.")

