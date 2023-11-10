from art import logo

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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# functions
def process_coins():
    """returns total coin from inserted coins"""
    print("Insert coins.")
    total = int(input("how many quaters?$ ")) * 0.25
    total += int(input("how many dimes?$ ")) * 0.10
    total += int(input("how many nickles?$ ")) * 0.05
    total += int(input("how many pennies?$ ")) * 0.01
    return total

def is_transaction_sucessfull (money_received, drink_cost):
    """check if the money received is more or equal to the drink costs"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} dollars in change")
        global profit
        profit += change
        return True
    else:
        print("Sorry that's not enough money. Money refunde")
        return False

def is_resources_sufficient(order_indredients):
    """reutrns true if resources are enough false it not enough"""
    for item in order_indredients:
        if order_indredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            exit()
    return True

    
def make_coffee(drink_name, order_indredients):
    """subtracting the orderd indrediens from the resources"""
    for item in order_indredients:
        resources[item] -= order_indredients[item]
    print(f"Here is your {drink_name}☕")

# actual code
is_on = True 
while is_on:
    print(logo)
    choice = str(input("What would ypu like? (espresso/latte/cappuccino): ").lower())
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}g")
        print(f"Money: {profit}")
    else:
        drink = MENU[choice]
        is_resources_sufficient(drink['ingredients'])
        payment = process_coins()
        if is_transaction_sucessfull(payment, drink["cost"]):
            make_coffee(choice, drink["ingredients"])


