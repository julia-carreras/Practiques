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
    "machine_money": 5,
}

def report():
    water_remaining = resources.get('water')
    milk_remaining = resources.get('milk')
    coffee_remaining = resources.get('coffee')
    money_remaining = resources.get('machine_money')

    print(f"Water: {water_remaining}ml")
    print(f"Milk: {milk_remaining}ml")
    print(f"Coffee: {coffee_remaining}g")
    print(f"Money: ${money_remaining:.2f}")

def enough_ingredients():
    water_remaining = resources.get('water')
    milk_remaining = resources.get('milk')
    coffee_remaining = resources.get('coffee')

    order_water = MENU[order]['ingredients']['water']
    order_milk = MENU[order]['ingredients'].get('milk', 0)
    order_coffee = MENU[order]['ingredients']['coffee']

    if order_water > water_remaining:
        print("Sorry there's not enough water.")
    if order_milk > milk_remaining:
        print("Sorry there's not enough milk.")
    if order_coffee > coffee_remaining:
        print("Sorry there's not enough coffee.")
    elif order_water <= water_remaining and order_milk <= milk_remaining and order_coffee <= coffee_remaining:
        resources.update({'water': water_remaining - order_water, 'milk': milk_remaining - order_milk,
                          'coffee': coffee_remaining - order_coffee})
        return True


def dollar_count():
    client_money = 0
    client_money += (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return client_money

def money_change(client_money, order):
    order_cost = MENU[order]["cost"]
    change = client_money - order_cost

    if client_money >= order_cost:
        resources.update({'machine_money': resources['machine_money'] + client_money})
        print(f"Here is ${change:.2f} in change.")
    else:
        print("Sorry, that's not enough money. Money refunded")


turn_on_off = "on"
while turn_on_off == "on":
    order = input("What would you like? (espresso / latte / cappuccino): ").lower()

    if order == "report":
        report()

    elif order == "off":
        turn_on_off = "off"

    elif order == "espresso" or order == "latte" or order == "cappuccino":
        enough_ingredients()
        if True:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            client_money = dollar_count()
            money_change(client_money, order)
            print(f"Here's your {order}. Enjoy!")
