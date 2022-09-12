# Ariel Schwalb
# September 12, 2022
# 
# This is my second assignment. I will write a program
# to calcuate a table's order at a restaurant.

# Declare variables

i = 0
table_order = []
menu_prices = []
total = 0
tax = 0
grand_total = 0

# Print restaurant heading. 
print("Tatami Asian Fusion Restaurant \n")

# Create the table order list.
table_order = ["Veggie Sushi -", "Pad Thai -", "Dim Sum -", "Miso Soup -", "Simosas -"]

# Create the menu prices list.
menu_prices = [13.99, 12.99, 8.99, 5.99, 7.99]

# Create for loop to print out each item with its price.
for order, price in zip(table_order, menu_prices):
    print(f"{order}", f"${price}")

# Find the total cost.
total = 13.99 + 12.99 + 8.99 + 5.99 + 7.99
print(f"\nTotal: ${total}")

# Find the tax. 
tax = total * 0.0625
print("Tax 6.25%: ${:.2f}".format(tax))

# Find the grand total.
grand_total = total + tax
print("Grand Total: ${:.2f} \n".format(grand_total))

# Print the goodbye message.
print("Thanks for coming to Tatami Asian Fusion! We hope you enjoyed your meal. See you next time!")
 


