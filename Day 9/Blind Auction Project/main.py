from art import logo
print(logo)


bidders = {}

if_more_added = True
while if_more_added == True:
    # TODO-1: Ask the user for input ✔️
    name = input("What is your name?: ")
    price = int(input("What is your bid?: "))

    # TODO-2: Save data into dictionary {name: price}
    bidders[name] = price

    # TODO-3: Whether if new bids need to be added
    ask = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if ask == "yes":
        if_more_added = True
        print("\n" * 100)  # clears the screen
    elif ask == "no":
        if_more_added = False
    else:
        print("\n" * 100)  # clears the screen
        print("Type the right thing, noob. Since you didn't input a valid answer I will assume there ARE other bidders.")

# TODO-4: Compare bids in dictionary
print(bidders) # test
check_max= []
for name[price] in bidders:
    check_max.append(price)
    max(check_max)

#winning_bid = max()
