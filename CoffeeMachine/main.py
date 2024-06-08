LATTE = "latte"
CAPPUCCINO = "cappuccino"
ESPRESSO = "espresso"
INGREDIENTS = "ingredients"
COST = "cost"

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

money = 0.0

PENNY = "penny"
NICKLE = "nickle"
DIME = "dime"
QUARTER = "quarter"

CURRENCIES = {
    "penny": .01,
    "nickle": .05,
    "dime": .1,
    "quarter": .25
}

def machine_has_resources_for_drink(selection):
    drink = MENU[selection]
    for ingredient in drink[INGREDIENTS]:
        if resources[ingredient] < drink[INGREDIENTS][ingredient]:
            print(f"sorry, not enough {ingredient}")
            return False
    return True


def make_string_plural(in_string):
    out_string = ""
    if in_string[len(in_string) - 1] == "y":
        for char in range(0, len(in_string) - 1):
            out_string += in_string[char]
        out_string += "ies"
        return out_string
    out_string = in_string
    return out_string + "s"


def get_money():
    total_cash = 0.0
    for currency in CURRENCIES:
        total_cash += int(input(f"How many {make_string_plural(currency)}?")) * CURRENCIES[currency]
    return total_cash


def is_money_enough_for_drink(cash_inserted, selection):
    return MENU[selection][COST] <= cash_inserted


def calculate_change(cash_inserted, selection):
    return cash_inserted - MENU[selection][COST]


def make_drink(selection):
    drink = MENU[selection]
    for ingredient in drink[INGREDIENTS]:
        resources[ingredient] -= drink[INGREDIENTS][ingredient]
    print(f"enjoy your {selection}")


def log_report():
    for resource in resources:
        print(f"{resource}: {resources[resource]}")
    print(f"Money : {money}")


def fill_machine():
    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100


def get_order():
    user_order = ""
    while user_order == "":
        user_input = input("what would you like to drink?")
        if MENU.__contains__(user_input):
            user_order = user_input
        elif user_input == "report":
            log_report()
        elif user_input == "fill":
            fill_machine()
        elif user_input == "off":
            user_order = "off"
    return user_order


def process_customer():
    global money
    order = get_order()
    if order == "off":
        return False
    if machine_has_resources_for_drink(order):
        amount = get_money()
        if is_money_enough_for_drink(amount, order):
            money += MENU[order][COST]
            make_drink(order)
            print(f"here is your change: ${calculate_change(amount, order)}")
        else:
            print(f"not enough money for {order}")
    return True


run_machine = True


while run_machine:
    run_machine = process_customer()