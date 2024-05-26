from Ingredients import menu
from Ingredients import resources
print("Welcome to the coffee machine!!")

machine_status = True


def money_count():
    """ Takes in the coins and tells the total money received."""
    print("Please insert coins.")
    quarters = (int(input("How many quarters?"))) * 0.25
    dimes = (int(input("How many dimes?"))) * 0.1
    nickles = (int(input("How many nickles?"))) * 0.05
    pennies = (int(input("How many pennies?"))) * 0.01
    total = round(quarters + dimes + nickles + pennies, 2)
    return total


def espresso():
    """Responsible for orders related to espresso."""
    resources["water"] = resources["water"]-menu["espresso"]["ingredients"]["water"]
    resources["coffee"] = resources["coffee"]-menu["espresso"]["ingredients"]["coffee"]


def latte():
    """Responsible for orders related to latte."""
    resources["water"] = resources["water"]-menu["latte"]["ingredients"]["water"]
    resources["coffee"] = resources["coffee"] - menu["latte"]["ingredients"]["coffee"]
    resources["milk"] = resources["milk"] - menu["latte"]["ingredients"]["milk"]


def cappuccino():
    """Responsible for orders related to cappuccino."""
    resources["water"] = resources["water"] - menu["cappuccino"]["ingredients"]["water"]
    resources["coffee"] = resources["coffee"] - menu["cappuccino"]["ingredients"]["coffee"]
    resources["milk"] = resources["milk"] - menu["cappuccino"]["ingredients"]["milk"]


money = 0
while machine_status:
    choice = input("What would you like? (Espresso/Latte/Cappuccino) ").lower()
    if choice == "report":
        for things in resources:
            amount = resources[things]
            print(f"{things}: {amount}")
        print(f"money: {money}")
    elif choice == "off":
        machine_status = False
    elif choice == "espresso":
        if resources["water"] >= 50 and resources["coffee"] >= 18:
            var = money_count()
            print(f"total: {var}")
            if var > 1.5:
                change = round((var - 1.5), 2)
                print(f"Here is your ${change} change. Enjoy your Espresso☕")
                espresso()
                money += 1.5
            elif var == 1.5:
                print("Enjoy your Espresso☕")
                espresso()
                money += 1.5
            elif var < 1.5:
                print("Please enter sufficient coins.")
        else:
            print("Please refill the ingredients.")

    elif choice == "latte":
        if resources["water"] >= 200 and resources["coffee"] >= 24 and resources["milk"] >= 150:
            var = money_count()
            print(f"total: {var}")
            if var > 2.5:
                change = round((var - 2.5), 2)
                print(f"Here is your ${change} change. Enjoy your Latte☕")
                latte()
                money += 2.5
            elif var == 2.5:
                print("Enjoy your Latte☕")
                latte()
                money += 2.5
            elif var < 2.5:
                print("Please enter sufficient coins.")
        else:
            print("Please refill the ingredients.")

    elif choice == "cappuccino":
        if resources["water"] >= 250 and resources["coffee"] >= 24 and resources["milk"] >= 100:
            var = money_count()
            print(f"total: {var}")
            if var > 3.0:
                change = round((var - 3.0), 2)
                print(f"Here is your ${change} change. Enjoy your Cappuccino☕")
                cappuccino()
                money += 3.0
            elif var == 3.0:
                print("Enjoy your Cappuccino☕")
                cappuccino()
                money += 3.0
            elif var < 3.0:
                print("Please enter sufficient coins.")
        else:
            print("Please refill the ingredients.")

