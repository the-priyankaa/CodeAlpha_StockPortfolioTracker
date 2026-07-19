# Dictionary containing predefined stock prices

stock_prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 140, "AMZN": 145, "MSFT": 330}

# Dictionary to store the user's stock holdings

portfolio = {}

# Ask the user to enter stock holdings

print("Enter stock holdings (leave stock name empty to finish):")

# Continue taking input until the user presses Enter without typing a stock name

while True:

    # Get stock name from the user and convert it to uppercase

    name = input("Stock name (e.g. AAPL): ").strip().upper()

    # Stop taking input if the stock name is empty

    if not name:
        break

    # Get the quantity of shares for the entered stock

    qty = input(f"Quantity of {name}: ").strip()

    # Check whether the quantity is a valid integer

    try:
        qty = int(qty)

    # Display an error message if the quantity is invalid

    except ValueError:
        print("Invalid quantity, skipping.")
        continue
    
    # Add the quantity to the portfolio dictionary
    # If the stock already exists, update its quantity

    portfolio[name] = portfolio.get(name, 0) + qty

# Variable to store the total investment value

total = 0

# Display the portfolio summary

print("\n=== Portfolio Summary ===")

# Loop through each stock in the portfolio

for name, qty in portfolio.items():

    # Get the stock price from the predefined dictionary

    price = stock_prices.get(name)

    # Skip the stock if its price is not available

    if price is None:
        print(f"{name}: {qty} shares (price unknown, skipping)")
        continue

    # Skip the stock if its price is not available

    sub_total = price * qty

    # Add the stock value to the total investment

    total += sub_total

    # Display stock details

    print(f"{name}: {qty} shares @ ${price} = ${sub_total:,.2f}")

# Display the total investment value

print(f"\nTotal investment value: ${total:,.2f}")

# Display the total investment value

save = input("\nSave to file? (txt/csv/n): ").strip().lower()

# Save the portfolio summary as a text file

if save == "txt":

    with open("portfolio.txt", "w") as f:

        f.write(f"Total investment value: ${total:,.2f}\n")

    print("Saved to portfolio.txt")

# Save the portfolio details as a CSV file

elif save == "csv":

    with open("portfolio.csv", "w") as f:

        # Write the CSV header

        f.write("Stock,Quantity,Price,Subtotal\n")

        # Write each stock's details to the CSV file

        for name, qty in portfolio.items():

            price = stock_prices.get(name, 0)

            f.write(f"{name},{qty},{price},{price * qty}\n")

    print("Saved to portfolio.csv")

# If the user chooses not to save the file

else:

    print("Not saved.")