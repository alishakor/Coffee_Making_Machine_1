# import TODO as TODO

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# COFFEE MAKING MACHINE
profit = 0


def initial_resources_report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    initial_cost = f"{profit}"
    return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney:${initial_cost}"


def customer_coffee_choice():
    if user_choice == "report":
        print(initial_resources_report())
    else:
        drink = MENU[user_choice]
        print(drink)
        if is_resource_sufficient(drink["ingredients"]):
            payment_made = process_coins()
            if is_transaction_successful(payment_made, drink["cost"]):
                make_coffee(user_choice, drink["ingredients"])


def is_resource_sufficient(coffee_ingredients):
    """Return true if ingredient is sufficient False if it's not"""
    for item in coffee_ingredients:
        if coffee_ingredients[item] >= resources[item]:
            print(f"Sorry, there's insufficient {item} to prepare {user_choice}")
            return False
    return True


def process_coins():
    """Returns the total cost of the coin inserted in the machine"""
    print("Please insert coins.")
    # Note: 1 quarter = $0.25; 1 dime = $0.10, 1 nickel = $0.05 & 1 penny = $0.01
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))
    total_cost = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    total_cost = round(total_cost, 2)
    return total_cost


def is_transaction_successful(money_received, cost_of_drink):
    if money_received > cost_of_drink:
        change = money_received - cost_of_drink
        change = round(change, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += cost_of_drink
        return True
    else:
        print(f"Sorry, the money is not enough to buy {user_choice}. ${money_received} refunded")
        return False


def make_coffee(coffee_name, coffee_ingredients):
    """Deduct the required ingredient from the initial/current resources"""
    for item in coffee_ingredients:
        resources[item] -= coffee_ingredients[item]
    coffee_name = user_choice
    print(f"Here is your {user_choice}.Enjoy!")


# # TODO 1: user_choice(input), for next_customer(while loop)

machine_on = True


while machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino) ").lower()
    if user_choice == "off":
        machine_on = False
    else:
        customer_coffee_choice()



# TODO 2: Turn_off_machine (if machine is "OFF", end the program )


# TODO 3:  if the user enters report (Print dictionary of available resource in the format specified)


# TODO 4: (a)Define function to check / compare the current resource with the total resource
# def is_resource_sufficient(coffee_ingredients):
#     is_enough = True
#     for item in coffee_ingredients:
#         if coffee_ingredients[item] >= resources[item]:
#             print("Sorry, not enough resources")
#             is_enough = False
#         return True


# TODO 6:check if sufficient_balance, refund money if less but if enough, add money to the
#  initial balance and show it in the next report


# TODO 7: Make Coffee. Deduct fee. Print out info




# Dictionary Lessons
# Nesting of dictionaries


# def espresso():
#     water_esp = MENU["espresso"]["ingredients"]["water"]
#     coffee_esp = MENU["espresso"]["ingredients"]["coffee"]
#     cost_esp = MENU["espresso"]["cost"]
#     return f'{water_esp}, {coffee_esp}'


# def latte():
#     water_lat = MENU["latte"]["ingredients"]["water"]
#     milk_lat = MENU["latte"]["ingredients"]["milk"]
#     coffee_lat = MENU["latte"]["ingredients"]["coffee"]
#     cost_lat = MENU["latte"]["cost"]

# def cappuccino():
#     water_cap = MENU["cappuccino"]["ingredients"]["water"]
#     milk_cap = MENU["cappuccino"]["ingredients"]["milk"]
#     coffee_cap = MENU["cappuccino"]["ingredients"]["coffee"]
#     cost_cap = MENU["cappuccino"]["cost"]
#     return f"Water: {water_cap}ml\nMilk: {milk_cap}ml\nCoffee: {coffee_cap}g\nMoney:${cost_cap}"
