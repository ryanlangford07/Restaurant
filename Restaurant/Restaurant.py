menu = {
    "Pizza": 7.30,
    "Pie": 3.45,
    "Burger": 4.50,
    "Chips": 2.00,
    "Onion rings": 2.30,
    "Drink": 1.50
}
#This is the displayed menu for the customer to browse for what they are looking for. 
customer_order = []
total_cost = 0.0
while True:
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: £{price:.2f}")
    choice = input("Enter the name of the item you'd like to order (or finish to complete your order): ")
 #This is where the user inputs the item that they want to order and once they have done ordering they can type done and their order would be complete. 
    if choice.lower() == 'finish':
        break
    if choice in menu:
        customer_order.append(choice)
        total_cost += menu[choice]
    else:
        print("Sorry, that item is not on the menu. Try choosing from the menu")
 #i use an append to allow the user to add what they want after adding other items, so the order does not finish until the user types finished.
if customer_order:
    print("In Your Order:")
    for item in customer_order:
        print(item)
    print(f"Total Cost: £{total_cost:.2f}")
else:
    print("You haven't placed any orders.")
print("Thank you for ordering!")
#This is the end of the program, as it has given the user their order and the total cost, and then thanks them for odering but if they have not ordered anything, it says they have no order. 